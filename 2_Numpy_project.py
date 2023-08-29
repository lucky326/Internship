import numpy as np
#1
days=np.array(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
month=np.array(['November','December','January','Februrary'])
data=np.array([8,21,9,22,14,28,10,20,11,23,10,27,12,26,
10,29,11,22,7,29,-13,24,14,31,7,31,13,24,
7,28,10,32,13,30,8,24,9,25,8,32,14,25,
12,29,8,22,12,21,13,31,13,31,11,28,12,22,
13,25,12,28,6,30,13,28,11,22,6,28,15,30,
11,29,8,30,10,25,6,20,9,25,10,29,6,30,
14,27,6,30,14,28,14,32,15,28,9,31,9,25,
8,20,11,25,7,28,6,29,14,21,8,32,15,31,
2,20,5,21,8,21,3,20,7,21,3,4,21,6,
2,20,5,21,3,18,3,22,7,21,6,2,20,4,
6,19,8,19,8,22,2,18,2,22,5,8,18,3,
2,21,4,21,3,20,6,22,3,20,7,3,18,2,
8,18,8,22,-10,22,11,19,11,20,12,71,18,9,
10,22,10,19,9,22,12,19,11,20,7,9,20,12,
12,18,12,20,7,21,9,21,11,18,12,8,20,11,
11,19,12,20,7,20,10,19,12,18,10,7,19,7
]).reshape(4,4,7,2)
#2
print(data.ndim,"\n",data.shape,'\n\n')
#3
print(data[:,0],'\n\n')
#4
print(data[:,:,1],'\n\n')
#5
print(data[[1,3],:,:,1],'\n\n')

#6
inx=data[0]<8
print(data[0,inx],'\n\n')

#7
inx=data[1,2]>20
print(data[1,2][inx],'\n\n')

#8
outlier=np.concatenate((data[data>40],data[data<0]))
print(outlier,'\n\n')

#9

#10
inx_plus=np.where(data>40)
inx_minus=np.where(data<0)
print(inx_plus,inx_minus,'\n\n')

#11
data[inx_plus]-=30
data[inx_minus]+=15

#12
max=data[:,:,:,1]
avg=np.average(max)
print(avg,'\n\n')

#13
min=data[1,:,:,0]
avg=np.average(min)
print(avg,'\n\n')

#14
temp=data[[1,2]]
avg=np.average(temp)
print(avg,'\n\n')

#15
temp=np.min(data[[1,2]])
inx=np.where(data[[1,2]]==temp)
print(temp)
for i in range(0,7):
    print(days[inx[2][i]],' week ',inx[1][i]+1,' ', month[inx[0][i]])
print('\n\n')

#16
temp=np.max(data[3])
inx=np.where(data[3]==temp)
print(temp)
print(days[inx[0]],'week',inx[1]+1, month[inx[2]],'\n\n')

#17
avg=np.average(data[0])
days_max=data[0,:,:,1]<avg
inx=np.where(days_max==True)
print(days[[inx[1]]],'\n\n')

#18
data1=data.reshape(4,56).copy()
print(data1,'\n\n')

#19
data_f=(data1*(9/5))+32
print(data_f,'\n\n')

#20
Dec_sort=np.sort(data_f[1])[::-1]
print(Dec_sort,'\n\n')

#21
t_sort=np.sort(data_f[:,[0,1,2,14,15,16,28,29,30,42,43,44]],axis=0)[::-1]
print(t_sort,'\n\n')

#22
diff_day=np.array([data[:,:,:,1]-data[:,:,:,0]])
print(diff_day,'\n\n')

#23
maxdiff_days=np.zeros((4,4,6))
for i in range(0,6):
    maxdiff_days[:,:,i]=data[:,:,i+1,1]-data[:,:,i,1]
print(maxdiff_days,'\n\n')

#24
mindiff_days=np.zeros((4,4,6))
for i in range(0,6):
    mindiff_days[:,:,i]=data[:,:,i+1,0]-data[:,:,i,0]
print(mindiff_days,'\n\n')

#25
difference=np.concatenate((maxdiff_days,mindiff_days))
print(difference,'\n\n')