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

    //enum을 쓰는 대신 union string literal로 대체가능
    type DaysOfWeek = 'Monday' | 'Tuesday' | 'Wednesday';
    let dayOfweek: DaysOfWeek = 'Monday';
    dayOfweek = 'Tuesday';

}