//9.1998년생인 내가 태국에서는 2541년생?!

const fs = require("fs");
const Data = fs.readFileSync("text.txt").toString().trim();

console.log(parseInt(Data) - 543);

//trim()은 문자열 양쪽에 공백을 제거해준다.
//split()는 문자열을 일정한 구분자로 잘라서 배열로 저장한다. 공백일 경우 공백으로 잘라서 문자를 나란히 배열해준다.
