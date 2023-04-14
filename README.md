# cs4279

```
cd Desktop
sudo apt-get install cmake build-essential git libopencv-dev libtclap-dev libmagic-dev
git clone https://github.com/AlexeyAB/darknet.git
cd darknet
nano Makefile
```
#### edit Makefile to set LIBSO=1, OPENMP=1, OPENCV=1. Save it
make
sudo cp libdarknet.so /usr/local/lib/
sudo cp include/darknet.h /usr/local/include/
sudo ldconfig
cd ..
git clone https://github.com/stephanecharette/DarkHelp.git
cd DarkHelp
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
make package
sudo dpkg -i darkhelp*.deb
# now cd back to desktop
git clone https://github.com/stephanecharette/DarkPlate
cd cs4279
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
cd ..
python3 flask_app.py
