#!/bin/bash
                                                                                                                 
for i in `cat Master_config.yaml | grep ^[A-Z]`                                                                  
do                                                                                                               
        j=${i/:/}                                                                                            
        echo $j
	mkdir -p $j;                                                                                 
        #x=$(cat ${i::-1}/placements_${i::-1}.txt | wc -l)                                                        
        if [[ ! -f "$j/placements.txt" ]]                                                                                       
        then
		cp -v ./English/placements.txt  $j/		
                #y=`head -n 1 ${i::-1}/placements_${i::-1}.txt`                                                   
                #echo 19 ${y:2:${#y}} >> ${i::-1}/placements_${i::-1}.txt                                         
        fi                                                                                                       
        python modify_poster.py 2 ${j};                                                                        
        #cp -v Final/Sample_images/000*_${i::-1}.jpg ${i::-1}/;                                                   
done 
