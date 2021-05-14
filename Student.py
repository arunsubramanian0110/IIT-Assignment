import DB_Connection

class Student:
    def __init__(self):
        self.con = DB_Connection.db_connect()
        self.mycursor = self.con.cursor()

    def studentDetails(self):
        self.StudentID = int(input("Enter the Student ID: "))
        self.StudentName = input("Enter the Student Name: ")
        self.StudentDept = input("Enter the Department: ")
        self.Mark1 = int(input("Enter the Mark1: "))
        self.Mark2 = int(input("Enter the Mark2: "))
        self.Mark3 = int(input("Enter the Mark3: "))
        self.Mark4 = int(input("Enter the Mark4: "))
        self.Mark5 = int(input("Enter the Mark5: "))

        self.totalMark = self.total(self.Mark1,self.Mark2,self.Mark3,self.Mark4,self.Mark5)
        self.averageMark = self.average(self.totalMark)
        self.gradeValue = self.grade(self.averageMark)
        self.create_Table()
        self.insert_Values()
        self.display_values()
        self.updatedName = input("Enter the name to be updated: ")
        self.updatedID = int(input("Enter the Student ID to which name to be changed: "))
        self.update_Value()
        self.display_values()
        self.deleteName = input("Enter the Student Name to delete the student details: ")
        self.delete_Values()
        self.display_values()

    def total(self,Mark1,Mark2,Mark3,Mark4,Mark5):
        return Mark1+Mark2+Mark3+Mark4+Mark5

    def average(self,totalMark):
        return totalMark/5

    def grade(self,averageMark):
        if averageMark > 85:
            return "S"
        elif averageMark > 70 and averageMark <= 85:
            return "A"
        elif averageMark > 60 and averageMark <= 70:
            return "B"
        elif averageMark > 50 and averageMark <= 60:
            return "C"
        elif averageMark > 40 and averageMark <= 50:
            return "D"
        else:
            return "F"

    def create_Table(self):
        self.mycursor.execute(
            "CREATE TABLE student (s_id int(25) AUTO_INCREMENT PRIMARY KEY, s_name VARCHAR(35) NOT NULL, dept VARCHAR(30), m1 int(3), m2 int(3), m3 int(3), m4 int(3), m5 int(3), toatlmark int(3), averagemark int(3), grade VARCHAR(1))")
        print("Table Created")


    def insert_Values(self):
        values = (self.StudentID,self.StudentName,self.StudentDept,self.Mark1,self.Mark2,self.Mark3,self.Mark4,self.Mark5,self.totalMark,self.averageMark,self.gradeValue)
        sql_querry = "INSERT INTO student (s_id,s_name,dept,m1,m2,m3,m4,m5,toatlmark,averagemark,grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute(sql_querry,values)
        print(self.mycursor.rowcount, " rows inserted at ID:", self.mycursor.lastrowid)
        self.con.commit()

    def display_values(self):
        sql = "SELECT * FROM student"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

    def update_Value(self):
        sql = "UPDATE student set s_name = %s WHERE s_id = %s"
        val = (self.updatedName,self.updatedID)
        self.mycursor.execute(sql,val)
        print("Student Name Updated")
        self.con.commit()


    def delete_Values(self):
        sql = "DELETE FROM student WHERE s_name = %s"
        value = (self.deleteName)
        self.mycursor.execute(sql,value)
        print("1 Student Details Deleted")
        self.con.commit()


s = Student()
s.studentDetails()
