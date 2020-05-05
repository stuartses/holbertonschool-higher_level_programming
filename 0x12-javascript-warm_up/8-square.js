#!/usr/bin/node
const X = Number(process.argv[2]);
let i, j;
if (isNaN(X)) console.log('Missing size');
for (i = 0; i < X; i++) {
  let row = '';
  for (j = 0; j < X; j++) row += 'X';
  console.log(row);
}
