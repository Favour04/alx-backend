import { createClient } from "redis"

const client = createClient()
client.on("error", (err) => console.log(`Redis client not connected to the server: ${err}`))
client.on("connect", () => console.log("Redis client connected to the server"))

const data = {
    "Portland": 50,
    "Seattle": 80,
    "New York": 20,
    "Bogota": 20,
    "Cali": 40,
    "Paris": 2,
}

const schoolName = "HolbertonSchools"
for (let key in data) {
    client.hset([schoolName, ...Object.entries({key:data[key]}).flat()],(err, data) => {
        if (err) {
            console.log(err)
        } else {
            console.log(`Relpy: 1`)
        }
    })
}

client.hgetall("HolbertonSchools", (err, data) => {
    if (err) {
        console.log(err)
    } else {
        console.log(data)
    }
})