if [ ! -d "cplusplus_python" ]; then
    exit
fi
pushd cplusplus_python

g++ -c -O2 -fPIC uswitcher.cpp -o uswitcher.o -I/usr/include/python2.7/
g++ -c -O2 -fPIC switcher.cpp -o switcher.o -I/usr/include/python2.7/
g++ -shared -O2 -o uswitcher.so uswitcher.o switcher.o -lpython2.7 -lboost_python
if [ "$?" = "0" ]; then
  cp uswitcher.so ../python/
  rm -fr uswitcher.o switcher.o
fi

popd
