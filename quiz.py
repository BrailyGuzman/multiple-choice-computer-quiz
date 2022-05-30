import time

print("[!} Welcome To This 10 Questions Computer Quiz!")
ready = input("[?] Are you ready? Y/N: ")


if ready == "Y":
    print("\n[/] Starting Quiz! :)")
else:
    quit()

time.sleep(1)

def quiz():
    question_1 = "\n1. What do you call a computer on a network that requests files from another computer?\n(A) A client\n(B) A host\n(C) A router\n(D) A web server"
    print(question_1)
    answer_1 = "The Answer is: A"
    input_1 = input("\nOption: ")
    if input_1 == "A" or "a":
        print("Correct!")
    else:
        print("Incorrect!" + answer_1)
    
    time.sleep(1)

    question_2 = "\n2. Hardware devices that are not part of the main computer system and are often added later to the system.\n(A) Peripheral\n(B) Clip art\n(C) Highlight\n(D) Execute"
    print(question_2)
    answer_2 = "The Answer is: A"
    input_2 = input("\nOption: ")
    if input_2 == "A" or "a":
        print("Correct!")
    else:
        print("Incorrect!"  + answer_2)

    time.sleep(1)

    question_3 = "\n3. The main computer that stores the files that can be sent to computers that are networked together is:\n(A) Clip art\n(B) Mother board\n(C) Peripheral\n(D) File server"
    print(question_3)
    answer_3 = "The Answer is: D"
    input_3 = input("\nOption: ")
    if input_3 == "D" or "d":
        print("Correct!")
    else:
        print("Incorrect!" + answer_3)
    
    time.sleep(1)

    question_4 = "\n4. How can you catch a computer virus?\n(A) Sending e-mail messages\n(B) Using a laptop during the winter\n(C) Opening e-mail attachments\n(D) Shopping on-line"
    print(question_4)
    answer_4 = "The Answer is: D"
    input_4 = input("\nOption: ")
    if input_4 == "C" or "d":
        print("Correct!")
    else:
        print("Incorrect!" + answer_4)
    
    time.sleep(1)

    question_5 = "\nGoogle (www.google.com) is a:\n(A) Search Engine\n(B) Number in Math\n(C) Directory of images\n(D) Chat service on the web"
    print(question_5)
    answer_5 = "The Answer is: A"
    input_5 = input("\nOption: ")
    if input_5 == "A" or "a":
        print("Correct!")
    else:
        print("Incorrect!" + answer_5)
    
    time.sleep(1)

    question_6 = "\nWhich is not an Internet protocol?\n(A) HTTP\n(B) FTP\n(C) STP\n(D) IP"
    print(question_6)
    answer_6 = "The Answer is: C"
    input_6 = input("\nOption: ")
    if input_6 == "C" or "c":
        print("Correct!")
    else:
        print("Incorrect!" + answer_6)
    
    time.sleep(1)

    question_7 = "\nWhich of the following is not a valid domain name?\n(A) www.yahoo.com\n(B) www.yahoo.co.uk\n(C) www.com.yahoo\n(D) www.yahoo.co.in"
    print(question_7)
    answer_7 = "The Answer is: C"
    input_7 = input("\nOption: ")
    if input_7 == "C" or "c":
        print("Correct!")
    else:
        print("Incorrect!" + answer_7)

    time.sleep(1)

    question_8 = "\nAOL stands for:\n(A) Arranged Outer Line\n(B) America Over LAN\n(C) Audio Over LAN\n(D) America On-line"
    print(question_8)
    answer_8 = "The Answer is: D"
    input_8 = input("\nOption: ")
    if input_8 == "D" or "d":
        print("Correct!")
    else:
        print("Incorrect!" + answer_8)
    
    time.sleep(1)

    question_9 = "\nAnother name for a computer chip is:\n(A) Execute\n(B) Micro chip\n(C) Microprocessor\n(D) Select"
    print(question_9)
    answer_9 = "The Answer is: B"
    input_9 = input("\nOption: ")
    if input_9 == "B" or "b":
        print("Correct!")
    else:
        print("Incorrect!" + answer_9)

    time.sleep(1)

    question_10 = "\n10. www stands for:\n(A) World Wide Web\n(B) World Wide Wares\n(C) World Wide Wait\n(D) World Wide War"
    print(question_10)
    answer_10 = "The Answer is: A"
    input_10 = input("\nOption: ")
    if input_10 == "A" or "a":
        print("Correct!")
    else:
        print("Incorrect!" + answer_10)

    print("You have completed this quiz!")
    time.sleep(3)
    quit()
quiz()
