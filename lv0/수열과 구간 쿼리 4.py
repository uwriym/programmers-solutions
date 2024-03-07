# https://school.programmers.co.kr/learn/courses/30/lessons/181922

def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1
    return arr


# main function
def main():
    result = solution([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]])
    print(result)


# run program
if __name__ == "__main__":
    main()
