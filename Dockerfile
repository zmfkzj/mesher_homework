FROM ubuntu:jammy


USER root

RUN apt-get update

# install cmake 
RUN apt-get install -y cmake pkg-config mesa-utils libglu1-mesa-dev freeglut3-dev mesa-common-dev libglfw3-dev git g++
RUN apt-get clean

RUN git clone https://github.com/pixpark/gpupixel.git

# start build
RUN mkdir /gpupixel/src/build 
WORKDIR /gpupixel/src/build

# Generate project
RUN cmake ..

# Build
RUN make