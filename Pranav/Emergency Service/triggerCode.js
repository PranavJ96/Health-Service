
const { MongoClient } = require('mongodb');
// Replace the uri string with your MongoDB deployment's connection string.
const uri = "mongodb+srv://user:QkSR7FzEQXs2hX0Y@emergencyservice.16zhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri);
let changeStream;
async function run() {
    await client.connect();
    const database = client.db("EmergencyService");
    const collection = database.collection("SOS_Request");
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
      console.log("received a change to the collection: \t", next);
    });
}
run().catch(console.dir);