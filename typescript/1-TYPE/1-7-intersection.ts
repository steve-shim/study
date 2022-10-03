{
       /**
        * Intersection Types: &
        */
       type Student = {
        name: string;
        score: number;
       };

       type Worker = {
        employeeId: number;
        work: () => void;
       }

       function internWork(person: Student & Worker){
        console.log(person.name, person.employeeId, person.work());
       }

       // 함수를 호출할 때 intersection에 포함된 모든 정보가 담긴 객체를 전달해야한다
       internWork({
        name: 'ellie',
        score:1,
        employeeId:123,
        work:()=>{},
       })
       
}