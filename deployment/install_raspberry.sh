#!/usr/bin/env bash
wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
bash Berryconda3-2.0.0-Linux-armv7l.sh -b
export INSTALL_DIR ="$HOME/berryconda3"

source $INSTALL_DIR/bin/activate
bash ./update_raspberry.sh
mkdir $HOME/deware_data/

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
