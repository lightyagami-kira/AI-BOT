import numpy as np
import os
path = "/home/sai/Desktop/Project/new_left"
print path
filenames = os.listdir(path)
i=1
k1 = "rename_left.py"
k2 = "rename_left.pyc"
for f in filenames:
	if f!=k1 and f!=k2:
		a = "left"+str(i)+".wav"
		os.rename(f,a)
		i = i+1
		print a
	#a = "back"+str(i)+".wav"
	#os.rename(f,a)
	#i = i+1
	#print a
			

