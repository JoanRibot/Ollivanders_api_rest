from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="120320",
  database="ollivanders"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Inventory (Name varchar(40) not null, Sell_in int not null, Quality int not null)")
mycursor.execute("INSERT INTO Inventory (Name, Sell_in, Quality) VALUES \
  ('Aged Brie', 2, 0), \
  ('Elixir of the Mongoose', 5, 7),\
  ('+5 Dexterity Vest', 10, 20),\
  ('Hand of Ragnaros', 0, 80),\
  ('Hand of Ragnaros', -1, 80),\
  ('TAFKAL80ETC concert', 15, 20),\
  ('TAFKAL80ETC concert', 10, 49),\
  ('TAFKAL80ETC concert', 5, 49),\
  ('Conjured Mana Cake', 3, 6)")
mydb.commit()