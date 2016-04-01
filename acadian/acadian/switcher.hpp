#ifndef __SWITCHER__
#define __SWITCHER__

#include <string>

using std::string;

string switcher(string s, char a, char b);

string switcher_recursive_helper(string& s, char a, char b, int i, int j);

string switcher_recursive(string s, char a, char b);

bool startswith(const string& haystack, int begin, int end, const string& needle);

string switcher2_recursive_helper(string s, string a, string b, int i, int j,
        int iend, bool ma, bool mb);

string switcher2_recursive(string s, string a, string b);

string switcher2(string s, string a, string b);

#endif
