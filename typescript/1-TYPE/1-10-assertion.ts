{
    /**
     * Type Assertions (비추)
     */
    function jsStrFunc(): any {
        return 'hello';
    }
    const result = jsStrFunc();
    //Type casting 방법 2개
    //TypeScript에서는 any를 반환하는거로 알기 떄문에 string이 반환되더라도 string API를 사용할 수 없다
    (result as string).length;
    <string>result.length;

    const wrong: any = [5];
    console.log((wrong as Array<number>).push(1000))
    console.log(wrong)

    function findNumbers(): number[] | undefined {
        return undefined;
    }
    const numbers = findNumbers();
    numbers!.push(2);

    //버튼객체가 존재하면 받아오고 존재하지 않으면 null을 받는데
    //null일때 에러를 막기 위해서 if문을 사용
    const button = document.querySelector('class')
    if(button){
        button.nodeValue;
    }
    //버튼이 무조건 존재한다고 하면 뒤에 느낌표를 쓴다
    const button = document.querySelector('class')!;

}