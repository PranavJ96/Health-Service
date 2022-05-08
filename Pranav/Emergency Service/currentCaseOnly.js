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
  res.sendFile(__dirname + '/currentCaseOnly.html');
});

var currentData = null;
io.on('connection', (socket) => {
    let changeStream;
    const database = client.db("EmergencyService");
    const collection = database.collection("SOS_Request");
    if(currentData != null){
      io.emit('SOS', currentData)
    }

    async function run() {
        await client.connect();
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
        currentData = next.fullDocument
        io.emit('SOS', next.fullDocument);
        // console.log("received a change to the collection: \t", next);
        });
    }
    run().catch(console.dir);
    socket.on('test', function(qwerty){
      currentData = null
    })
});
server.listen(4000, () => {
  console.log('listening on *:4000');
});