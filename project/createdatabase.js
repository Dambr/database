//										sudo mongod --dbpath=/
var MongoClient = require('mongodb').MongoClient;
var toPayments = require('./payments.json');
var toClients = require('./clients.json');
var toRegistration = require('./registration.json');
var toFriends = require('./friends.json');
var toHotel_info = require('./hotel_info.json');
var toCountry_info = require('./country_info.json');
var toGraft = require('./graft.json');
var toTransport = require('./transport.json');
var toInsurance = require('./insurance.json');
var toExcursion = require('./excursion.json');
var toBookkeepping = require('./bookkeepping.json');
var toSafe = require('./safe.json');
var toWorking_data = require('./working_data.json');
var toTax = require('./tax.json');
var toRoom_rental = require('./room_rental');
var toTour_information = require('./tour_information.json');
MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
	if (err) throw err;
	var dbo = db.db("mydb"); 
	dbo.createCollection("payments", function(err, res){
	dbo.createCollection("clients", function(err, res){
	dbo.createCollection("registration", function(err, res){
	dbo.createCollection("friends", function(err, res){
	dbo.createCollection("hotel_info", function(err, res){
	dbo.createCollection("country_info", function(err, res){
	dbo.createCollection("graft", function(err, res){
	dbo.createCollection("transport", function(err, res){
	dbo.createCollection("insurance", function(err, res){
	dbo.createCollection("excursion", function(err, res){
	dbo.createCollection("bookkeepping", function(err, res){
	dbo.createCollection("safe", function(err, res){
	dbo.createCollection("working_data", function(err, res){
	dbo.createCollection("tax", function(err, res){
	dbo.createCollection("room_rental", function(err, res){
	dbo.createCollection("tour_information", function(err, res){
	});});});});});});});});});});});});});});});});db.close();
	MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
		if (err) throw err;
		var dbo = db.db("mydb"); 	
		dbo.collection("payments").insertMany(toPayments, function(err, res){
		dbo.collection("clients").insertMany(toClients, function(err, res){	
		dbo.collection("registration").insertMany(toRegistration, function(err, res){
		dbo.collection("friends").insertMany(toFriends, function(err, res){
		dbo.collection("hotel_info").insertMany(toHotel_info, function(err, res){
		dbo.collection("country_info").insertMany(toCountry_info, function(err, res){
		dbo.collection("graft").insertMany(toGraft, function(err, res){
		dbo.collection("transport").insertMany(toTransport, function(err, res){
		dbo.collection("insurance").insertMany(toInsurance, function(err, res){
		dbo.collection("excursion").insertMany(toExcursion, function(err, res){
		dbo.collection("payments").insertMany(toBookkeepping, function(err, res){
		dbo.collection("safe").insertMany(toSafe, function(err, res){
		dbo.collection("working_data").insertMany(toWorking_data, function(err, res){
		dbo.collection("tax").insertMany(toTax, function(err, res){
		dbo.collection("room_rental").insertMany(toRoom_rental, function(err, res){
		dbo.collection("tour_information").insertMany(toTour_information, function(err, res){
		db.close();});});});});});});});});});});});});});});});});	
		MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
			if (err) throw err;
			var dbo = db.db("mydb");
			dbo.collection("payments").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("payments:");console.log(res);console.log();
			dbo.collection("clients").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("clients:");console.log(res);console.log();
			dbo.collection("registration").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("registration:");console.log(res);console.log();
			dbo.collection("friends").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("friends:");console.log(res);console.log();
			dbo.collection("hotel_info").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("hotel_info:");console.log(res);console.log();
			dbo.collection("country_info").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("country_info:");console.log(res);console.log();
			dbo.collection("graft").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("graft:");console.log(res);console.log();
			dbo.collection("transport").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("transport:");console.log(res);console.log();
			dbo.collection("insurance").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("insurance:");console.log(res);console.log();
			dbo.collection("excursion").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("excursion:");console.log(res);console.log();
			dbo.collection("payments").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("bookkeepping:");console.log(res);console.log();
			dbo.collection("safe").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("safe:");console.log(res);console.log();
			dbo.collection("working_data").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("working_data:");console.log(res);console.log();
			dbo.collection("tax").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("tax:");console.log(res);console.log();
			dbo.collection("room_rental").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("room_rental:");console.log(res);console.log();
			dbo.collection("tour_information").find({}, { projection: { _id: 0 }}).toArray(function(err, res){console.log("tour:");console.log(res);console.log();
			db.close();});});});});});});});});});});});});});});});});
		});
	});
});