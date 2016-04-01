""" To test functions in switcher.py

In setUp function, the program generates strings with pattern a in first 
half of string s, and pattern b in second half In each string, the number 
of pattern is between 1 to PATTERN_MAXNUM(=500). These strings(s) and 
patterns(a,b) are stored in list args1 and args2. Then it calls a simple 
implementation of switching algorithm called 'native_switcher' to calculate 
the results and save to lists res1 and res2. 'native_switcher' uses python 
builtin string functions, so it is very fast and simple.

In the test_* functions, different functions from switcher.py will be 
invoked with argument stored in args1 args2. The results returned will 
be compared with the results of 'native_switcher'. If there is any 
difference, it means the function from switcher.py has bug.

The following is what I get when running in my machine:

    $python test_switcher.py
    Testing 'switcher' and 'uswitcher' with 4000 test cases for each function.
    ----------------------------------------------------------------------
    [+]setUp is started...
    [-]setUp is done.(7.56s)
    
    [+]test_switcher is started...
    [-]test_switcher is done.(8.83s)
    .
    [+]test_switcher2 is started...
    [-]test_switcher2 is done.(7.51s)
    .
    [+]test_switcher2_recursive is started...
    [-]test_switcher2_recursive is done.(1.43s)
    .
    [+]test_switcher_recursive is started...
    [-]test_switcher_recursive is done.(3.61s)
    .
    [+]test_uswitcher is started...
    [-]test_uswitcher is done.(0.33s)
    .
    [+]test_uswitcher2 is started...
    [-]test_uswitcher2 is done.(0.86s)
    .
    [+]test_uswitcher2_recursive is started...
    [-]test_uswitcher2_recursive is done.(3.20s)
    .
    [+]test_uswitcher_recursive is started...
    [-]test_uswitcher_recursive is done.(0.27s)
    .
    ----------------------------------------------------------------------
    Ran 8 tests in 53.362s
    
    OK

"""
import sys
import unittest
import switcher as SW
import uswitcher as USW
from random import seed, randint
from collections import deque
from datetime import datetime


PATTERN_MAXNUM = 500
TESTCASE_NUM = 4000

seed()

def randomchar():
    return chr(randint(0, 25) + ord('a')) if randint(0,10)&1 else chr(randint(0, 58) + ord('A'))

RSTR = ''.join([randomchar() for i in range(100)])

def generate_str(a,b):
    que = deque()
    stk = []
    for i in range(randint(1,PATTERN_MAXNUM)):
        m1 = randint(0, len(RSTR))
        que.append(RSTR[m1:m1 + randint(0, 5)])
        m2 = randint(0, 10000)%len(RSTR)
        stk.append(RSTR[m2:m2 + randint(0, 5)])
    r1 = ''
    while len(que) > 0:
        p = que.popleft()
        tmp = randint(0,25)%len(RSTR)
        r1 += p.replace(a, RSTR[tmp:tmp + len(a)])
        r1 += a

    r2 = ''
    while len(stk) > 1:
        p = stk.pop()
        r2 += p.replace(b, chr(ord(b[0] if len(b) else 'x')))
        r2 += b

    padding = ''
    while len(r2) < len(r1):
        i = randint(0, 100) % len(RSTR)
        h = RSTR[i/2:i/2+1] if len(r2)%2==0 else b+RSTR[i/3:i/3+1]
        padding += h
        r2 = h + r2
    if len(r2) >len(r1):
        r2 = r2[len(r2)-len(r1):]
    return r1 + r2

def native_switcher(s, a, b):
    L, M, N, MI = len(s), len(a), len(b), len(s) >> 1
    if L < M + N or M == 0 or N == 0 or a == b or (M > MI or N > L - MI):
        return s
    s1, s2 = s[:MI], s[MI:]
    c = min(s1.count(a),s2.count(b))
    s_r, a_r, b_r = s2[::-1], a[::-1], b[::-1]
    return s1.replace(a,b,c) + s_r.replace(b_r,a_r,c)[::-1]

class SwitcherTest(unittest.TestCase):
    args1, args2, res1, res2 = [], [], [], []

    def setUp(self):
        """Prepare arguments and results for testing

        self.args1 stroes arguments as (s,a,b) where s is sring, a and b are length-1 char
        self.args2 stroes arguments as (s,a,b) where s is sring, a and b are strings of arbitrary length

        self.res1 stores results of switcher algorithm 1
        self.res2 stores results of switcher algorithm 2
        """
        if len(self.args1) > 0:
            return
        print "[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for c in range(TESTCASE_NUM):
            i = randint(0,50)%len(RSTR)
            j = randint(0,100)%len(RSTR)
            P1, P2 = RSTR[i:i+1], RSTR[j:j+1]
            s = generate_str(P1, P2)
            self.args1.append((s, P1, P2))

            P1, P2 = RSTR[i:i+randint(0,5)], RSTR[j:j+randint(0,10)]
            s = generate_str(P1,P2)
            self.args2.append((s,P1,P2))

        for arg in self.args1:
            self.res1.append(native_switcher(arg[0],arg[1],arg[2]))
        for arg in self.args2:
            self.res2.append(native_switcher(arg[0],arg[1],arg[2]))
        print "[-]setUp is done.({:.2f}s)".format((datetime.now()-start).microseconds/1e5)

    def test_switcher(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args1):
            self.assertEqual(self.res1[i], SW.switcher(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_switcher_recursive(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args1):
            self.assertEqual(self.res1[i], SW.switcher_recursive(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_switcher2(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args2):
            self.assertEqual(self.res2[i], SW.switcher2(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_switcher2_recursive(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args2):
            self.assertEqual(self.res2[i], SW.switcher2_recursive(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_uswitcher(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args1):
            self.assertEqual(self.res1[i], USW.switcher(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_uswitcher_recursive(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args1):
            self.assertEqual(self.res1[i], USW.switcher_recursive(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_uswitcher2(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args2):
            self.assertEqual(self.res2[i], USW.switcher2(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)

    def test_uswitcher2_recursive(self):
        print "\n[+]{} is started...".format(sys._getframe().f_code.co_name)
        start = datetime.now()
        for i,arg in enumerate(self.args2):
            self.assertEqual(self.res2[i], USW.switcher2_recursive(arg[0],arg[1],arg[2]))
        print "[-]{} is done.({:.2f}s)".format(sys._getframe().f_code.co_name, (datetime.now()-start).microseconds/1e5)


if __name__ == '__main__':
    print "Testing 'switcher' and 'uswitcher' with {} test cases for each function.".format(TESTCASE_NUM)
    print '----------------------------------------------------------------------'
    unittest.main()



