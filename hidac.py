#!/usr/bin/env python
import os, sys, random, easygui, re, base64, time
problem = ""
run = ""
inputt = ""
def help():
    print("Encoding-Decoding tool")
    print("Usage: ./hidac.py [type] [Option A] [number] [file] [Option B]")
    print("\033[1m------------------------------------------------------------------------\033[0m")
    print("\033[47m\033[90m[type]\033[0m")
    print("   -e   --for encode")
    print("   -d   --for decode")
    print("\033[1m------------------------------------------------------------------------")
    print("\033[47m\033[90m[Options A]\033[0m")
    print("|-----------|")
    print("|\033[101m while -e: \033[0m|" + "  -c        --for command line text input")
    print("|-----------|  -g        --for big text input (easygui codebox)")
    print("|           |***********************************************************")
    print("|\033[101m while -d: \033[0m|" + "[\033[1m\033[92m! @ # % *\033[0m]  --special character for space")
    print("|-----------|")
    print("Special character will tell the tool where the blank points are. So while decoding output will be readable")
    print("You can use any of the above characters you want and this specific character will be replaced with ' '. ")
    print("See [NOTES] for more")
    print("\033[1m------------------------------------------------------------------------")
    print("\033[47m\033[90m[number]\033[0m")
    print("Each letter of text while encoding is changing place and a random letter is replacing it.")
    print("Number will tell the tool how many potitions letter should be moved")
    print("The bigger the number, the bigger the output will be")
    print("\033[1m------------------------------------------------------------------------\033[0m")
    print("\033[47m\033[90m[File]\033[0m")
    print("While encoding tool will open the file and erase [if exists] everything so it can write output")
    print("While decoding tool will try to decode the text into the file based on number")
    print("\033[1m------------------------------------------------------------------------\033[0m")
    print("\033[47m\033[90m[Options B]\033[0m")
    print("|-----------|")
    print("|\033[101m while -e: \033[0m|" + "  -eb     --for base64 encoding")
    print("|-----------|")
    print("|\033[101m while -d: \033[0m|  -db     --for base64 decoding")
    print("|-----------|")
    print("\033[1m------------------------------------------------------------------------\033[0m")
    print("\033[47m\033[90m\033[1m[NOTES]\033[0m")
    print("If you want to make output of decoded text readalbe you should use a special character after each word")
    print("Example: special_character=@  hello@world, My!name!is!root")
    print("This way tool will replace special character with a gap ' '.")
    print("Else decoded output will be like helloworld, Mynameisroot")
    print("You can use: \033[92m\033[1m! @ # % *  \033[0m")
    print
    print(problem)
    sys.exit()
try:
    if len(sys.argv) < 2 or sys.argv[1]=="--help":
        print("1")
        help()
    if len(sys.argv) > 6:
        problem = "Too many arguments"
        help()
    if sys.argv[1] == "-e":
        if not "-eb" in sys.argv[-1] and len(sys.argv) == 6:
            problem = "Please re-check Option B"
            help()
        if sys.argv[2] == "-c":
            inputt = "normal"
        if sys.argv[2] == "-g":
            inputt = "gui"
        number = int(sys.argv[3])
        if number == 0:
            try:
                print("\n[!] Selecting 0 nothing will be encoded except base64 if selected")
                ans=raw_input("\n[1]Exit[2]Continue# ")
                if ans=="1":
                    sys.exit()
                elif ans=="2":
                    pass
                else:
                    print("Not valid command, taking the safe way")
                    sys.exit()
            except KeyboardInterrupt:
                print("\n\n[#] Exit signal captured")
                sys.exit()
        if number < 0:
            problem = "Wrong number input. [0+]"
            help()
        file = sys.argv[4]
        run = "encode"
    if sys.argv[1] == "-d":
        if not "-db" in sys.argv[-1] and len(sys.argv) == 6:
            problem = "Please re-check Option B"
            help()
        print sys.argv[2]
        special_character = sys.argv[2]
        number = int(sys.argv[3])
        if number < 0:
            problem = "Wrong number input. [0+]"
        file = sys.argv[4]
        run = "decode"
