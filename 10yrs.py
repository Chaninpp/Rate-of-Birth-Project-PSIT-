import pandas as pd
import pygal as pg
import csv
percent = pd.read_csv("project1.csv") #import file
per = []
for i in range(2551, 2561):
    per.append(float(percent[str(i)][1]))

line_chart = pg.Line()
line_chart.title = 'อัตราการเกิดในโรงพยาบาลในระยะเวลา10ปี(%)'
line_chart.x_labels = map(str, range(2551, 2561))
line_chart.add("Rate of birth in", per)
line_chart.render_to_file("10yrs.svg")   
