//8.??!

const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().trim();

console.log(`${Data}??!`);

// 해당 문제의 경우 입력 데이터가 여러개가 아닌 하나의 문자열이 따라서 split("")을 활용해
// 띄어쓰기를 없애고 파싱하는 과정이 필요없다. 대신 trim()을 사용해서 문자열 양 옆에 존재하는 공백을 지워야 하며,trim()을 사용하지않으면 정답이 아니다.
