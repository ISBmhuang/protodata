import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "/Users/user/workspace/data/"
riboreps = pd.ExcelFile(path+"isoreps.xlsx")

riborep1 = riboreps.parse("riboisorep1")
riborep2 = riboreps.parse("riboisorep2")
riborep3 = riboreps.parse("riboisorep3")

datlist = []

x=0

while x<117:
    # if x % 3 == 0:
    #     geneName = riborep1.loc[x,'gene']
    datlist.append(
    [0,((riborep1.loc[x,'ratio']+riborep2.loc[x,'ratio'] + riborep3.loc[x,'ratio']) / 3),
    ((riborep1.loc[x+1,'ratio']+riborep2.loc[x+1,'ratio'] + riborep3.loc[x+1,'ratio']) / 3),
    ((riborep1.loc[x+2,'ratio']+riborep2.loc[x+2,'ratio'] + riborep3.loc[x+2,'ratio']) / 3)]
    )
    #riborep1.loc[x,'ratio']
    x+=3

# print type(riborep1)

timepoints = [0,1,2,3]
labels = [1,2,3,4]

#print datlist

for x in datlist:
    plt.plot(timepoints, x)
    plt.grid(True)
    # plt.set_xticks(timepoints)
    plt.xticks(timepoints,labels)
    plt.yticks(np.arange(-3, 1.5, 0.5))
    plt.title('Log2 Ratios vs TP 1 Over Time')
    plt.xlabel('Time Point')
    plt.ylabel('Log2 Ratios vs TP 1')
#This might be a bit much.
plt.savefig('log2ratiosvstp_ribosomeisolated.png', format='png', dpi=3000)
