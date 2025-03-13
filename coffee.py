import ctypes
import time
import argparse
from colorama import init, Fore

init(autoreset=True)

GRN = Fore.LIGHTGREEN_EX
RST = Fore.RESET

coffee_cup = f"""
     s  s  s
      s  s  s
     s  s  s
   ############
   #----------#***
   #          #  *
    #        #**
      ######
====================
   coffee: {GRN}active{RST}
"""

parser = argparse.ArgumentParser(prog="coffee", description="Coffee", epilog="(c)2025 Ivaylo Vasilev")
parser.add_argument("--version", action="version", version="%(prog)s 2025.1", help="show program version")
args = parser.parse_args()


def coffee():
    print(coffee_cup)
    while True:
        try:
            ctypes.windll.kernel32.SetThreadExecutionState(0x00000001)
            ctypes.windll.kernel32.SetThreadExecutionState(0x00000002)
            time.sleep(60)
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    coffee()
