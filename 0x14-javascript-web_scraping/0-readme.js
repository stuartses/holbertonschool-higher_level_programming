#!/usr/bin/node
/* Read the content of a file */

// Include fs module
const fs = require('fs');

// Use fs.readFile() method to read the file
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  // Display the file content
  if (err) console.log(err);
  else console.log(data);
});
