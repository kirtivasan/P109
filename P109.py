import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["math score"].tolist()
dataset = []
for i in range(0,1000):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)




mean = sum(dataset)/len(dataset)
std_deviation = statistics.stdev(dataset)
median = statistics.median(dataset)
mode = statistics.mode(dataset)

first_std_deviation_start,first_std_deviation_end = mean - std_deviation,mean + std_deviation
second_std_deviation_start,second_std_deviation_end = mean - (2*std_deviation),mean + (2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean - (3*std_deviation),mean + (3*std_deviation)

fig = ff.create_distplot([dataset],["result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start], y = [0,0.17],mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17],mode = "lines", name = "STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start], y = [0,0.17],mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17],mode = "lines", name = "STANDARD DEVIATION 2"))

fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start], y = [0,0.17],mode = "lines", name = "STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end], y = [0,0.17],mode = "lines", name = "STANDARD DEVIATION 3"))


list_of_data_within_1_std_deviation = [result for result in  dataset if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in  dataset if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in  dataset if result > third_std_deviation_start and result < third_std_deviation_end]

print("mean of this data is {}".format(mean))
print("median of this data is {} ".format(median))
print("mode of this data is {}".format(mode))
print("standard deviation of this data is {}".format(std_deviation))

fig.show()

print("{}% of data lies within 1st standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dataset)))
print("{}% of data lies within 2nd standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dataset)))
print("{}% of data lies within 3rd standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dataset)))
