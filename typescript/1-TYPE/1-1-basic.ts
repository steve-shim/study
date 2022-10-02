{
    /**
     * JavaScript
     * Primitive: number, string, boolen, bigint, symbol, null, undefined
     * Object: function, array ...
     */

    //number
    const num:number = 3;

    //string
    const str:string = '3';

    //boolean
    const boal:boolean = false;

    //undefined 단독으로는 안쓰임
    //무언가가 있거나 없을 때 undefined 많이 쓰임
    let age: number | undefined;
    age = undefined;
    age = 1;
    function find(): number | undefined {
        return undefined
    }

    //null
    let person: string | null;

    //unknown (똥)
    let notSure:unknown = 0;
    notSure = 'he';
    notSure = true;

    //any (똥)
    let anything:any = 0;
    anything = 'hello';
    anything = 1;

    //void (함수에서 아무것도 리턴하는거 없음)
    function print(): void {
        console.log('hello');
        return;
    }

    //never (에러를 던지던지, 무한루프로 함수가 끝나지 않게 해야한다)
    function throwError(message: string): never {
        //message -> server (log)
        throw new Error(message);
        while(true){
        }
    }

    //object (똥)
    let obj: object; 
    function acceptSomeObject(obj: object ) {
    acceptSomeObject({name:'ellie'});
    acceptSomeObject({animal:'dog'});
    }
}