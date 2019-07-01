import matplotlib.pyplot as mpl
slices=[8,10,15,20,35]
activities=['Close up','Pepsodent','Meswak','Colgate','Sensodyne']
cols=['c','m','r','g','b']
mpl.pie(slices,labels=activities,colors=cols,shadow=True,startangle=30,explode=(0,0,0,0,0.1),autopct='%.2f%%')
mpl.title("Percentage of people using ToothPaste")
mpl.legend()
mpl.show()
