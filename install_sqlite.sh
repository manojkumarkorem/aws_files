#!/bin/bash
sudo yum update
wget https://www.sqlite.org/2018/sqlite-autoconf-3240000.tar.gz
tar zxvf sqlite-autoconf-3240000.tar.gz
cd sqlite-autoconf-3240000/
./configure --prefix=/usr/local
make
sudo make install
