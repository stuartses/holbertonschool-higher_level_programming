#!/usr/bin/node
if (process.argv.length <= 3) console.log(0);
else {
  /*
    implements compare function (a, b) to allow a right sort
    with negative and cero integers
  */
  const sortArgv = process.argv.slice(2).sort(function (a, b) {
    return a - b;
  });
  console.log(sortArgv[sortArgv.length - 2]);
}
