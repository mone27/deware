#!/usr/bin/env bash
## to install this do    wget https://raw.githubusercontent.com/mone27/deware/master/deployment/install_raspberry.sh
if [ ! -d "$HOME/berryconda3" ]; then
    wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
    bash Berryconda3-2.0.0-Linux-armv7l.sh -b
fi

INSTALL_DIR="$HOME/berryconda3"

echo $INSTALL_DIR

source $INSTALL_DIR/bin/activate


mkdir -p $HOME/deware_data/

mkdir -p deware_downloads
cd deware_downloads
if [ ! -d "deware" ]; then
	git clone https://github.com/mone27/deware.git
else
	cd deware
	git fetch --all
	git reset --hard origin/master
	cd ..
fi
cd deware

pip install -r requirements.txt

python setup.py install


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