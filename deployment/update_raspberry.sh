#!/usr/bin/env bash
mkdir deware_donwloads
cd deware_downloads
git clone https://github.com/mone27/deware.git
python setup.py install
export INSTALL_DIR ="$HOME/berryconda3"
rm $INSTALL_DIR/lib/python3.6/site-packages/deware/core/settings.py
mv $INSTALL_DIR/lib/python3.6/site-packages/deware/core/settings_raspberry.py $INSTALL_DIR/lib/python3.6/site-packages/deware/core/settings.py
# cd .. ; rm deware_downloads
