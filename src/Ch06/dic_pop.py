
# 코드 6-2 : 딕셔너리의 항목 삭제와 dic[1] 항목의 변화 여부


dic = {0:11, 1:22, 2:33, 3:44, 4:55}
# 딕셔너리의 (키,값) 튜플쌍을 반환하는 items() 함수로 항목 출력
print('pop(0) 이전 :', dic.items())
print('pop(0) 이전 dic[1] = ', dic[1])
dic.pop(0)  # 키 0을 이용하여 (0, 11) 항목을 삭제하였음
print('pop(0) 이후 :', dic.items())
print('pop(0) 이후 dic[1] = ', dic[1])
