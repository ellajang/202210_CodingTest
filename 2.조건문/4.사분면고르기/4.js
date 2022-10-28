//4.사분면 고르기

const Data = require("fs").readFileSync("text.txt").toString().split("\n");

const x = parseInt(Data[0]);
const y = parseInt(Data[1]);

if (x > 0 && y > 0) {
  console.log("1");
} else if (x < 0 && y > 0) {
  console.log("2");
} else if (x < 0 && y < 0) {
  console.log("3");
} else {
  console.log("4");
}

// require("fs").readFileSync("/dev/stdin").toString()로 풀수 있으나 해당 경로 접근 권한 문제로 백준코딩에서는 런타임에러가 발생한다. 따라서 readFileSync(0)으로 수정하였다.
