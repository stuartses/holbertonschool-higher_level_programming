#!/usr/bin/node
/* Get request and computes the number of tasks completed by user id */

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  const tasks = {};
  const results = JSON.parse(body);

  for (let i = 0; i < results.length; i++) {
    const userId = results[i].userId;
    if (results[i].completed === true) {
      if (userId in tasks) tasks[userId]++;
      else tasks[userId] = 1;
    }
  }
  console.log(tasks);
});
