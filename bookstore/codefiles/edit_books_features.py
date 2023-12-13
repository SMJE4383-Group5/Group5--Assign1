from PyQt5 import QtCore, QtGui, QtWidgets
from codefiles.catalog import db
from sqlalchemy import text
import shutil ,re , os , random
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox


class Ui_BookEditWindow(object):
    # Initialization function, setting initial variables
    def __init__(self, book_id, main_self):
        self.book_id = book_id
        self.main_self = main_self
        self.base_query = "SELECT Book.picture_url, Book.name, Book.author, Book.description, book_publisher.quantity,"\
                        +"\n    Publisher.name, Book.price "\
                        +"\n    FROM book_publisher"\
                        +"\n    JOIN Book ON book_publisher.book_id=Book.id"\
                        +"\n    JOIN Publisher ON Publisher.id=book_publisher.publisher_id"\
                        +"\n    LEFT JOIN book_order ON book_order.book_id=book.id and book_order.publisher_id=Publisher.id"\
                        +"\n    GROUP BY Book.id, Publisher.id"\
                        +f"\n    HAVING Book.id={self.book_id}"

        self.category_query = "SELECT Category.name FROM Category JOIN book_category ON Category.id=book_category.category_id"+\
                            f"\n    WHERE book_category.book_id={self.book_id}"
        
        self.categoryBoxes = []
        self.initial = []
        self.initialCats = []
        self.newData = []

    # Function to display a message box based on type, title, and text
    def OkMsgBox(self,type, title, text):
        msg = QMessageBox()
        if type == 'warning':
            msg.setIcon(QMessageBox.Warning)
        else:
            msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # Function to place category checkboxes dynamically
    def placeCatBoxes(self):

        query = "SELECT name FROM category"
        catResult = list(db.engine.execute(text(query)))
        x=-65
        y=100
        
        for index, cat in enumerate(catResult):    
       
            if index % 3 == 0:
                x += 86
                y = 18
            elif index % 3 == 1:
                y = 43
            else:
                y = 68       

            self.categoryBoxes.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents_addbook_main))
            self.categoryBoxes[index].setObjectName(cat[0])
            self.categoryBoxes[index].setGeometry(QtCore.QRect(x, y, 80, 22))
            self.categoryBoxes[index].setText(str(cat[0]))

    # Function to retrieve publisher names from the database
    def getPublishers(self):
        query = "SELECT name FROM Publisher"
        return [res[0] for res in list(db.engine.execute(text(query)))]

    # Function to populate the UI with book details
    def fillInfo(self):

        result = list(db.engine.execute(text(self.base_query)))[0]
        self.initial = [str(res) for res in result]

        try:
            catNames = list(db.engine.execute(text(self.category_query)))[0]
            self.initialCats = [cat for cat in catNames]
        except:
            pass
  
        self.input_addbook_picture.setText(self.initial[0])
        self.input_publisher_name_2.setText(self.initial[1])
        self.input_publisher_author.setText(self.initial[2])
        self.plainTextEdit_publisher_description.setPlainText(self.initial[3])
        self.input_publisher_quantity.setText(self.initial[4])
        self.pubCombo1.setCurrentText(self.initial[5])
        self.input_publisher_price.setText(self.initial[6])
        
        for index, cat in enumerate(self.categoryBoxes):
            if cat.objectName() in self.initialCats:
                self.categoryBoxes[index].setChecked(True)

    # Function to update book information in the database
    def update_info(self):
        from codefiles.bookstore_interface import Ui_MainWindow
        import codefiles.bookstore_interface

        self.newData = [
            self.input_addbook_picture.text(),
            self.input_publisher_name_2.text(),
            self.input_publisher_author.text(),
            self.plainTextEdit_publisher_description.toPlainText(),
            self.input_publisher_quantity.text(),
            self.pubCombo1.currentText(),
            self.input_publisher_price.text()
        ]
        selectedCategories = []
        for cat in self.categoryBoxes:
            if cat.isChecked():
                selectedCategories.append(cat.objectName())


        nochanges = (self.newData == self.initial) and (self.initialCats == selectedCategories)
        if nochanges:
            self.OkMsgBox("warning", "process fail", "There are no changes detected!")
        elif '' in self.newData:
            self.OkMsgBox("warning", "process fail", "input field/fields can not be empty!")
        elif not self.newData[4].isdigit() or not self.newData[6].isdigit():
            self.OkMsgBox("warning", "process fail", "Invalid input for price or quantity!")
        else:            
            
            try:
                url = str(random.randint(9999,9999999))+"_"+os.path.basename(self.newData[0])
                shutil.copy(self.newData[0], f"pictures/{url}")
                self.newData[0] = url

                    
                query = f"SELECT id FROM Publisher WHERE name='{self.newData[5]}'"
                publisher_id = list(db.engine.execute(text(query)))[0][0]

                query = f"DELETE FROM book_publisher WHERE book_id={self.book_id}"
                db.engine.execute(text(query))

                query = "INSERT INTO book_publisher(book_id, publisher_id, quantity)"\
                        +f"\n    VALUES({self.book_id}, {publisher_id}, {self.newData[4]})"
                db.engine.execute(text(query))

                query = f"DELETE FROM book_category WHERE book_id={self.book_id}"
                db.engine.execute(text(query))
                for cat in self.categoryBoxes:
                        if cat.isChecked():
                            query = f"SELECT id FROM category WHERE name='{cat.objectName()}'"
                            category_id = list(db.engine.execute(text(query)))[0][0]
                            query = f"INSERT INTO book_category(book_id, category_id) VALUES({self.book_id}, {category_id})"
                            db.engine.execute(text(query))

                query = "UPDATE Book"\
                        +f"\n   SET name='{self.newData[1]}', author='{self.newData[2]}',"\
                        +f"\n   picture_url='{self.newData[0]}', price={self.newData[6]}, description='{self.newData[3]}'"\
                        +f"\n   WHERE id={self.book_id}"
                db.engine.execute(text(query))
                self.OkMsgBox("information", "success", "Book info updated sucessfully!")
                self.initial = self.newData
            except:               
                self.OkMsgBox("warning", "process fail", "Something went wrong while uploading photo!")
            
           
        Ui_MainWindow.update_main_window(self.main_self)

    # Function to get a picture file using file dialog
    def getPicture(self):
        url, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'New Photo', '', '(*.jpg *.gif *.png *.jpeg)')
        self.input_addbook_picture.setText(url)

    # Function to set up the UI components
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 346, 494))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_addbook_main = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_addbook_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_addbook_main.setObjectName("gridLayout_addbook_main")
        self.label_addbook_picture = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_picture.setObjectName("label_addbook_picture")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_picture, 7, 0, 1, 1)
        self.label_addbook_author = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_author.setObjectName("label_addbook_author")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_author, 1, 0, 1, 1)
        self.input_publisher_name_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_publisher_name_2.setObjectName("input_publisher_name_2")
        self.gridLayout_addbook_main.addWidget(self.input_publisher_name_2, 0, 1, 1, 1)
        self.input_publisher_author = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_publisher_author.setObjectName("input_publisher_author")
        self.gridLayout_addbook_main.addWidget(self.input_publisher_author, 1, 1, 1, 1)
        self.label_addbook_category = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_category.setObjectName("label_addbook_category")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_category, 6, 0, 1, 1)
        self.label_addbook_description = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_description.setObjectName("label_addbook_description")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_description, 4, 0, 1, 1)
        self.plainTextEdit_publisher_description = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_publisher_description.setObjectName("plainTextEdit_publisher_description")
        self.gridLayout_addbook_main.addWidget(self.plainTextEdit_publisher_description, 4, 1, 1, 1)
        # publisher to do selection of combo box
        self.pubCombo1 = QtWidgets.QComboBox(self.layoutWidget)
        self.gridLayout_addbook_main.addWidget(self.pubCombo1, 5, 1, 1, 1)
        publishers = self.getPublishers()
        self.pubCombo1.addItems(publishers)

        self.input_publisher_quantity = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_publisher_quantity.setObjectName("input_publisher_quantity")
        self.gridLayout_addbook_main.addWidget(self.input_publisher_quantity, 3, 1, 1, 1)
        self.scrollArea_addbook_category = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea_addbook_category.setWidgetResizable(True)
        self.scrollArea_addbook_category.setObjectName("scrollArea_addbook_category")
        self.scrollAreaWidgetContents_addbook_main = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_addbook_main.setGeometry(QtCore.QRect(0, 0, 254, 68))
        self.scrollAreaWidgetContents_addbook_main.setObjectName("scrollAreaWidgetContents_addbook_main")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_addbook_main)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # category to check the boxes
        self.placeCatBoxes()

        self.scrollArea_addbook_category.setWidget(self.scrollAreaWidgetContents_addbook_main)
        self.gridLayout_addbook_main.addWidget(self.scrollArea_addbook_category, 6, 1, 1, 1)
        self.label_addbook_quantity = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_quantity.setObjectName("label_addbook_quantity")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_quantity, 3, 0, 1, 1)
        self.button_addbook_submit = QtWidgets.QPushButton(self.layoutWidget)
        self.button_addbook_submit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.button_addbook_submit.setObjectName("button_addbook_submit")
        # submit the button event handler
        self.button_addbook_submit.clicked.connect(lambda: self.update_info())

        self.gridLayout_addbook_main.addWidget(self.button_addbook_submit, 8, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_addbook_publisher = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_publisher.setObjectName("label_addbook_publisher")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_publisher, 5, 0, 1, 1)
        self.input_publisher_price = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_publisher_price.setObjectName("input_publisher_price")
        self.gridLayout_addbook_main.addWidget(self.input_publisher_price, 2, 1, 1, 1)
        self.label_addbook_price = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_price.setObjectName("label_addbook_price")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_price, 2, 0, 1, 1)
        self.frame_addbook_picture = QtWidgets.QFrame(self.layoutWidget)
        self.frame_addbook_picture.setMinimumSize(QtCore.QSize(0, 38))
        self.frame_addbook_picture.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_addbook_picture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addbook_picture.setObjectName("frame_addbook_picture")
        self.button_addbook_broswer = QtWidgets.QPushButton(self.layoutWidget)
        self.button_addbook_broswer.setMaximumSize(QtCore.QSize(80, 24))
        self.button_addbook_broswer.setMinimumSize(QtCore.QSize(80, 24))
        self.button_addbook_broswer.setGeometry(QtCore.QRect(95, 470, 80, 24))
        self.button_addbook_broswer.setObjectName("button_addbook_broswer")
        # picture's browse button event handler
        self.button_addbook_broswer.clicked.connect(lambda: self.getPicture())

        self.input_addbook_picture = QtWidgets.QLineEdit(self.frame_addbook_picture)
        self.input_addbook_picture.setGeometry(QtCore.QRect(0, 10, 500, 21))
        self.input_addbook_picture.setMinimumSize(QtCore.QSize(500, 0))
        self.input_addbook_picture.setObjectName("input_addbook_picture")
        self.gridLayout_addbook_main.addWidget(self.frame_addbook_picture, 7, 1, 1, 1)
        self.label_addbook_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_addbook_name.setObjectName("label_addbook_name")
        self.gridLayout_addbook_main.addWidget(self.label_addbook_name, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menu_bar.setObjectName("menu_bar")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        # the initial fill
        self.fillInfo()

        self.translateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Function to translate the UI components
    def translateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit.Book.Info"))
        self.label_addbook_picture.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Image_Link</span></p></body></html>"))
        self.label_addbook_author.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Author</span></p></body></html>"))
        self.label_addbook_category.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Genres</span></p></body></html>"))
        self.label_addbook_description.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Book_Summary</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_addbook_quantity.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Quantity</span></p></body></html>"))
        self.button_addbook_submit.setText(_translate("MainWindow", "Submit_The_Edit"))
        self.label_addbook_publisher.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Publisher</span></p></body></html>"))
        self.label_addbook_price.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Price</span></p></body></html>"))
        self.button_addbook_broswer.setText(_translate("MainWindow", "Explorer"))
        self.label_addbook_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:11pt;\">Title</span></p></body></html>"))

