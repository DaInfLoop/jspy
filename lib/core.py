import importlib
import traceback
import lib.internals.debug as debug
from json import loads

def throw_error(err, traceback = None):
  print(f'\033[31;1;4m{err}')
  if traceback:
    traceback = traceback.split('\n')
    traceback.pop()
    print("\n".join(traceback))
  print('\033[0m')
  return exit(1)

class Object(object):
    def __init__(self, dict):
      self.__dict__ = dict

      for key, value in dict.items():
        setattr(self, key, value)
  
    def __str__(self):
      return str(self.__dict__)

def createObject(dict={}):
  obj = Object(dict)

  return obj
      
import os
import sys

__requireCache__ = {}

def require(file): 
  defaultPkgs = {
    "jspy:fs": "lib.fs",
    "jspy:events": "lib.events",
    "jspy:json": "lib.json", # Built-in import
    "jspy:path": "lib.path",
		"jspy:process": "lib.process", # Built-in import
    "jspy:debug": "lib.debug"
  }
  returnVal = None

  if __requireCache__.get(defaultPkgs.get(file, file), False):
    return __requireCache__.get(defaultPkgs.get(file, file))
  
  try:
    returnVal = importlib.import_module(defaultPkgs.get(file, file))
    if 'exports' in dir(returnVal):
      returnVal = returnVal.exports

  except BaseException as err:
    try:
      if not file.endswith('.json'):
        raise err
      with open(file, 'r') as r:
        returnVal = loads(r.read())
    except BaseException as err2:
      return throw_error(f"[{debug.get_full_class_name(err2)}]: {err2}")

  __requireCache__[defaultPkgs.get(file, file)] = returnVal
  return returnVal
class Console:
  log = print

  def clear():
    os.system("clear" if os.name == "nt" else "cls")

@property
def true():
  return True

@property
def false():
  return False

null = None

@true.setter
def true():
  raise SyntaxError('cannot assign to true')

@false.setter
def false():
  raise SyntaxError('cannot assign to false')

                             
console = Console()