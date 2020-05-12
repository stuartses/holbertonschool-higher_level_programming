#!/usr/bin/node
/* Get the status code of a http request */

const request = require('request');
request
  .get(process.argv[2])
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
