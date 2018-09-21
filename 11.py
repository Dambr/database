import json
import MySQLdb
import random
from datetime import datetime
con = MySQLdb.connect('host', 'user', 'passwd', 'db')
cur = con.cursor(MySQLdb.cursors.DictCursor)
file = open("url", 'wr')

sender = ['fname1 lname1', 'fname2 lname2', 'fname3 lname3', 'fname4 lname4', 'fname5 lname5']
recipient = sender[:]
recipient.reverse()
rang = ['manger', 'worker', 'cashier', 'cleaner', 'worker']
using_oil = ['92', '95', '98', '76', '95']
oil_firm_name = ['RusOIL', 'EngOIL', 'GerOIL', 'SweOIL', 'SpainOil']
mark_oil = using_oil
clas = ['food', 'oil']
mark_car = ['mark1', 'mark2', 'mark3', 'mark4', 'mark5']
food_firm_name = ['RusFood', 'EngFood', 'GerFood', 'SweFood', 'SPAINfood']
food_name = ['Snikers', 'Orbit', 'Apple', 'Orange', 'Bread']
chemicals_name = ['Soda', 'Oksid', 'Gas', 'Paint', 'Rubber']
fname = ['fname1', 'fname2', 'fname3', 'fname4', 'fname5']
lname = ['lname1', 'lname2', 'lname3', 'lname4', 'lname5']
holiday = [0,0,0,0,0]
hospital = [0,0,0,0,0]


cur.execute("CREATE TABLE payments(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, sender VARCHAR(40), recipient VARCHAR(40), sum INT NOT NULL, datatime VARCHAR(40))")
cur.execute("CREATE TABLE transact(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, sender VARCHAR(40), recipient VARCHAR(40), datatime VARCHAR(40))")
cur.execute("CREATE TABLE registration(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, who VARCHAR(40), id_payment INT NOT NULL, id_transact INT NOT NULL, datatime VARCHAR(40))")
cur.execute("CREATE TABLE people_oil(id INT NOT NULL, fname VARCHAR(40), lname VARCHAR(40), rang VARCHAR(40), cash INT NOT NULL)")
cur.execute("CREATE TABLE clients(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, id_payment INT NOT NULL, using_oil VARCHAR(40), sum INT NOT NULL, datatime VARCHAR(40))")
cur.execute("CREATE TABLE supplier_oil(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, firm_name VARCHAR(40), mark_oil VARCHAR(40), cost_oil VARCHAR(40), id_driver INT NOT NULL)")
cur.execute("CREATE TABLE drivers(id INT NOT NULL, fname VARCHAR(40), lname VARCHAR(40), id_car INT NOT NULL, datatime VARCHAR(40), class VARCHAR(40))")
cur.execute("CREATE TABLE cars_oil(id INT NOT NULL, id_driver INT NOT NULL, mark_car VARCHAR(40), carrying INT NOT NULL)")
cur.execute("CREATE TABLE cars_truck(id INT NOT NULL, id_driver INT NOT NULL, mark_car VARCHAR(40), carrying INT NOT NULL)")
cur.execute("CREATE TABLE supplier_food(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, id_driver VARCHAR(40), firm_name VARCHAR(40), food_name VARCHAR(40), sum_food INT NOT NULL)")
cur.execute("CREATE TABLE schedule(datatime_begin VARCHAR(40), datatime_end VARCHAR(40), id_person INT NOT NULL, fname VARCHAR(40), lname VARCHAR(40))")
cur.execute("CREATE TABLE chemicals(id INT NOT NULL, chemicals_name VARCHAR(40), fname_who VARCHAR(40), lname_who VARCHAR(40), datatime VARCHAR(40))")
cur.execute("CREATE TABLE hcs(id_contract INT NOT NULL PRIMARY KEY AUTO_INCREMENT, sum INT NOT NULL, datatime VARCHAR(40))")
cur.execute("CREATE TABLE bookkeeping(id_person INT NOT NULL PRIMARY KEY AUTO_INCREMENT, fname VARCHAR(40), lname VARCHAR(40), status VARCHAR(40), sum INT NOT NULL, holiday INT NOT NULL, hospital INT NOT NULL)")
cur.execute("CREATE TABLE safe(id_person INT NOT NULL, pass_number INT NOT NULL, access_level INT NOT NULL)")
cur.execute("CREATE TABLE people_food(id INT NOT NULL, fname VARCHAR(40), lname VARCHAR(40), rang VARCHAR(40), cash INT NOT NULL)")



