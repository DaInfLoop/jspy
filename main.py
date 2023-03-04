from lib import *
from lib import __dirname # Python sucks, so you have to import the "__dirname" manually

fs = require("jspy:fs");
events = require("jspy:events");
path = require("jspy:path");

def urmom(func): return lambda *args, **kwargs: (print("start"),func(*args,**kwargs),print("end"))

@urmom
def a(text):
  print("a", text)

a("hello!")