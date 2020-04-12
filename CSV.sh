#!/bin/bash

python save_csv.py 
#rsync -azvP ~/CoVid/covid19_infographics/Sample.csv akshat@10.112.22.40:/home/akshat/Documents/Covid/covid19_infographics/
rsync -azvP ~/CoVid/covid19_infographics akshat@10.112.22.40:/home/akshat/Documents/Covid/
