from flask import Flask
from flask import abort
import json
import MySQLdb
import random
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	cmd1 = "GET: /<table> - show information in table"
	cmd2 = "PUT: /add_person/<fname>/<lname>/<summ>/<clas> - add new person with the specified parameters"
	cmd3 = "PUT: /add_event/<event>/<sender>/<recipient> - add new event with the specified parameters"
	answer = [cmd1, cmd2, cmd3]
	answer = tuple(answer)
	return json.dumps(answer, sort_keys=True, indent=4)

@app.route("/<table>")
def show(table):
	con = MySQLdb.connect('localhost', 'root', '123456', 'test')
	cur = con.cursor(MySQLdb.cursors.DictCursor)
	file = open("/home/dambr/Desktop/file.txt", 'a')
	cur.execute("SELECT * FROM "+str(table))
	file.write(str(datetime.now())+" GET "+str(table))
	file.write("\n")
	answer = json.dumps(cur.fetchall(), sort_keys=True, indent=4)
	file.close()
	cur.close()
	con.close()
	return answer





@app.route("/add_person/<fname>/<lname>/<summ>/<clas>", methods=['PUT'])
def addperson(fname, lname, summ, clas):
	if clas not in ('food', 'oil', 'driver'):
		return "Sorry, unknown class-name"
	con = MySQLdb.connect('localhost', 'root', '123456', 'test')
	cur = con.cursor(MySQLdb.cursors.DictCursor)
	file = open("/home/dambr/Desktop/file.txt", 'a')
	rang = ['manger', 'worker', 'cashier', 'cleaner', 'worker']
	oil_firm_name = ['RusOIL', 'EngOIL', 'GerOIL', 'SweOIL', 'SpainOil']
	mark_car = ['BMW', 'Mersedes', 'Oka', 'Lada', 'Opel']
	food_name = ['Snikers', 'Orbit', 'Apple', 'Orange', 'Bread']
	food_firm_name = ['RusFood', 'EngFood', 'GerFood', 'SweFood', 'SPAINfood']
	car_class = ['food', 'oil']
	mark_oil = ['92', '95', '98', '76', '95']
	cur.execute("INSERT INTO bookkeeping(fname,lname,status,summ,holiday,hospital) VALUES(%s, %s, %s, %s, %s, %s)", (fname, lname, clas, summ, 0, 0))
	con.commit()
	cur.execute("SELECT MAX(id_person) FROM bookkeeping")
	idmax = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM bookkeeping WHERE id_person ="+str(idmax))
	file.write(str(datetime.now())+" PUT Bookkeeping: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")


	cur.execute("INSERT INTO safe(id_person, pass_number, access_level) VALUES(%s, %s, %s)",(idmax, idmax**4*4, random.randint(1,3)))
	con.commit()
	cur.execute("SELECT MAX(id_person) FROM safe")
	idmax = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM safe WHERE id_person ="+str(idmax))
	file.write(str(datetime.now())+" PUT Safe: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")

	cur.execute("INSERT INTO schedule(datatime_begin, datatime_end, id_person, fname, lname) VALUES(%s, %s, %s, %s, %s)",('0'+str(idmax+3)+'-05-2018 1'+str(idmax+3)+':0'+str(idmax+3)+':0'+str(idmax+3), '1'+str(idmax+1)+'-05-2018 1'+str(idmax+1)+':0'+str(idmax+1)+':0'+str(idmax+1), idmax, fname, lname))
	con.commit()
	cur.execute("SELECT MAX(id_person) FROM schedule")
	idmax = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM schedule WHERE id_person ="+str(idmax))
	file.write(str(datetime.now())+" PUT Schedule: ")
	file.write("\n")
	file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
	file.write("\n")

	if clas == 'food':
		cur.execute("INSERT INTO people_food(id, fname, lname, rang, cash) VALUES(%s, %s, %s, %s, %s)",(idmax, fname, lname, rang[random.randint(0,4)], summ))
		con.commit()
		cur.execute("SELECT MAX(id) FROM people_food")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM people_food WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT People_food: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")
	if clas == 'oil':
		cur.execute("INSERT INTO people_oil(id, fname, lname, rang, cash) VALUES(%s, %s, %s, %s, %s)",(idmax, fname, lname, rang[random.randint(0,4)], summ))
		con.commit()
		cur.execute("SELECT MAX(id) FROM people_oil")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM people_oil WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT People_oil: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")
	if clas == 'driver':
		class_car = car_class[random.randint(0,1)]
		cur.execute("INSERT INTO drivers(id, fname, lname, id_car, class) VALUES(%s, %s, %s, %s, %s)",(idmax, fname, lname, idmax, class_car))
		con.commit()
		cur.execute("SELECT MAX(id) FROM drivers")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM drivers WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT Drivers: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")
		if class_car == 'oil':
			cur.execute("INSERT INTO supplier_oil(firm_name, mark_oil, cost_oil, id_driver) VALUES(%s, %s, %s, %s)",(oil_firm_name[random.randint(0,4)], mark_oil[random.randint(0,4)], 40+idmax, idmax))
			con.commit()
			cur.execute("SELECT MAX(id) FROM supplier_oil")
			idmax = cur.fetchall()[0]['MAX(id)']
			cur.execute("SELECT * FROM supplier_oil WHERE id ="+str(idmax))
			file.write(str(datetime.now())+" PUT Supplier_oil: ")
			file.write("\n")
			file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
			file.write("\n")

			cur.execute("INSERT INTO cars_oil(id, id_driver, mark_car, carrying) VALUES(%s, %s, %s, %s)",(idmax, idmax, mark_car[random.randint(0,4)], idmax*1000))
			con.commit()
			cur.execute("SELECT MAX(id) FROM cars_oil")
			idmax = cur.fetchall()[0]['MAX(id)']
			cur.execute("SELECT * FROM cars_oil WHERE id ="+str(idmax))
			file.write(str(datetime.now())+" PUT Cars_oil: ")
			file.write("\n")
			file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
			file.write("\n")

		if class_car == 'food':
			cur.execute("INSERT INTO supplier_food(id_driver, firm_name, food_name, summ_food) VALUES(%s, %s, %s, %s)",(idmax, food_firm_name[random.randint(0,4)], food_name[random.randint(0,4)], idmax+100-idmax**2))
			con.commit()
			cur.execute("SELECT MAX(id) FROM supplier_food")
			idmax = cur.fetchall()[0]['MAX(id)']
			cur.execute("SELECT * FROM supplier_food WHERE id ="+str(idmax))
			file.write(str(datetime.now())+" PUT Supplier_food: ")
			file.write("\n")
			file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
			file.write("\n")

			cur.execute("INSERT INTO cars_truck(id, id_driver, mark_car, carrying) VALUES(%s, %s, %s, %s)",(idmax, idmax, mark_car[random.randint(0,4)], idmax*1000))
			con.commit()
			cur.execute("SELECT MAX(id) FROM cars_truck")
			idmax = cur.fetchall()[0]['MAX(id)']
			cur.execute("SELECT * FROM cars_truck WHERE id ="+str(idmax))
			file.write(str(datetime.now())+" PUT Cars_truck: ")
			file.write("\n")
			file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
			file.write("\n")



	cur.execute("SELECT MAX(id_person) FROM bookkeeping")
	idmax = cur.fetchall()[0]['MAX(id_person)']
	cur.execute("SELECT * FROM bookkeeping WHERE id_person ="+str(idmax))
	answer = json.dumps(cur.fetchall(), sort_keys=True, indent=4)
	file.close()
	cur.close()
	con.close()
	return answer

