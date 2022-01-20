#Importing libraries
import random
import string

#Creating a Function
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
from itertools import repeat

#Creating dictionaries
dict=['GROCERIES','FURNITURE','FIRSTAID','STATIONARY']
GROCERIES={'apple':'apple','watermelon':'watermelon','soda':'soda','Milk':'Milk','Bread':'Bread','Cheese':'Cheese',
 'Cereals':'Cereals','Tomato sauce':'Tomato sauce','Mustard':'Mustard','Salsa':'Salsa',
 'Hot pepper sauce':'Hot pepper sauce','Eggs':'Eggs','Tofu':'Tofu','Butter':'Butter',
 'Chocolate':'Chocolate','Banana':'Banana','Mango':'Mango','Water':'Water','Potato':'Potato'}

FURNITURE={'Armchair':'Armchair','stool':'stool','Bean Bag Chair':'Bean Bag Chair','Bed':'Bed','Bunk bed':'Bunk bed','Bookshelf':'Bookshelf',
 'Carpet':'Carpet','Cupboard':'Cupboard','Couch':'Couch','Cushion':'Cushion','Curtain':'Curtain','Desk':'Desk','Desk Chair':'Desk Chair',
 'Grandfather Clock':'Grandfather Clock','Garden Bench':'Garden Bench',
 'Table':'Table','Hat Stand':'Hat Stand','Shelf':'Shelf','Rocking chair':'Rocking chair'}

FIRSTAID={'Plaster':'Plaster','Gauze':'Gauze','Bandages':'Bandages','Safty pins':'Safty pins','Gloves':'Gloves','Tweezers':'Tweezers',
 'Scissors':'Scissors','Thermometer':'Thermometer','Skin Rash Cream':'Skin Rash Cream','Painkillers':'Painkillers',
 'Cough medicine':'Cough medicine','Eye wash':'Eye wash','Sticky tape':'Sticky tape','Asprin':'Asprin',
 'Antacid':'Antacid','Nasal Spray':'Nasal Spray','Insect Repellent':'Insect Repellent','Sunscreen':'Sunscreen',
 'Mask':'Mask'}

STATIONARY={'Pens':'Pens','Highlighter':'Highlighter','Permanent Marker':'Permanent Marker','Eraser':'Eraser','Pencil':'Pencil',
 'Pencil Sharpener':'Pencil Sharpener','Ruler':'Ruler','Plain Paper':'Plain Paper','Glue':'Glue',
 'Paper Clips':'Paper Clips','Sticky tape':'Sticky tape','Calculator':'Calculator','Utitity Knife':'Utitity Knife',
 'Rubber Bands':'Rubber Bands',
 'Stapeler':'Stapeler','Envelope':'Envelope','WhiteBoard':'WhiteBoard','Geometry Box':'Geometry Box','Scarpbook':'Scarpbook',
 'Wall hooks':'Wall hooks'}


#Creating logic and giving instructions
for i in repeat(None,100):
    print("do you wish to create a produce database")
    i=input()
    if i=="yes":
        print("which item do you want to keep a record of?")
        l=input()
    if any(l in word for word in GROCERIES):
        print("enter a number ")
        result_str=input()
    elif any(l in word for word in FURNITURE):
    print("enter a number ")
    result_str=input()
    elif any(l in word for word in FIRSTAID):
        print("enter a number ")
        result_str=input()
    elif any(l in word for word in STATIONARY):
        print("enter a number ")
        result_str=input()
    else:
        print("invalid input")
        break
    z=l 
    f={z:result_str}
    print(f)
    if i=="no":
        print("ok")
        break

print("thank you")
