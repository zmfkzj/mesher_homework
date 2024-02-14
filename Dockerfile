FROM ubuntu:jammy


USER root

RUN apt-get update

# install cmake 
RUN apt-get install -y cmake pkg-config mesa-utils libglu1-mesa-dev freeglut3-dev \
    mesa-common-dev libglfw3-dev \
    git g++ python3-pip && \
    apt-get clean

RUN git clone --recurse-submodules https://github.com/zmfkzj/mesher_homework.git

### gpupixel build

RUN mv /mesher_homework/gpupixel.h /mesher_homework/gpupixel/src/core/gpupixel.h
# start build
RUN mkdir /mesher_homework/gpupixel/src/build 
WORKDIR /mesher_homework/gpupixel/src/build

# Generate project
RUN cmake ..

# Build
RUN make && rm -rf /mesher_homework/gpupixel/src/build

RUN mv /mesher_homework/gpupixel/output/library/linux/debug/libgpupixel.so /mesher_homework/libgpupixel.so


### gpupixel build
WORKDIR /mesher_homework

RUN pip3 install -r requirements.txt