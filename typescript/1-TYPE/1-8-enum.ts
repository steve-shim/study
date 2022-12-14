{
    /**
     * Enum
     */
    //JavaScript
    const MAX_NUM = 6;
    const MAX_STUDENTS_PER_CLASS = 10;
    const MONDAY = 0;
    const TUESDAY = 1;
    const WENDNESDAY = 2;
    const DAYS_ENUM = Object.freeze({"MONDAY":1,"TUESDAY":2,"WENDNESDAY":3})
    const dayOfToday = DAYS_ENUM.MONDAY;
    console.log(dayOfToday)

    //TypeScript (비추)
    //enum에 값을 지정하지 않으면 0부터 시작한다
    //문자열을 할당할거면 문자열을 하나씩 =로 할당해줘야한다
    enum Days {
        Monday = 1, // 0 
        Tuesday, // 1
        Wednesday, // 2
        Thursday, // 3
        Friday, // 4
        Saturday, // 5
        Sunday, // 6
    }
    console.log(Days.Monday);
    const day = Days.Saturday;
    console.log(day);

    //다른 언어에서는 enum이 매우 유용하지만
    //Typescript에서는 enum을 쓰는 대신 union string literal로 대체가능
    type DaysOfWeek = 'Monday' | 'Tuesday' | 'Wednesday';
    let dayOfweek: DaysOfWeek = 'Monday';
    dayOfweek = 'Tuesday';

}