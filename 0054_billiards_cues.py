# Problema Tacos de Bilhar
# OBI 2016 - Primeira Fase - Nível 1
from collections import Counter


def consult_cue(stock_queries):
    made = 0
    # Creates a container with Counter({number: quantity})
    count_queries = Counter(stock_queries)
    # Creates a dictionary with {quantities_repeated: quantity}
    count_amount = dict(Counter(count_queries.values()))
    for key, value in dict(count_amount).items():
        # quantities_repeated is odd. Ex.: 3 x 100 cm (4 made) + 3 x 80 cm (4 made) + 3 x 50 cm (4 made) = 12 cues made
        if key % 2:
            made += (key + 1) * value
        # quantities_repeated is even. Ex.: 2 x 100 cm (2 made) + 2 x 80 cm (2 made) + 2 x 50 cm (2 made) = 6 cues made
        else:
            made += key * value
    return made

    # This is a solution with Time Limit Exceeded complexity O(n^2)
    #
    # for consult in stock_queries:
    #   if consult in stock:
    #       stock.remove(consult)
    #   else:
    #       stock.append(consult)
    #       made += 2
    # return made


# This validation makes it slower, but still less than 1 sec for 10^5
def validate(c, stock_queries):
    constraints = True
    for number in stock_queries:
        if not (number in range(1, (10 ** 6) + 1)):
            constraints = False
            break
    if constraints and 1 <= c <= 10**5:
        print(consult_cue(stock_queries))


def main():
    c = int(input())
    stock_queries = list(map(int, input().split()))
    validate(c, stock_queries)


if __name__ == "__main__":
    main()
