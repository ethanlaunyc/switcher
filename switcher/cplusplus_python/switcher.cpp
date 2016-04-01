#include "switcher.hpp"

using namespace std;

string switcher(string s, char a, char b) {
    int L = s.size(), i = 0, j = L-1;
    if (L < 2 || a==b) return s;
    for (; i<(L >> 1); ++i) {
        if (s[i] != a) continue;
        for (; j >= (L >> 1); --j) {
            if (s[j] != b) continue;
            swap(s[i], s[j]);
            break;
        }
    }
    return s;
}

string switcher_recursive_helper(string& s, char a, char b, int i, int j) {
    int MI = s.size() >> 1;
    if (i >= MI || j < MI)
        return s;
    int ni = i + 1, nj = j - 1;
    if (s[i] == a && s[j] != b) {
        --ni;
    } else if (s[i] != a && s[j] == b) {
        ++nj;
    } else if (s[i] == a && s[j] == b) {
        swap(s[i], s[j]);
    }
    while (nj>= MI && s[nj]!=b) --nj;
    while (ni< MI && s[ni]!=a) ++ni;
    return switcher_recursive_helper(s, a, b, ni, nj);
}

string switcher_recursive(string s, char a, char b) {
    return (s.size()< 2 || a == b) ? s : switcher_recursive_helper(s, a, b, 0, s.size() - 1);
}

bool startswith(const string& haystack, int begin, int end, const string& needle) {
    if (needle.size() > end - begin)
        return false;
    for (int i = 0; i<needle.size(); ++i) {
        if (begin + i>=end || needle[i] != haystack[begin + i])
            return false;
    }
    return true;
}

string switcher2_recursive_helper(string s, string a, string b, int i, int j,
        int iend, bool ma, bool mb)
{
    int L = s.size(), M = a.size(), N = b.size();
    if (i >= iend || j < iend)
        return s;

    ma = ma || startswith(s, i, iend, a);
    mb = mb || startswith(s, j, L, b);

    if (!ma && !mb) {
        ++i, --j;
    } else if (ma && !mb) {
        --j;
    } else if (!ma && mb) {
        ++i;
    } else if (ma && mb) {
        string tmp;
        for (int k = 0; k<i; ++k) { tmp.push_back(s[k]); }
        tmp += b;
        for (int k = i + M; k<j; ++k) { tmp.push_back(s[k]); }
        tmp += a;
        for (int k = j + N; k<L; ++k) { tmp.push_back(s[k]); }
        s = tmp;
        iend += N - M, i += N, j -= M;
        ma = false, mb = false;
    }
    while (i<iend && s[i]!=a[0])
        ++i;
    while (j>=iend && s[j]!=b[0])
        --j;
    return switcher2_recursive_helper(s, a, b, i, j, iend, ma, mb);
}

string switcher2_recursive(string s, string a, string b) {
    int L = s.size(), M = a.size(), N = b.size(), MI = L>>1;
    if (L < M + N || M == 0 || N == 0 || a == b || M > MI || N > L - MI)
        return s;
    return switcher2_recursive_helper(s, a, b, 0, L - N, MI, false, false);
}

string switcher2(string s, string a, string b) {
    int L = s.size(), M = a.size(), N = b.size(), MI = L>>1;
    if (L < M + N || M == 0 || N == 0 || a == b || M > MI || N > L-MI)
        return s;

    int i = 0, j = L - 1;
    for (; i<MI && j>=MI; ++i) {
        if (startswith(s, i, MI, a)) {
            for (; j >= MI; --j) {
                if (startswith(s, j, L, b)) {
                    for (int x = 0; x<M; ++x) { s[i + x] = 0; }
                    for (int x = 0; x<N; ++x) { s[j + x] = 0; }
                    j -= N;
                    break;
                }
            }
            i += M - 1;
        }
    }
    string ns;
    for (int i = 0; i<L; ++i) {
        if (s[i] == 0) {
            i += i<MI ? M-1 : N-1;
            ns += i<MI ? b : a;
        } else {
            ns.push_back(s[i]);
        }
    }
    return ns;
}

/*
vector<vector<string> > vts = {
    { "", "", "", "" },
    { "", "a", "e","" },
    { "a", "a", "", "a" },
    { "ab", "", "", "ab" },
    { "ab", "a", "b", "ba" },
    { "bab", "a", "b", "bab" },
    { "baba", "a", "b", "bbaa" },
    { "ab", "henry", "woo", "ab" },
    { "abxcdefe", "a", "e", "ebxcdefa"},
    { "abacdeff", "a", "e", "ebacdaff" },
    { "henrywoo", "henry", "woo", "henrywoo" },
    { "henrywoodd", "henry", "", "henrywoodd" },
    { "wooddhenry", "", "henry", "wooddhenry" },
    { "abcabdefff", "ab", "eff", "effcabdabf" },
    { "ahenrywoodd", "henry", "", "ahenrywoodd" },
    { "henryddwoo", "henry", "woo", "wooddhenry" },
    { "henrywoodd", "henry", "woo", "woohenrydd" },
    { "abhenryddwcdww", "henry", "w", "abwddwcdwhenry" }
};

int main() {
    for (auto t : vts) {
        cout << t[0] << "," << t[1] << "," << t[2] << "," << t[3] << endl;
        if (t[1].size() == 1 && t[2].size() == 1) {
            assert(switcher(t[0], t[1][0], t[2][0]) == t[3]);
            assert(switcher_recursive(t[0], t[1][0], t[2][0]) == t[3]);
        }
        cout << (switcher2(t[0], t[1], t[2]) == t[3]) << "|"<< switcher2(t[0], t[1], t[2]) << endl;
        cout << (switcher2_recursive(t[0], t[1], t[2]) == t[3]) << "~" << switcher2_recursive(t[0], t[1], t[2]) << endl;
    }
    return 0;
}
*/
