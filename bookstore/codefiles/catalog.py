from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import time
from os.path import exists


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#Defining SQL queries to create tables and fill them with initial data in a SQLite database.
tableQueries = [

    "CREATE TABLE User("
    +"\n    id INTEGER PRIMARY KEY AUTOINCREMENT,"
    +"\n    username VARCHAR(100) UNIQUE NOT NULL,"
    +"\n    password VARCHAR(150) NOT NULL,"
    +"\n    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    +"\n    is_admin BOOLEAN DEFAULT FALSE"
    +"\n );",

     
    "CREATE TABLE Customer("
    +"\n    user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
    +"\n    first_name VARCHAR(100) NOT NULL,"
    +"\n    last_name VARCHAR(150) NOT NULL,"
    +"\n    phone_number VARCHAR(20) NOT NULL,"
    +"\n    address TEXT NOT NULL,"
    +"\n    FOREIGN KEY(user_id) REFERENCES User(id)"
    +"\n );",
    
     
    "CREATE TABLE Book("
    +"\n    id INTEGER PRIMARY KEY AUTOINCREMENT,"
    +"\n    name VARCHAR(100) NOT NULL,"
    +"\n    author VARCHAR(150),"
    +"\n    picture_url VARCHAR(255),"
    +"\n    price INT NOT NULL,"
    +"\n    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    +"\n    description TEXT NOT NULL"
    +"\n );",

     
    "CREATE TABLE Publisher("
    +"\n    id INTEGER PRIMARY KEY AUTOINCREMENT,"
    +"\n    name VARCHAR(100) UNIQUE NOT NULL,"
    +"\n    phone_number VARCHAR(20) NOT NULL,"
    +"\n    website_url VARCHAR(255)"
    +"\n );",


    "CREATE TABLE Category("
    +"\n    id INTEGER PRIMARY KEY AUTOINCREMENT,"
    +"\n    name VARCHAR(100) NOT NULL"
    +"\n );",
     

   "CREATE TABLE book_order("
    +"\n    book_id INT,"
    +"\n    customer_id INT,"
    +"\n    publisher_id INT,"
    +"\n    quantity INT NOT NULL,"
    +"\n    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    +"\n    FOREIGN KEY(customer_id) REFERENCES Customer(user_id),"
    +"\n    FOREIGN KEY(book_id) REFERENCES Book(id),"
    +"\n    FOREIGN KEY(publisher_id) REFERENCES Publisher(id),"
    +"\n    PRIMARY key(book_id, customer_id)"
    +"\n );",


    "CREATE TABLE book_category("
    +"\n    book_id INT,"
    +"\n    category_id INT,"
    +"\n    FOREIGN KEY(book_id) REFERENCES Book(id),"
    +"\n    FOREIGN KEY(category_id) REFERENCES Category(id),"
    +"\n    PRIMARY key(book_id, category_id)"
    +"\n );",


    "CREATE TABLE book_publisher("
    +"\n    book_id INT,"
    +"\n    publisher_id INT,"
    +"\n    quantity INT NOT NULL,"
    +"\n    FOREIGN KEY(book_id) REFERENCES Book(id),"
    +"\n    FOREIGN KEY(publisher_id) REFERENCES Publisher(id),"
    +"\n    PRIMARY key(book_id, publisher_id)"
    +"\n );",

]

