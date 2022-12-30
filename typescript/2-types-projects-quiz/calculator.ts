/**
 * Let's make a calculator 🧮
 */

//Union type 지정
type Command = 'add' | 'substract' | 'multiply' | 'divide' | 'remainder'
function calculate(mode: Command, num1: number, num2: number) {
    switch(mode){
        case 'add':
            return num1 + num2;
        case 'substract':
            return num1 - num2;
        case 'multiply':
            return num1 * num2;
        case 'divide':
            return num1 / num2;
        case 'remainder':
            return num1 % num2;
        default:
            throw new Error('unknown command')
    }
}

console.log(calculate('add', 1, 3)); // 4
console.log(calculate('substract', 3, 1)); // 2
console.log(calculate('multiply', 4, 2)); // 8
console.log(calculate('divide', 4, 2)); // 2
console.log(calculate('remainder', 5, 2)); // 1
//console.log(calculate('rddd', 5, 2)); // 1
