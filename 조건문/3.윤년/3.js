//3.윤년
const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().trim();

const x = parseInt(Data);

if (x % 4 == 0 && (x % 100 != 0 || x % 400 == 0 * x)) {
  console.log("1");
} else {
  console.log("0");
}

//&& == and
//\\ == or
