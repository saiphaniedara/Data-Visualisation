import matplotlib.pyplot as mpl
population_ages=[2,42,42,4,52,102,110,120,121,25,122,130,111,115,112,80,75,65,54,44,43,42,0,16]
bins=[p for p in range(0,131) if p%10==0]
mpl.hist(population_ages,bins,histtype='bar',rwidth=0.8)
mpl.xlabel("Age range")
mpl.ylabel("Total no of people")
mpl.title("Histogram Example")
mpl.legend()
mpl.show()
