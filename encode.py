import os
import platform
import time
from pystyle import Center

class USERPLATFORMCONNECT(object):
    def __init__(self) -> None:
        os.system("cls")
        try:
            if "3.10.6" in platform.python_version():
                try:
                    if "64" in platform.machine() and "32" not in platform.machine():
                        import encode as enc
                        enc.base64encode_decoode()
                    elif "32" in platform.machine() and "64" not in platform.machine():
                        import encodex as enc
                        enc.base64encode_decoode()
                except(ValueError,KeyError):
                    print(Center.XCenter("invalid platform device or not supported "))
                    pass
                pass
        except(platform.errno,KeyError,AttributeError):
            print()
            print(Center.XCenter("Your python is old version, please upgrade first"))
            pass
        pass
USERPLATFORMCONNECT()
