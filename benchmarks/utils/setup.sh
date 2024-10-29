#!/bin/bash

# Install CUDA 11.2
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
rm cuda-keyring_1.0-1_all.deb
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update
sudo apt-get -y install cuda=11.2.0-1

# Install GraalVM 21.0.0.2
wget https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-21.0.0.2/graalvm-ce-java8-linux-amd64-21.0.0.2.tar.gz
tar xfz graalvm-ce-java8-linux-amd64-21.0.0.2.tar.gz
rm graalvm-ce-java8-linux-amd64-21.0.0.2.tar.gz
gu install nodejs

# Build gpjson
cd gpjson
./gradlew build
./gradlew copyToGraalVM -PgraalVMDirectory=$GRAAL_HOME # Do not use with graalvm >= 22 

# Install java 8 and set it as default
sudo apt install openjdk-8-jdk
sudo update-alternatives --config java

# Keep bash session open
exec bash

# Install Data Center GPU manager (for A100)
sudo apt-get update
sudo apt-get install -y datacenter-gpu-manager
sudo apt-get install cuda-drivers-fabricmanager-520
sudo service nvidia-fabricmanager start