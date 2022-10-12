//2.시험성적

const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().trim();

const x = parseInt(Data);

if (100 >= x && x >= 90) {
  console.log("A");
} else if (89 >= x && x >= 80) {
  console.log("B");
} else if (79 >= x && x >= 70) {
  console.log("C");
} else if (69 >= x && x >= 60) {
  console.log("D");
} else {
  console.log("F");
}
