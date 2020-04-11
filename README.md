# covid19_infographics
Infographics for COVID-19

There are 4 infographics in total which have to be populated with various
translations. We will work on 4 different branches since each of the image has
different strings which need to be populated at different places.

The four branches are named `infographx`, where `x` goes from `1` to `4`. To
work on infograph1 images you need to switch to correct branch,

```
git checkout infograph1
```

You will notice two important files, `Master_config.yaml`. This contains the
information of different fonts and font sizes for each language. The second is
a `placements.txt` file in each of the `language` folders which contains the x,
y positions and the width limit of each line. To produce images for infograph1
in English, run

```
python modify_poster.py 1 English
```

To work on other languages, add the appropriate information of fonts in the
`Master_config.yaml` file. Create directory for the language, and then add a
placements.txt file. Run `modify_poster.py`.
