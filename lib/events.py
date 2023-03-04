from lib.core import *

class EventEmitter:
  def __init__(self):
    self.listeners = {}

  def on(self, event_name, func):
    if event_name not in self.listeners:
      self.listeners[event_name] = []
      
    self.listeners[event_name].append({
      'func': func,
      'once': False
    })

  def once(self, event_name, func):
    if event_name not in self.listeners:
      self.listeners[event_name] = []

    self.listeners[event_name].append({
      'func': func,
      'once': True
    })

  def emit(self, event_name, *args, **kwargs):
    if event_name not in self.listeners:
      return false
      
    for listener in self.listeners[event_name]:
      if listener['once']:
        listener['func'](*args, **kwargs)
        del self.listeners[event_name][self.listeners[event_name].index(listener)]
      else:
        listener['func'](*args, **kwargs)
        
    return true

  def event(self, event_name, once=False):
    def my_decor(func):
      if once:
        self.once(event_name, func)
      else:
        self.on(event_name, func)
      return func
    return my_decor

def on(emitter, event_name, func):
  EventEmitter.on(emitter, event_name, func)

def once(emitter, event_name, func):
  EventEmitter.once(emitter, event_name, func)

def emit(emitter, event_name, *args, **kwargs):
  EventEmitter.emit(emitter, event_name, *args, **kwargs)

def event(emitter, event_name, once=False):
  EventEmitter.event(emitter, event_name, once)