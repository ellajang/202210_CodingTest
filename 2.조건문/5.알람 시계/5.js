//5.알람시계

const Data = require("fs").readFileSync("text.txt").toString().split(" ");

const H = parseInt(Data[0]);
const M = parseInt(Data[1]);

if (M > 44) {
  console.log(H, M - 45);
} else if (M < 45) {
  if (H > 0) {
    console.log(H - 1, M + 15);
  } else {
    console.log(23, M + 15);
  }
}
