def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []
    bad = {}
    for i in range(m):
        bad[pattern[i]] = i
    shift = [0] * (m + 1)
    border = [0] * (m + 1)
    i, j = m, m + 1
    border[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j
    j = border[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border[j]
    res = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            res.append(s)
            s += shift[0]
        else:
            bc = j - bad.get(text[s + j], -1)
            gs = shift[j + 1]
            s += max(bc, gs)
    return res

print(boyer_moore("abracadabra", "abra"))