for i in range(5):
	
	ids = i+1
	sum = (i+1)**3
	datatime = '0'+str(i+1)+'-05-2018 1'+str(i+1)+':0'+str(i+1)+':0'+str(i+1)
	cash = 2**(i+1)+1024-(i+1)**2
	cost_oil = 40+i**2
	carrying = (i+1)*1000
	sum_food = i+100-i**2
	datatime_begin = '0'+str(i+3)+'-05-2018 1'+str(i+3)+':0'+str(i+3)+':0'+str(i+3)
	datatime_end = '1'+str(i+1)+'-05-2018 1'+str(i+1)+':0'+str(i+1)+':0'+str(i+1)
	pass_number = i**4+9*i-5
	access_level = i+1


	cur.execute("INSERT INTO payments(sender, recipient, sum, datatime) VALUES(%s, %s, %s, %s)", (sender[i], recipient[i], sum, datatime))
	con.commit()
	cur.execute("SELECT MAX(id) FROM payments")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM payments WHERE id ="+str(id))
	file.write(str(datetime.now())+" Payments: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO transact(sender, recipient, datatime) VALUES(%s, %s, %s)",(sender[i], recipient[i], datatime))
	con.commit()
	cur.execute("SELECT MAX(id) FROM transact")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM transact WHERE id ="+str(id))
	file.write(str(datetime.now())+" Transact: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO registration(who, id_payment, id_transact, datatime) VALUES(%s, %s, %s, %s)",(sender[i], ids, ids, datatime))
	con.commit()
	cur.execute("SELECT MAX(id) FROM registration")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM registration WHERE id ="+str(id))
	file.write(str(datetime.now())+" Registration: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO people_oil(id, fname, lname, rang, cash) VALUES(%s, %s, %s, %s, %s)",(ids, fname[i], lname[i], rang[i], cash))
	con.commit()
	cur.execute("SELECT MAX(id) FROM people_oil")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM people_oil WHERE id ="+str(id))
	file.write(str(datetime.now())+" People_oil: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO clients(id_payment, using_oil, sum, datatime) VALUES(%s, %s, %s, %s)",(ids, using_oil[i], sum, datatime))
	con.commit()
	cur.execute("SELECT MAX(id) FROM clients")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM clients WHERE id ="+str(id))
	file.write(str(datetime.now())+" Clients: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO supplier_oil(firm_name, mark_oil, cost_oil, id_driver) VALUES(%s, %s, %s, %s)",(oil_firm_name[i], mark_oil[i], cost_oil, ids))
	con.commit()
	cur.execute("SELECT MAX(id) FROM supplier_oil")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM supplier_oil WHERE id ="+str(id))
	file.write(str(datetime.now())+" Supplier_oil: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO drivers(id, fname, lname, id_car, datatime, class) VALUES(%s, %s, %s, %s, %s, %s)",(ids, fname[i], lname[i], ids, datatime, clas[random.randint(0,1)]))
	con.commit()
	cur.execute("SELECT MAX(id) FROM drivers")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM drivers WHERE id ="+str(id))
	file.write(str(datetime.now())+" Drivers: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO cars_oil(id, id_driver, mark_car, carrying) VALUES(%s, %s, %s, %s)",(ids, ids, mark_car[i], carrying))
	con.commit()
	cur.execute("SELECT MAX(id) FROM cars_oil")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM cars_oil WHERE id ="+str(id))
	file.write(str(datetime.now())+" Cars_oil: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO cars_truck(id, id_driver, mark_car, carrying) VALUES(%s, %s, %s, %s)",(ids, ids, mark_car[i], carrying))
	con.commit()
	cur.execute("SELECT MAX(id) FROM cars_truck")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM cars_truck WHERE id ="+str(id))
	file.write(str(datetime.now())+" Cars_truck: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO supplier_food(id_driver, firm_name, food_name, sum_food) VALUES(%s, %s, %s, %s)",(ids, food_firm_name[i], food_name[i], sum_food))
	con.commit()
	cur.execute("SELECT MAX(id) FROM supplier_food")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM supplier_food WHERE id ="+str(id))
	file.write(str(datetime.now())+" Supplier_food: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO schedule(datatime_begin, datatime_end, id_person, fname, lname) VALUES(%s, %s, %s, %s, %s)",(datatime_begin, datatime_end, id, fname[i], lname[i]))
	con.commit()
	cur.execute("SELECT MAX(id_person) FROM schedule")
	id = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM schedule WHERE id_person ="+str(id))
	file.write(str(datetime.now())+" Schedule: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO chemicals(id, chemicals_name, fname_who, lname_who, datatime) VALUES(%s, %s, %s, %s, %s)",(ids, chemicals_name[i], fname[i], lname[i], datatime))
	con.commit()
	cur.execute("SELECT MAX(id) FROM chemicals")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM chemicals WHERE id ="+str(id))
	file.write(str(datetime.now())+" Chemicals: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO hcs(sum, datatime) VALUES(%s, %s)",(sum, datatime))
	con.commit()
	cur.execute("SELECT MAX(id_contract) FROM hcs")
	id = cur.fetchall()[0]['MAX(id_contract)']
	cur.execute("SELECT * FROM hcs WHERE id_contract ="+str(id))
	file.write(str(datetime.now())+" Hcs: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO bookkeeping(fname, lname, status, sum, holiday, hospital) VALUES(%s, %s, %s, %s, %s, %s)",(fname[i], lname[i], rang[i], sum, holiday[i], hospital[i]))
	con.commit()
	cur.execute("SELECT MAX(id_person) FROM bookkeeping")
	id = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM bookkeeping WHERE id_person ="+str(id))
	file.write(str(datetime.now())+" Bookkeeping: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO safe(id_person, pass_number, access_level) VALUES(%s, %s, %s)",(ids, pass_number, access_level))
	con.commit()
	cur.execute("SELECT MAX(id_person) FROM safe")
	id = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM safe WHERE id_person ="+str(id))
	file.write(str(datetime.now())+" Safe: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	cur.execute("INSERT INTO people_food(id, fname, lname, rang, cash) VALUES(%s, %s, %s, %s, %s)",(ids, fname[i], lname[i], rang[i], cash))
	con.commit()
	cur.execute("SELECT MAX(id) FROM people_food")
	id = cur.fetchall()[0]['MAX(id)']
	cur.execute("SELECT * FROM people_food WHERE id ="+str(id))
	file.write(str(datetime.now())+" People_food: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")
	



file.close()
cur.close()
con.close()
