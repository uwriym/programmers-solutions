# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    result = 1
    while True:
        if result * slice >= n: 
            break
        result += 1
    return result


# main function
def main():
    result = solution(4, 12)
    print(result)


# run program
if __name__ == "__main__":
    main()
