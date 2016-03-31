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

- The string and characters are all alphanumeric with ascii encoding

https://gist.github.com/melpomene/2359537
"""

def switcher(s, a, b):
    """ iteratively switching a and b between first and second halves of string s inwardly
    Args:
        s: string to be switched
        a: a length-1 character
        b: a length-1 character

    Returns:
        a switched string
    """
    L = len(s)
    if L<2 or len(a)!=1 or len(b)!=1:
        return s
    i, j, s = 0, L-1, list(s)
    while i<(L>>1):
        if s[i] == a:
            while j >= (L>>1):
                if s[j]==b:
                    s[i], s[j] = s[j], s[i]
                    j -= 1
                    break
                j -= 1
        i += 1
    return ''.join(s)

def switcher_recursive(s, a, b):
    def __switcher_recursive(s, a, b, i, j):
        if i >= (len(s) >> 1) or j < (len(s)>>1):
            return s
        ni, nj = i + 1, j - 1
        if s[i] == a and s[j] != b:
            ni -= 1
        elif s[i] != a and s[j] == b:
            nj += 1
        elif s[i] == a and s[j] == b:
            s[i], s[j] = s[j], s[i]
        return __switcher_recursive(s, a, b, ni, nj)
    L = len(s)
    return s if (L<2 or len(a)!=1 or len(b)!=1) else ''.join(__switcher_recursive(list(s), a, b, 0, L-1))

##################################################################################################
def sequal(haystack, begin, end, needle):
    for i, v in enumerate(needle):
        if begin + i>=end or needle[i] != haystack[begin + i]:
            return False
    return True

def switcher2(s, a, b):
    L, M, N = len(s), len(a), len(b)
    if L < M + N or len(a)==0 or len(b)==0:
        return s
    s, a, b = list(s), list(a), list(b)

    def set_null(s, i):
        s[i]='\0'

    i, j, count = 0, L - 1, 0
    while i<(L >> 1) and j>=L>>1:
        if sequal(s, i, L>>1, a):
            while j>=L>>1:
                if sequal(s, j, L, b):
                    [set_null(s, i+k) for k in range(M)]
                    [set_null(s, j+k) for k in range(N)]
                    count += 2
                    j -= 1
                    break
                j -= 1
            i += M-1
        i += 1

    ns = []
    i, c = 0, count>>1
    while i<L:
        if s[i] == '\0':
            if i < (L >> 1) and count>=c:
                i += M-1
                ns += b
            else:
                i += N-1
                ns += a
            count -= 1
        else:
            ns.append(s[i])
        i += 1
    return ''.join(ns)

def switcher2_recursive(s, a, b):
    def __switcher2_recursive(s, a, b, i, j, iend, ma, mb):
        L, M, N= len(s), len(a), len(b)
        if i >= iend or j < (L>>1):
            return list(s)
        ni, nj = i, j
        s, a, b = list(s), list(a), list(b)

        ma = ma or sequal(s, i, iend, a)
        mb = mb or sequal(s, j, L, b)
        if not ma and not mb:
            ni+=1
            nj-=1
        elif ma and not mb:
            nj-=1
        elif not ma and mb:
            ni+=1
        elif ma and mb:
            s = s[:i] + b + s[i+M:j] + a + s[j+N:L]
            iend += N - M
            ni += N
            ma = mb = False
        return __switcher2_recursive(s, a, b, ni, nj, iend, ma, mb)

    L, M, N= len(s), len(a), len(b)
    return s if (L<M + N or M==0 or N==0) else ''.join(__switcher2_recursive(s, a, b, 0, L - 1, L >> 1, False, False))


testcase=[
    [ "abcd", "a", "", "abcd"                    ],
	[ "henrywoodd", "henry", "", "henrywoodd"    ],
	[ "", "", "", ""                             ],
	[ "ab", "", "", "ab"                         ],
	[ "abacdeff", "a", "e", "ebacdaff"           ],
	[ "wooddhenry", "", "henry", "wooddhenry"    ],
	[ "abxcdefe", "a", "e", "ebxcdefa"           ],
	[ "babb", "a", "b", "bbba"                   ],
	[ "baba", "a", "b", "bbaa"                   ],
	[ "bab", "a", "b", "bab"                     ],
	[ "", "a", "e",""                            ],
	[ "ab", "a", "b", "ba"                       ],
	[ "abcabdefff", "ab", "eff", "effcabdabf"    ],
	[ "ab", "henry", "woo", "ab"                 ],
	[ "henrywoo", "henry", "woo", "henrywoo"     ],
	[ "henryddwoo", "henry", "woo", "wooddhenry" ],
	[ "henrywoodd", "henry", "woo", "woohenrydd" ],
	[ "abhenryddwcdww", "henry", "w", "abwddwcdwhenry"]
]

for tc in testcase:
    if len(tc[1])<=1 and len(tc[2])<=1:
        print switcher(tc[0], tc[1], tc[2]) == tc[3]
        print switcher_recursive(tc[0], tc[1], tc[2]) == tc[3]
    print switcher2(tc[0], tc[1], tc[2]) == tc[3]
    print switcher2_recursive(tc[0], tc[1], tc[2]) == tc[3]
