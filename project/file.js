var MongoClient = require('mongodb').MongoClient;
var http = require('http');
var express = require('express');
var app = express();
app.get('/payments', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("payments").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/clients', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("clients").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/registration', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("registration").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/friends', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("friends").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/hotel_info', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("hotel_info").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/country_info', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("country_info").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/graft', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("graft").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/transport', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("transport").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/insurance', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("insurance").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/excursion', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("excursion").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/bookkeepping', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("bookkeepping").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/safe', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("safe").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/working_data', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("working_data").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/tax', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("tax").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/room_rental', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("room_rental").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('/tour_information', function(req, result){
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb");
		dbo.collection("tour_information").find({}, { projection: { _id: 0 }}).toArray(function(err, res){result.send(res);
		db.close();
		});
	});
});
app.get('*', function(req, result){
	var answer = [
		{
			"/payments": "информация по платежам",
			"/clients": "информация о клиентах",
			"/registration": "данные о регистрации граждан",
			"/friends": "сведения о организациях-компаньонах",
			"/hotel_info": "информация об отелях",
			"/country_info": "информация о странах",
			"/graft": "сведения о прививках",
			"/transport": "данные по видам транспорта",
			"/insurance": "информация от страховых кампаний",
			"/excursion": "планируемые экскурсионные программы",
			"/bookkeepping": "бухгалтерия",
			"/safe": "служба безопасности",
			"/working_data": "данные о сотрудниках",
			"/tax": "отчеты по налогам",
			"/room_rental": "информация по аренде помещений",
			"/tour_information": "информация о туре",
		}
	];
	result.send(answer);
});
app.listen(4012, '127.0.0.1');
console.log('Work!');