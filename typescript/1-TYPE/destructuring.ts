//객체 Object Destructuring
const obj = {
    a : 'string',
    b : 12,
    c : true 
  }
  
const {a,b} = obj
console.log("a",a) // 'string'
console.log("b",b) // 12
  
const {a:a1, ...etc} = obj
console.log("a",a1) // 'string'
console.log("etc",etc)// {b:12, c:true}
console.log("etc.b",etc.b) // 12
console.log("etc.c",etc.c) // true

let student: [string, number];
student = ['shim',123]

//튜플 Object Destructuring
//사용하는 쪽에서 name10이랑 age10변수 지정해서 사용할 수는 있다
const [name10, age10] = student;
console.log("name",name10)
console.log("age",age10)