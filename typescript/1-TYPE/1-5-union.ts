{
    /**
     * Union Types: OR
     * 발생할수 있는 여러 case중에 하나만 할당해야할 때 (선택지의 제한을 걸어 에러의 위험을 줄일수 있다)
     */
    type Direction = 'left' | 'right' | 'up' | 'down';
    function move2(direction: Direction){
        console.log(direction);
    }
    move2('right')

    type TileSize = 8 | 16 | 32;
    const tile: TileSize = 32

    //function: login -> success, fail
    type SuccessState = {
        result: 'success';
        response: {
            body: string;
        };
    };
    type FailState = {
        result: 'fail';
        reason: string;
    };
    type LoginState = SuccessState | FailState;
    function login2(): LoginState {
        return {
            result: 'success',
            response:{
                body: 'logged in',
            },
        };
    }
    //LoginState를 Promise하는 비동기로 짤수 있다
    //function login(id:string, password:string): Promise<LoginState>{}

    //printLoginState(state: LoginState)
    //success -> body 출력
    //fail    -> reason 출력
    function printLoginState2(state: LoginState){
        //state.reason 작성하는 시점에는 state아래 response가 있는지 reason이 있는지 모른다
        //따라서 discriminatd union을 만들어서 result키 안의 값으로 조건문 분기하는 것이 더 좋다
        if('response' in state){
            console.log(`축하축하 ${state.response.body}`);
        } else{
            console.log(`😭 ${state.reason}`);
        }
    }
}