import os
from lib.core import createObject
import lib.internals.debug
import lib.internals.errors
import typing

class ERR_INVALID_ARG_TYPE(lib.internals.errors.Error):
  def __init__(self, name, expected, actual):
    self.message = f"The \"{name}\" argument must be of type {expected}. Received type {lib.internals.debug.get_full_class_name(actual)}"
    self.name = "ERR_INVALID_ARG_TYPE"


CONSTANTS = createObject({
  "UV_FS_SYMLINK_DIR": 1,
  "UV_FS_SYMLINK_JUNCTION": 2,
  "O_RDONLY": 0,
  "O_WRONLY": 1,
  "O_RDWR": 2,
  "UV_DIRENT_UNKNOWN": 0,
  "UV_DIRENT_FILE": 1,
  "UV_DIRENT_DIR": 2,
  "UV_DIRENT_LINK": 3,
  "UV_DIRENT_FIFO": 4,
  "UV_DIRENT_SOCKET": 5,
  "UV_DIRENT_CHAR": 6,
  "UV_DIRENT_BLOCK": 7,
  "S_IFMT": 61440,
  "S_IFREG": 32768,
  "S_IFDIR": 16384,
  "S_IFCHR": 8192,
  "S_IFBLK": 24576,
  "S_IFIFO": 4096,
  "S_IFLNK": 40960,
  "S_IFSOCK": 49152,
  "O_CREAT": 64,
  "O_EXCL": 128,
  "UV_FS_O_FILEMAP": 0,
  "O_NOCTTY": 256,
  "O_TRUNC": 512,
  "O_APPEND": 1024,
  "O_DIRECTORY": 65536,
  "O_NOATIME": 262144,
  "O_NOFOLLOW": 131072,
  "O_SYNC": 1052672,
  "O_DSYNC": 4096,
  "O_DIRECT": 16384,
  "O_NONBLOCK": 2048,
  "S_IRWXU": 448,
  "S_IRUSR": 256,
  "S_IWUSR": 128,
  "S_IXUSR": 64,
  "S_IRWXG": 56,
  "S_IRGRP": 32,
  "S_IWGRP": 16,
  "S_IXGRP": 8,
  "S_IRWXO": 7,
  "S_IROTH": 4,
  "S_IWOTH": 2,
  "S_IXOTH": 1,
  "F_OK": 0,
  "R_OK": 4,
  "W_OK": 2,
  "X_OK": 1,
  "UV_FS_COPYFILE_EXCL": 1,
  "COPYFILE_EXCL": 1,
  "UV_FS_COPYFILE_FICLONE": 2,
  "COPYFILE_FICLONE": 2,
  "UV_FS_COPYFILE_FICLONE_FORCE": 4,
  "COPYFILE_FICLONE_FORCE": 4
})

"""
const getValidMode = hideStackFrames((mode, type) => {
  let min = kMinimumAccessMode;
  let max = kMaximumAccessMode;
  let def = F_OK;
  if (type === 'copyFile') {
    min = kMinimumCopyMode;
    max = kMaximumCopyMode;
    def = mode || kDefaultCopyMode;
  } else {
    assert(type === 'access');
  }
  if (mode == null) {
    return def;
  }
  validateInteger(mode, 'mode', min, max);
  return mode;
});
"""

"""
const validateInteger = hideStackFrames(
  (value, name, min = NumberMIN_SAFE_INTEGER, max = NumberMAX_SAFE_INTEGER) => {
    if (typeof value !== 'number')
      throw new ERR_INVALID_ARG_TYPE(name, 'number', value);
    if (!NumberIsInteger(value))
      throw new ERR_OUT_OF_RANGE(name, 'an integer', value);
    if (value < min || value > max)
      throw new ERR_OUT_OF_RANGE(name, `>= ${min} && <= ${max}`, value);
  },
);
"""

def validateInteger(value, name, minimum, maximum):
  if lib.internals.debug.get_full_class_name(value) != "int":
    raise ERR_INVALID_ARG_TYPE(name, "int", value)
  
  if value < minimum or value > maximum:
    pass

def getValidMode(mode: int, type: str) -> int:
  minMode = min(CONSTANTS.F_OK, CONSTANTS.W_OK, CONSTANTS.R_OK, CONSTANTS.X_OK)
  maxMode = CONSTANTS.F_OK | CONSTANTS.W_OK | CONSTANTS.R_OK | CONSTANTS.X_OK
  default = CONSTANTS.F_OK

  if type == 'copyFile':
    minMode = 0
    maxMode = 0
    default = mode or 0
  else:
    if type != 'access':
      raise Error("The expression evaluated to a falsy value.")

  if mode == None:
    return default

  validateInteger(mode, 'mode', minMode, maxMode)
  return mode

"""
Tests a user's permissions for the file or directory
"""
def access(path: str, mode: int, callback: typing.Callable) -> None:
  if lib.internals.debug.get_full_class_name(mode) != "int":
    callback = mode
    mode = CONSTANTS.F_OK


raise ERR_INVALID_ARG_TYPE("testVar", "int", 92.4).throwableVer

exports = createObject({
  "CONSTANTS": CONSTANTS,
  
  "access": access
})