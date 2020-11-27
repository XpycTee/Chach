import ctypes

from ctypes import wintypes

FLASHW_STOP = 0
FLASHW_CAPTION = 0x00000001
FLASHW_TRAY = 0x00000002
FLASHW_ALL = 0x00000003
FLASHW_TIMER = 0x00000004
FLASHW_TIMERNOFG = 0x0000000C


class FLASHWINFO(ctypes.Structure):
    _fields_ = (('cbSize', wintypes.UINT),
                ('hwnd', wintypes.HWND),
                ('dwFlags', wintypes.DWORD),
                ('uCount', wintypes.UINT),
                ('dwTimeout', wintypes.DWORD))


    def __init__(self, hwnd, flags=FLASHW_TRAY, count=5, timeout_ms=0):
        self.cbSize = ctypes.sizeof(self)
        self.hwnd = hwnd
        self.dwFlags = flags
        self.uCount = count
        self.dwTimeout = timeout_ms