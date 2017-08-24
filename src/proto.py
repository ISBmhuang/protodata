import numpy as np
import pandas as pd
import xlrd

path = "/Users/user/workspace/data/"
data = pd.ExcelFile(path+"proteomicsdata.xlsx")
ribogenes = xlrd.open_workbook(path+"ribogenes.xlsx")
ribogenes = ribogenes.sheet_by_index(0)

#print (data.sheet_names)

rep1 = data.parse("Lysate-BR1", parse_cols=[0,2,6,10])
rep2 = data.parse("Lysate-BR2", parse_cols=[0,2,6,10])
rep3 = data.parse("Lysate-BR3", parse_cols=[0,2,6,10])

avgrep = []
ribolist = []
values = ['e2 vs. e1_log2_sfc', 'e3 vs. e1_log2_sfc', 'e4 vs. e1_log2_sfc']
ribo1 = []
ribo2 = []
ribo3 = []
#pd.DataFrame()

ribo1i = []
ribo2i = []
ribo3i = []

ribodata1 = []
ribodata2 = []
ribodata3 = []

# print rep1

z=1

# for protein in rep1["protein"]:
#     print x
#     x+=1

while z<57:
    ribolist.append(ribogenes.cell(z, 0).value)
    z+=1

#for gene in avgrep:
#    print rep1[]

x=0
y=0
z=0

while x<940:
    if (rep1.loc[x,'protein'] in ribolist):
        riborep1 = rep1.loc[x,'protein']
        ribo1i.append(str(x)+str(riborep1))
        ribo1.append(str(riborep1))
        # print "rep1" + riborep1
    x+=1

# print "ribo1"
# print ribo1

while y<938:
    if (rep2.loc[y,'protein'] in ribolist):
        riborep2 = rep2.loc[y,'protein']
        ribo2i.append(str(y)+str(riborep2))
        ribo2.append(str(riborep2))
        # print "rep2" + riborep2
    y+=1

# print "ribo2"
# print ribo2

while z<906:
    if (rep3.loc[z,'protein']in ribolist):
        riborep3 = rep3.loc[z,'protein']
        ribo3i.append(str(z)+str(riborep3))
        ribo3.append(str(riborep3))
        # print "rep3" + riborep3
    z+=1

# print "ribo3"
# print ribo3

set1 = set(ribo3) - (set(ribo3)-set(ribo1))
set2 = set(ribo3) - (set(ribo3)-set(ribo2))
finalset = set2 - (set2 - set1)

# print len(finalset)
#print finalset

finalset = list(finalset)
# finalset.sort()
#print finalset
#print finalset.type

a=0
b=0
c=0

#CLEAN THIS UP INTO FUNCTIONS
for gene in finalset:
    for genei in ribo1i:
        for vi in values:
            letbeg = genei.index("V")
            geneName = genei[letbeg:]
            rowNum = int(genei[:letbeg])
            if geneName == gene:
                geneValue = rep1.loc[rowNum,vi]
                ribodata1.append(str(geneName)+"_tp"+vi[1]+","+str(geneValue))
    for genei in ribo2i:
        for vi in values:
            letbeg = genei.index("V")
            geneName = genei[letbeg:]
            rowNum = int(genei[:letbeg])
            if geneName == gene:
                geneValue = rep2.loc[rowNum,vi]
                ribodata2.append(str(geneName)+"_tp"+vi[1]+","+str(geneValue))
    for genei in ribo3i:
        for vi in values:
            letbeg = genei.index("V")
            geneName = genei[letbeg:]
            rowNum = int(genei[:letbeg])
            if geneName == gene:
                geneValue = rep3.loc[rowNum,vi]
                ribodata3.append(str(geneName)+"_tp"+vi[1]+","+str(geneValue))



        #print ribo
        # if x :
        # print rep1.loc[x,'protein']
        #
        #
        # for value in values:
        #     avgrep.append(
        #     rep1.loc[x,'protein'] + "_tp" + value[1]
        #     + ":" + str((rep1.loc[x,value] + rep2.loc[x,value]
        #     + rep3.loc[x,value]) / 3)
        #     )


#print avgrep
print "avgrep len " + str(len(avgrep))
print "rep1 len " + str(len(ribo1))
print "rep2 len " + str(len(ribo2))
print "rep3 len " + str(len(ribo3))
#print rep1.shap
print len(ribodata1)
print len(ribodata2)
print len(ribodata3)

# np.savetxt('riborep1.out', ribodata1)
# np.savetxt('riborep2.out', ribodata2)
# np.savetxt('riborep3.out', ribodata3)

#print ribodata1
#print ribodata2
#print ribodata3

riborep1file = open('riborep1.txt', 'w')
for item in ribodata1:
    riborep1file.write("%s\n" % item)

riborep2file = open('riborep2.txt', 'w')
for item in ribodata2:
    riborep2file.write("%s\n" % item)

riborep3file = open('riborep3.txt', 'w')
for item in ribodata3:
    riborep3file.write("%s\n" % item)
