from tabulate import tabulate
import mysql.connector
connect=mysql.connector.connect(host="localhost",port="3306",user="root",password="_____",database=" _____")
########IN PASSWORD PART PUT YOUR SQL SERVER PASSWORD
def deposit ():
    ACCNO=input("ENTER THE ACCOUNT NUMBER: ")
    NAME=input("ENTER THE NAME: ")
    AMOUNT=int(input("ENTER THE AMOUNT: "))
    res=connect.cursor()
    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res.execute(sql,user)
    result=res.fetchone()
    total=result[0]+AMOUNT

    sql="update users set AMOUNT=%s where ACCNO=%s"
    totals=(total,ACCNO)
    res.execute(sql,totals)
    connect.commit()
    print("MONEY DEPOSITED SUCCESFULLY")
    pass

def withdraw ():
    ACCNO=input("ENTER THE ACCOUNT NUMBER: ")
    NAME=input("ENTER THE NAME: ")
    PASS=input("ENTER THE PASSWORD: ")
    AMOUNT=int(input("ENTER THE AMOUNT: "))
    res=connect.cursor()
    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res.execute(sql,user)
    result=res.fetchone()
    total=result[0]-AMOUNT

    sql="update users set AMOUNT=%s where ACCNO=%s"
    totals=(total,ACCNO)
    res.execute(sql,totals)
    connect.commit()
    print("MONEY WITHDRAWED SUCCESFULLY")

    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res=connect.cursor()
    res.execute(sql,user)
    result=res.fetchone()
    print("BALANCE FOR ",NAME, "IS", result[0] )
    pass

def balance():
    ACCNO=input("ENTER THE ACCOUNT NUMBER: ")
    NAME=input("ENTER THE NAME: ")
    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res=connect.cursor()
    res.execute(sql,user)
    result=res.fetchone()
    print("BALANCE FOR ",NAME, "IS", result[0] )
    pass

def admin(USERNAME,PASSWORD):
    qval=(USERNAME,PASSWORD)
    pass


def aahl():
    res=connect.cursor()
    sql="SELECT ACCNO,NAME,PHNO,ACCTYPE,AMOUNT from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ACCNO","NAME","PHNO","ACCTYPE","AMOUNT"]))
    pass
def accreate(ACCNO,NAME,PHNO,ACCTYPE,AMOUNT,PASS):
    res=connect.cursor()
    sql="insert into users(ACCNO,NAME,PHNO,ACCTYPE,AMOUNT,PASS) values (%s,%s,%s,%s,%s,%s)"
    user=(ACCNO,NAME,PHNO,ACCTYPE,AMOUNT,PASS)
    res.execute(sql,user)
    connect.commit()
    print("ACCOUNT CREATED SUCCESSFULLY")
    pass

def admincreate(USERNAME,NAME,PASS):
    res=connect.cursor()
    sql="insert into admins(USERNAME,NAME,PASS) values (%s,%s,%s)"
    admins=(USERNAME,NAME,PASS)
    res.execute(sql,admins)
    connect.commit()
    print("ACCOUNT CREATED SUCCESSFULLY")
    pass

def closeacc(ACCNO):
    res=connect.cursor()
    sql= "delete from users WHERE ACCNO=%s"
    user=(ACCNO,)
    res.execute(sql,user)
    connect.commit()
    print("ACCOUNT DELETED SUCCESSFULLY")
    pass

'''def modifyacc():
    ACCNO=int(input("ENTER ACCOUNT NUMBER: "))
    NAME=input("ENTER NAME: ")
               
    ACCTYPE=input("ENTER ACCOUNT TYPE (CURRENT/SAVINGS): ")
                    
    if ACCTYPE=="CURRENT":
        res=connect.cursor()
        ACTYPE="SAVINGS"
        print("")
        sql="replace into users ACCNO = %s,NAME = %s,ACCTYPE = %s"
        user=(ACCNO,NAME,ACTYPE)
        res.execute(sql,user)
        connect.commit()
        pass
    elif ACCTYPE=="SAVINGS":
        res=connect.cursor()
        sql="replace into users ACCNO = %s,NAME = %s,ACCTYPE = 'CURRENT'"
        user=(ACCNO,NAME,)
        res.execute(sql,user)
        connect.commit()
        pass'''
    


if connect:
    print("")
    
else:
    print("INVALID DATA")


        
# start of the program
ch=''
num=0
#intro()

while ch != 8:
    #system("cls");
    print("\t_______________________MAIN MENU__________________________")
    print("\t1. DEPOSIT AMOUNT")
    print("\t2. WITHDRAW AMOUNT")
    print("\t3. BALANCE ENQUIRY")
    print("\t4. ADMIN CONSOLE")
    print("\t5. ADMIN CREATION")
    print("\t6. EXIT")
    print("\tSelect Your Option (1-6) : ")
    ch = input("Enter your choice : ")
    #system("cls");
    
    if ch == '1':
        
       
        deposit()
        
    elif ch =='2':
        
        withdraw()
    elif ch == '3':
        balance()
    elif ch == '4':
        USERNAME=input("ENTER THE USER NAME: ")
        PASSWORD=input("ENTER THE PASSWORD: ")
        admin(USERNAME,PASSWORD)
        #ch= int(input("\tEnter The account No. : "))
        ac=''
        if ch=='4':
            
            while ac!=5:
                print("\t_________________ADMIN CONSOLE___________________")
                print("\t1. NEW ACCOUNT CREATION")
                print("\t2. ALL ACCOUNT HOLDERS LIST")
                print("\t3. CLOSE AN ACCOUNT")
                #print("\t4. MODIFY AN ACCOUNT(SAVINGS/CURRENT)")
                print("\t4. EXIT")
                print("\tSelect Your Option (1-4) : ")
                ac = input("Enter your choice : ")

                if ac=='1':
                    ACCNO=int(input("ENTER ACCOUNT NUMBER: "))
                    NAME=input("ENTER NAME: ")
                    PHNO=int(input("ENTER PHONE NUMBER: "))
                    ACCTYPE=input("ENTER ACCOUNT TYPE (CURRENT/SAVINGS): ")
                    AMOUNT=int(input("ENTER THE AMOUNT -DEFAULT(0-RS): "))
                    PASS=int(input("ENTER ACCOUNT PASSWORD: "))
                    accreate(ACCNO,NAME,PHNO,ACCTYPE,AMOUNT,PASS)
                   
                elif ac=='2':
                    aahl()
                    
                elif ac=='3':
                    ACCNO=int(input("ENTER ACCOUNT NUMBER: "))
                    #NAME=input("ENTER NAME: ")
                    #ACCTYPE=input("ENTER ACCOUNT TYPE (CURRENT/SAVINGS): ")
                    closeacc(ACCNO)
                
                    
                elif ac=='4':
                    break
                else:
                    print("INVALID CHOICE")
                    
                
            


        
        
    elif ch == '5':
        USERNAME=input("ENTER USER NAME: ")
        NAME=input("ENTER NAME: ")
        PASS=input("ENTER PASSWORD: ")
        admincreate(USERNAME,NAME,PASS)
        
        


        
        #display();
    
    elif ch == '6':
        print("\t__________________THANKS FOR USING SHAS BANK MANAGEMENT_______________________")
        break
    else :
        print("Invalid choice")
    
    #ch = input("Enter your choice : ")
===================================================================



