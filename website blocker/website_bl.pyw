import time # to help sleep for while
from datetime import datetime as dt

# hosts to be blocked
host_path = r"C:\Windows\System32\drivers\etc\hosts"
host_temp = "hosts"
redirect = "127.0.0.0"
website_list = ["www.facebook.com","facebook.com"]


# blocker
while True :


    # if time between 8am and 4pm

    if(dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() <  dt(dt.now().year, dt.now().month, dt.now().day, 17)):
        print("Working Hours..")

        # reading the content of hostfile into content
        with open(host_path, "r+") as file:
            content = file.read()

            # reading each website in the website list
            for website in website_list:
                if(website in  content) :
                    pass
                else :
                    file.write("\n"+redirect +" "+ website)



    # if the websites are present in the hosts file
    else:
        print("Not working hours")

        # Opening the file initially as append mode in with clause
        with open(host_path , "r+") as file:

            # reading content as a whole for initial check
            content = file.read()

            # moving file pointer to the top again to read as lines
            file.seek(0)
            content_line = file.readlines()

            # check if any website from our list is present in content
            if any(website in content for website in website_list):

                # if present move to position 0
                file.seek(0)

                # Copy each line to the file (this may overwrite)
                for line in content_line:


                    # ignoring the lines containing our website
                    if not any(website in line for website in website_list):
                        file.write(line)

                # Removing the remaining lines
                file.truncate()
    time.sleep(20)
