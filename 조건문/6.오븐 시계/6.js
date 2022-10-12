//6.오븐시계

const Data = require("fs").readFileSync("text.txt").toString().split("\n");

const A = parseInt(Data[0].split(" ")[0]);
const B = parseInt(Data[0].split(" ")[1]);
const C = parseInt(Data[1]);

h = parseInt((A * 60 + B + C) / 60);
m = (A * 60 + B + C) % 60;

if (h >= 24) {
  h -= 24;
}
console.log(h, m);
