#!/usr/bin/node
if (process.argv.length <= 3) console.log(0);
else {
  const sortArgv = process.argv.slice(2).sort().reverse();
  console.log(sortArgv[1]);
}
