class Error(BaseException):
  def __init__(self, message):
    self.message = message
    self.name = self.__class__.__name__

  @property
  def throwableVer(self):
    return Exception(f"[{self.name}]: {self.message}")

  @property
  def msg(self):
    return self.message

  @msg.setter
  def msg(self, newMessage):
    self.message = newMessage

class RangeError(Error):
  pass

class ReferenceError(Error):
  pass

class SyntaxError(Error):
  pass

class TypeError(Error):
  pass

class URIError(Error):
  pass