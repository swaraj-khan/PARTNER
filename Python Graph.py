#Importing some libraries 
import random
import numpy as np 
import matplotlib.pyplot as plt

#Creating respective lists
list=['GROCERIES','FURNITURE','FIRSTAID','STATIONARY']
GROCERIES=['apple','watermelon','soda','Milk','Bread','Cheese',
 'Cereals','Tomato sauce','Mustard','Salsa',
 'Hot pepper sauce','Eggs','Tofu','Butter',
 'Chocolate','Banana','Mango','Water','Potato']
FURNITURE=['Armchair','stool','Bean Bag Chair','Bed','Bunk bed','Bookshelf',
 'Carpet','Cupboard','Couch','Cushion','Curtain','Desk','Desk Chair',
 'Grandfather Clock','Garden Bench',
 'Table','Hat Stand','Shelf','Rocking chair']
FIRSTAID=['Plaster','Gauze','Bandages','Safty pins','Gloves','Tweezers',
 'Scissors','Thermometer','Skin Rash Cream','Painkillers',
 'Cough medicine','Eye wash','Sticky tape','Asprin','Antacid','Nasal Spray','Insect Repellent','Sunscreen',
 'Mask']
STATIONARY=['Pens','Highlighter','Permanent Marker','Eraser','Pencil',
 'Pencil Sharpener','Ruler','Plain Paper','Glue',
 'Paper Clips','Sticky tape','Calculator','Utitity Knife',
 'Rubber Bands',
 'Stapeler','Envelope','WhiteBoard','Geometry Box','Scarpbook',
 'Wall hooks']

#Creating Logic and giving instruction on what to do with the user's input
for i in range(0,100):
 g=0
 f=0
 fa=0
 s=0
 ITEM_SOLD=input("INPUT THE RECENTLY SOLD ITEMS~ ")
 if any(ITEM_SOLD in word for word in GROCERIES):
     g=g+1
 
 elif any(ITEM_SOLD in word for word in FURNITURE):
     f=f+1
 
 elif any(ITEM_SOLD in word for word in FIRSTAID):
     fa=fa+1
 
 elif any(ITEM_SOLD in word for word in STATIONARY):
     s=s+1
 else:
     break
 print(g,f,fa,s)

#Closing values
data = {'groceries':g, 'furniture':f, 'firstaid':fa,'stationary':s} 
courses = list(data.keys()) 
values = list(data.values()) 
fig = plt.figure(figsize = (10, 5)) 
plt.bar(courses, values, color ='maroon',width = 0.4)
plt.xlabel("amount sold") 
plt.ylabel("category") 
plt.title("table") 
plt.show()
