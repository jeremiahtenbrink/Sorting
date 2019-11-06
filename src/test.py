def numberOfWays(cases):
    answers = []
    for a, b in cases:
        answer = 0
        for i in range(min(a, b)):
            answer += ((a - i) * (b - i))
        answers.append(answer)
    return answers


numberOfWays([[2, 1], [2, 3]])
