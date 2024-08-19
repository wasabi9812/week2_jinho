from collections import deque

N, M = map(int, input().split())
maze = [[] for _ in range(N)]
for i in range(N):
    mazedata = input().strip()
    for j in range(len(mazedata)):
        maze[i].append(int(mazedata[j]))

# 상하좌우 이동을 위한 dx, dy 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])
    maze[x][y] = 1  # 시작점도 거리에 포함되므로 1로 설정

    while queue:
        x, y = queue.popleft()

        # 목표 지점에 도착하면 종료
        if x == N-1 and y == M-1:
            return maze[x][y]

        # 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 가능 여부 확인
            if 0 <= nx < N and 0 <= ny < M:  # 범위 내에 있고
                if maze[nx][ny] == 1:  # 이동 가능하면
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 1  # 이동 거리를 기록

    return -1  # 도착할 수 없는 경우

# BFS를 통해 시작점에서 최단 경로를 탐색합니다.
result = bfs(0, 0)
print(result)