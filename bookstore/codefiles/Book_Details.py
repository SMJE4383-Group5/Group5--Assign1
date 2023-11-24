from PyQt5 import QtCore, QtGui, QtWidgets
from codefiles.catalog import db
from sqlalchemy import text


class Ui_BookDetailWindow(object):

    # Initialization function, setting initial variables
    def __init__(self, book_id):
        # Initializing data for the book detail view
        self.close_button = None
        self.book_id = book_id
        # Base SQL query for retrieving book details
        self.base_query ="SELECT Book.picture_url, Book.name, Book.author, Book.description, book_publisher.quantity,"\
                        +"\n    Publisher.name, Book.date_added, Book.price "\
                        +"\n    FROM book_publisher"\
                        +"\n    JOIN Book ON book_publisher.book_id=Book.id"\
                        +"\n    JOIN Publisher ON Publisher.id=book_publisher.publisher_id"\
                        +"\n    LEFT JOIN book_order ON book_order.book_id=book.id and book_order.publisher_id=Publisher.id"\
                        +"\n    GROUP BY Book.id, Publisher.id"\
                        +f"\n    HAVING Book.id={self.book_id}"

        # SQL query for retrieving book categories, THE CATEGORY REPRESENT THE GENRES OF BOOKS
        self.category_query = "SELECT Category.name FROM Category JOIN book_category ON Category.id=book_category.category_id"+\
                            f"\n    WHERE book_category.book_id={self.book_id}"
        # Execute queries and store book details
        self.bookData = list(db.engine.execute(text(self.base_query)))
        self.bookData = self.bookData[0]

    # Function to fill in book details into the UI elements
    def fill_Items(self):

        categories = []
        bookData = self.bookData
        try:  # Retrieve and handle book categories
            catNames = list(db.engine.execute(text(self.category_query)))[0]
            categories = [cat for cat in catNames]
        except:
            categories = "There is no category"
        # Set labels in the User Interface with book details
        self.book_name_detail_label.setText(bookData[1])
        self.author_book_detail_label.setText(bookData[2])
        self.description_book_detail_label.setText(bookData[3])
        self.quantity_book_detail_label.setText(str(bookData[4]))
        self.publisher_book_detail_label.setText(bookData[5])
        self.date_book_detail_label.setText(bookData[6])
        self.price_book_detail_label.setText(str(bookData[7]))
        self.category_book_detail_label.setText(str(categories))

    # Function to close the Book Detail Window
    def close_the_window(self, BookDetailWindow):
        BookDetailWindow.deleteLater()

    # Set up User Interface elements for the book detail window
    def setupUi(self, BookDetailWindow):
        BookDetailWindow.setObjectName("BookDetailWindow")
        BookDetailWindow.resize(327, 674)
        # Set up main frame and other User Interface components
        self.central_widget = QtWidgets.QWidget(BookDetailWindow)
        self.central_widget.setObjectName("central_widget")
        self.main_frame = QtWidgets.QFrame(self.central_widget)
        self.main_frame.setGeometry(QtCore.QRect(20, 20, 301, 611))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.detail_book_image = QtWidgets.QGraphicsView(self.main_frame)
        self.detail_book_image.setStyleSheet("#detail_book_image { background-image: url(pictures/" + self.bookData[
            0] + ");background-repeat: no-repeat;background-attachment: fixed;background-position: center;border:0px;}")
        self.detail_book_image.setGeometry(QtCore.QRect(10, 10, 261, 191))
        self.detail_book_image.setObjectName("detail_book_image")
        self.scrollArea = QtWidgets.QScrollArea(self.main_frame)
        self.scrollArea.setGeometry(QtCore.QRect(9, 209, 281, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollView_book_detail = QtWidgets.QWidget()
        self.scrollView_book_detail.setGeometry(QtCore.QRect(0, -208, 265, 557))
        self.scrollView_book_detail.setObjectName("scrollView_book_detail")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollView_book_detail)
        self.gridLayout.setObjectName("gridLayout")
        self.quantity_book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.quantity_book_detail.setMinimumSize(QtCore.QSize(0, 50))
        self.quantity_book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.quantity_book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quantity_book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quantity_book_detail.setObjectName("quantity_book_detail")
        self.quantity_book_detail_title_label = QtWidgets.QLabel(self.quantity_book_detail)
        self.quantity_book_detail_title_label.setGeometry(QtCore.QRect(10, 19, 58, 16))
        self.quantity_book_detail_title_label.setObjectName("quantity_book_detail_title_label")
        self.quantity_book_detail_label = QtWidgets.QLabel(self.quantity_book_detail)
        self.quantity_book_detail_label.setGeometry(QtCore.QRect(87, 19, 151, 20))
        self.quantity_book_detail_label.setObjectName("quantity_book_detail_label")
        self.gridLayout.addWidget(self.quantity_book_detail, 3, 0, 1, 1)
        self.description__book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.description__book_detail.setMinimumSize(QtCore.QSize(0, 100))
        self.description__book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.description__book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.description__book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description__book_detail.setObjectName("description__book_detail")
        self.description_book_detail_label = QtWidgets.QLabel(self.description__book_detail)
        self.description_book_detail_label.setGeometry(QtCore.QRect(10, 10, 241, 71))
        self.description_book_detail_label.setObjectName("description_book_detail_label")
        self.gridLayout.addWidget(self.description__book_detail, 2, 0, 1, 1)
        self.book_name_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.book_name_detail.setMinimumSize(QtCore.QSize(0, 55))
        self.book_name_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.book_name_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.book_name_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.book_name_detail.setObjectName("book_name_detail")
        self.book_name_detail_label = QtWidgets.QLabel(self.book_name_detail)
        self.book_name_detail_label.setGeometry(QtCore.QRect(10, 13, 231, 31))
        self.book_name_detail_label.setObjectName("book_name_detail_label")
        self.gridLayout.addWidget(self.book_name_detail, 0, 0, 1, 1)
        self.price_book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.price_book_detail.setMinimumSize(QtCore.QSize(0, 50))
        self.price_book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.price_book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.price_book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.price_book_detail.setObjectName("price_book_detail")
        self.price_book_detail_title_label = QtWidgets.QLabel(self.price_book_detail)
        self.price_book_detail_title_label.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.price_book_detail_title_label.setObjectName("price_book_detail_title_label")
        self.price_book_detail_label = QtWidgets.QLabel(self.price_book_detail)
        self.price_book_detail_label.setGeometry(QtCore.QRect(60, 20, 171, 20))
        self.price_book_detail_label.setObjectName("price_book_detail_label")
        self.gridLayout.addWidget(self.price_book_detail, 7, 0, 1, 1)
        self.date_book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.date_book_detail.setMinimumSize(QtCore.QSize(0, 50))
        self.date_book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.date_book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_book_detail.setObjectName("date_book_detail")
        self.date_book_detail_title_label = QtWidgets.QLabel(self.date_book_detail)
        self.date_book_detail_title_label.setGeometry(QtCore.QRect(10, 17, 81, 16))
        self.date_book_detail_title_label.setObjectName("date_book_detail_title_label")
        self.date_book_detail_label = QtWidgets.QLabel(self.date_book_detail)
        self.date_book_detail_label.setGeometry(QtCore.QRect(90, 15, 151, 20))
        self.date_book_detail_label.setObjectName("date_book_detail_label")
        self.gridLayout.addWidget(self.date_book_detail, 5, 0, 1, 1)
        self.author_book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.author_book_detail.setMinimumSize(QtCore.QSize(0, 55))
        self.author_book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.author_book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.author_book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.author_book_detail.setObjectName("author_book_detail")
        self.author_book_detail_label = QtWidgets.QLabel(self.author_book_detail)
        self.author_book_detail_label.setGeometry(QtCore.QRect(50, 13, 191, 31))
        self.author_book_detail_label.setObjectName("author_book_detail_label")
        self.author_book_detail_title_label = QtWidgets.QLabel(self.author_book_detail)
        self.author_book_detail_title_label.setGeometry(QtCore.QRect(20, 21, 21, 16))
        self.author_book_detail_title_label.setObjectName("author_book_detail_title_label")
        self.gridLayout.addWidget(self.author_book_detail, 1, 0, 1, 1)
        self.publisher_book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.publisher_book_detail.setMinimumSize(QtCore.QSize(0, 50))
        self.publisher_book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.publisher_book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.publisher_book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.publisher_book_detail.setObjectName("publisher_book_detail")
        self.publisher_book_detail_title_label = QtWidgets.QLabel(self.publisher_book_detail)
        self.publisher_book_detail_title_label.setGeometry(QtCore.QRect(10, 16, 61, 16))
        self.publisher_book_detail_title_label.setObjectName("publisher_book_detail_title_label")
        self.publisher_book_detail_label = QtWidgets.QLabel(self.publisher_book_detail)
        self.publisher_book_detail_label.setGeometry(QtCore.QRect(90, 16, 161, 20))
        self.publisher_book_detail_label.setObjectName("publisher_book_detail_label")
        self.gridLayout.addWidget(self.publisher_book_detail, 4, 0, 1, 1)
        self.category_book_detail = QtWidgets.QFrame(self.scrollView_book_detail)
        self.category_book_detail.setMinimumSize(QtCore.QSize(0, 87))
        self.category_book_detail.setMaximumSize(QtCore.QSize(16777215, 70))
        self.category_book_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_book_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_book_detail.setObjectName("category_book_detail")
        self.category_book_detail_title_label = QtWidgets.QLabel(self.category_book_detail)
        self.category_book_detail_title_label.setGeometry(QtCore.QRect(10, 10, 58, 16))
        self.category_book_detail_title_label.setMinimumSize(QtCore.QSize(0, 0))
        self.category_book_detail_title_label.setObjectName("category_book_detail_title_label")
        self.category_book_detail_label = QtWidgets.QLabel(self.category_book_detail)
        self.category_book_detail_label.setGeometry(QtCore.QRect(80, 9, 161, 71))
        self.category_book_detail_label.setObjectName("category_book_detail_label")
        self.gridLayout.addWidget(self.category_book_detail, 6, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollView_book_detail)
        self.close_button = QtWidgets.QPushButton(self.main_frame)
        self.close_button.setGeometry(QtCore.QRect(100, 570, 80, 24))
        self.close_button.clicked.connect(lambda: self.close_the_window(BookDetailWindow))
        self.close_button.setObjectName("close_button")
        BookDetailWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(BookDetailWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 327, 21))
        self.menu_bar.setObjectName("menu_bar")
        BookDetailWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(BookDetailWindow)
        self.status_bar.setObjectName("status_bar")
        BookDetailWindow.setStatusBar(self.status_bar)

        # call fill items function to fill in the data
        self.fill_Items()
        # Set up translations and connect signals
        self.translateUi(BookDetailWindow)
        QtCore.QMetaObject.connectSlotsByName(BookDetailWindow)

    # Function to translate the User Interface components
    def translateUi(self, BookDetailWindow):
        # Translate User Interface elements
        _translate = QtCore.QCoreApplication.translate
        BookDetailWindow.setWindowTitle(_translate("BookDetailWindow", "Book_Details"))
        self.quantity_book_detail_title_label.setText(_translate("BookDetailWindow", "Stock:"))
        # self.quantity_book_detail_label.setText(_translate("BookDetailWindow", "20"))
        self.price_book_detail_title_label.setText(_translate("BookDetailWindow", "Price:"))
        # self.price_book_detail_label.setText(_translate("BookDetailWindow", "50"))
        self.date_book_detail_title_label.setText(_translate("BookDetailWindow", "Time_Added:"))
        # self.date_book_detail_label.setText(_translate("BookDetailWindow", "2023/11/18"))
        # self.author_book_detail_label.setText(_translate("BookDetailWindow", "ANDY GRIFFITHS"))
        self.author_book_detail_title_label.setText(_translate("BookDetailWindow", "By: "))
        self.publisher_book_detail_title_label.setText(_translate("BookDetailWindow", "Publisher:"))
        # self.publisher_book_detail_label.setText(_translate("BookDetailWindow", "GRIFFITHS"))
        self.category_book_detail_title_label.setText(_translate("BookDetailWindow", "Genres:"))
        # self.category_book_detail_label.setText(_translate("BookDetailWindow", "children"))
        self.close_button.setText(_translate("BookDetailWindow", "Close_Button"))