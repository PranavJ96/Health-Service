// function test(){
//   const { MongoClient } = require('mongodb');
// const uri = "mongodb+srv://user:QkSR7FzEQXs2hX0Y@emergencyservice.16zhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
// const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
// client.connect(err => {
//   change_stream = client.EmergencyService.SOS_Request.watch([{
//      '$match': {
//          'operationType': { '$in': ['insert'] }
//      }
//      }])
//     changeStream.on("change", next => {
//     // process any change event
//     console.log("received a change to the collection: \t", next);
//     });
//   // perform actions on the collection object
//   client.close();
// });
// }
var io = require('socket.io')(8080); // The port should be different of your HTTP server.

io.on('connection', function (socket) { // Notify for a new connection and pass the socket as parameter.
    console.log('new connection');

    var incremental = 0;
    setInterval(function () {
        console.log('emit new value', incremental);

        socket.emit('update-value', incremental); // Emit on the opened socket.
        incremental++;
    }, 1000);

});