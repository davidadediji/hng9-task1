const express = require('express')
const dotenv = require('dotenv')

dotenv.config();

const port = process.env.PORT || 5000
const age = process.env.AGE
const bio = process.env.BIO

const app = express();

app.get('/', (req, res)=>{
    res.json({
        "slackUsername":"davidadediji",
        "backend":true,
        "age":age,
        "bio":bio
    })
    res.end();
})


app.listen(port, ()=>{
    console.log(`listening on port ${port}`)
})