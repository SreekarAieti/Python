import sqlite3 as s
from root_models.dbfuns import *
from tkinter import messagebox

class AuthModel:

    def __init__(self):
        self.conn = s.connect('users_db')
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
        self.create_table(self.cursor)
        self.createAuser()

    def create_table(self,c):
        query1='''CREATE TABLE IF NOT EXISTS "authentic_user" (
	            "id"	INTEGER ,
	            "role"	TEXT NOT NULL,
	            PRIMARY KEY("id")
                )'''
        query2='''CREATE TABLE IF NOT EXISTS "users" (
                "id"	INTEGER,
                "name"	TEXT,
                "email"	TEXT,
                "phone"	INTEGER ,
                "password"	TEXT,
                "role"	TEXT,
                PRIMARY KEY (id),
                FOREIGN KEY (id) REFERENCES authentic_user
                )'''
        query3 = '''create table  if not exists attendance(
                attd_id integer primary key AUTOINCREMENT,
                user_id integer,
                date default current_date ,
                time default current_time ,
                status text,
                foreign key(user_id) references users on delete cascade 
                )'''
        try:
            c.execute(query1)
            c.execute(query2)
            c.execute(query3)
            self.conn.commit()
        except:
            print('some db error in create_table')

    def createAuser(self):
        query1 = '''SELECT * FROM authentic_user WHERE id=1'''
        query = '''insert into authentic_user values(1,'admin')'''
        try:
            status = fetchone_fun(self.conn, query1)
            if status:
                pass
            else:
                result = execute_fun(self.conn, query)
                self.conn.commit()
        except:
            print('error')
    def getUser(self, id, password):
        query = "SELECT * FROM users WHERE id='%s'" % (id)
        try:
            result = fetchone_fun(self.conn, query)
            return result
        except:
            print('some db error in getUser')

    def getUserrole(self,id):
        query1="SELECT role FROM authentic_user WHERE id='%s'"%(id)
        query2="SELECT id FROM users WHERE id='%s'"%(id)
        try:
            result=[]
            data=fetchone_fun(self.conn,query1)
            result.append(data)
            data=fetchone_fun(self.conn,query2)
            result.append(data)
            return  result
        except s.Error as e:
            print("some db error in getUserRole",e)

    def User_delete(self,id):
        query="DELETE FROM users WHERE id='%s'"%(id)
        try:
            result = execute_fun(self.conn,query)
            self.conn.commit()
            return result
        except:
            print("some db error in getUserRole")
    def createUser(self, id,names,email, phone, password, role):
        query = "INSERT INTO users (id,name,email,phone,password,role) VALUES('%s','%s','%s','%s','%s','%s')" % (id,names,email, phone, password, role)
        try:
            result = insert_fun(self.conn, query)
            if result==True:
                return True
            else:
                return result
        except:
            messagebox.showinfo('AuthModel','error in createUser')

    def update_attendance(self, id):
            query = f'''insert into attendance(user_id,status) values ('%s','%s')''' % (id, 'ACTIVE')
            try:
                result = execute_fun(self.conn, query)
                self.conn.commit()
                return True
            except:
                print('some thig went wrong while inserting the attendace')
                return False

    def get_all(self,id):
        if not id:
            query = 'SELECT * FROM attendance'
        else:
            query='''select * from attendance where user_id="%s"'''%(id)
        try:
            result = fetchall_fun(self.conn, query)
            self.conn.commit()
            return result
        except:
            print('some thig went wrong while inserting the attendace')
            return False

    def get_id(self,id):
        query='''select id,name,email,phone from users where id="%s"'''%(id)
        result=fetchone_fun(self.conn,query)
        self.conn.commit()
        if result:
            return  result
        else:
            return False

    def updating(self,id,name,gmail,phone):
        query='''update users set name="%s",email="%s",phone="%s" where id="%s"'''%(name,gmail,phone,id)
        result= execute_fun(self.conn, query)
        self.conn.commit()
        if result:
            return True
        else:
            return False

    def add_to_table(self,id,role):
        query='''insert into authentic_user(id, role) values("%s","%s")'''%(id,role)
        result=execute_fun(self.conn,query)
        self.conn.commit()
        if result:
            return True
        else:
            return False