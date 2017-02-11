import mysql.connector as mysql

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

def db(method, data):

        try:
            db = mysql.connect("fishackathonide.database.windows.net","fishackathonide","hackathonide4!","",charset='utf8')
            cursor = db.cursor()

        except mysql.Error as e:
          print(e)

