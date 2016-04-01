g++ -c -O2 -fPIC m.cpp -o m.o -I/usr/include/python2.7/
g++ -c -O2 -fPIC switcher.cpp -o switcher.o -I/usr/include/python2.7/
g++ -shared -O2 -o uswitcher.so m.o switcher.o -lpython2.7 -lboost_python
