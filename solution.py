import pandas as pd
import numpy as np
import math
df=pd.read_csv("A1.csv",sep=",",encoding='CP949')

df=df.as_matrix()
y=len(df)


for i in range(y):
    if np.isnan(df[i,12]):
        df[i,12]=2000



aa1=np.std(df[:,6])
bb1=np.std(df[:,7])
cc1=np.std(df[:,9])
dd1=np.std(df[:,10])



#로그로 구할때 함수
def g(i,x1,x2,x3,x4):
    return (((math.log(x1)-math.log(df[i,6])))**2+((math.log(x2)-math.log(df[i,7])))**2+((math.log(x3)-math.log(df[i,9])))**2+((x4-df[i,10])/dd1)**2)**0.5

#정규화한 거리로 구하는 함수
def g(i,a1,a2,a3,a4,x1,x2,x3,x4):
    return (a1*((x1-df[i,6])/aa1)**2+a2*((x2-df[i,7])/bb1)**2+a3*((x3-df[i,9])/cc1)**2+a4*((x4-df[i,10])/dd1)**2)**0.5


#절대값으로 구한 함수
def g(i,x1,x2,x3,x4):
    return abs((x1-df[i,6])/aa1)+abs((x2-df[i,7])/bb1)+abs((x3-df[i,9])/cc1)+abs((x4-df[i,10])/dd1)




c=np.arange(y)
c=c.astype(float)

for i in range(y):
    c[i]=g(i,64.0,200.0,10000,2010)
    
cc=c.reshape(y,1)
df1=np.hstack((df,cc))




test1=pd.DataFrame(df1)
test1_1=test1.sort_values(by=13, axis=0, ascending=True, kind='quicksort', na_position='last')
test1_1.columns = ["도", "시군구", "읍면동","번지","주거유형","도로조건","대지면적","연면적","거래년월","거래가격","건축년도","도로명","그거","유사도"]



print("조건\n","대지면적:",64.0,",연면적:",200.0,",거래가격:",10000,",건축년도:",2010)
test1_1.head()