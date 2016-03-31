// acadian.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <vector>
#include <string>
#include <assert.h>
#include <iostream>

using namespace std;

string switcher(string s, char a, char b) {
	int L = s.size(), i = 0, j = L-1;
	if (L < 2) return s;
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
	if (i >= (s.size() >> 1) || j < (s.size()>>1)) return s;
	int ni = i + 1, nj = j - 1;
	if (s[i] == a && s[j] != b) {
		--ni;
	}
	else if (s[i] != a && s[j] == b) {
		++nj;
	}
	else if (s[i] == a && s[j] == b) {
		swap(s[i], s[j]);
	}
	return switcher_recursive_helper(s, a, b, ni, nj);
}

string switcher_recursive(string s, char a, char b) {
	return (s.size()< 2) ? s : switcher_recursive_helper(s, a, b, 0, s.size() - 1);
}

bool stringequal(const string& haystack, int head, int tail, const string& needle) {
	for (int i = 0; i<needle.size(); ++i) {
		if (head + i>tail || needle[i] != haystack[head + i])
			return false;
	}
	return true;
}

string switcher2_recursive_helper(string s, string a, string b, int i, int j, int iend, bool ma, bool mb) {
	int L = s.size(), M = a.size(), N = b.size();
	if (i >= iend || j < (L>>1)) return s;
	int ni = i, nj = j;
	ma = ma || stringequal(s, i, iend - 1, a);
	mb = mb || stringequal(s, j, L - 1, b);
	if (!ma && !mb) {
		++ni, --nj;
	}
	else if (ma && !mb) {
		--nj; //opt
	}
	else if (!ma && mb) {
		++ni;
	}
	else if (ma && mb) {
		string tmp;
		for (int k = 0; k<i; ++k) { tmp.push_back(s[k]); }
		tmp += b;
		for (int k = i + M; k<(N?j:j+1); ++k) { tmp.push_back(s[k]); }
		tmp += a;
		for (int k = j + ((N==0)?1:N); k<L; ++k) { tmp.push_back(s[k]); }
		s = tmp;
		iend += N - M;
		ni += N;
		ma = false, mb = false;
	}
	return switcher2_recursive_helper(s, a, b, ni, nj, iend, ma, mb);
}

string switcher2_recursive(string s, string a, string b) {
	int L = s.size(), M = a.size(), N = b.size();
	if (M + N == 0) return s;
	return (L<M + N) ? s : switcher2_recursive_helper(s, a, b, 0, L - 1, L >> 1, false, false);
}

string switcher2(string s, string a, string b) {
	int L = s.size(), M = a.size(), N = b.size();
	if (L < M + N || M + N == 0) return s;

	auto mark = [](string& s, int i, int M, int j, int N) {
		for (int k = 0; k<M; ++k) { s[i + k] = '\0'; }
		for (int k = 0; k<N; ++k) { s[j + k] = '\0'; }
	};

	int i = 0, j = L - 1, count = 0;
	for (; i<(L>>1) && j>=(L>>1); ++i) {
		if (stringequal(s, i, (L >> 1) - 1, a)) {
			for (; j >= L >> 1; --j) {
				if (stringequal(s, j, L - 1, b)) {
					mark(s, i, M, j, N);
					++++count;
					break;
				}
			}
			i += M - 1;
		}
	}
	string ns{ "" };
	int c = count>>1;
	for (int i = 0; i<L; ++i) {
		if (s[i] == '\0') {
			if (i < (L >> 1) && count>=c) {
				i += M - 1;
				ns += b;
			}
			else {
				i += N - 1;
				ns += a;
			}
			count--;
		} else {
			ns.push_back(s[i]);
		}
	}
	while (count-- != 0){
		if (N == 0) ns += a;
		if (M == 0) ns = b + ns;
	}

	return ns;
}

vector<vector<string>> vts = {
	{ "", "", "", "" },
	{ "ab", "", "", "ab" },
	{ "abacdeff", "a", "e", "ebacdaff" },
	{ "henrywoodd", "henry", "", "wooddhenry" },
	{ "wooddhenry", "", "henry", "henrywoodd" },
	{ "abxcdefe", "a", "e", "ebxcdefa"},
	{ "babb", "a", "b", "bbba" },
	{ "baba", "a", "b", "bbaa" },
	{ "a", "a", "", "a" },
	{ "abacdeff", "a", "e", "ebacdaff" },
	{ "bab", "a", "b", "bab" },
	{ "abacdeff", "a", "e", "ebacdaff" },
	{ "", "a", "e","" },
	{ "ab", "a", "b", "ba" },
	{ "baba", "a", "b", "bbaa" }, //
	{ "abcabdefff", "ab", "eff", "effcabdabf" },
	{ "ab", "henry", "woo", "ab" },
	{ "henrywoo", "henry", "woo", "henrywoo" },
	{ "henryddwoo", "henry", "woo", "wooddhenry" },
	{ "henrywoodd", "henry", "woo", "woohenrydd" },
	{ "ahenrywoodd", "henry", "", "ahenrywoodd" },
	{ "abhenryddwcdww", "henry", "w", "abwddwcdwhenry" }
};
int main() {
	for (auto t : vts) {
		//cout << t[0] << "," << t[1] << "," << t[2] << "," << t[3] << endl;
		if (t[1].size() == 1 && t[2].size() == 1) {
			assert(switcher(t[0], t[1][0], t[2][0]) == t[3]);
			assert(switcher_recursive(t[0], t[1][0], t[2][0]) == t[3]);
		}
		cout << (switcher2(t[0], t[1], t[2]) == t[3]) << "|"<< switcher2(t[0], t[1], t[2]) << endl;
		cout << (switcher2_recursive(t[0], t[1], t[2]) == t[3]) << "~" << switcher2_recursive(t[0], t[1], t[2]) << endl;
	}
	return 0;
}
