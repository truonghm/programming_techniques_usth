import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

from loading_dataset import get_data
from stats import mean, variance, covariance, regression, median

def mean_population(weight, height):
    print("mean of height and weight is:", mean(weight), mean(height))

def median_population(weight, height):
    print("median of height and weight is:", median(weight), median(height))

def variance_population(weight, height):
    print("variance of height and weight is:", variance(weight), variance(height))

def plot_weight_vs_height(weight, height):
    plt.figure()
    plt.scatter(weight, height)
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Weight/Height population')
    plt.yticks([i for i in range(150, 210, 10)])
    plt.xticks([i for i in range(30, 100, 10)])
    plt.show()

def plot_weight_height_regression(weight, height):
    plt.figure()
    plt.scatter(weight, height)
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Weight/Height population')
    plt.yticks([i for i in range(150, 210, 10)])
    plt.xticks([i for i in range(30, 100, 10)])
    a, b =  regression(weight, height)
    x = np.linspace(30,100,70)
    y = a*x+b
    plt.plot(x, y, '-r')
    plt.show()

def plot_women_weight_height_regression(sex, weight, height):
    weight = np.array([weight[i] for i, s in enumerate(sex) if s == 'f'])
    height = np.array([height[i] for i, s in enumerate(sex) if s == 'f'])
    plt.figure()
    plt.scatter(weight, height)
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Weight/Height of women')
    plt.yticks([i for i in range(150, 210, 10)])
    plt.xticks([i for i in range(30, 100, 10)])
    a, b =  regression(weight, height)
    x = np.linspace(30,100,70)
    y = a*x+b
    plt.plot(x, y, '-r')
    plt.show()

def plot_women_vs_men_weight_height_regression(sex, weight, height):
    weight_f = np.array([weight[i] for i, s in enumerate(sex) if s == 'f'])
    height_f = np.array([height[i] for i, s in enumerate(sex) if s == 'f'])
    weight_m = np.array([weight[i] for i, s in enumerate(sex) if s == 'h'])
    height_m = np.array([height[i] for i, s in enumerate(sex) if s == 'h'])

    plt.subplot(1, 2, 1)
    plt.scatter(weight_m, height_m)
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Men')
    plt.yticks([i for i in range(150, 210, 10)])
    plt.xticks([i for i in range(30, 100, 10)])
    a, b =  regression(weight_m, height_m)
    x = np.linspace(30,100,70)
    y = a*x+b
    plt.plot(x, y, '-r')

    plt.subplot(1, 2, 2)
    plt.scatter(weight_f, height_f)
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Women')
    plt.yticks([i for i in range(150, 210, 10)])
    plt.xticks([i for i in range(30, 100, 10)])
    a, b =  regression(weight_f, height_f)
    x = np.linspace(30,100,70)
    y = a*x+b
    plt.plot(x, y, '-r')
    plt.show()


def plot_bmi_compare_hist(sex, weight, height):
    bmi = (weight/height**2)*10000
    m_count_under = 0
    f_count_under = 0
    m_count_over = 0
    f_count_over = 0
    for s, val in zip(sex, bmi):
        # print(s, val)
        if val <= 18.5:
            if s == 'f':
                f_count_under += 1
            else:
                m_count_under += 1
        elif val >= 25:
            if s == 'f':
                f_count_over += 1
            else:
                m_count_over += 1
    # print(m_count, f_count)

    plt.subplot(1, 2, 1)
    plt.bar(['Male', 'Female'], [f_count_under, m_count_under], color=['blue', 'orange'], width=1)
    colors = {'Male':'blue', 'Female':'orange'}         
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)
    plt.title("Underweight")
    # plt.show()

    plt.subplot(1, 2, 2)
    plt.bar(['Male', 'Female'], [f_count_over, m_count_over], color=['blue', 'orange'], width=1)
    colors = {'Male':'blue', 'Female':'orange'}         
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)
    plt.title("Overweight")
    plt.show()


def plot_bmi_hist(sex, weight, height):
    bmi = (weight/height**2)*10000
    m_count = 0
    f_count = 0
    for s, val in zip(sex, bmi):
        # print(s, val)
        if val >= 18.5 and val <= 25:
            if s == 'f':
                f_count += 1
            else:
                m_count += 1
    # print(m_count, f_count)
    plt.bar(['Male', 'Female'], [m_count, f_count], color=['blue', 'orange'], width=1)
    colors = {'Male':'blue', 'Female':'orange'}         
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)
    plt.title("BMI between male and female")
    plt.show()

def plot_density(x, y):
    nbins=300
    k = kde.gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    # Make the plot
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto')
    plt.colorbar()
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.show()

def plot_density_nipy_spectral(x, y):
    nbins=300
    k = kde.gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    # Make the plot
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', cmap='nipy_spectral')
    plt.colorbar()
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.show()


data = get_data('population.csv')

sex = data[:,0,]
weight = np.array([int(i) for i in data[:,1,]])
height = np.array([int(i) for i in data[:,2,]])

mean_population(weight, height)
median_population(weight, height)
variance_population(weight, height)

plot_weight_vs_height(weight, height)
plot_weight_height_regression(weight, height)
plot_women_weight_height_regression(sex, weight, height)
plot_women_vs_men_weight_height_regression(sex, weight, height)
plot_bmi_hist(sex, weight, height)
plot_bmi_compare_hist(sex, weight, height)
plot_density(weight, height)
plot_density_nipy_spectral(weight, height)