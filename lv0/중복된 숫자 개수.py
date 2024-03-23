# https://school.programmers.co.kr/learn/courses/30/lessons/120583

def solution(array, n):
    return array.count(n)


# main function
def main():
    result = solution([1, 1, 2, 3, 4, 5], 1)
    print(result)


# run program
if __name__ == "__main__":
    main()
