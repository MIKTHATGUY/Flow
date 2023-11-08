import xml.etree.ElementTree as ET

import sys, random, base64, argparse


parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-un','--username', help='changes author name to be put in files it defaults to the one saved in user file', required=False)
parser.add_argument('-s','--single', help='only changes selected file',required=False, default=False)
parser.add_argument('-a','--all', help='changes every file', required=False, action='store_true', default=True)
parser.add_argument('-nn','--noname', help="dosen't change the name of the author", required=False, action='store_true', default=False)
parser.add_argument('-pn','--changepcname', help="dosen't change the name", required=False, default=False)

args = parser.parse_args()




def main(filename):

    global username, n, tag, value, date
    print(f"---------------Started parsing {filename}--------------")
    tree = ET.parse(filename)
    # print(myroot)
    root_node = tree.getroot()
    try:
        usernamef = open("user", "r")
        username = usernamef.read()
        usernamef.close()
    except FileNotFoundError:
        print(f"couldn't find the user file run the program like this : {sys.argv[0]} -n")
        exit(-1)

    def GenerateBase64(data):
        data = data.split(" ")[0] + ";" + f'\"{data.split(" ")[1]} \"'
        if (args.changepcname != False):
            pc = args.changepcname
        else:
            pc = os.environ['COMPUTERNAME']
        ret = username + ";" + pc + ";" + data + ";" + str(random.randint(2600, 2900))
        return base64.b64encode(ret.encode("ascii")).decode("ascii")
    date = "11 11"
    for tag in root_node.findall('attributes/attribute'):
        # Get the value of the heading attribute

        attname = tag.get("name")
        if attname == "authors":
            value = tag.get("value")
            if value != username and args.noname != True:
                tag.set("value", username)
                print("Changing name")
        if attname == "saved":
            value = tag.get("value")
            date = value
            print(date)



    for tag in root_node.findall('attributes/attribute'):
        # Get the value of the heading attribute
        value = tag.get("value")
        strin = GenerateBase64(date)
        attname = tag.get("name")
        if attname == "created":

            tag.set("value", strin)
            print("Changing creation")

        elif attname == "edited":
            tag.set("value", strin)
            print("Changing edit")


    tree.write(filename)
    print(f"--------------Finished parsing {filename}--------------")
    print()


import os

# directory/folder path




if (args.username):
    if (len(str(args.username).split(" ")) > 1):
        nome = args.username
    else:
        nome = input("Name and surname not recognize please input them rignt now with the format: \nName Surname\n")

    try:
        print("Name saved successfully!")
        with open("user", "w+") as my_file:
            nome = nome.split(" ")
            my_file.write(nome[0][0].upper() + nome[0][1].upper() + "." + nome[1].upper())
    except Exception as e:
        pass


if (args.single):
    # removes name
    main(args.single)
    sys.exit(0)

if (args.all):
    dir_path = os.getcwd()

    # list to store files
    res = []

    # Iterate directory
    for file_path in os.listdir(dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file_path)):
            # add filename to list
            try:
                if file_path.split(".")[1] == "fprg":
                    res.append(file_path)
            except:
                pass

    # removes name
    for film in res:
        main(film)

    sys.exit(0)



print("Use -h to see functionalities")