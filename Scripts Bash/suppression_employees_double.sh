#!/bin/bash

nbLigne=$(wc -l employe_win.txt | cut -d " " -f 1)
i=1
echo $nbLigne
while read ligne
do
	adresse=$(echo $ligne | cut -d \| -f 4)
	echo $adresse	
	grep $adresse employe_win.txt > temp
	cat temp
	sed -i "/$adresse/d" employe_win.txt
	head -n 1 temp >> employe.txt
done < employe_win.txt

