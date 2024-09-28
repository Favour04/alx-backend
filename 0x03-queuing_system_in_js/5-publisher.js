import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client.publish = promisify(client.publish)

function publishMessage(message, time) {
    console.log("About to send MESSAGE", message)

    setTimeout(() => {
        client.publish("holberton school channel", message) 
    }, time)    
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);