from enum import unique

import numpy as np

arr=np.array([1,2,3,4])
print(arr)

arr1=np.arange(0,8,2)                                       # Function1 .arange()
print("\n",arr1)                                            # Print the objects in array with declared range followed by the symmetric difference between the objects

arr2=np.random.rand(2,3)                                    # Function2 .random.rand()
print("\n",arr2)                                            # Print random objects based on given no. of rows and columns

arr3=np.array([[2,3],[3,5],[6,7]])                          # Declared an array in a row and column form
print("\n",arr3.shape)                                      # Function3 .shape

arr4=np.array([10,20,30,40])                                # Direct indexing
print("\n",arr4)

arr5=np.array([3,1,2])
print("\n",np.sum(arr5))                                    # Function4 np.sum()

arr6=np.array([1,2,2,3,4,4,5])
print("\n",np.unique(arr6))                                 # Function5 np.unique()

arr7=np.array([12,5,0,3])
print("\n",np.sort(arr7))                                   # Function6 np.sort()

arr8=np.array([1,4,9,12])
print("\n",np.sqrt(arr8))                                   #Function7 np.sqrt()

print("\n",arr7 + arr4)                                     # Direct implementing operations on elements like array
print("\n",arr * arr4)                                      # **This works on arrays with same structure only**