import matplotlib.pyplot as mpl
x=[3,4.1,5,6,6.1,6.3]
y=[25,25,30,29,42,46]
mpl.scatter(x,y,label='scatter plot',s=40,color='c',marker='o')
mpl.xlabel('x')
mpl.ylabel('y')
mpl.title('My Graph')
mpl.legend()
mpl.show()
