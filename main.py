from lib import *
from lib import __dirname # Python sucks, so you have to import the "__dirname" manually

events = require("jspy:events");
path = require("jspy:path");

# Use this file to test anything.
emitter = events.EventEmitter()