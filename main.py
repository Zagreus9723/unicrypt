import json
import base64
import os
import random
import time

filename = ""
def main():
    mode = input("What would you like to do?\n1: Create a new dictionary\n2: Encode a message\n3: Decode a message\n[?]: ")
    if mode == "1":
        if os.path.exists('index.json'):
            ()
        else:
            r = open('index.json', 'w')
            op = {
                "p": {
                },
                "t": {
                }
            }
            json.dump(op, r, indent=4)
            r.close()
        file = input("Input file name for utf-8 characters\nDon't include extension\n[?]: ")
        if os.path.exists(f"{file}.txt"):
            ()
        else:
            open(f"{file}.txt", "w")
        r = open(f"{file}.txt", "a", encoding="utf-8")
        y = 0
        gen = input("Input number of utf-8 characters to gen\nAt least 5k is needed, don't put more than 50k\n[?]: ")
        for i in range(32, 0x110000):
            if y < int(gen):
                try:
                    r.write(chr(i) + "\n")
                    y = y + 1
                except:
                    ()
            else:
                ()
        charz = []
        r.close()
        u = open(f"{file}.txt", "r", encoding="utf-8")
        for char in u.readlines():
            if char not in charz:
                charz.append(char)
            else:
                ()
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=1234567890/+"
        print("Generating encoder values")
        ap = open(f"index.json", "r+", encoding="utf-8")
        a = json.loads(ap.read())
        for char in text:
            for char1 in text:
                t = random.choice(charz)
                charz.remove(t)
                try:
                    t = str(t).replace("\n", "")
                except:
                    ()
                jsonn = {
                    f"{char}{char1}": f"{t}"
                }
                a[f"p"].update(jsonn)
        print("Generating decoder values")
        for x in a['p']:
            jsonn = {
                f"{a['p'][x]}": f"{x}"
            }
            a["t"].update(jsonn)
        ap.seek(0)
        json.dump(a, ap, indent=4)
        ap.close()
        bfile = open("index.json", "r")
        binary_file_data = bfile.read()
        binary_file_data = binary_file_data.encode('utf-8')
        base64_encoded_data = base64.b64encode(binary_file_data)
        s = base64_encoded_data.decode('utf-8')
        uu = open(f"{input('Name of dictionary [?]: ')}.nog", "w")
        uu.write(s)
        uu.close()
        bfile.close()
        os.remove("index.json")
        print("Done!")
        time.sleep(5)
        os.system("cls")
        os.system('clear')
    elif mode == "2":
        message = input("Message to encode [?]: ")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        s = base64_bytes.decode('ascii')
        to = open(f'{input("Name of dictionary [?]: ")}.nog', "r")
        td = to.read()
        b = td.encode('ascii')
        base64_bytes = base64.b64decode(b)
        se = base64_bytes.decode('ascii')
        t = json.loads(se)
        to.close()
        tt = True
        newstr = ''
        while tt == True:
            try:
                y = s[:2]
                try:
                    newstr = newstr + chr(int(t['p'][f'{y}']))
                except:
                    newstr = newstr + t['p'][f'{y}']
                s = s[2:]
            except Exception as E:
                tt = False
        with open("text.txt", "w", encoding="utf-8") as d:
            d.write(newstr)
        print(newstr)
        print("Done!")
        time.sleep(5)
        os.system("cls")
        os.system('clear')
    elif mode == "3":
        s = input("Message to decode [?]: ")
        to = open(f'{input("Name of dictionary [?]: ")}.nog', "r")
        td = to.read()
        b = td.encode('utf-8')
        base64_bytes = base64.b64decode(b)
        se = base64_bytes.decode('ascii')
        t = json.loads(se)
        to.close()
        tt = True
        newstr = ''
        while len(s) > 0:
            try:
                y = s[:1]
                s = s[1:]
                newstr = newstr + t['t'][f'{y}']
            except Exception as E:
                ()
        b = newstr.encode('ascii')
        base64_bytes = base64.b64decode(b)
        s = base64_bytes.decode('ascii')
        print(s)
        print("Done")
        time.sleep(5)
        os.system("cls")
        os.system("clear")
    else:
        print("Wrong")
    main()


main()
