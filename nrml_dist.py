from os import stat
from numpy import median
import plotly.express as px
import statistics
import csv
import pandas as pd

df = pd.read_csv("std_data.csv")

math_list = df["math score"].to_list()

mean = statistics.mean(math_list)
mode = statistics.mode(math_list)
median = statistics.median(math_list)
std = statistics.stdev(math_list)

print("Mean, Median and Mode of Math score is : {},{} and {} respectivly." .format(mean,median,mode))

std1_strt, std1_end = mean - std, mean + std
std2_strt, std2_end = mean - (2*std), mean + (2*std)
std3_strt, std3_end = mean - (3*std), mean + (3*std)

math_list_std1 = [result for result in math_list if result>std1_strt and result<std1_end]
math_list_std2 = [result for result in math_list if result>std2_strt and result<std2_end]
math_list_std3 = [result for result in math_list if result>std3_strt and result<std3_end]

print("{}% of data for Height lies within 1st Standard Deviartion" .format(len(math_list_std1)*100.0/len(math_list)))
print("{}% of data for Height lies within 2nd Standard Deviartion" .format(len(math_list_std2)*100.0/len(math_list)))
print("{}% of data for Height lies within 3rd Standard Deviartion" .format(len(math_list_std3)*100.0/len(math_list)))