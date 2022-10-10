//11.나머지
const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().split(" ");

A = parseInt(Data[0]);
B = parseInt(Data[1]);
C = parseInt(Data[2]);

console.log((A + B) % C);
console.log(((A % C) + (B % C)) % C);
console.log((A * B) % C);
console.log(((A % C) * (B % C)) % C);
