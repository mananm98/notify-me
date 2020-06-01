#!/usr/bin/env python
# coding: utf-8

from IPython.core.magic import register_cell_magic
from IPython.display import Audio, display
import time


@register_cell_magic
def notify_me(line,cell):
    start = time.time()
    try:
       exec(cell)
       end = time.time()
       print("\n\nExecution time --> ",round(end - start,2),"Seconds")
       display(Audio(url='https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay=True))
    except Exception as e:
       print(type(e).__name__, " : ",e)
       end = time.time()
       print("\n\nExecution time --> ", round(end - start,2),"Seconds")
       display(Audio(url='https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay=True))
