def countingValleys(steps: int, path: list[str]) -> int:
    altitude = 0
    valleys = 0
    in_valley = False

    for step in path:
        if step == "U":
            altitude += 1
        else:
            altitude -= 1

        if altitude == -1 and not in_valley:
            in_valley = True
            valleys += 1
        elif altitude == 0 and in_valley:
            in_valley = False

    return valleys


print(countingValleys(8, ["UDDDUDUU"]))
