# https://school.programmers.co.kr/learn/courses/30/lessons/181924

def solution(arr, queries):
    for query in queries:
        temp = arr[query[-1]] # 원래 값 저장
        arr[query[-1]] = arr[query[0]]
        arr[query[0]] = temp

    return arr


# main function
def main():
    result = solution([0, 1, 2, 3, 4], [[0, 3], [1, 2], [1, 4]])
    print(result)


# run program
if __name__ == "__main__":
    main()
