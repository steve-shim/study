{
    /**
     * Type Aliases
     */
    type Text = string;
    const name: string = 'steve';
    const name2: Text = 'steve';
    const address: Text = 'korea';
    type Num = number;
    type Student = {
        name: string;
        age: number;
    };

    // 원시type뿐만 아니라 object type도 원하는 타입으로 만들 수 있다
    // Student type으로 자료형을 만드면
    // name, age -> key만 쓸 수 있다
    const students: Student = {
        name: 'steve',
        age: 12,
    }

    /**
     * String Literal Types
     */
    type Name = 'name';
    let ellieName: Name;
    ellieName = 'name';
    type JSON = 'json';
    const json: JSON = 'json';

    type Boal = true;
    const isCat: Boal = true;
}