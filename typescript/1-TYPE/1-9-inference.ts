/**
 * Type Inference
 * type이 뻔한 경우에 type을 생략하고 할당하면 할당된 type 기준으로 설정
 */

let text: string = 'hello';
let text2 = 'hello';
text2 = 'aa';

//함수 인자에 기본값으로 문자열이 들어가서 기본 타입이 문자열이 된다
function print(message = 'hello'){
    console.log(message);
}
print('hello');

// 함수 return type이 void인 경우에는 생략하지만
// 그렇지 않을 때는 return type을 지정해주는 것이 좋다
function add(x: number, y: number): number {
    return x + y;
}
