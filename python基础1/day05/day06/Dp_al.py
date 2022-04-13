def main():
    item = list(map(int, input().split()))
    overall, partitial = item[0], item[0]
    for i in range(1, len(item)):
        # 查看部分和和item[i], 如果当前的部分和加上item[i]之后还没有item【i】大，jirang
        partitial = max(item[i], item[i] + partitial)
        overall = max(partitial, overall)
    print(overall)

def climb_stair():
    stairs = int(input())
    dp = {}
    dp[1] = 1
    dp[2] = 2
    for i in range(3, stairs + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[stairs])


if __name__ == '__main__':
    climb_stair()