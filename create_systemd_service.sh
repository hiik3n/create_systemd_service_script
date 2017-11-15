#!/bin/bash
#clear
if [ $# -lt 2 ]
  then
    echo "Not all arguments supplied"
    echo 'please input the full path of script and name of service to run'
    exit 1
fi

PAR1=$1
PAR2=$2

if [ -e $PAR1 ]
then
    chmod +x $PAR1
else
    echo 'Input the full path of script is not found'
    exit 1
fi

if [ $# -eq 2 ]
  then
    echo Generating service file for  $PAR1 name $PAR2
    sudo /usr/bin/python gen_systemd_service_file.py -p $PAR1 -n $PAR2
fi

if [ -e $PAR2.service ]
then
    sudo mv $PAR2.service /lib/systemd/system/
    echo Moved $PAR2.service to /lib/systemd/system/
fi

if [ -e /lib/systemd/system/$PAR2.service ]
then
    sudo chmod 644 /lib/systemd/system/$PAR2.service
    sudo systemctl daemon-reload
    sudo systemctl enable $PAR2.service
    echo Enable $PAR2.service 
    echo DONE.
fi
