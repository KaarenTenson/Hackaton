import subprocess
import os
def splitaeg(aeg):
    aeg=str(aeg)
    aeg=aeg.strip("\n").strip('')
    list1=aeg.split(":")
    for el in list1:
        if el[0]=="0":
            el=el[1]
    print(list1)
    return int(list1[0])*3600+int(list1[1])*60+int(list1[2])
def timer(aeg, protsess, heahalb, eelmine=0):
    algustime=subprocess.run(['ps', '-C', protsess, "-o", "etime="], capture_output=True, text=True)
    runtime=splitaeg(algustime.stdout)
    print(runtime)
    if heahalb=="hea":
        return(aeg+(runtime-eelmine), runtime)
    if heahalb =="halb":
        return(aeg-(runtime-eelmine), runtime)

