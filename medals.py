# Problema Medalhas
# OBI 2016 - Segunda Fase - Nível Júnior
def reward_swimmer(times):
    # In a real situation, sorted(times) would be better, so as not to lose the initial list
    times.sort()
    for time, index in times:
        print(index)


def validate(times):
    constraints = True
    # If the elements are distinct integers
    for i in range(1, len(times)):
        if times[i][0] == times[i - 1][0]:
            constraints = False
            break
    # If the elements are 1 <= time <= 1000
    for time in times:
        if not (time[0] in range(1, 1001)):
            constraints = False
            break
    if constraints:
        reward_swimmer(times)


def main():
    times = []
    # T1, T2, T3 added in a loop with range, try to be generalist
    for t in range(3):
        # Create tuples so you don't need two lists
        times.append((int(input()), t + 1))
    # Not really needed in challenges
    validate(times)


if __name__ == "__main__":
    main()
