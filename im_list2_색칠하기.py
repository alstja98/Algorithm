T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    regions = []
    for _ in range(N):
        region = list(map(int, input().split()))
        regions.append(region)

    grid = [[0 for _ in range(10)] for _ in range(10)]  # point 1. 2차원 리스트 초기화

    for region in regions:
        x1, y1, x2, y2, color = region
        for i in range(x1, x2+1):       # point 2. 특정 영역 범위 설정
            for j in range(y1, y2+1):
                grid[i][j] += color
    
    purple_count = sum(row.count(3) for row in grid)  # point 3. 2차원 리스트에서 특정 숫자의 개수 세기

    print(f"#{test_case} {purple_count}")

    