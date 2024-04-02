# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    # max_count 구하기
    max_count = 0
    for num in array:
        num_count = array.count(num)
        if num_count > max_count:
            max_count = num_count

    max_num = None
    max_count_count = 0
    for num in array:
        if array.count(num) != max_count: continue
        if max_num == num: continue
        
        max_num = num
        max_count_count += 1
        
        if max_count_count > 1:
            max_num = -1
            break

    return max_num
        
        


# main function
def main():
    result = solution([1, 2, 3, 3, 3, 4])
    print(result)


# run program
if __name__ == "__main__":
    main()
