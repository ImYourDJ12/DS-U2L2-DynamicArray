# Devon Taylor
# U2L2
# DS
# 9/24/24

import ctypes

class DynamicArray:
  def __init__(self):
    self.__n = 0 # number of elements in array, default 0
    self.__capacity = 1 # max number of elements, default 1
    self.__A = self.__make_array(self.__capacity)

  def __len__(self):
    return self.__n

  def get_cap(self):
    return self.__capacity

  def __resize(self):
    self.__capacity *= 2
    oldArray = self.__A
    newArray = self.__make_array(self.__capacity)
    for i in range(0, self.__n):
      newArray[i] = oldArray[i]
    self.__A = newArray
    return newArray
      
  def append(self, item):
    if self.__n == self.__capacity:
      self.__resize()
    self.__A[self.__n] = item
    self.__n += 1




  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[k]

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()
