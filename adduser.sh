#!/bin/bash

REPEAT_CHECK=$0

while [ $REPEAT_CHECK = $0 ]
do

    echo "Please enter a username for the new user"
    read USERNAME

    echo "Please enter a password"
    read PASSWORD

    echo "Please enter a group name"
    read GROUP

    if [ $USERNAME ] && [ $PASSWORD ];
    then
        sudo useradd $USERNAME -p $PASSWORD
        sudo groupadd $GROUP
        sudo usermod -aG $GROUP $USERNAME
    else
        echo "Please enter a valid username and password"
    fi

    echo "Would you like to add a new user? (yes/no)"
    read ANSWER

    if [ $ANSWER = "yes" ]
    then
        echo "Prompts will re-run"
    else
        REPEAT_CHECK = $(( REPEAT_CHECK + 1 ))
        print $REPEAT_CHECK
    fi
done

