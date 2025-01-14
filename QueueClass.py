# Your code and heading goes here
class ArrayQueue:
  def __init__(self):
    self.__capacity = 5
    self.__queue = [None for i in range(self.__capacity)]
    self.__size = 0
    self.__front = 0

  def enqueue(self,new):
    """Adds a new element to the queue"""
    if self.__size == self.__capacity:
      self.__resize(self.__queue)
    index = (self.__front + self.__size) % self.__capacity
    self.__queue[index] = new
    self.__size += 1
    
  def __resize(self,queue):
    """Doubles the capacity and reorganizes the data"""
    newqueue = [None for i in range(self.__capacity * 2)]
    for i in range(self.__capacity):
     
      index = (self.__front + i) % self.__capacity
      newqueue[i] = self.__queue[index]
    self.__queue = newqueue  
    self.__capacity += self.__capacity
    self.__front = 0

  def dequeue(self):
    """Removes and returns the first element"""
    empty = self.__is_empty()
    if empty == True:
      raise IndexError("List is empty")
    value = self.__queue[self.__front]
    self.__queue[self.__front] = None
    self.__size -= 1
    self.__front = (self.__front + 1) % self.__capacity
    return value
    
  #remove and return the first index
  #sets front to the next element in the queue 
  #lowers size
  # 
  def first(self):
    """Returns the first element in the queue"""
    empty = self.__is_empty()
    if empty == True:
      raise IndexError("List is empty")
    else:
      return self.__queue[self.__front]

  def __is_empty(self):
    """Checks if the queue is empty"""
    if self.__size == 0:

      return True
    else:
      return False 
  def __len__(self):
    """Returns the size of the queue"""
    return self.__size  

  def __str__(self):
      """Converts queue into printable string"""
      out = "FRONT> "
      pointer = self.__front
      for i in range(self.__size):
        out += str(self.__queue[pointer]) + " "
        pointer = (pointer + 1) % self.__capacity

      return out + "<BACK"