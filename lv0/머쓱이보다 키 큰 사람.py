# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    return list(x > height for x in array).count(True)


# main function
def main():
    result = solution([149, 180, 192, 170], 167)
    print(result)


# run program
if __name__ == "__main__":
    main()
