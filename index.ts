import express, { Application, Request, Response } from "express";
import { username, age, bio, port } from './config/env'

const app: Application = express();

app.get('/', (req: Request, res: Response) => {
    res.json({
        "slackUsername": username,
        "backend": true,
        "age": age,
        "bio": bio
    })
})


app.listen(port, () => {
    console.log(`listening on port ${port}`)
})