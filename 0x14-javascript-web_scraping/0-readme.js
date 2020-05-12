#!/usr/bin/node
// Include fs module
var fs = require('fs');

// Use fs.readFile() method to read the file
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  // Display the file content
  if (err) console.error(err);
  else process.stdout.write(data);
});
