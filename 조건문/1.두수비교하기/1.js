//1.두 수 비교하기

const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().split(" ");

const A = parseInt(Data[0]);
const B = parseInt(Data[1]);

if (A > B) {
  console.log(">");
} else if (A < B) {
  console.log("<");
} else {
  console.log("==");
}
