import os
import platform
import time

class USERPLATFORMCONNECT(object):
    def __init__(self) -> None:
        os.system("cls")
        try:
            if "3.10.6" in platform.python_version():
                try:
                    if "64" in platform.machine() and "32" not in platform.machine():
                        print("This device is 64bit")
                        time.sleep(3)
                    elif "32" in platform.machine() and "64" not in platform.machine():
                        print("This is 32bit device")
                        time.sleep(3)
                except(ValueError,KeyError):
                    print(" invalid platform device or not supported ")
                    pass
                pass
        except(platform.errno,KeyError,AttributeError):
            print()
            print("Your python is tool old version")
            pass
        pass
USERPLATFORMCONNECT()
