const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const uri = "mongodb+srv://user:QkSR7FzEQXs2hX0Y@emergencyservice.16zhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri);    
const io = new Server(server);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});
io.on('connection', (socket) => {
    let changeStream;
    const database = client.db("EmergencyService");
    const collection = database.collection("SOS_Request");
    debugger;
    async function run() {
        await client.connect();
        collection.find().toArray(function(err, result) {
            io.emit('All Records', result);
          });
        // io.emit('All Records', collection.find());
        // open a Change Stream on the "haikus" collection
        var filter = [{
            $match: {
                $and: [
                    { operationType: "insert" }]
            }
        }];
        changeStream = collection.watch(filter);
        // set up a listener when change events are emitted
        changeStream.on("change", next => {
        // process any change event
        collection.find().toArray(function(err, result) {
            io.emit('All Records', result);
          });
        // io.emit('chat message', next.fullDocument);
        // console.log("received a change to the collection: \t", next);
        });
    }
    run().catch(console.dir);
    io.on('forceDisconnect', function(){
        print("socket disconnected")
        socket.disconnect();
    });
});
server.listen(3000, () => {
  console.log('listening on *:3000');
});