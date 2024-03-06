# https://school.programmers.co.kr/learn/courses/30/lessons/181925

def solution(numLog):
    before_log = 0
    result = ""
    for log in numLog:
        if before_log == log:
            continue
        elif before_log + 1 == log:
            result += "w"
        elif before_log - 1 == log:
            result += "s"
        elif before_log + 10 == log:
            result += "d"
        elif before_log - 10 == log:
            result += "a"

        before_log = log

    return result


# main function
def main():
    result = solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])
    print(result)


# run program
if __name__ == "__main__":
    main()
