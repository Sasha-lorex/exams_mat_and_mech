#Here is a Python code of the KMP algorithm
def KMPSearch(word, txt):
    m = len(word)
    n = len(txt)
    lps = [0] * m
    j = 0
    i = 0
    count = 0
    computeLPS(word, m, lps)
    while i < n:
        if word[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and word[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count


def computeLPS(word, m, lps):
    len = 0
    i = 1
    while i < m:
        if word[i] == word[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


s = "ttttttt"
s1 = "tt"

count = KMPSearch(s1, s)
print("Количество вхождений", s1, "в", s, "равно", count)
