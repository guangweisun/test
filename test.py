import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from random import randint


#传参函数1的书写
def Pass_parameters(*parameter):
    print(parameter)
Pass_parameters(*c)

#生成0-1中每隔0.1的数
c=np.arange(0,1.1,0.1)


#迭代二维数组
file_name_1 = pd.read_excel("F:\PythonSave/Freshman training_5_26/m1.xlsx", header=None)
for x in file_name_1:
    print(0)
    
    

