import matplotlib.pyplot as mpl
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
playing=[8,5,7,8,13]
working=[7,8,7,2,2]
mpl.stackplot(days,sleeping,eating,playing,working,colors=['c','r','y','m'])
mpl.xlabel("days")
mpl.ylabel("hours")
mpl.plot([],[],color='c',label='Sleeping')
mpl.plot([],[],color='r',label='Eating')
mpl.plot([],[],color='y',label='Playing')
mpl.plot([],[],color='m',label='Working')
mpl.title("Day wise data")
mpl.legend()
mpl.show()
