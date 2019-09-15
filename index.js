/* 
    The Node.JS module "express" is used to host a webserver using "index.html" as its homepage.
*/

var express = require("express");
var app = express();

// The express() app is given access to the "/public" folder, containing the CSS and other required files.
app.use(express.static('public'));
app.use('/css', express.static(__dirname + '/public/css'));
app.use('/js', express.static(__dirname + '/public/js'));
app.use('/images', express.static(__dirname + '/public/images'));

/* 
    The server is setup on port 80, the default webpage TCP port. 
    The server address is left blank, and defaults to 192.168.100.1.
*/
var server = app.listen(80, '', function(){
    console.log("Server started at %s:%s", server.address().address, server.address().port);
});