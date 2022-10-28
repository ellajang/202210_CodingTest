// 10.킹, 퀸, 룩, 비숍, 나이트, 폰

const fs = require("fs");
const inputPiece = fs
  .readFileSync("text.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);
// map() 메소드는 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환한다. map((요소,인덱스) => {return 요소})
//예를들어,
// const a = [1,2,3,4]
// const n = a.map(x => x*2)
// consol.log(n)
// 결과는 [2,3,6,8]이 나온다.

const piece = [1, 1, 2, 2, 2, 8];
const result = piece.map((i, idx) => {
  return i - inputPiece[idx];
});
//map을 통해 for문 대신 사용 가능
console.log(result.join(" "));
//join을 통해 출력값을 띄어쓰기로 구분해줌 join을 입력하지 않으면,
// ","로 구분 됨
