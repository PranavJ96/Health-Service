const {MongoClient} = require('mongodb');
const neo4j = require('neo4j-driver')
async function main(){
    /**
     * Connection URI. Update <username>, <password>, and <your-cluster-url> to reflect your cluster.
     * See https://docs.mongodb.com/ecosystem/drivers/node/ for more details
     */
    // const uri = "mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority";
    const uri = "mongodb://localhost:27017";
    const client = new MongoClient(uri);
 
    try {
        // Connect to the MongoDB cluster
        await client.connect();
 
        // Make the appropriate DB calls
        await  listDatabases(client);
 
    } catch (e) {
        console.error(e);
    } finally {
        await client.close();
    }
}
async function listDatabases(client){
    databasesList = await client.db().admin().listDatabases();
 
    console.log("Databases:");
    databasesList.databases.forEach(db => console.log(` - ${db.name}`));
};
main().catch(console.error);

//Neo4j
// const driver = neo4j.driver('bolt://localhost:7687', neo4j.auth.basic(user, password))
// const session = driver.session()
// const personName = 'Alice'

// try {
//   const result = await session.run(
//     'CREATE (a:Person {name: $name}) RETURN a',
//     { name: personName }
//   )

//   const singleRecord = result.records[0]
//   const node = singleRecord.get(0)

//   console.log(node.properties.name)
// } finally {
//   await session.close()
// }

// // on application exit:
// await driver.close()