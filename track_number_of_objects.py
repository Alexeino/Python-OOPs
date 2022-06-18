# A Program to keep track of objects created of a class...
import  gc
class Track:
    count = 0
    def __init__(self):
        Track.count = Track.count+1
        print(id(Track.count))

    
    @classmethod
    def  garbage(cls):
        if cls.count == 0:
            del(cls.count)
            gc.collect()
            try:
                print(cls.count)
            except AttributeError as e:
                print(e)
        else:
            print("{} nos. of objects present ...".format(cls.count))

    def add(x,y):
        print(x+y)
    

t1 = Track()
t2 = Track()
print("Number of objects created :",Track.count)
#t3 = Track()
print("Number of objects created :",Track.count)

Track.garbage()