@app.route('/add_event/<event>/<sender>/<recipient>', methods=['PUT'])
def add_event(event, sender, recipient):
	if event not in ('payments', 'transact'):
		return "Sorry, unknown event"
	con = MySQLdb.connect('localhost', 'root', '123456', 'test')
	cur = con.cursor(MySQLdb.cursors.DictCursor)
	file = open("/home/dambr/Desktop/file.txt", 'a')
	using_oil = ['92', '95', '98', '76', '95']
	chemicals_name = ['Soda', 'Oksid', 'Gas', 'Paint', 'Rubber']
	if event == 'payments':
		summ = random.randint(100, 1000)
		datatime = datetime.datetime(2018, random.randint(1,12), random.randint(1,28), hour=random.randint(1,23), minute=random.randint(1,59))
		cur.execute("INSERT INTO payments(sender, recipient, summ, datatime) VALUES(%s, %s, %s, %s)", (sender, recipient, summ, datatime))
		con.commit()
		cur.execute("SELECT MAX(id) FROM payments")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM payments WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT Payments: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("INSERT INTO registration(who, id_payment, id_transact, datatime) VALUES(%s, %s, NULL, %s)",(sender, idmax, datatime))
		con.commit()
		cur.execute("SELECT MAX(id) FROM registration")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM registration WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT Registration: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("INSERT INTO clients(id_payment, using_oil, summ, datatime) VALUES(%s, %s, %s, %s)",(idmax, using_oil[random.randint(0,4)], summ, datatime))
		con.commit()
		cur.execute("SELECT MAX(id) FROM clients")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM clients WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT Clients: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("INSERT INTO hcs(summ, datatime) VALUES(%s, %s)",(summ, datatime))
		con.commit()
		cur.execute("SELECT MAX(id_contract) FROM hcs")
		idmax = cur.fetchall()[0]['MAX(id_contract)']
		cur.execute("SELECT * FROM hcs WHERE id_contract ="+str(idmax))
		file.write(str(datetime.now())+" PUT Hcs: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("SELECT MAX(id) FROM payments")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM payments WHERE id ="+str(idmax))
		answer = json.dumps(cur.fetchall(), sort_keys=True, indent=4)
		file.close()
		cur.close()
		con.close()
		return answer


	if event == 'transact':
		datatime = datetime(2018, random.randint(1,12), random.randint(1,28), hour=random.randint(1,23), minute=random.randint(1,59))
		cur.execute("INSERT INTO transact(sender, recipient, datatime) VALUES(%s, %s, %s)",(sender, recipient, datatime))
		con.commit()
		cur.execute("SELECT MAX(id) FROM transact")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM transact WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT Transact: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("INSERT INTO registration(who, id_payment, id_transact, datatime) VALUES(%s, NULL, %s, %s)",(sender, idmax, datatime))
		con.commit()
		cur.execute("SELECT MAX(id) FROM registration")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM registration WHERE id ="+str(idmax))
		file.write(str(datetime.now())+" PUT Registration: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("INSERT INTO chemicals(id, chemicals_name, fname_who, datatime) VALUES(%s, %s, %s, %s)",(idmax, chemicals_name[random.randint(0,4)], sender, datatime))
		con.commit()
		cur.execute("SELECT MAX(id) FROM chemicals")
		id = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM chemicals WHERE id ="+str(id))
		file.write(str(datetime.now())+" PUT Chemicals: ")
		file.write("\n")
		file.write(json.dumps(cur.fetchall(), sort_keys=True, indent=4))
		file.write("\n")

		cur.execute("SELECT MAX(id) FROM transact")
		idmax = cur.fetchall()[0]['MAX(id)']
		cur.execute("SELECT * FROM transact WHERE id ="+str(idmax))
		answer = json.dumps(cur.fetchall(), sort_keys=True, indent=4)
		file.close()
		cur.close()
		con.close()
		return answer

