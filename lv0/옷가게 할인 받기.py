# https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    percent = 100
    if price >= 500000: percent = 80
    elif price >= 300000: percent = 90
    elif price >= 100000: percent = 95
    return int(price * (percent / 100))

# main function
def main():
    result = solution(580000)
    print(result)


# run program
if __name__ == "__main__":
    main()
