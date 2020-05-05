#!/usr/bin/node
exports.addMeMaybe = function (n, fn) {
  n++;
  fn(n);
};
