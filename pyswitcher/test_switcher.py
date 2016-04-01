import unittest as ut
from switcher import *
from random import *
from collections import deque


def randomchar():
    return chr(randint(0, 25) + ord('a')) if randint(0,10)&1 else chr(randint(0, 58) + ord('A'))

RSTR = ''.join([randomchar() for i in range(100)])

def generate_str(a,b):
    que = deque()
    stk = []
    for i in range(randint(1,300)):
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

    return r1 + r2 ## before switching

def naive_switcher(s, a, b):
    L, M, N, MI = len(s), len(a), len(b), len(s) >> 1
    if L < M + N or M == 0 or N == 0 or a == b or (M > MI or N > L - MI):
        return s
    s1, s2 = s[:MI], s[MI:]
    c = min(s1.count(a),s2.count(b))
    s_r, a_r, b_r = s2[::-1], a[::-1], b[::-1]
    return s1.replace(a,b,c) + s_r.replace(b_r,a_r,c)[::-1]
    
class stkwitcherTest(ut.TestCase):
    def setUp(self):
        self.args1 = []
        self.args2 = []
        self.res1 = []
        self.res2 = []
        for c in range(2000):
            i = randint(0,50)%len(RSTR)
            j = randint(0,100)%len(RSTR)
            P1 = RSTR[i:i+randint(0,5)]
            P2 = RSTR[j:j+randint(0,10)]
            s = generate_str(P1,P2)
            self.args1.append((s,P1,P2))

            P3, P4 = RSTR[i:i+1], RSTR[j:j+1]
            s = generate_str(P3,P4)
            self.args2.append((s,P3,P4))
        for arg in self.args1:
            self.res1.append(naive_switcher(arg[0],arg[1],arg[2]))
        for arg in self.args2:
            self.res2.append(naive_switcher(arg[0],arg[1],arg[2]))

    def test_switcher2(self):
        for i,arg in enumerate(self.args1):
            self.assertEqual(self.res1[i], switcher2(arg[0],arg[1],arg[2]))

    def test_switcher2_recursive(self):
        for i,arg in enumerate(self.args1):
            self.assertEqual(self.res1[i], switcher2_recursive(arg[0],arg[1],arg[2]))

    def test_switcher(self):
        for i,arg in enumerate(self.args2):
            self.assertEqual(self.res2[i], switcher(arg[0],arg[1],arg[2]))

    def test_switcher_recursive(self):
        for i,arg in enumerate(self.args2):
            self.assertEqual(self.res2[i], switcher_recursive(arg[0],arg[1],arg[2]))

if __name__ == '__main__':
    ut.main()



