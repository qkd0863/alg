edges = [ 
  (0, 4, 463), (0, 11, 347), (0, 12, 410), (0, 20, 294), (0, 21, 360), 
  (1, 5, 61), (1, 10, 343), (1, 17, 395), (2, 6, 162), (2, 10, 431), 
  (2, 16, 135), (2, 17, 415), (2, 18, 281), (2, 23, 435), (3, 4, 59), 
  (3, 15, 230), (3, 21, 118), (4, 11, 393), (4, 15, 273), (5, 9, 341), 
  (5, 10, 333), (5, 23, 427), (6, 10, 268), (6, 12, 432), (6, 14, 465), 
  (6, 16, 298), (6, 18, 278), (6, 19, 199), (7, 9, 120), (7, 13, 257), 
  (7, 24, 410), (8, 11, 275), (8, 12, 111), (8, 15, 407), (8, 19, 420), 
  (8, 20, 481), (9, 10, 341), (9, 23, 253), (9, 24, 357), (11, 15, 141), 
  (12, 16, 194), (12, 19, 410), (12, 20, 370), (12, 22, 324), (13, 14, 375), 
  (13, 17, 323), (13, 22, 318), (13, 23, 83), (14, 19, 350), (14, 24, 211), 
  (15, 21, 177), (16, 18, 348), (16, 20, 421), (18, 24, 377), (19, 22, 211), 
  (19, 23, 376), (22, 23, 400), (23, 24, 335), 
]
num_vertex = 25

print('Using Maximul Matching')

# build adj set from edges
from collections import defaultdict
g = defaultdict(set)
for ...:
  ???
  ???

# 구하려는 Set Cover 해 정점들
vc = set()

vertices = set(range(num_vertex))
covered_edge = 0
while covered_edge < n_edges:
  u = ??? # randomly select from vertices
  v = ??? # u 에 연결된 점 하나 뽑아오기
  ??? # v 도 vertices 에서 제거

  for n in u,v:
    vc.add(u)
    # # remove edges connected to u
    for k in range(n_cities):
      if ??:#n에서 k로 가는 선이 살아있다면(안 지워졌다면)
        ??#그 선은 지운다
        if??:# k에서 n으로 가는 선이 살아 있다면(안 지워졌다면)
          ??#그 선은 지운다
    covered_edge += ???


  # # vc.add(u)
  # # remove edges connected to u
  # covered_edge += ???
  # # vc.add(v)
  # # remove edges connected to v
  # covered_edge += ???

print(len(vc), vc)

