
# 코드 4-18 : 인자를 빠뜨린 호출


def print_star(n):            # 인자를 하나 필요로 함
    for _ in range(n):
        print('************************')

print_star() # 인자가 없으므로 에러 발생
