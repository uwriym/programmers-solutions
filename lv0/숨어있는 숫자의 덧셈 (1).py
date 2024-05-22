# https://school.programmers.co.kr/learn/courses/30/lessons/120851

# `isdigit()` 메서드로 확인 가능하다.
def solution(my_string):
    result = 0
    for c in my_string:
        try:
            if str(int(c)) == c:
                result += int(c)
        except:
            continue
    return result


# main function
def main():
    result = solution("1a2b3c4d123")
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
