from datetime import datetime
import glob2
tym = datetime.now()
tymstr = tym.strftime("%Y_%m_%d_%H_%M_%S")
with open("%s.txt" %tymstr , "a+") as writefile :
    for name in glob2.glob("file?.txt"):
        with open(name, "r") as readfile :
            content = readfile.read()
            writefile.write(content+"\n")
