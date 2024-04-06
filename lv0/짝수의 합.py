# https://school.programmers.co.kr/learn/courses/30/lessons/120831

solution = lambda n: sum(list(i for i in range(n+1) if i % 2 == 0))


# main function
def main():
    result = solution(10)
    print(result)


# run program
if __name__ == "__main__":
    main()
