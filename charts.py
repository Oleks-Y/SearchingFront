import matplotlib
import matplotlib.pyplot as plt
import os


def getChart(name, x_axis, y_axis, title):
    matplotlib.use('Agg')
    plt.plot(x_axis, y_axis)
    plt.xticks(rotation='vertical')
    plt.title(title)
    #plt.xlabel(" ", fontsize=10)
    #plt.rcParams["figure.figsize"] = [4,4]
    plt.savefig("{}.png".format(name),bbox_inches='tight')
    plt.clf()
    return "{}.png".format(name)
def getChart_OneAxis(name, y_axis, title):
    matplotlib.use('Agg')
    plt.plot(y_axis)
    plt.title(title)
    plt.savefig("{}.png".format(name))
    plt.clf()
    return "{}.png".format(name)
def structureData(arr):
    print(arr)
    matplotlib.use('Agg')
    x_axis = []
    y_axis = []
    for i in arr:
        x_axis.append( i)
        y_axis.append(arr[i])
    print(x_axis)
    print(y_axis)
    return x_axis, y_axis