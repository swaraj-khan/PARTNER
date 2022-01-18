#the lists
import mysql.connector as c
import random
list=['GROCERIES','FURNITURE','FIRSTAID','STATIONARY']
print("\n The list of GROCERIES \n")
GROCERIES=['apple','watermelon','soda','Milk','Bread','Cheese',
 'Cereals','Tomato sauce','Mustard','Salsa',
 'Hot pepper sauce','Eggs','Tofu','Butter',
 'Chocolate','Banana','Mango','Water','Potato']
db=c.connect(host='localhost',database='data',user='root',password='Welcome2MYSQL')
mc=db.cursor()
mc.execute("select*from groceries")
for i in mc:
 print(i)
print("\n The list of FURNITURE \n")
FURNITURE=['Armchair','stool','Bean Bag Chair','Bed','Bunk bed','Bookshelf',
 'Carpet','Cupboard','Couch','Cushion','Curtain','Desk','Desk Chair',
 'Grandfather Clock','Garden Bench',
 'Table','Hat Stand','Shelf','Rocking chair']
db=c.connect(host='localhost',database='data',user='root',password='Welcome2MYSQL')
mc=db.cursor()
mc.execute("select*from furniture")
for i in mc:
 print(i)
print("\n The list of FIRSTAID \n")
FIRSTAID=['Plaster','Gauze','Bandages','Safty pins','Gloves','Tweezers',
 'Scissors','Thermometer','Skin Rash Cream','Painkillers',
 'Cough medicine','Eye wash','Sticky tape','Asprin',
 'Antacid','Nasal Spray','Insect Repellent','Sunscreen',
 'Mask']
db=c.connect(host='localhost',database='data',user='root',password='Welcome2MYSQL')
mc=db.cursor()
mc.execute("select*from firstaid")
for i in mc:
 print(i)
print("\n The list of STATIONARY \n")
STATIONARY=['Pens','Highlighter','Permanent Marker','Eraser','Pencil',
 'Pencil Sharpener','Ruler','Plain Paper','Glue',
 'Paper Clips','Sticky tape','Calculator','Utitity Knife',
 'Rubber Bands',
 'Stapeler','Envelope','WhiteBoard','Geometry Box','Scarpbook',
 'Wall hooks']
db=c.connect(host='localhost',database='data',user='root',password='Welcome2MYSQL')
mc=db.cursor()

mc.execute("select*from stationary")
for i in mc:
 print(i)
# alteration if required 
print("do you want to make alterations to any of these lists")
print("if alterations are to be made please enter 1")
print("if alterations are not to be made please enter 2")
input_alt=int(input("please enter an input: "))
if input_alt==1:
    print("enter the name of the list to be altered")
    input_alt_ls=str(input("the list ~ "))
    if input_alt_ls=="groceries":
        print("enter the new item in groceries")
         input_alt_gr=str(input("~"))
         GROCERIES.append(input_alt_gr)
         print(GROCERIES)
    elif input_alt_ls=="furniture":
        print("enter the new item in furniture")
    input_alt_fr=str(input("~"))
     FURNITURE.append(input_alt_fr)
     print(FURNITURE)
    elif input_alt_ls=="firstaid":
        print("enter the new item in firstaid")
        input_alt_fa=str(input("~"))
        FIRSTAID.append(input_alt_fa)
        print(FIRSTAID)
 
    elif input_alt_ls=="stationary":
        print("enter the new item in stationary")
        input_alt_st=str(input("~"))
        STATIONARY.append(input_alt_st)
        print(STATIONARY)
     else:
        print("\na wrong entry has been made...moving onwards")
if input_alt==2:
    print("thank you, now moving forwards")

    
# recommendation code
print("\nhere are the list of items ")
ITEM_SOLD=input("INPUT THE RECENTLY SOLD ITEMS~ ")
if any(ITEM_SOLD in word for word in GROCERIES):
    GROCERIES=random.choice(GROCERIES)
    print("Do you want us to recommend a product to place on an offer ?")
    print("Please type : ")
    print("1 - to accept offer")
    print("2 - to decline offer : ")
    input_gr=int(input("Please Enter Input : "))
    if(input_gr==1):
        print("Here is our Product Recomndation : ",GROCERIES)
    elif(input_gr==2):
        print("No Problem Have a nice day")
    else:
        print("Please enter valid input")
elif any(ITEM_SOLD in word for word in FURNITURE):
    FURNITURE=random.choice(FURNITURE)
    print("Do you want us to recommend a product to place on an offer ?")
    print("Please type : ")
    print("1 - to accept offer")
    print("2 - to decline offer : ")
    input_fr=int(input("Please Enter Input : "))
    if(input_fr==1):
        print("Here is our Product Recomndation : ",FURNITURE)
    elif(input_fr==2):
        print("No Problem Have a nice day")
    else:
        print("Please enter valid input")
elif any(ITEM_SOLD in word for word in FIRSTAID):
    FIRSTAID=random.choice(FIRSTAID)
    print("Do you want us to recommend a product to place on an offer ?")
    print("Please type : ")
    print("1 - to accept offer")
    print("2 - to decline offer : ")
    input_fa=int(input("Please Enter Input : "))
    if(input_fa==1):
        print("Here is our Product Recomndation : ",FIRSTAID)
    elif(input_fa==2):
        print("No Problem Have a nice day")
    else:
        print("Please enter valid input")
elif any(ITEM_SOLD in word for word in STATIONARY):
    STATIONARY=random.choice(STATIONARY)
    print("Do you want us to recommend a product to place on an offer ?")
    print("Please type : ")
    print("1 - to accept offer")
    print("2 - to decline offer : ")
    input_st=int(input("Please Enter Input : "))
    if(input_st==1):
        print("Here is our Product Recomndation : ",STATIONARY)
    elif(input_st==2):
        print("No Problem Have a nice day")
    else:
     print("Please enter valid input")

