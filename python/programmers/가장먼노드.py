'''
def solution(n, edge):
     answer = 0
    
     # 이중 배열의 안의 배열 정렬
     for i in range(len(edge)):
          edge[i] = sorted(edge[i])
     # 이중 배열의 바깥 배열 정렬
     edge = sorted(edge)

     # 엣지 개수 만큼 0 채운 배열 만듬
     num = [0 for i in range(n)]

     d = []
     for i in range(len(edge)):
          if edge[i][0] == 1:
               d[edge[i][1]] = 1

     for i in range(len(edge)):
          if d[edge[i][1]] != 0:
               continue
          else:
               d[edge[i][1]] = d[edge[i][0]]
          
     print(d)

     return answer
'''

from collections import deque
def solution(n, edge):
     graph = [[] for _ in range(n)]

     # 그래프 연결 정보 초기화.
     for node, connect in edge:
          graph[node - 1].append(connect - 1)
          graph[connect - 1].append(node - 1)

     # visited로 노드 간의 길이를 카운트.
     visited = [0] + [-1] * (n - 1)
     
     # 첫 번째 시작 노드는 [1번 노드]
     q = deque([[0, 0]])

     while q:
          cur_node, dist = q.popleft()

          for next_node in graph[cur_node]:
               if visited[next_node] == -1:
                    q.append([next_node, dist + 1])
                    visited[next_node] = dist + 1

     # visited의 max값과 그것을 카운트 한것은 가장 먼 노드의 수.
     return visited.count(max(visited))


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)
