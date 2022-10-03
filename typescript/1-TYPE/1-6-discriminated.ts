{
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
    function login(): LoginState {
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
    function printLoginState(state: LoginState){
        //state.reason 작성하는 시점에는 state아래 response가 있는지 reason이 있는지 모른다
        // if('response' in state){
        //     console.log(`축하축하 ${state.response.body}`);
        // } else{
        //     console.log(`😭 ${state.reason}`);
        // }
        // 반면 state.result는 항상 존재한다.!
        if(state.result === 'success'){
            console.log(`축하축하 ${state.response.body}`);
        } else{
            console.log(`😭 ${state.reason}`);
        }
    }
}