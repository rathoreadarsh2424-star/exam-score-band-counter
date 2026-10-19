def lower_bound(scores, target):
    """Return the first index i where scores[i] >= target."""
    left, right = 0, len(scores)

    while left < right:
        mid = (left + right) // 2
        if scores[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def countInBand(scores, low, high):
    """Count scores in the inclusive range [low, high] in O(log n) time."""
    first = lower_bound(scores, low)
    after_last = lower_bound(scores, high + 1)
    return after_last - first


if __name__ == "__main__":
    scores = [35, 42, 42, 50, 58, 58, 58, 63, 71, 88]

    print(countInBand(scores, 42, 58))   # Expected: 6
    print(countInBand(scores, 90, 100))  # Expected: 0
