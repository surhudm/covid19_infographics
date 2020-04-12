#!/bin/bash

#python save_csv.py
for i in `cat Master_config.yaml | grep ^[A-Z]`                
do       
        j=${i/:/}   
        echo $j
	mkdir -p $j;           
        #cp -v ./English/placements.txt  $j/ 
	if [[ ! -f "$j/placements.txt" ]]                 
        then
		cp -v ./English/placements.txt  $j/		
        fi   
        python modify_poster.py 3 ${j} 1.77;  
        cp -v Sample_images/Image_000*_${j}.jpg ${j}/;         
done 
