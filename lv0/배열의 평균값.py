# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    return sum(numbers) / len(numbers)


# main function
def main():
    result = solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
