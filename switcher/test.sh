#!/bin/bash
#
# To test switcher to uswitcher
#

if [ ! -d "python" ]; then
    exit
fi

cd python
if [ -f "uswitcher.so" ]; then
    python test_switcher.py
else
    echo "*********************************************************************"
    echo "Cannot find switcher.so, now run python version only..."
    echo "*********************************************************************"
    python test_switcher.py SwitcherTest
    #python test_switcher.py UswitcherTest
fi

