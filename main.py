import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import of functions.py
from functions import generate_data, example_data, get_weighted_sum, sigmoid, cross_entropy, update_weights, update_bias

#definition of bias, learning rate, and epochs to run
bias = 0.5
l_rate=0.01
epochs = 40
epoch_loss=[]

#definition of data set lenght and number of layers
n_layers=3 #number of layers of input data (x1, x2, x3, ... xn)
n_data=50 #number or lenght of input data set

#definition of data and weights at beggining to start iterations
data, weights = generate_data(n_data, n_layers)

#Definitions of the train model that will import all functions from functions.py
def train_model(data, weights, bias, l_rate, epochs):
    for e in range(epochs):
        individual_loss=[]
        for i in range(len(data)):
            feature=data.loc[i][:-1] #excluding last column because is target coulumn
            target = data.loc[i][-1]
            w_sum= get_weighted_sum(feature, weights, bias)
            prediction = sigmoid(w_sum)
            loss = cross_entropy(target, prediction)
            individual_loss.append(loss)
            #now comes gradient descent
            ##print("OLD Values")
            ##print(weights, bias)
            weights = update_weights(weights, l_rate, target, prediction, feature)
            bias = update_bias(bias, l_rate, target, prediction)
            ##print("NEW Values")
            ##print(weights, bias)
        average_loss=sum(individual_loss)/len(individual_loss)
        epoch_loss.append(average_loss)
        print("********************************")
        print("epoch: ", e)
        print("loss: ", average_loss)
        print("updated weights: ", weights)

#Running user interface and train model
print("\n Press 1 to generate dataset and target randomly \n Press 2 to run example \n")
user = int(input())
if (user==1):
    print("Option 1: random dataset \n")
    data, weights = generate_data(n_data, n_layers)
    print("\n initial data: \n", data)
    print("\n initial weights \n", weights)
    train_model(data, weights, bias, l_rate, epochs)
elif (user==2):
    print("Option 2: Example \n")
    data, weights = example_data()
    train_model(data, weights, bias, l_rate, epochs)
else:
    print("wrong option")
#Plot the average loss usin pandas and save plot as PDF file
df = pd.DataFrame(epoch_loss)
df_plot = df.plot(kind="line", grid=True).get_figure()
df_plot.savefig("Training_loss.pdf")
print("ver gráfica en pdf del error")
