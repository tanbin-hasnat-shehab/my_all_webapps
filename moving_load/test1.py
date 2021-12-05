
from anastruct import SystemElements
import math
import matplotlib.pyplot as plt 
import numpy as np
import plotly.express as px

load=[10,20,30,40,50,60,70,80,90,100]
#inter distances
trial_distances=[0,1,2,3,2,2,3,2,3,4]


dist=[]
m_a=0
for i in range(len(trial_distances)):
	
	if i ==0:
		dist.append(trial_distances[i])
	else:
		m_a=m_a+trial_distances[i-1]
		dist.append(-1*(m_a+trial_distances[i]))

print(f'absolute dist array is {dist}')


my_d=[]
my_d=[]
for i in range(-10*dist[-1]):
        
	dx=[]
	for j in range(len(dist)):
		dx.append(dist[j]+0.5*i)
	my_d.append(dx)

  




class mBeams():
	def __init__(self,length,x1,x2,load_list,dist_list):
		self.length=length
		self.x1=x1
		self.x2=x2
		self.load_list=load_list
		self.dist_list=dist_list

l1=mBeams(5, 0, 5,[],[])
l2=mBeams(6, 5, 11,[],[])
l3=mBeams(7, 11, 18,[],[])

beams=[]
beams.append(l1)
beams.append(l2)
beams.append(l3)
total_length=l1.length+l2.length+l3.length

start=beams[0].x1
arr=[]

for i in range(len(beams)):
	lower=beams[i].x1
	higher=beams[i].x2
	for j in range(len(my_d)):
		tr_val=[]
		tr_val2=[]
		for k in range(len(dist)):
			if my_d[j][k]>=lower and my_d[j][k]<=higher:
				tr_val.append(load[my_d[j].index(my_d[j][k])])
				tr_val2.append(my_d[j][k])
		
		beams[i].load_list.append(tr_val)
		beams[i].dist_list.append(tr_val2)

ss=SystemElements()

print(f'beam 1 load list is {beams[0].load_list} \n\nand dist list is {beams[0].dist_list}')
print(f'beam 1 load list is {beams[1].load_list} \n\nand dist list is {beams[1].dist_list}')
print(f'beam 1 load list is {beams[2].load_list} \n\nand dist list is {beams[2].dist_list}')




