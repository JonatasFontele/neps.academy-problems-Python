# Problema Tacos de Bilhar
# OBI 2016 - Primeira Fase - Nível 1
from collections import Counter


# This is the fastest solution
def consult_cue(stock_queries):
    made = 0
    # Creates a container that stores elements as a dictionary with Counter({number: quantity})
    count_queries = Counter(stock_queries)
    # Creates a container that stores elements as a dictionary with {quantities_repeated: quantity}
    count_amount = Counter(count_queries.values())
    for key, value in count_amount.items():
        # quantities_repeated is odd. Ex.: 3 x 100 cm (4 made) + 3 x 80 cm (4 made) + 3 x 50 cm (4 made) = 12 cues made
        if key % 2:
            made += (key + 1) * value
        # quantities_repeated is even. Ex.: 2 x 100 cm (2 made) + 2 x 80 cm (2 made) + 2 x 50 cm (2 made) = 6 cues made
        else:
            made += key * value
    return made

# This is the second fastest solution
# def consult_cue2(stock_queries):
#     count_queries = Counter(stock_queries)
#     count_amount = Counter(count_queries.values())
#     return sum([(key + 1) * value if key % 2 else key * value for key, value in count_amount.items()])

# This is the third fastest solution
# def consult_cue3(stock_queries):
#     count_queries = Counter(stock_queries)
#     count_amount = Counter(count_queries.values())
#     return sum(list(map(lambda kv: my_func(kv[0], kv[1]), count_amount.items())))
# def my_func(key, value):
#     if key % 2:
#         return (key + 1) * value
#     return key * value

# This is a solution with Time Limit Exceeded complexity O(n^2) the slower
# It's better for short input and a great time of repetitions of the function in the process.
# def consult_cue4(stock_queries):
#   stock = []
#   made = 0
#   for consult in stock_queries:
#       if consult in stock:
#           stock.remove(consult)
#       else:
#           stock.append(consult)
#           made += 2
#   return made


def main():
    int(input())
    stock_queries = list(map(int, input().split()))
    print(consult_cue(stock_queries))


if __name__ == "__main__":
    main()
