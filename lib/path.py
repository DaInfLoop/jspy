from lib import *
import re

__os = os.name

@property
def delimiter():
  return ";" if __os == 'nt' else ":"

@property
def sep():
  return "\\"+"\\" if __os == 'nt' else "/"

def basename(path, ext=None):
  path = path.split(sep)[-1]

  if (ext and path.endswith(ext)):
    path = path[:-len(ext)] 

  return path

def dirname(path):
  return path.split(sep)[-2]

def extname(path):
  last = basename(path)

  last = last.split('.')

  if len(last) == 1:
    return ""

  last = "."+last[-1]

  return last

def format(pathObject):
  if __os == 'nt':
    dir = pathObject.get("dir", None)
    base = pathObject.get("base", "")

    if dir == None:
      return base

    if dir[-1] == sep:
      return dir+base

    return dir+sep+base
  else:
    dir = pathObject.get("dir", '') + sep if pathObject.get("dir", '') else ""

    base = pathObject.get("base", '')
  
    return dir + base

def isAbsolute(path):
  if __os == 'nt':
    splitDeviceRe = r"^([a-zA-Z]:|[\\\/]{2}[^\\\/]+[\\\/]+[^\\\/]+)?([\\\/])?([\s\S]*?)$"

    matches = re.match(splitDeviceRe, path)

    if matches:
      m = matches.group(1) or ""
      return ((not not m) and (m != "") or not not matches.group(2))
      
  else:
    return path[0] == "/";

def join(*args):
  if __os == 'nt':
    paths = []
    for path in args:
      if debug.get_full_class_name(path) == "str":
        paths.append(path)
      else:
        raise TypeError("Arguments to path.join must be strings")


    
    joined = "\\".join(paths)

    return joined
  else:
    path = ""
    for seg in args:
      if debug.get_full_class_name(seg) == "str":
        if seg:
          if not path:
            path = seg
          else:
            path = f"{path}/{seg}"


    return path