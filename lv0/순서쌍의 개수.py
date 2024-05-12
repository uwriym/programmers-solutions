# https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0: result += 1
    return result



# main function
def main():
    result = solution(20)
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
