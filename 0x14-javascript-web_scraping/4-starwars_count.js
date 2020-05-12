#!/usr/bin/node
/* Get request and count the character */

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  const results = JSON.parse(body).results;
  let count = 0;

  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const charac = characters[j].split('/');
      const id = parseInt(charac[charac.length - 2]);
      if (id === 18) count++;
    }
  }
  console.log(count);
});
