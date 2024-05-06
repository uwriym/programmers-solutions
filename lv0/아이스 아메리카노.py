# https://school.programmers.co.kr/learn/courses/30/lessons/120819

def solution(money):
    return [int(money / 5500), money % 5500]


# main function
def main():
    result = solution(15000)
    print(result)


# run program
if __name__ == "__main__":
    main()
