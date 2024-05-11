# https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    return list(len(str) for str in strlist)


# main function
def main():
    result = solution(["We", "are", "the", "world!"])
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
