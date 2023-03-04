# jspy
The definition of: I got bored so I decided to make Javascript in Python.

## Usage:
1) First install the library   
2) Import it within your code:
```py
from lib import *
# All set!
```

Note that jspy is not complete yet, so contributions on the [GitHub repo](https://github.com/DaInfLoop/jspy) are welcome!

## Documentation

<details>
  <summary>Core</summary>
### class Object
Class you can use to create an object. This is not the recommended way to create an object, and you should use `createObject()` instead.

### lib#createObject
Create an object from a dictionary.

Usage:
```py
myObj = createObject({"hello": "world"})
```

### lib#require
Import a module/JSON file.

Usage:
```py
# Imagine I have a file in the same directory called "coolFile.py"

coolFile = require('coolFile')
```

### class Console
The console class. This does nothing special being called manually, so just use the `console` variable.

### true/false/null
Self-explanatory. `true == True`, `false == False`, `null == None`.
</details>

<details>
  <summary>JSON</summary>
Already pre-imported, but you can run <code>require('jspy:json')</code> to re-import.

### JSON#parse -> lib.core.Object
Parse a JSON object and make it into an Object.

Usage:
```py
parsed = JSON.parse('{"hello":"world"}')

console.log(parsed) # {"hello": "world"}
```

### JSON#stringify -> str
Stringify a dict. You can specify how many spaces you want for the indent.

Usage:
```py
myDict = {"hello": "world"}

console.log(JSON.stringify(myDict, null, 2))
"""
{
  "hello": "world"
}
"""
```
</details>

<details>
  <summary>Events</summary>
Import via <code>require('jspy:events')</code>.

### class EventEmitter
Create an EventEmitter.

Usage:
```py
emitter = EventEmitter()
```

### EventEmitter#on -> null
Register an event.

Usage:
```py
emitter.on('event', handler)
```

### EventEmitter#once -> null
Register an event that will delete itself when emitted.

Usage:
```py
emitter.once('event', handler)

# After `handler` is run, the event will no longer run `handler`.
```

### @EventEmitter#event -> Callable
A decorator that you can add to a function to register it as an event.

Usage:
```py
# emitter.on
@emitter.event('event')
def onHandler(args):
  console.log(args)

# emitter.once
@emitter.event('event', once=True)
def onceHandler(args):
  console.log(args)
```

### EventEmitter#emit -> bool
Emit an event. Runs all event handlers. Returns `True` if an event handler was found, or `False` if one wasn't found.

Usage:
```py
@emitter.event('event')
def onHandler(args):
  console.log(args)

emitter.emit('event', "hello!") # prints "hello!"
```
</details>