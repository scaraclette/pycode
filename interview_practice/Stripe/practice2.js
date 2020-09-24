const https = require("https")

const url = "https://jsonmock.hackerrank.com/api/football_matches?year=2011&team1=barcelona&page=1"

let data = ""

https.request(url, res => {
    res.on('data', d => {
        data += d
    })
    res.on('end', () => {
        console.log('Finished parsing')
    })
}).end()

