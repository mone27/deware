#!/usr/bin/env bash
mkdir deware_downloads
cd deware_downloads
git clone https://github.com/mone27/deware.git
python setup.py install
export INSTALL_DIR ="$HOME/berryconda3"
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
# cd .. ; rm deware_downloads
