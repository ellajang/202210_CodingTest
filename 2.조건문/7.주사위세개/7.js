//7.주사위세개

const Data = require("fs").readFileSync("text.txt").toString().split(" ");

const a = parseInt(Data[0]);
const b = parseInt(Data[1]);
const c = parseInt(Data[2]);

if (a === b && b === c && a === c) {
  console.log(10000 + a * 1000);
} else if (a === b || a === c) {
  console.log(1000 + a * 100);
} else if (c === b) {
  console.log(1000 + c * 100);
} else {
  const t = Math.max(a, b, c);
  console.log(t * 100);
}

// ==로 제출시 틀렸고 ===로 수정해서 맞았다.
// ==의 경우 옆의 값을 비교 전에 강제 형변환을 수행한다. 이과정으로 피연산자들을 공통 타입으로 만들어 그안에 잇는 값만을 비교하는 느슨한 비교라고 할수 있다.
// ===의 경우 강제 형변환 과정을 수행하지 않는 엄격한 비교이다.
//==와 ===를 구별하는 이유는 타입을 따로 지정해주지 않는 자바스크립트의 변수 특성상 이를 구별하기 위해 만든 것이라고 생각합니다.
