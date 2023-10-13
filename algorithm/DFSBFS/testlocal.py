'''
global선언 없이 함수 내에서 전역변수를 사용할 경우
print(a) , if a == 1: 과 같이 조회하는 기능만 가능하다.
'''
# a = 10
# def prac():
#     print(a)
# print(a)
# prac()


'''
local variable 'a' referenced before assignment 에러
'''
a = 10
def prac2():
    global a
    a += 10
    print(a)
    
print(a)
prac2()