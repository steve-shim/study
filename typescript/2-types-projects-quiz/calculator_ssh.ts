/**
 * Let's make a calculator 🧮
 */

function calculate_ssh(mode: string, num1: number, num2: number) {
    switch(mode){
        case 'add':
            return num1 + num2;
            break;
        case 'substract':
            return num1 - num2;
            break;
        case 'multiply':
            return num1 * num2;
            break;
        case 'divide':
            return num1 / num2;
            break;
        case 'remainder':
            return num1 % num2;
            break;
        default:
            break;
    }
}

console.log(calculate_ssh('add', 1, 3)); // 4
console.log(calculate_ssh('substract', 3, 1)); // 2
console.log(calculate_ssh('multiply', 4, 2)); // 8
console.log(calculate_ssh('divide', 4, 2)); // 2
console.log(calculate_ssh('remainder', 5, 2)); // 1
