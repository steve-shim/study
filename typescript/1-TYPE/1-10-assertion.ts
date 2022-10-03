{
    /**
     * Type Assertions (비추)
     */
    function jsStrFunc(): any {
        return 'hello';
    }
    const result = jsStrFunc();
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

    const button = document.querySelector('class')
    if(button){
        button.nodeValue;
    }
}