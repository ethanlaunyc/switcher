""" switcher of first and second half of a string

a. Write a function that takes in a string S, a character C1, and another character C2, and switches occurrences of C1
in the first half of string S with occurrences of C2 in the second half of string S.  The function should only switch
these characters until one of the sides runs out of their respective character.  The switching should be done from the
outsides of the strings inward; in other words, it should always replace outermost characters first.

For instance, an example function

    switcheroo1("abacdeff","a","e")

would return "ebacdaff" because there was only one instance of "e" in the second half of the string.

Assume you do not have the use of string functions, but you do have the ability to compare characters with "=".  Assume
that all strings are represented as arrays.  Use any programming language that you like. The function can return a new
string and does not need to do the switching in-place.

b. Same as above, but now instead of switching characters, the function should switch any two given strings S1 and S2.

For instance,

    switcheroo2("abcabdefff","ab","eff")

would return "effcabdabf".

c. Redo a using recursion.

d. Redo b using recursion.

Assumptions:

- If string length is odd, the median will be considered as the first element of second half

Take 'abc' as an example, 'a' is the first half, and 'bc' is the second half

- If S1 or S2 is null string, or C1 or C2 is null character, the switching will not happen because null character can
be considered as matching arbitrary place or not matching any place at all. Another reason is null string/character
has different meaning in different languages like Python and C/C++. If we consider null char or null string, the
algorithm will have different implementation for different languages.

- The string and characters are all ascii encoding characters

- https://gist.github.com/melpomene/2359537
"""


__all__ = ['switcher', 'switcher2',
           'switcher_recursive', 'switcher2_recursive']


def switcher(s, a, b):
    """ Iteratively switching character a and b between first and second halves of string s inwardly

    Args:
        s: string to be switched
        a: a length-1 character
        b: a length-1 character

    Returns:
        a switched string

    Complexity:
        Time: O(N)
        Space: O(1)
    """
    L, M, N, MI = len(s), len(a), len(b), len(s) >> 1
    if L < 2 or M != 1 or N != 1 or a == b:
        return s
    i, j, s = 0, L - 1, list(s)
    while i < MI and j >= MI:
        if s[i] == a:
            while j >= MI:
                if s[j] == b:
                    s[i], s[j] = s[j], s[i]
                    j -= 1
                    break
                j -= 1
        i += 1
    return ''.join(s)


def switcher_recursive(s, a, b):
    """ Recursively switching a and b between first and second halves of string s inwardly

    Args:
        s: string to be switched
        a: a length-1 character
        b: a length-1 character

    Returns:
        a switched string

    Complexity:
        Time: O(N)
        Space: O(1)
    """
    L, M, N, MI = len(s), len(a), len(b), len(s) >> 1

    def __switcher_recursive(s, a, b, i, j):
        if i >= MI or j < MI:
            return s
        ni, nj = i, j
        if s[i] == a and s[j] != b:
            nj -= 1
        elif s[i] != a and s[j] == b:
            ni += 1
        elif s[i] == a and s[j] == b:
            s[i], s[j] = s[j], s[i]
            ni += 1; nj -= 1
        else:
            ni += 1; nj -= 1
        while nj>=MI and s[nj]!=b: nj -= 1
        while ni <MI and s[ni]!=a: ni += 1
        return __switcher_recursive(s, a, b, ni, nj)
    if L < 2 or M != 1 or N != 1 or a == b:
        return s
    else:
        try:
            return ''.join(__switcher_recursive(list(s), a, b, 0, L - 1))
        except RuntimeError, e:
            print "Stackoverflow: %s. Please use iterative version!" % str(e)
            print "s={},a={},b={}".format(''.join(s), ''.join(a), ''.join(b))
            return None



def startswith(haystack, begin, end, needle):
    """ A helper function to check if haystack starts with needle at index range [begin, end)

    Args:
        haystack: list, list to be searched in
        begin: int, head index of haystack range
        end: int, past to last index of haystack range
        needle: list, list to be compared with

    Returns:
        True if haystack at range [begin,end) starts from needle

    Complexity:
        Time: O(N) where N is the length of needle
        Space: O(1)
    """
    assert(len(haystack) >= end and begin <= end)
    if (len(needle) > end - begin):
        return False
    for i, v in enumerate(needle):
        if begin + i >= end or needle[i] != haystack[begin + i]:
            return False
    return True


def switcher2(s, a, b):
    """ Iteratively switching string a and string b between first and second halves of string s inwardly

    Args:
        s: string to be switched
        a: string to be put into the second half of s
        b: string to be put into the first half of s

    Returns:
        A switched string

    Complexity:
        Time:
            O(N*M) where N is len(s), M is max(len(a), len(b))
            Expected/average time complexity is O(N)
        Space:
            O(N) where N is length of s
    """
    L, M, N, MI = len(s), len(a), len(b), len(s) >> 1
    if L < M + N or M == 0 or N == 0 or a == b or (M > MI or N > L - MI):
        return s

    if isinstance(s, str):
        s, a, b = list(s), list(a), list(b)
    i, j, k, ns = 0, L - N, 0, []
    while i < MI and j >= MI:
        if startswith(s, i, MI, a):
            while j >= MI:
                if startswith(s, j, L, b):
                    for x in range(M):
                        s[i + x] = 0
                    for x in range(N):
                        s[j + x] = 0
                    j -= N
                    break
                j -= 1
            i += M - 1
        i += 1  # O(MN)

    while k < L:
        if s[k] == 0:
            k += (M if k < MI else N) - 1
            ns += (b if k < MI else a)
        else:
            ns.append(s[k])
        k += 1
    return ''.join(ns)


