# https://school.programmers.co.kr/learn/courses/30/lessons/181923

def solution(arr, queries):
    result = []
    for s, e, k in queries:
        min_num = None
        i = s
        while i <= e:
            if arr[i] <= k:
                i += 1
                continue

            if min_num is None:
                min_num = arr[i]
                i += 1
                continue

            if min_num > arr[i]:
                min_num = arr[i]

            i += 1

        if min_num is None:
            result.append(-1)
        else:
            result.append(min_num)

    return result


# main function
def main():
    result = solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]])
    print(result)


# run program
if __name__ == "__main__":
    main()
