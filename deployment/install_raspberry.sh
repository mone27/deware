#!/usr/bin/env bash
## to install this do    wget https://raw.githubusercontent.com/mone27/deware/master/deployment/install_raspberry.sh
if [ ! -d "$HOME/berryconda3" ]; then
    wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
    bash Berryconda3-2.0.0-Linux-armv7l.sh -b
fi

INSTALL_DIR = "$HOME/berryconda3"

source ${INSTALL_DIR}/bin/activate


mkdir $HOME/deware_data/

mkdir deware_downloads
cd deware_downloads
git clone https://github.com/mone27/deware.git
python setup.py install

rm $INSTALL_DIR/lib/python3.6/site-packages/deware/core/settings.py
mv $INSTALL_DIR/lib/python3.6/site-packages/deware/core/settings_raspberry.py $INSTALL_DIR/lib/python3.6/site-packages/deware/core/settings.py


sudo echo "[Unit]
Description=deware core which collects data from serial port and save it to db
After=multi-user.target

[Service]
ExecStart=$INSTALL_DIR/bin/python -m deware.core.main
Type=simple
Restart=always

[Install]
WantedBy=default.target" > /etc/systemd/system/deware-core.service
sudo systemctl daemon-reload
sudo systemd-analize deware-core.service
sudo systemctl enable deware-core.service
sudo systemctl start deware-core.service
