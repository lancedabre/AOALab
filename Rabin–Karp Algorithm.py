def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    base = 256
    mod = 10**9 + 7
    p_hash = 0
    t_hash = 0
    h = 1
    for _ in range(m - 1):
        h = (h * base) % mod
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
    result = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            result.append(i)
        if i < n - m:
            t_hash = (t_hash - ord(text[i]) * h) % mod
            t_hash = (t_hash * base + ord(text[i + m])) % mod
    return result

print(rabin_karp("abracadabra", "abra"))