import numpy as np #Importing the Numpy Library.
import matplotlib.pyplot as plt #Importing the Matplotlib Library.

c4 = [
25.116,
24.903,
24.972,
25.078,
24.952,
25.206,
25.362,
25.367,
25.507,
25.636,
25.065,
24.846
]

c5 = [
24.805,
25.064,
25.131,
25.218,
25.041,
25.08,
25.339,
24.921,
24.836,
24.684,
24.849,
25.025
]

c10 = [
25.017,
25.08,
25.241,
25.398,
25.414,
25.048,
24.638,
24.639,
24.7,
24.843,
25.193,
25.245
]

c18mine = [
25.076,
25.42,
24.744,
25.681,
25.684,
25.893,
25.885,
24.972,
25.175,
25.337,
25.507,
25.567
]

c18book = [
25.05,
25.555,
25.339,
25.549,
25.659,
25.786,
25.742,
24.965,
25.029,
25.4,
25.371,
25.568
]

c32 = [
26.461,
27.458,
27.635,
28.141,
26.131,
26.122,
27.242,
26.918,
26.647,
27.365,
25.813,
26.422
]

c56 = [
26.334,
26.51,
26.561,
26.108,
25.972,
26.584,
26.893,
27.466,
25.743,
26.582,
26.69,
26.132
]

date =[
465.781,
476.707,
478.986,
482.401,
485.216,
489.037,
493.528,
498.824,
503.852,
510.819,
520.949,
522.959
]

c4d = 0.0527
c5d = 0.0366
c10d = 0.0661
c18Md = 0.0740
c18Bd = 0.0110
c32d = 0.2045
c56d = 0.0869



plt.figure(1)
plt.plot(date, c4)
plt.errorbar(date, c4, yerr=c4d, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 4") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 4.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(2)
plt.plot(date, c5)
plt.errorbar(date, c5, yerr=c5d, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 5") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 5.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(3)
plt.plot(date, c10)
plt.errorbar(date, c10, yerr=c10d, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 10") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 10.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(4)
plt.plot(date, c18mine)
plt.errorbar(date, c18mine, yerr=c18Md, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 18(Mine)") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 18M.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(5)
plt.plot(date, c18book)
plt.errorbar(date, c18book, yerr=c18Bd, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 18(Book)") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 18B.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(6)
plt.plot(date, c32)
plt.errorbar(date, c32, yerr=c32d, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 32") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 32.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(7)
plt.plot(date, c56)
plt.errorbar(date, c56, yerr=c56d, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.title("Cepheid 56") #Setting the title of graph.
plt.xlabel("Julian Date (-244900)") #Setting the x-axis label.
plt.ylabel('Apparent Magnitude, M') #Setting the y-axis label.
plt.savefig('Cepheid 56.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();