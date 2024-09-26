import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", err => console.log(`Redis client not connected to the server: ${err}`))
client.on("connect", () => console.log("Redis client connected to the server"))
client.set = promisify(client.set)
client.get = promisify(client.get)

async function setNewSchool(schoolName, value) {
    try {
        let resp = await client.set(schoolName, value)
        console.log(`Reply: ${resp}`)
    } catch(error) {
        console.log(error)
    }
}

async function displaySchoolValue(schoolName) {
    try {
        let value = await client.get(schoolName)
        console.log(value)
    } catch(error) {
        console.log(error)
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');