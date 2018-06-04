import random
import os

class Celebrity(object):
    def __intit__(self,voxid,name,gender,nationality,dataset):
        self.voxid = voxid
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.dataset = dataset

infile = open("vox1_meta.csv",'r')
rawdat = infile.readlines()
infile.close()

for i in rawdat:
    entry = i.split()

file_path1 = ''
file_path2 = ''
file_path3 = ''
file_path4 = ''
file_path_test = ''

#lists id folders
x = os.listdir("Audio")
for i in x:
    voxid = str(i[5:])
    #lists id subfolders
    y = os.listdir("Audio\\" + i)
    for ii in y:
        #lists wav files
        z = os.listdir("Audio\\" + i + "\\" + ii)
        for iii in z:
            splitting = random.random()
            if splitting<1/5:
                file_path1 += voxid + " " + "\\".join((i,ii,iii)) + "\n"
            elif splitting>1/5 and splitting<2/5:
                file_path2 += voxid + " " + "\\".join((i,ii,iii)) + "\n"
            elif splitting>2/5 and splitting<3/5:
                file_path3 += voxid + " " + "\\".join((i,ii,iii)) + "\n"                
            elif splitting>3/5 and splitting<3/5:
                file_path4 += voxid + " " + "\\".join((i,ii,iii)) + "\n"
            elif splitting>4/5:
                file_path_test += voxid + " " + "\\".join((i,ii,iii)) + "\n"

wfile1 = open("file_path1.txt",'w')
wfile1.write(file_path1)
wfile1.close()

wfile2 = open("file_path2.txt",'w')
wfile2.write(file_path2)
wfile2.close()

wfile3 = open("file_path3.txt",'w')
wfile3.write(file_path3)
wfile3.close()

wfile4 = open("file_path4.txt",'w')
wfile4.write(file_path4)
wfile4.close()

wfile5 = open("file_path_test.txt",'w')
wfile5.write(file_path_test)
wfile5.close()