def switcher2_recursive(s, a, b):
    """ Recursively switching string a and string b between first and second halves of string s inwardly

    Args:
        s: string to be switched
        a: string to be put into the second half of s
        b: string to be put into the first half of s

    Returns:
        A switched string

    Complexity:
        Time:
            O(N*M) where N is len(s), M is max(len(a), len(b))
            Expected/average time complexity is O(N)
        Space:
            O(N) where N is length of s
    """
    L, M, N, MI = len(s), len(a), len(b), len(s) >> 1

    def __switcher2_recursive(s, a, b, i, j, iend, ma, mb, sd):
        if i >= iend or j < iend:
            return list(s)
        ni, nj = i, j
        if isinstance(s, str):
            s, a, b = list(s), list(a), list(b)

        ma = ma or startswith(s, i, iend, a)
        mb = mb or startswith(s, j, L, b)
        if not ma and not mb:
            nj -= 1
            while nj>=iend and s[nj]!=b[0]: nj -= 1
            ni += 1
            while ni<iend and s[ni]!=a[0]: ni += 1
        elif ma and not mb:
            nj -= 1
            while nj>=iend and s[nj]!=b[0]: nj -= 1
        elif not ma and mb:
            ni += 1
            while ni<iend and s[ni]!=a[0]: ni += 1
        elif ma and mb:
            s = s[:i] + b + s[i + M:j] + a + s[j + N:L]
            iend += N - M
            ni += N
            nj -= M
            ma = mb = False
        return __switcher2_recursive(s, a, b, ni, nj, iend, ma, mb, sd+1)

    if L < M + N or M == 0 or N == 0 or a == b or (M > MI or N > L - MI):
        return s
    else:
        try:
            return ''.join(__switcher2_recursive(s, a, b, 0, L - N, MI, False, False, 0))
        except RuntimeError, e:
            print "Stackoverflow:%s. Please use iterative version!" % str(e)
            print "s={},a={},b={}".format(''.join(s), ''.join(a), ''.join(b))
            return None


if __name__ == '__main__':
    testcase = [
        ['pcsiknueagfokyvdalvdigonzxwptojxgvdgfmdcbnawgivdcfrhpwlqlgfmvdptojxgalvdvdnzxwvdaigonzxwvdxglpawpfhnrvdslckynrvsuquxadckynrvsxadckynrvsigkynrvsjbsggckynrvsgaigonkynrvsvkpcsiknuekynrvsalkynrvsqlkynrvsskynrvs','vd','kynrvs',''],
        ['ekmyifqtyupgakbjpfqtslbruwmemsfqtjzaosouyupgakfqtvthfufqtrtozkafkbjcutozfrtoukafutozfrtotoswuopflvutozfrtoutozfrto','fqt','utozfrto',''],
        ["", "", "", ""],
        ["", "", "e", ""],
        ["", "a", "", ""],
        ["ab", "", "", "ab"],
        ["ab", "a", "b", "ba"],
        ["bab", "a", "b", "bab"],
        ["abcd", "a", "", "abcd"],
        ["baba", "a", "b", "bbaa"],
        ["babb", "a", "b", "bbba"],
        ["ab", "henry", "woo", "ab"],
        ["abacdeff", "a", "e", "ebacdaff"],
        ["abxcdefe", "a", "e", "ebxcdefa"],
        ["henrywoo", "henry", "woo", "henrywoo"],
        ["henrywoodd", "henry", "", "henrywoodd"],
        ["wooddhenry", "", "henry", "wooddhenry"],
        ["abcabdefff", "ab", "eff", "effcabdabf"],
        ["henryddwoo", "henry", "woo", "wooddhenry"],
        ["henrywoodd", "henry", "woo", "woohenrydd"],
        ["aaaaabbbbbb", "a", "bbbbbb", "bbbbbbaaaaa"],
        ["abhenryddwcdww", "henry", "w", "abwddwcdwhenry"],
        ["abhenryddwcdww", "henry", "henry", "abhenryddwcdww"],
        ['x' * 23 + "henryahenrybhenrychenry", "x",
            "henry", 'henry' * 4 + 'x' * 19 + 'xaxbxcx'],
        ["henryahenrybhenrychenryxxxxxxxxxxxxxxxxxxxxxxx",
            "henry", "x", 'xaxbxcx' + 'x' * 19 + 'henry' * 4],
    ]

    for tc in testcase:
        print switcher2_recursive(tc[0], tc[1], tc[2]) == tc[3],
        if len(tc[1]) <= 1 and len(tc[2]) <= 1:
            print switcher(tc[0], tc[1], tc[2]) == tc[3],
            print switcher_recursive(tc[0], tc[1], tc[2]) == tc[3],
        print switcher2_recursive(tc[0], tc[1], tc[2]) == tc[3],
        print switcher2(tc[0], tc[1], tc[2]) == tc[3],