except ValueError:
    problem = "No number specidied. Check your input"
    help()
except IndexError:
    problem = "Please check your input"
    help()
def main():
    def encode():
        global number
        global file
        global problem
        try:
            if inputt=="normal":
                ans=raw_input("Encode text: ")
            elif inputt=="gui":
                ans=easygui.codebox(msg="Enter text", title="Text encoding")
            else:
                problem = "Wrong mode. Check your input"
                help()
            f=open(file, "w")
            f.close()
            text="q!!!!!!!!@@@@@@@#######%wer%t%yuio%p%as%lkd%jg%hz%m*x*n*c*b*vQWERTYUIOPAL*SK%DJFHG#ZM@XNC!BV1234567890"
            a = ans.split()
            f=open(file, "a")
            os.system("clear")
            print("\n[+] [MESSAGE]\n")
            time.sleep(3)
            for g in a:
                b = g.split()
                for p in g:
                    for i in xrange(number):
                        q = random.choice(text)
                        print '\033[93m%s\033[0m' % q,
                        f.write(q)
                    print '\033[91m%s\033[0m' % p,
                    f.write(p)

            for i in xrange(number):
                q2=random.choice(text)
                print "\033[93m%s\033[0m" % q2,
                f.write(q2)
            f.close()
            l = ""
            if "-eb" in sys.argv[-1]:
                f = open(file, "r").read()
                f2 = base64.b64encode(f)
                #f.close()
                fil=open(file, "w")
                fil.write(f2)
                fil.close()
                l = " -->base64"
            print("\n----------------------")
            fi=open(file, "r").read()
            print("\n\n[+] Saving encoded message%s\n" % l)
            time.sleep(3)
            print(str(fi))
            time.sleep(2)
            print("\n[+] Output stored at %s" % file)
            print("   - Number: %d" % number)
            print("   - Size  : %sb" % os.path.getsize(file))
            print("   - Length: %d" % len(str(fi)))
            sys.exit()
        except KeyboardInterrupt:
            print("\nInterrupted by User")
            sys.exit()
        except OverflowError:
            problem =  "Just too much. Please enter smaller number"
            help()
    def decode():
        global file
        global number
        b64 = ""
        p = ""
        try:
            os.system("clear")
            if "-db" in sys.argv[-1]:
                    print("[+] Trying to read the file and decode <base64>")
                    b64 = "yes"
            if b64 == "yes":
                fi=open(file, "r").read()
                try:
                    f = base64.b64decode(fi)
                except TypeError:
                    print("  [-] Couldnt find base64 encoding")
                    print("[+] Continue without -db")
                    p = "yes"
            if b64 != "yes" or p =="yes":
                f = open(file, "r").read()
                f=str(f)
            filee=open("temporary_result_file.txt", "w")
            filee.close()
            print("[+] Removing characters based on number")
            print("----------------------------------------\033[93m")
            for i in xrange(number,len(f), number+1):
                d = f[i]
                d = d.replace("\r", "")
                d = d.replace("\n", "")
                print d,
                file=open("temporary_result_file.txt", "a")
                file.write(d)
                file.close()
            print("\033[0m\n----------------------------------------")
            print("[+] Saving > temporary_result_file.txt")
            print("[+] catting output with better look\n\033[93m")
            fil=open("temporary_result_file.txt", "r").read()
            #fil = re.sub(fil[-1],"",fil)
            print fil
            print("\033[0m\n[+] Trying to remove selected special character")
            fil = re.sub(special_character, " ", fil)
            print("[+] Printing final result")
            print('\n\033[46m' + fil + "\033[0m")
            print("\033[0m\n[+] Removing temporary_result_file.txt")
            #os.system("rm temporary_result_file.txt")
            sys.exit()
        except KeyboardInterrupt:
            print("\nInterrupted by user..")
            sys.exit()
    if run=="encode":
        encode()
    elif run=="decode":
        try:
            decode()
        except IOError:
            global problem
            problem = "No such file exists"
            help()
    else:
        problem = "Wrong type. Check your input"
        help()
main()
