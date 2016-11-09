#!/bin/bash

while read ligne
do
	adresse=$(echo $ligne | cut -d \| -f 2)
	grep $adresse employe.txt > temp
	if [ $(wc -l temp | cut -d " " -f 1) == 0 ] ; then
		sed -i "/$adresse/d" eventlog_entreprise.txt
	fi
done < eventlog_entreprise.txt

