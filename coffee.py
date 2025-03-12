import ctypes
import time
import datetime
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
parser.add_argument("-t", "--time", action="store_true", help="show elapsed time")
parser.add_argument("--version", action="version", version="%(prog)s 2025.2-beta1", help="show program version")
args = parser.parse_args()


def coffee():
    print(coffee_cup)
    start_time = datetime.datetime.now()
    while True:
        try:
            ctypes.windll.kernel32.SetThreadExecutionState(0x00000001)
            ctypes.windll.kernel32.SetThreadExecutionState(0x00000002)
            time.sleep(60)
        except KeyboardInterrupt:
            break
    end_time = datetime.datetime.now()

    if args.time:
        elapsed_time = (end_time - start_time)
        elapsed_time = str(elapsed_time).split(".")[0]
        h, m, s = elapsed_time.split(":")
        print(f"elapsed time: {h}h {m}min {s}sec")


if __name__ == "__main__":
    coffee()