dataFillQueries = [

    "INSERT INTO  User(Username, Password, Isadmin)"
    +"\n    VALUES('SY', '123456', TRUE),"
    +"\n    ('OW', '123456', TRUE),"
    +"\n    ('KC', '123456', FALSE),"
    +"\n    ('HL', '123456', FALSE);",

    "INSERT INTo customer(First_Name,Last_Name, user_id, Phone_No., Address)"
    +"\n    VALUES('salma', 'yasser', 2, '01139399201', 'UTMKL.'),"
    +"\n    ('ong', 'wee', 3, '0105380384', 'UTMKL.'),"
    +"\n     ('khoo', 'ching', 4, '0112762653', 'UTMKL.'),"
    +"\n     ('Haris', 'Lutfi', 5, '01139568566', 'UTMKL.');",


    "INSERT INTO book(Title, Author, Image_Link, Price, Book_Summary)"
    +"\n    VALUES('THE 156-STORY TREEHOUSE', 'ANDY GRIFFITHS','156-story-treehouse-hc.png',"
    +"\n    RM50, 'Andy and Terry are celebrating Christmas in their 156-storey treehouse which now has 13 new storeys'),"
    +"\n    ('A MILLION TO ONE, 'TONY FAGGIOLI','A MILLION TO ONE.jpg',"
    +"\n    RM50, 'As our story unfolds, it becomes clear that there is hell, and then there is hell on earth.And worst of all...there are some demons you never see coming.'),"
    +"\n    ('HARRY POTTER AND THE CURESED CHILD', 'J.K.ROWLING','Harry-Potter-and-the-Cursed-Child-Special-Rehearsal.jpg',"
    +"\n    RM50, 'It is about the journey Albus takes while growing up, and the roles he and his best friend, play when dark forces, once again threaten the fate of the planet.'),"
    +"\n    ('LADYBIRD BY DESIGN', 'LAWRENCE ZEEGEN','Ladybird by design.jpeg',"
    +"\n    RM40, ' A delightful trip down memory lane. Swamped with those well loved and fondly remembered texts that were part of our upbringing.'),"
    +"\n    ('SURVIVAL GUIDE MAKING FRIENDS', 'CRIST, JAMES J','s705_survival_guide_making_friends.jpg',"
    +"\n    RM30, 'Friendships make us happier and healthier.'),"
    +"\n    ('THE FIRST WORLD WAR', 'JOHN KEEGAN','THE FIRST WORLD WAR.jpeg',"
    +"\n    RM20, 'The First World War created the modern world. A conflict of unprecedented ferocity, it abruptly ended the relative peace and prosperity of the Victorian era, unleashing such demons of the twentieth century as mechanized warfare and mass death.'),"
    +"\n    ('THE LORD OF THE RINGS PART ONE: THE FELLOWSHIP OF THE RING', 'J.R.R.TOLKIEN','The lord of the rings.jpg',"
    +"\n    RM60, 'The Fellowship of the Ring consists of nine walkers who set out on the quest to destroy the One Ring, in opposition to the nine Black Riders: Frodo Baggins, Sam Gamgee, Merry Brandybuck and Pippin Took; Gandalf; the Men Aragorn and Boromir, son of the Steward of Gondor; the Elf Legolas; and the Dwarf Gimli.'),"
    +"\n    ('THE PAST IS RISING, 'KATHRYN BYWATERS','THE PAST IS RISING.jpg',"
    +"\n    RM70, 'The Past Is Rising is a compelling fantasy epic that revolves around the uprising of dark forces bent on wresting a kingdom from its rightful rulers. Several warriors will discover that their true destinies are to salvage their kingdom and defeat the rising evil. At fourteen, Erik dreams of past glories.'),"
    +"\n    ('YELLOWFACE, 'R.F.KUANG','YELLOWFACE.jpg',"
    +"\n    RM80, 'A satire of racial diversity in the publishing industry as well as a metafiction about social media, particularly Twitter. Yellowface is Kuang's first venture into literary fiction'),"
    +"\n    ('Encyclopedic Dictionary Of English Usage, 'N.H.Mager and S.K.Mager','DICTIONARY.jpg',"
    +"\n    RM100, 'Dictionary Book');",

    "INSERT INTO publisher(Publisher_Name, Phone_Number, Website_Link)"
    +"\n    VALUES('GRIFFITHS', '123445', 'https://www.andygriffiths.com.au/'),"
    +"\n    ('FAGGIOLI', '234566', 'https://tonyfaggioli.com/'),"
    +"\n    ('Rowling', '346773', 'https://en.wikipedia.org/wiki/J._K._Rowling'),"
    +"\n    ('ZEEGEN', '456782', 'https://zeegen.me/'),"
    +"\n    ('JAMES J', '456782', 'https://www.jamesjcrist.com/books.html'),"
    +"\n    ('KEEGAN', '456782', 'https://en.wikipedia.org/wiki/John_Keegan'),"
    +"\n    ('TOLKIEN', '456782', 'https://www.tolkiensociety.org/author/biography/'),"
    +"\n    ('BYWATERS', '456782', 'https://www.kathrynbywaters.com/about'),"
    +"\n    ('KUANG', '456782', 'https://en.wikipedia.org/wiki/R._F._Kuang'),"
    +"\n    ('Mager', '456782', 'https://www.goodreads.com/book/show/5651551-the-complete-letter-writer');",


    "INSERT INTO category(name)"
    +"\n    VALUES('Novel'), ('History'), ('Educational'),"
    +"\n    ('Philosophy'), ('Litrature'), ('Children'), (Encyclopedic)"
    +"\n    ('Comic');",


    "INSERT INTO book_order(book_id, customer_id, publisher_id, quantity)"
    +"\n    VALUES(1, 2, 3, 12),"
    +"\n    (3, 2, 3, 3),"
    +"\n    (6, 3, 2, 1),"
    +"\n    (8, 4, 1, 2),"
    +"\n    (4, 5, 1, 7),"
    +"\n    (5, 2, 4, 4);",

    
    "INSERT INTO book_category(book_id, category_id)"
    +"\n    VALUES(1, 1), (1, 5), (2, 1),(2, 5), (3, 1), (3, 5),(3, 7), (4, 1), (4, 5), (5, 3), (5, 6),"
    +"\n    (6, 4), (6, 2), (6, 7),(7, 1), (7, 2), (7, 8),(8, 1), (8, 9), (8, 8);",


    "INSERT INTO book_publisher(book_id, publisher_id, quantity)"
    +"\n    VALUES(1, 3, 0), (2, 5, 10), (3, 3, 16), (4, 1, 1), (5, 4, 17), (6, 2, 110),"
    +"\n    (7, 2, 76), (8, 1, 35);"

]


file_exists = exists('codefiles/db.sqlite3')

if not file_exists:
    for table in tableQueries:
        print(table)
        db.engine.execute(text(table))

    for table in dataFillQueries:
        print(table)
        db.engine.execute(text(table))
    