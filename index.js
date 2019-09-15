var express = require("express");
var app = express();

app.use(express.static('public'));

app.use('/css', express.static(__dirname + '/public/css'));
app.use('/js', express.static(__dirname + '/public/js'));
app.use('/images', express.static(__dirname + '/public/images'));

var server = app.listen(80, '', function(){
    var port = server.address().port;
    console.log("Server started at http://192.168.100.1:%s", port);
});