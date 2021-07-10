import statistics as st
import pandas as pd
import random as rd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df= pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
pupulation_mean=st.mean(data)
print("mean population:",pupulation_mean)

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=rd.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean_dataset=st.mean(dataset)
    return mean_dataset

def plot_graph(mean_list):
    mean=st.mean(mean_list)
    fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))  
    fig .show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_means(30)
        mean_list.append(set_of_means)
    plot_graph(mean_list)
    mean_of_sample=st.mean(mean_list)
    print("mean of sample:",mean_of_sample)

setup()