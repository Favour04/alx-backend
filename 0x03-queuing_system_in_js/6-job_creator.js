import { createQueue } from "kue";

const queue = createQueue()

let obj = {
        "phoneNumber": "string",
        "message": "string",
    }

const job = queue.create(
    "push_notification_code",
    obj,
).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`)
    }
}
)

job.on("complete", () => console.log("complete"))
.on("failed", () => console.log("failed"))