# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        str_i = str(i)
        result = ""
        for c in str_i:
            if c != "5" and c != "0":
                continue
            result += c
        if len(result) == len(str_i):
            answer.append(int(result))

    return [-1] if len(answer) == 0 else answer


# main function
def main():
    result = solution(10, 20)
    print(result)


# run program
if __name__ == "__main__":
    main()
