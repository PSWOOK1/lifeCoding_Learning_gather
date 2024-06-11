print('hello world')
print("hello world")
print('''
      hello
      world
      ''') # 줄바꿈 하기 위해선 따옴표 3개 연속, 터미널에서도 줄바꿈 된 상태로 출력
print("""
      hello
      world
      """) # 상동

print('1'+'1')
print("'1'+'1'") # "" 가 '' 보다 큰 취급
print('hello world'*10) # text를 n번 반복해서 출력
print(len('hello world'*10)) # text를 n번 반복해서 나온 출력값의 글자 수가 몇 개 인가?
print('hello world'.replace('world', 'universe')) # 'world' 라는 text를 찾아서 'universe'로 바꾼다 (text가 존재하지 않거나 오타가 있으면 무시)

