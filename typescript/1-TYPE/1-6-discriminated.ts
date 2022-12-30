{
    //function: login -> success, fail
    //discriminated union: 동일한 키를 갖고있지만 state별로 다른 값을 가져서
    //Union끼리 차별화를 둔다 
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
        // if('response' in state){ // response가 state안에 있는 경우는 성공한 경우
        //     console.log(`축하축하 ${state.response.body}`);
        // } else{ // response가 state안에 없는 경우는 실패한 경우
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