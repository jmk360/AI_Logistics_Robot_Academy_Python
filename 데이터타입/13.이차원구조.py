# 1, 2, 3 차원은 인공지능에서 많이 나온다.
d0 = 10
d1 = [10, 20, 30, 40] # 1차원(vector)
d2 = [  [10, 20], [10, 20]  ] # 2차원(matrix)
d22 = [  (10, 20), (10, 20)  ]
d222 = [{'aa':10, 'bb':20},{'aa':30, 'bb':40}] # 딕셔너리도 1차원이다.
d3 = [  [  [10, 20], [10, 20]  ], [  [10, 20], [10, 20]  ] ] # 3차원

print(d2[0][1])
print(d222[1]['bb'])