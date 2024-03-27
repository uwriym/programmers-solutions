# https://school.programmers.co.kr/learn/courses/30/lessons/120806

def solution(num1, num2):
    return int((float(num1) / num2)*1000)


# main function
def main():
    result = solution(7, 3)
    print(result)


# run program
if __name__ == "__main__":
    main()
