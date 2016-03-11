#!/usr/bin/env bash
# This script install PhantomJS in your Debian/Ubuntu System
#
# This script must be run as root
#

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

CHROMEDRIVER_VERSION="2.21"
ARCH=$(uname -m)

if ! [ $ARCH = "x86_64" ]; then
	echo "This requires a 64-bit version of debian linux or ubuntu"
	exit 1
fi

apt-get update
apt-get install libxss1 libappindicator1 libindicator7 xvfb unzip -y

#install chrome for linux
cd ~
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome*.deb
apt-get install -f -y
dpkg -i google-chrome*.deb

#install chromedriver for linux
wget -N http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv -f chromedriver /usr/local/share/chromedriver
ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
ln -s /usr/local/share/chromedriver /usr/bin/chromedriver