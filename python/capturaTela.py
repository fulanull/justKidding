#File with 2 function to take an screenshot in linux


import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

from Xlib import display, X
from PIL import Image
#PIL



#Try to integrate with PIL to return an PIL Image
def screenShot1():
    # full screenshot
    window = Gdk.get_default_root_window()
    pb = Gdk.pixbuf_get_from_window(window, *window.get_geometry())
    pb.savev("full.png", "png", (), ())

    # # screenshots for all windows
    # window = Gdk.get_default_root_window()
    # screen = window.get_screen()
    # typ = window.get_type_hint()
    # for i, w in enumerate(screen.get_window_stack()):
    #     pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
    #     pb.savev("{}.png".format(i), "png", (), ())

    # # screenshot active window
    # screen = Gdk.get_default_root_window().get_screen()
    # w = screen.get_active_window()
    # pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
    # pb.savev("active.png", "png", (), ())


#Works with PIL, but too slow
def screenShot2():
    dsp = display.Display()
    root = dsp.screen().root
    w = root.get_geometry().width
    h = root.get_geometry().height
    print(dsp.get_display_name(), w, h)
    raw = root.get_image(0, 0, w, h, X.ZPixmap, 0xffffffff)
    image = Image.frombytes("RGB", (w, h), raw.data, "raw", "BGRX")
    # image.show()
    # image.save("teste.png")
    return image

def performanceTest():
    import time
    counter=10
    while counter:
        print(time.perf_counter(), counter)
        screenShot2()
        counter -=1



# screenShot2()
performanceTest()
