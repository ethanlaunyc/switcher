def switcher(s, a, b):
    L = len(s)
    if L<2:
        return s
    i ,j = 0, L-1
    s = list(s)
    while i<(L>>1):
        if s[i] == a:
            while j>=(L>>1):
                if s[j]==b:
                    s[i], s[j] = s[j], s[i]
                    j -= 1
                    break
                j -= 1
        i+=1
    return ''.join(s)

def switcher_recursive(s, a, b):
    def switcher_recursive_helper(s, a, b, i, j):
        if i >= (len(s) >> 1) or j < (len(s)>>1):
            return s
        ni, nj = i + 1, j - 1
        if s[i] == a and s[j] != b:
            ni -= 1
        elif s[i] != a and s[j] == b:
            nj += 1
        elif s[i] == a and s[j] == b:
            s[i], s[j] = s[j], s[i]
        return switcher_recursive_helper(s, a, b, ni, nj)
    return s if (len(s)< 2) else ''.join(switcher_recursive_helper(list(s), a, b, 0, len(s)-1))

##################################################################################################
def sequal(haystack, head, tail, needle):
    for i, v in enumerate(needle):# (int i = 0; i<needle.size(); +=1i) {
        if head + i>tail or needle[i] != haystack[head + i]:
            return False
    return True

def switcher2(s, a, b):
    L, M, N = len(s), len(a), len(b)
    if L < M + N:
        return s
    s, a, b = list(s), list(a), list(b)

    def set_null(s, i):
        s[i]='\0'

    i, j, count = 0, L - 1, 0
    while i<(L >> 1) and j>=L>>1:
        if sequal(s, i, (L>>1)-1, a):
            while j>=L>>1:
                if sequal(s, j, L-1, b):
                    [set_null(s, i+k) for k in range(M)]# change mark to range [{1,2},{3,4}]
                    [set_null(s, j+k) for k in range(N)]
                    count += 1
                    j -= 1
                    break
                j -= 1
            i += M-1
        i += 1

    ns = []
    i = e = 0
    while i<L:
        if s[i] == '\0':
            e += 1
            if (count and e == M) or (not count and e == N):
                ns += b if count else a
                e = 0
                if count:
                    count -= 1
        else:
            ns.append(s[i])
        i += 1
    return ''.join(ns)


def switcher2_recursive_helper(s, a, b, i, j, iend, ma, mb):
    L, M, N= len(s), len(a), len(b)
    if (i >= iend or j < (L>>1)):
        return list(s)
    ni, nj = i, j
    s, a, b = list(s), list(a), list(b)

    ma = ma or sequal(s, i, iend - 1, a)
    mb = mb or sequal(s, j, L - 1, b)
    if not ma and not mb:
        ni+=1
        nj-=1
    elif ma and not mb:
        nj-=1 #opt
    elif not ma and mb:
        ni+=1
    elif ma and mb:
        s = s[:i] + b + s[i+M:j] + a + s[j+N:L]
        #s = tmp;
        iend += N - M
        ni += N
        ma = mb = False
    return switcher2_recursive_helper(s, a, b, ni, nj, iend, ma, mb)

def switcher2_recursive(s, a, b):
    L, M, N= len(s), len(a), len(b)
    if M + N == 0:
        return s
    return s if (L<M + N) else ''.join(switcher2_recursive_helper(s, a, b, 0, L - 1, L >> 1, False, False))


testcase=[
    ["abacdeff", "a", "e", "ebacdaff"],
    ["abxcdefe", "a", "e", "ebxcdefa"]
]

for tc in testcase:
    print switcher(tc[0], tc[1], tc[2]) == tc[3]
    print switcher_recursive(tc[0], tc[1], tc[2]) == tc[3]
    print switcher2(tc[0], tc[1], tc[2]) == tc[3]
    print switcher2_recursive(tc[0], tc[1], tc[2]) == tc[3]


