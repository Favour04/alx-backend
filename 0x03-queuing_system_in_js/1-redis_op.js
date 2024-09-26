import { createClient, redis} from "redis";

const client = createClient();

client.on("error", err => console.log(`Redis client not connected to the server: ${err}`))
client.on("connect", () => console.log("Redis client connected to the server"))

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.log(err)
        } else {
            console.log(`Reply: ${reply}`)
        }
    })
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, data) => {
        if (err) {
            console.log(err)
        } else {
            console.log(data)
        }
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');