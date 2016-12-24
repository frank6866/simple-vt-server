var app = require('http').createServer(handler), 
    io = require('socket.io').listen(app), 
    fs = require('fs')

app.listen(8080);
// io.set('log level', 1);//将socket.io中的debug信息关闭

function handler (req, res) {
  fs.readFile(__dirname + '/index.html',function (err, data) {  
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }    
    res.writeHead(200, {'Content-Type': 'text/html'});    
    res.end(data);
  });
}

var stdin = process.openStdin();

var net = require('net')
var host = '127.0.0.1'
var port = 9999

var server = net.createServer();
// server.on('connection', handleConnection);
server.listen(port, host)

/*
function handleConnection(conn) {
  conn.on('data', onConnData)

  function onConnData(d) {
    console.log("DATA: " + d)
  }
}
*/


io.sockets.on('connection', function (socket) {
    /*   
    stdin.addListener("data", function(d){
      socket.emit('news', { hello: d.toString() });
    })
    */

    server.on('connection', function(sock){
      sock.on('data',function(data){
        data_str = data.toString()
        console.log("DATA:" + data_str)
        socket.emit('news', { hello: data_str});
      })
    })

    /*
    socket.on('my other event', function (data) {
      console.log(data);
    });
    */
});

// net module ref : 
// https://blog.yld.io/2016/02/23/building-a-tcp-service-using-node-js/#.WF4WM7FY6Ho


