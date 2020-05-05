#!/usr/bin/node
if (process.argv.length <= 3) console.log(0);
const sortArgv = process.argv.slice(2).sort().reverse();
console.log(sortArgv[1]);
