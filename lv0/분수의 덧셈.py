# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(numer1, denom1, numer2, denom2):
    new_numer = (numer1 * denom2) + (numer2 * denom1)
    new_denom = denom1 * denom2

    yaksu_of_new_numer = get_yaksu(new_numer)
    yaksu_of_new_denom = get_yaksu(new_denom)

    best_yaksu = 1
    for yaksu in reversed(yaksu_of_new_numer):
        if yaksu in yaksu_of_new_denom:
            best_yaksu = yaksu
            break

    print(yaksu_of_new_numer)
    print(yaksu_of_new_denom)
    print(best_yaksu)

    return [int(new_numer / best_yaksu), int(new_denom / best_yaksu)]


def get_yaksu(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0: result.append(i)
    return result

# main function
def main():
    result = solution(1, 2, 3, 4)
    print(result)


# run program
if __name__ == "__main__":
    main()
