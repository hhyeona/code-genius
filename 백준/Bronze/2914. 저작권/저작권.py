'''
저작권 개수 / 수록된 곡 개수

곡의 개수/ 평균 (올림)  - 적어도 몇개의 저작권 곡이 있는지. (반올림 예상해서 -1 해주면 될듯.? )
'''
j, s = map(int,input().split())
print(j*(s-1)+1)