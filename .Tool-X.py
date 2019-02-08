# Tool Name :- Tool Kit
# Author :- labib azad
# Date :- 9/02/2019
# Powered By :- Aex Software's

import sys
import os
from modules.logo import exit
from modules.menu import ToolX

class chk(object):
  def chos(self):
    if "linux" in sys.platform:
      # Running Tool-X on linux ....
      pass
    elif "darwin" in sys.platform:
      pass
      # print("Sorry, its not available for mac right now...")
      ex()
    elif "win" in sys.platform:
      print("Sorry, its not available for windows right now...")
      ex()
    else:
      print("If Tool-X not support for \'%s\' right now !!!" %sys.platform)

def Tool_X():
  try:
	chk().chos()
	ToolX()

  except KeyboardInterrupt:
	exit()
Tool_X()
