#!/usr/bin/env python
#
# Code to insert text in poster jpg files.
#
# Copyright: Surhud More (IUCAA) 2020
#
# Bug reports/comments: Open github issues, or send pull requests

import textwrap
from PIL import Image, ImageDraw, ImageFont
from os import path
import numpy as np
import sys
import pandas

class fill_poster:
    def __init__(self, image):
        self.imagename = image
        self.image = Image.open(image+".jpeg")
        self.fullwidth = self.image.width

    # Outputs text centered on the whole picture. The value of x is ignored in this case
    def output_centered_text(self, message, x, y, width, font=None, color='rgb(0, 0, 0)', printoffset=False):

        offsety = 0
        # This class will write out the line in the file in multiple lines and center it.
        for line in textwrap.wrap(message, width):
            w, h = self.draw.textsize(line, font=font)
            self.draw.text(((self.image.width-w)/2, y + offsety), line, font=font, fill=color)
            offsety += font.getsize(line)[1]

    # Outputs text starting at particular x, y
    def output_fixed_width_text(self, message, x, y, width, font, color='rgb(0, 0, 0)'):
        offsety = 0
        for line in textwrap.wrap(message, width):
            w, h = self.draw.textsize(line, font=font)
            self.draw.text((x, y+offsety), line, font=font, fill=color)
            offsety += font.getsize(line)[1]*1.3

    def convert(self, ii, strings, plx, ply, width, language, fonts):
        # Initiate image
        self.draw = ImageDraw.Draw(self.image)

        # Add all the strings at the right places with the right fonts
        self.output_centered_text(strings["1"], plx[0], ply[0], width[0], font=fonts["1"], color='rgb(0, 70, 140)')
        self.output_centered_text(strings["2"], plx[1], ply[1], width[1], font=fonts["2"])
        self.output_fixed_width_text(strings["3"], plx[2], ply[2], width[2], font=fonts["3"])
        self.output_fixed_width_text(strings["4"], plx[3], ply[3], width[3], font=fonts["3"])
        self.output_fixed_width_text(strings["5"], plx[4], ply[4], width[4], font=fonts["3"])
        self.output_fixed_width_text(strings["6"], plx[5], ply[5], width[5], font=fonts["3"])

        # Save the file
        self.image.save(self.imagename+"_%s.jpeg" % language)

if __name__ == "__main__":

    imagenum = int(sys.argv[1])
    language = sys.argv[2]

    # Read the placements file, format will be:
    # x, y, width
    plx, ply, width = np.loadtxt("%s/placements.txt" % (language), unpack=1)

    # For every string read x, y, 

    # Read the fonts information
    from yaml import load, Loader
    fin = open("Master_config.yaml", "r")
    config = load(fin, Loader=Loader)

    # Setup fonts
    fonts = {}
    fonts["1"] = ImageFont.truetype(config[language]["font1"], size=config[language]["size1"])
    fonts["2"] = ImageFont.truetype(config[language]["font2"], size=config[language]["size2"])
    fonts["3"] = ImageFont.truetype(config[language]["font3"], size=config[language]["size3"])

    # Read the translations
    df = pandas.read_csv("Sample.csv")
    df.fillna("", inplace = True)

    strings = {}
    # First read the Series title
    jj = 1
    strings["%d" % jj] = df["%s" % language].values[0] 
    jj = jj + 1

    # Setup translation strings for each language
    for ii in range(1, df["%s" % language].values.size):
       
        if df.Image.values[ii] !=  imagenum:
            continue

        strings["%d" % jj] = df["%s" % language].values[ii]
        jj = jj + 1

    # Now output
    a = fill_poster("Sample_images/Image_%05d" % imagenum)
    a.convert(imagenum, strings, plx, ply, width, language, fonts)
