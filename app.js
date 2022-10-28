const express = require('express')

const app = express();

app.get('/', (req, res)=>{
    res.json({
        "slackUsername":"davidadediji",
        "backend":true,
        "age":24,
        "bio":"backend developer"
    })
    res.end();
})


app.listen(3000, ()=>{
    console.log('listening on port 3000')
})