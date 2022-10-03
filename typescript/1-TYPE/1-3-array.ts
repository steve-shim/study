{
    //Array 를 정의하는 2가지 방법
    const fruits: string[] = ['사과','바나나'];
    const scores: Array<number> = [1,3,4];

    //object의 불변성을 보장하기 위해서는 readonly를 써야하는데
    //string[] 방식으로 object(array)를 지정해야 readonly를 사용가능하다
    function printArray(fruits: readonly string[]){
        //fruits.push('당근') 이러면 에러
    }

    //Tuple (고정된 size의 서로다른 type이 있을 때)
    //but 권장x -> interface, type alias, class로 사용하는 것 권장
    //권장안하는 이유는 각 index에 뭐가 들었는지 숫가로 확인 어려움
    let student: [string, number];
    student = ['name',123]
    console.log(student[0])
    console.log(student[1])

    //Object Destructuring
    //사용하는 쪽에서 name이랑 age변수 지정해서 사용할 수는 있다
    const [name, age] = student;
    console.log("name",name)
    console.log("age",age)
}