def getSize(n):
    size = 0
    while n > 0:
        n = n // 10
        size += 1
    return size

def square(n):
    return n * n

def isHappy(n):
    seen = set()

    while n != 1:
        # 셋 써서 중복 나오면 루프니
        if n in seen:
            return False
        seen.add(n)

        curSum = 0
        temp = n

        # 자릿수별로 쪼개기
        while temp > 0:
            cur = temp % 10
            curSum += square(cur)
            temp = temp // 10

        n = curSum

    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")