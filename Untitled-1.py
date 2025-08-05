def min_moves(chips):
    n = len(chips)
    total = sum(chips)
    if total % n != 0:
        print("Не целое")
        return

    target = total // n
    diffs = []
    for chip in chips:
        diffs.append(chip - target)

    min_moves = float('inf')
    
    for start in range(n):
        balance = 0
        moves = 0
        for i in range(n):
            idx = (start + i) % n
            balance += diffs[idx]
            moves += abs(balance)
        min_moves = min(min_moves, moves)

    return min_moves


# === Тесты ==
print(min_moves([1, 5, 9, 10, 5]))
print(min_moves([1, 2, 3]))
print(min_moves([0, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
print(min_moves([3,2,2,3,1,1,2]))