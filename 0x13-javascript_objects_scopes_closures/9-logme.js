#!/usr/bin/node
// count times of log item

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
