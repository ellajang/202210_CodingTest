// 12.곱셈

const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().split("\n");

const A = parseInt(Data[0]);
const B = parseInt(Data[1]);

console.log(A * (B % 10));
console.log(A * parseInt((B % 100) / 10));
console.log(A * parseInt(B / 100));
console.log(A * B);
