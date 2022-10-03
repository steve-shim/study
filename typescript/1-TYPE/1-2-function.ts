{
    // //js
    // function jsAdd(num1,num2){
    //     return num1+num2
    // }

    // //ts
    // function add(num1:number, num2:number):number{
    //     return num1+num2
    // }

    // //js
    // function jsFetchNum(id){
    //     //code...
    //     //code...
    //     return new Promise((resolve, reject) => {
    //         resolve(100);
    //     });
    // }

    // //ts: string을 인자로 받아서 리턴값은 Promise인데 숫자를 Promise한다
    // //Promise는 무언가 Fetch가 완료되고난 후에 숫자의 데이터를 리턴하겠구나
    // function tsFetchNum(id:string): Promise<number>{
    //     //code...
    //     //code...
    //     return new Promise((resolve, reject) => {
    //         resolve(100);
    //     });
    // }

    //Optional parameter (?)
    function printName(firstName:string, lastName?:string){
        console.log(firstName);
        console.log(lastName);
    }
    printName('steve','shim');
    printName('steve');
    printName('steve', undefined);

    //Default parameter
    function printMessage(message: string = 'default message'){
        console.log(message);
    }
    printMessage();

    //Rest parameter
    function addNumbers(...numbers: number[]): number {
        let accsum = 0
        numbers.forEach(element => {
            accsum += element            
        });
        return accsum;
    }
    console.log(addNumbers(1,2));
    console.log(addNumbers(1,2,3,4));

    function addNumbersReduce(...numbers: number[]): number {
        return numbers.reduce((a,b)=>a+b);
    }
    console.log(addNumbersReduce(1,2));
    console.log(addNumbersReduce(1,2,3,4));
}