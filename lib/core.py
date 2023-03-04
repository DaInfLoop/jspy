import importlib
import traceback
import lib.internals.debug as debug
from json import loads
class BaseError(BaseException):
  def __init__(self, message):
    self.message = message
    self.name = "BaseError"

  @property
  def throwableVer(self):
    return BaseException(f"[{self.name}]: {self.message}")

  @property
  def msg(self):
    return self.message

  @msg.setter
  def msg(self, newMessage):
    self.message = newMessage

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

def createObject(dict={}, environLike=False):
  if environLike:
    obj = __createEnvironLikeObject__(dict)
  else:
    obj = Object(dict)

  return obj
      
import os
import sys

def __createEnvironLikeObject__(data={}):
    if os.name == 'nt':
        def check_str(value):
            if not isinstance(value, str):
                raise TypeError("str expected, not %s" % type(value).__name__)
            return value
        encode = check_str
        decode = str
        def encodekey(key):
            return encode(key).upper()
    else:
        encoding = sys.getfilesystemencoding()
        def encode(value):
            if not isinstance(value, str):
                raise TypeError("str expected, not %s" % type(value).__name__)
            return value.encode(encoding, 'surrogateescape')
        def decode(value):
            return value.decode(encoding, 'surrogateescape')
        encodekey = encode
    return os._Environ(data,
        encodekey, decode,
        encode, decode, None, None)

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
    os.system("")

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