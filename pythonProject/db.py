import mysql.connector

class DB:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="classicmodels"
        )

    def find_all_table_names(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")
        myresult = mycursor.fetchall()

        result = []
        for x in myresult:
            result.append(x[0])

        return result

    def find_all_rows_in_table(self,table_name):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM " + table_name)
        myresult = mycursor.fetchall()

        result = []
        for x in myresult:
            row = []
            for y in x:
                row.append(str(y))
            result.append(row)

        return result


