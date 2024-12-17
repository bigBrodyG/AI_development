# HOW TO USE FACE_RECOGNITION
### USEFUL RESOURCES
[Cool short video](https://youtu.be/-HzUuTRyL_Q)
[English video](https://www.youtube.com/watch?v=5yPeKQzCPdI) --> [freecodes](https://pysource.com/free-source-codes/)
[Other English video](https://youtu.be/D5xqcGk6LEcl)

## CREATE ENVIROMENT 
Initially, open terminal and put this commands:
```
sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh #if you are using x86 distro
curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-aarch64.sh #if you are using ARM64 distro
curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-s390x.sh #if you are using IBMZ/LinuxOne/s390x 
```
Install Anaconda 3
```
bash ~/Anaconda3-2024.10-1-Linux-x86_64.sh #if you are using different distro, check file name with `ls`
```
Then, refresh enviroment:
```
source ~/.bashrc
```
You can also control whether or not your shell has the base environment activated each time it opens. The following commands only work if conda has been initialized first:
```
conda config --set auto_activate_base True
```
Full tutorial [here](https://docs.anaconda.com/anaconda/install/)

## INSTALL DEPENDENCIES
Install Cmake:
```
pip install cmake
```
Warning the `pip` command requires python enviroment active
### INSTALL DLIB
To install dlib for python on Ubuntu, follow this step:
- [x] Install requirements
```
sudo apt-get update #update system packages
sudo apt-get install build-essential cmake #if you've aready installed it, skip this step
sudo apt-get install libopenblas-dev liblapack-dev #packages for dlib
sudo apt-get install libx11-dev libgtk-3-dev #packages for dlib
sudo apt-get install python python-dev python-pip #python packages to install correctly dlib
sudo apt-get install python3 python3-dev python3-pip #python packages to install correctly dlib
```
- [ ] Install dlib
```
pip install numpy
pip install dlib
```
- [ ] Check dlib version
Initialize **python3 shell** with `python3` 
```
import dlib
dlib.__version__
```
Check version. If you can do this, you have installed correctly dlib.
### INSTALL OTHER REQUIREMENTS
```
pip install face_recognition #if your python version is at least 3.0, use pip3 command
pip install opencv-python #if your python version is at least 3.0, use pip3 command
```
