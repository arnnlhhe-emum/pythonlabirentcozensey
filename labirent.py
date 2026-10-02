import time
import os

harita = [
    [1,1,1,1,1,1,1],
    [1,"R",0,0,1,0,1],
    [1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,"E",1],
    [1,1,1,1,1,1,1],
]
def haritayıgöster():
    os.system('cls')
    for satır in harita:
        print(" ".join(str(eleman)for eleman in satır))
    print("-"*15)

haritayıgöster()
robotsatır=1
robotsütun=1

while True:
    if harita[robotsatır][robotsütun] == "E":
        print("robot çıkışa ulaştı")
        break

    harita[robotsatır][robotsütun] = "R"
    haritayıgöster()
    time.sleep(0.4)

    harita[robotsatır][robotsütun] = "."

    if harita[robotsatır][robotsütun + 1] in (0, "E"):
        robotsütun += 1
    elif harita[robotsatır + 1][robotsütun] in (0, "E"):
        robotsatır += 1
    elif harita[robotsatır][robotsütun - 1] in (0, "E"):
        robotsütun -= 1
    elif harita[robotsatır - 1][robotsütun] in (0, "E"):
        robotsatır -= 1
    else:
        print("gidecek yer yok")
        break