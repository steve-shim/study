'''
mutable 객체의 경우에는 객체를 생성하지 않고 바로 수정이 가능하기에 전역변수로 지정을 하지 않아도 
로컬 mutable 변수의 값이 수정된다. 하지만 로컬 immutable 변수는 test함수 안에서 수정하려고 해도,
지역변수로써 immutable라는 이름의 객체를 새로 생성하고 할당한 것이기에 로컬 immutable 변수는
변하지가 않는다. 
이렇기에 immutable 객체는 수정하려면 함수안에서 global을 사용해 전역변수로 지정을 해줘야 한다.
'''

immutable = False
mutable = [False]

def test():
    immutable = True
    mutable[0] = True
    
test()
print(f"immutable: {immutable}")
print(f"mutable: {mutable}")

# immutable = False
# mutable = [False]

# def test():
#     global immutable
#     immutable = True
#     mutable[0] = True
    
# test()
# print(f"immutable: {immutable}")
# print(f"mutable: {mutable}")