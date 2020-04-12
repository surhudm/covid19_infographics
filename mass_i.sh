#!/bin/bash

#python save_csv.py
for i in `cat Master_config.yaml | grep ^[A-Z]`                
do       
        j=${i/:/}   
        echo $j
	      mkdir -p $j;           
        #cp -v ./English/placements.txt  $j/ 
        #x=$(cat ${i::-1}/placements_${i::-1}.txt | wc -l)
        if [[ ! -f "$j/placements.txt" ]]                 
        then
              cp -v ./English/placements.txt  $j/	
              #y=`head -n 1 ${i::-1}/placements_${i::-1}.txt`                                                   
              #echo 19 ${y:2:${#y}} >> ${i::-1}/placements_${i::-1}.txt
        fi   
        python modify_poster.py 3 ${j} 1.77;  
        cp -v Sample_images/Image_000*_${j}.jpg ${j}/;         

done 
