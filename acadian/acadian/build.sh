g++ -c -fPIC m.cpp -o switcher.o -I/usr/include/python2.7/ -std=c++11
g++ -shared -o switcher.so switcher.o -lpython2.7 -lboost_python
