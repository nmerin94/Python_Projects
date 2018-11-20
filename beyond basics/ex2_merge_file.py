from datetime import datetime
tym = datetime.now()
tymstr = tym.strftime("%Y_%m_%d_%H_%M_%S")
with open("%s.txt" %tymstr , "a+") as writefile :
    for i in range(1,4) :
        with open("file%s.txt" %i , "r") as readfile :
            content = readfile.read()
            writefile.write(content+"\n")
