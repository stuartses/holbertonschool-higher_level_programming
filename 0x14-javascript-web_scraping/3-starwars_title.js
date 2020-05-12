#!/usr/bin/node
/* Get content by id in a http request */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

/*
request
  .get(url)
  .on('response', function (response) {
    console.log(JSON.parse(response));
  });
*/

request(url, function (err, res, body) {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
