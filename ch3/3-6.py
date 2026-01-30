# 답안 예시
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빽;
result += (n - 1)
print(result)