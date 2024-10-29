import numpy as np

array1=np.array([10,22,100])
array2=np.array([[124,-96,114,1],[56,78,0,-36]])

ygnd=np.sum(array1)
kpytma=np.prod(array1)
oqymt=np.mean(array1)

print("Bir o'lchamli massiv elementlari:\n",array1)
print("Ikki o'lchamli massiv elementlari:\n",array2)
print("Bir o'lchamli massiv elementlari yig'indisi:\n",ygnd)
print("Bir o'lchamli massiv elementlari ko'paytmasi:\n",kpytma)
print("Bir o'lchamli massiv elementlari o'rta qiymati:\n",oqymt)