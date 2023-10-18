
# we are creating object only once if next time we will create it will return the same object

class Singloton:
  def __new__(cls):
    if not hasattr(cls,'inst'):
      cls.inst = super().__new__(cls)
    return cls.inst

singleton = Singloton()
new_singleton = Singloton()
 
print(singleton is new_singleton)
#this will give true
