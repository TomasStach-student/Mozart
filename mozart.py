import wave
import random
from uloha2 import menuet, trio
from pathlib import Path

def menet():
    menuet1=[]
    for takt in range(0,16):
        menet_riadok = random.randint(1,10) #dve kocky
        cislo_takt_menuet=menuet[menet_riadok][takt]
        menuet1.append(cislo_takt_menuet)
    print("menuet:", menuet1)

def tro():
    trio1=[]
    for takt in range(0, 16):
        trio_riadok=random.randint(1,5) #jedna koncka
        cislo_takt_trio=trio[trio_riadok][takt]
        trio1.append(cislo_takt_trio)
    print("trio:",trio1)

    