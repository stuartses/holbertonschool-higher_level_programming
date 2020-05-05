#!/usr/bin/node
const argNum = Number(process.argv[2]);
if (isNaN(argNum)) console.log('Not a number');
else console.log('My number: ' + argNum);
