#!/usr/bin/node
const argvLen = process.argv.length;
if (argvLen <= 2) console.log('No argument');
if (argvLen === 3) console.log('Argument found');
if (argvLen > 3) console.log('Arguments found');
