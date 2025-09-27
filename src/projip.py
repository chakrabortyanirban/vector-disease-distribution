#project ip
'''To create a platform which will provide a comparative analysis of vector borne diseases of 
different districts of West Bengal according to the data it is provided with. The user will be 
able to access data in the form of a graph; of different vector borne diseases and sort the 
data by district and health district and year.'''
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
#mydb=mysql.connector.connect(host="localhost",user="root",password="rishav2008",database="projip")
mydb=mysql.connector.connect(host="localhost",user="root",password="Password@123",database="projip")
cus=mydb.cursor()
def updation (cas,x):
    val=(cas,x)
    cus.execute(sql,val)
    mydb.commit()
    print("QUERY OK")
    
while True:    
    inpout=int(input('''to input data press1
    to delete press 2
    to analyse press 3'''))
    if inpout==1:
        yr=int(input('''press 1 to enter into database of present year
    press 2 to enter into database of last year
    press 3 to enter into database of year before last year'''))
        y=str(input("enter name the disease:"))
        cas=int(input("enter number of cases"))
        x=str(input("enter name of district:"))
        
        if yr==1:
            if y=="dengue":
                sql="UPDATE districtc SET dengue=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
            if y=="malaria":
                sql="UPDATE districtc SET malaria=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
            if y=="chikungunya":
                sql="UPDATE districtc SET chikungunya=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
            if y=="japanese_encephalitis":
                 sql="UPDATE districtc SET japanese_encephalitis=%s WHERE districtname =%s "
                 updation(cas,x)
                 print("QUERY OK")
            if y=="kala_azar":
                sql="UPDATE districtc SET kala_azar=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
            if y=="lymphatic_filariasis":
                sql="UPDATE districtc SET lymphatic_filariasis=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
        if yr==2:
             if y=="dengue":
                sql="UPDATE districtp SET dengue=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="malaria":
                sql="UPDATE districtp SET malaria=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="chikungunya":
                sql="UPDATE districtp SET chikungunya=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="japanese_encephalitis":
                 sql="UPDATE districtp SET japanese_encephalitis=%s WHERE districtname =%s "
                 updation(cas,x)
                 print("QUERY OK")
             if y=="kala_azar":
                sql="UPDATE districtp SET kala_azar=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="lymphatic_filariasis":
                sql="UPDATE districtp SET lymphatic_filariasis=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
        if yr==3:
             if y=="dengue":
                sql="UPDATE districtp1 SET dengue=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="malaria":
                sql="UPDATE districtp1 SET malaria=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="chikungunya":
                sql="UPDATE districtp1 SET chikungunya=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="japanese_encephalitis":
                 sql="UPDATE districtp1 SET japanese_encephalitis=%s WHERE districtname =%s "
                 updation(cas,x)
                 print("QUERY OK")
             if y=="kala_azar":
                sql="UPDATE districtp1 SET kala_azar=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
             if y=="lymphatic_filariasis":
                sql="UPDATE districtp1 SET lymphatic_filariasis=%s WHERE districtname =%s "
                updation(cas,x)
                print("QUERY OK")
            
            
            
    if inpout==2:
        yer=int(input('''press 1 to delete from database of present year
    press 2 to delete from database of last year
    press 3 to delete from database of year before last year'''))
        ch=int(input('''to delete all entries of a district press 1
    to delete all entries of a disease press 2
    to delete specific entries press 3'''))
        if yer==1:
            if ch==1:
                o=str(input("enter name of district"))
                sql1="UPDATE districtc SET malaria=NULL, dengue=NULL, japanese_encephalitis=NULL, kala_azar=NULL, lymphatic_filariasis=NULL WHERE districtname=%s"
                val=(o,)
                cus.execute(sql1,val)
                mydb.commit()
                print("QUERY OK")
            if ch==2:
                f=str(input("enter name of disease"))
                if f=="dengue":
                    sql="UPDATE districtc SET dengue=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="malaria":
                    sql="UPDATE districtc SET malaria=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="chikungunya":
                    sql="UPDATE districtc SET chikungunya=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="japanese_encephalitis":
                    sql="UPDATE districtc SET japanese_encephalitis=NULL"
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="kala_azar":
                    sql="UPDATE districtc SET kala_azar=NULL "
                    d=cus.execute(sql)
                    mydb.commit()
                    print("QUERY OK")
                if f=="lymphatic_filariasis":
                    sql="UPDATE districtc SET lymphatic_filariasis=NULL "
                    d=cus.execute(sql)
                    mydb.commit()
                    print("QUERY OK")
            if ch==3:
                 y=str(input("enter name the disease:"))
                 cas="NULL"
                 x=str(input("enter name of district:"))
                 if y=="dengue":
                     sql="UPDATE districtc SET dengue=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="malaria":
                     sql="UPDATE districtc SET malaria=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="chikungunya":
                     sql="UPDATE districtc SET chikungunya=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="japanese_encephalitis":
                      sql="UPDATE districtc SET japanese_encephalitis=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
                 if y=="kala_azar":
                      sql="UPDATE districtc SET kala_azar=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
                 if y=="lymphatic_filariasis":
                      sql="UPDATE districtc SET lymphatic_filariasis=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
        if yer==2:
            if ch==1:
                o=str(input("enter name of district"))
                sql1="UPDATE districtp SET malaria=NULL, dengue=NULL, japanese_encephalitis=NULL, kala_azar=NULL, lymphatic_filariasis=NULL WHERE districtname=%s"
                val=(o,)
                cus.execute(sql1,val)
                mydb.commit()
                print("QUERY OK")
            if ch==2:
                f=str(input("enter name of disease"))
                if f=="dengue":
                    sql="UPDATE districtp SET dengue=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="malaria":
                    sql="UPDATE districtp SET malaria=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="chikungunya":
                    sql="UPDATE districtp SET chikungunya=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="japanese_encephalitis":
                    sql="UPDATE districtp SET japanese_encephalitis=NULL"
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="kala_azar":
                    sql="UPDATE districtp SET kala_azar=NULL"
                    d=cus.execute(sql)
                    mydb.commit()
                    print("QUERY OK")
                if f=="lymphatic_filariasis":
                    sql="UPDATE districtp SET lymphatic_filariasis=NULL"
                    d=cus.execute(sql)
                    mydb.commit()
                    print("QUERY OK")
            if ch==3:
                 y=str(input("enter name the disease:"))
                 cas="NULL"
                 x=str(input("enter name of district:"))
                 if y=="dengue":
                     sql="UPDATE districtp SET dengue=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="malaria":
                     sql="UPDATE districtp SET malaria=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="chikungunya":
                     sql="UPDATE districtp SET chikungunya=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="japanese_encephalitis":
                      sql="UPDATE districtp SET japanese_encephalitis=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
                 if y=="kala_azar":
                      sql="UPDATE districtp SET kala_azar=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
                 if y=="lymphatic_filariasis":
                      sql="UPDATE districtp SET lymphatic_filariasis=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
        if yer==3:
            if ch==1:
                o=str(input("enter name of district"))
                sql1="UPDATE districtp1 SET malaria=NULL, dengue=NULL, japanese_encephalitis=NULL, kala_azar=NULL, lymphatic_filariasis=NULL WHERE districtname=%s"
                val=(o,)
                cus.execute(sql1,val)
                mydb.commit()
                print("QUERY OK")
            if ch==2:
                f=str(input("enter name of disease"))
                if f=="dengue":
                    sql="UPDATE districtp1 SET dengue=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="malaria":
                    sql="UPDATE districtp1 SET malaria=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="chikungunya":
                    sql="UPDATE districtp1 SET chikungunya=NULL  "
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="japanese_encephalitis":
                    sql="UPDATE districtp1 SET japanese_encephalitis=NULL"
                    d=cus.execute(sql)
                    mydb.commit()       
                    print("QUERY OK")
                if f=="kala_azar":
                    sql="UPDATE districtp1 SET kala_azar=NULL "
                    d=cus.execute(sql)
                    mydb.commit()
                    print("QUERY OK")
                if f=="lymphatic_filariasis":
                    sql="UPDATE districtp1 SET lymphatic_filariasis=NULL "
                    d=cus.execute(sql)
                    mydb.commit()
                    print("QUERY OK")
            if ch==3:
                 y=str(input("enter name the disease:"))
                 cas="NULL"
                 x=str(input("enter name of district:"))
                 if y=="dengue":
                     sql="UPDATE districtp1 SET dengue=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="malaria":
                     sql="UPDATE districtp1 SET malaria=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="chikungunya":
                     sql="UPDATE districtp1 SET chikungunya=%s WHERE districtname =%s "
                     updation(cas,x)
                     print("QUERY OK")
                 if y=="japanese_encephalitis":
                      sql="UPDATE districtp1 SET japanese_encephalitis=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
                 if y=="kala_azar":
                      sql="UPDATE districtp1 SET kala_azar=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
                 if y=="lymphatic_filariasis":
                      sql="UPDATE districtp1 SET lymphatic_filariasis=%s WHERE districtname =%s "
                      updation(cas,x)
                      print("QUERY OK")
            
            

    if inpout==3:
        ch3=int(input('''To retrieve raw data from database press 1
    To visualize in form of line graph press 2'''))
        if ch3==1:
             yer=int(input('''press 1 to retrive from database of present year
    press 2 to retrieve from database of last year
    press 3 to retrieve from database of year before last year'''))
             if yer==1:
                 sql="SELECT * FROM districtc"
                 cus.execute(sql)
                 myres=cus.fetchall()
                 df=pd.DataFrame(myres)
                 print(df)
             if yer==2:
                 sql="select*from districtp"
                 cus.execute(sql)
                 d=cus.fetchall()
                 df=pd.DataFrame(d)
                 print(df)
             if yer==3:
                 sql="select*from districtp1"
                 cus.execute(sql)
                 d=cus.fetchall()
                 df=pd.DataFrame(d)
                 print(df)
        if ch3==2:
            ch4=int(input( '''To get graph of the same district for three consequitive years press 1
    To get graph of all the districts for the same year press 2'''))
            if ch4==1:
                nm=str(input("enter district name"))
                
                sql="select malaria,dengue,chikungunya,japanese_encephalitis,kala_azar,lymphatic_filariasis from districtc where districtname=%s"
                cus.execute(sql)
                yar1=cus.fetchall()
                dc=list[yar1]
                print(dc)
                
                x=['Malaria',' Dengue',' Chikungunya',' Japanese Encephalitis (JE)',' Kala-azar',' Lymphatic Filariasis']
                   
                plt.plot(x,dc)
                #plt.plot(x,year2)
                #plt.plot(x,year3)
                plt.legend(True)
                plt.ylabel("number of cases")
                plt.xlabel("disease name")
                plt.show()
            
                
            
            
            
                '''sql1="select malaria,dengue,chikungunya,japanese_encephalitis,kala_azar,lymphatic_filariasis from districtp where districtname=%s"
                cus.execute(sql1,nm)
                year2=cus.fetchall()
                sql2="select malaria,dengue,chikungunya,japanese_encephalitis,kala_azar,lymphatic_filariasis from districtp1 where districtname=%s"
                cus.execute(sql2,nm)
                year3=cus.fetchall()'''
              
                
            
            
                     
         
        
                    
                

        
        
    

    
