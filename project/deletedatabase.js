var MongoClient = require('mongodb').MongoClient;
MongoClient.connect("mongodb://localhost:27017/myproject",{ useNewUrlParser: true }, function(err, db){
	if (err) throw err;
	var dbo = db.db("mydb");
	dbo.collection("payments").deleteMany(function(err, res){
	dbo.collection("clients").deleteMany(function(err, res){	
	dbo.collection("registration").deleteMany(function(err, res){
	dbo.collection("friends").deleteMany(function(err, res){
	dbo.collection("hotel_info").deleteMany(function(err, res){
	dbo.collection("country_info").deleteMany(function(err, res){
	dbo.collection("graft").deleteMany(function(res){
	dbo.collection("transport").deleteMany(function(err, res){
	dbo.collection("insurance").deleteMany(function(err, res){
	dbo.collection("excursion").deleteMany(function(err, res){
	dbo.collection("bookkeepping").deleteMany(function(err, res){
	dbo.collection("safe").deleteMany(function(err, res){
	dbo.collection("working_data").deleteMany(function(err, res){
	dbo.collection("tax").deleteMany(function(err, res){
	dbo.collection("room_rental").deleteMany(function(err, res){
	dbo.collection("tour_information").deleteMany(function(err, res){
	db.close();});});});});});});});});});});});});});});});});
});