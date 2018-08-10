import inspect
from pprint import pprint

def dump(obj):
  v = ""
  for attr in dir(obj):
    v = ("%s, obj.%s = %r" % (v, attr, getattr(obj, attr)))
  return v

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
def main():
	x = MyClass()
	#variables = x.__dict__.keys()
 	variables =  dir(x)
        print "hello %s" % (variables,)
	pprint(variables)
	print dump(x)
  
if __name__== "__main__":
  main()
