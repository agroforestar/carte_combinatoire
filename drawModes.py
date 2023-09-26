DRAW_TXT = 0x0001
DRAW_DART = 0x0010
DRAW_FACE = 0x0100

def checkDrawMode (val, mode):
    if val&mode == mode:
        return True
    else:
        return False
