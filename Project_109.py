import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")

performance = df['reading score'].tolist()

mean = statistics.mean(performance)
median = statistics.median(performance)
mode = statistics.mode(performance)
std_deviation = statistics.stdev(performance)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

thin_1_std_deviation = [result for result in performance if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in performance if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in performance if result > third_std_deviation_start and result < third_std_deviation_end]

print("The mean of this data set is  ",mean)
print("The median of this data set is ",median)
print("The mode of this data set is ",mode)
print("The standard deviation of this data set is ",sd)
print("The percent of data that lies within 1 standard deviation is ",len(thin_1_std_deviation)*100.0/len(performance))
print("The percent of data that lies within 2 standard deviations is ",len(thin_2_std_deviation)*100.0/len(performance))
print("The percent of data that lies within 3 standard deviations is ",len(thin_3_std_deviation)*100.0/len(performance))