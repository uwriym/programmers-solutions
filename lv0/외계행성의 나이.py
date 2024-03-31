# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    result = ""
    for num in str(age): result += (chr(int(num) + 97))
    return result


# main function
def main():
    result = solution(23)
    print(result)


# run program
if __name__ == "__main__":
    main()
