# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    for c in control:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        else:
            n -= 10

    return n


# main function
def main():
    result = solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])
    print(result)


# run program
if __name__ == "__main__":
    main()
