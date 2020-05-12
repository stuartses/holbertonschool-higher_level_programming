#!/usr/bin/node
/* Get the status code of a http request */

const request = require('request');
/*
request(process.argv[2], function (error, response) {
  console.log('error:', error);
  console.log('code:', response && response.statusCode);
});
*/

request
  .get(process.argv[2])
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
