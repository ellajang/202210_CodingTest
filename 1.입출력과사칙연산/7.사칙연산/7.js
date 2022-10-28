// 7.사칙연산

const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().split(" ");

const A = parseInt(Data[0]);
const B = parseInt(Data[1]);

console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(parseInt(A / B));
console.log(A % B);
