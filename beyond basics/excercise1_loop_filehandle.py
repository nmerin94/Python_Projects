temperatures = [10, -20, -289, 100]
x=None
def c_to_f(c):
    if c < -273.15:
        return None
    else:
        f = c* 9/5 + 32
        return f
for t in temperatures:
    with open("ex1.txt","a+") as myfile:
        x = c_to_f(t)
        if (x):
            myfile.write(str(x)+"\n")
