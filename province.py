import pandas as pd
import pygal as pg
import csv
percent = pd.read_csv("project1.csv") #import file
prov = []
cen = []
north = []
nest = []
south = []
for i in range(2551, 2561):
    cen.append(float(percent[str(i)][3]))
    north.append(float(percent[str(i)][29]))
    nest.append(float(percent[str(i)][47]))
    south.append(float(percent[str(i)][68]))

line_chart = pg.Line()
line_chart.title = 'อัตราการเกิดในโรงพยาบาลในระยะเวลา10ปี (%)'
line_chart.x_labels = map(str, range(2551, 2561))
line_chart.add('Central region',cen)
line_chart.add('Northern Thailand',north)
line_chart.add('Northeastern Thailand',nest)
line_chart.add('Northeastern Thailand',south)
line_chart.render_to_file("province.svg")
