import random
from colorama import Fore

options: list[str] = []
with open('input.txt', 'r') as f:
    for line in f:
        options.append(line.strip())

pairs = [(a, b) for i, a in enumerate(options[:-1]) for b in options[i+1:]]

# Shuffle pairs
random.shuffle(pairs)

# Check scores

scores = {option: 0 for option in options}

for i, (a, b) in enumerate(pairs):
    print(f"\nPair {i+1}/{len(pairs)}\n")

    print(Fore.GREEN + "a: " + a + Fore.RESET)
    print(Fore.BLUE + "b: " + b + Fore.RESET)

    while True:
        choice = input(Fore.YELLOW + "a or b? " + Fore.RESET).strip().lower()
        if choice == 'a':
            scores[a] += 1
            break
        if choice == 'b':
            scores[b] += 1
            break
        print(Fore.RED + "Try again" + Fore.RESET)

leaderboard = [*scores.items()]
leaderboard.sort(key=lambda item: -item[1])

print("\nRESULTS\n")
print("\n".join((f"#{i+1} ({score}): {option}" for i, (option, score) in enumerate(leaderboard))))
