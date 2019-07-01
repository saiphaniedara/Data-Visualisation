#without using explode and autopct
import matplotlib.pyplot as mpl
slices=[8,10,15,20,35]
activities=['Close up','Pepsodent','Meswak','Colgate','Sensodyne']
cols=['c','m','r','g','b']
mpl.pie(slices,labels=activities,colors=cols,shadow=True)
mpl.title("Percentage of people using ToothPaste")
mpl.legend()
mpl.show()
