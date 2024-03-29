var app = require('http').createServer(handler);
var io = require('socket.io').listen(app);
var fs = require('fs');

app.listen(8081);
function handler(req, res) {
	fs.readFile(
		__dirname + '/index.html',
		function(err, data) {
			if (err) {
				res.writeHead(500);
				return res.end('Error loading index.html');
			}
			res.writeHead(200);
			res.end(data);
		}
	);
}

io.sockets.on('connection',
	function(socket) {
		socket.on('voteSent',
			function(data) {
				io.sockets.emit('voteReceived', data);
			}
		);
		
		socket.on('answerSent',
			function(data) {
				io.sockets.emit('answerReceived', data);
			}
		);
	}
);