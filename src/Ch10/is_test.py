
# 코드 10-8 : 인스턴스의 아이덴티티 연산자 : is, is not 연산자


list_a = [10, 20, 30]
list_b = [10, 20, 30]

if list_a is list_b:
    print('list_a is list_b')
else:
    print('list_a is not list_b')
