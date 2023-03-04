from lib.core import *
import json

def parse(dict):
  return createObject(json.loads(dict))

def stringify(dict, _, spaces):
  return json.dumps(dict, indent=spaces)