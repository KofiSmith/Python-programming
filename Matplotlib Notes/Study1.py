import matplotlib.pyplot as plt


#Raw Data
apple_price=[93.95,112.15,104.05,144.85,169.49]
ms_price=[39.01,50.39,57.09,69.98,94.39]
year=[2014,2015,2016,2017,2018]

#Plotting both apple price and ms price on the same chart
#plt.plot(year, apple_price, year,ms_price)



#Creating a grid for the plots
fig_1 = plt.figure(1, figsize=(1,1))
apple = fig_1.add_subplot(1,2,1)
ms = fig_1.add_subplot(1,2,2)
#apple.plot(year, apple_price)
#ms.plot(year, ms_price)

plt.show() #This displays the graph

