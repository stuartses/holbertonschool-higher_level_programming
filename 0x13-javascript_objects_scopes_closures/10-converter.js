#!/usr/bin/node

// converts from base 10 to other using Closure functions
exports.converter = function (base) {
  function conversion (number) {
    return number.toString(base);
  }

  return conversion;
};
