# License Plate Recognition from a Video Stream
## Final Project for CS 4279 at Vanderbilt University

Here are the steps to set it up locally. First, let's set up Darknet:
```
cd Desktop

sudo apt-get install cmake build-essential git libopencv-dev libtclap-dev libmagic-dev

git clone https://github.com/AlexeyAB/darknet.git

cd darknet

nano Makefile
```
#### At this point, edit the Makefile to set LIBSO=1, OPENMP=1, OPENCV=1 and other parameters as needed. Consider turning GPU=1 and CUDNN=1 if you have CUDA installed.
```
make

sudo cp libdarknet.so /usr/local/lib/

sudo cp include/darknet.h /usr/local/include/

sudo ldconfig
```

Now, let's set up DarkHelp, a C++ API wrapper for darknet.
```
cd ..

git clone https://github.com/stephanecharette/DarkHelp.git

cd DarkHelp

mkdir build

cd build

cmake -DCMAKE_BUILD_TYPE=Release ..

make

make package

sudo dpkg -i darkhelp*.deb
```

Now, cd back to your Desktop, and 
# now cd back to desktop
git clone https://github.com/malikudit/cs4279.git
cd cs4279
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
cd ..
python3 flask_app.py
