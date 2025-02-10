import phone_classes as p

phones=[]
user_input=""
while True:
    print("Stored phones:")
    for i in range(len(phones)):
        print(f"{i+1}. {phones[i].name}")
    print("creating a phone: cr [type: bp (button phone), sp (smartphone), fp (foldable phone)]\n"
          "selecting a phone: sl [phone index]\n"
          "deleting phones: del [phone index1] [phone index2] ...\n"
          "clear all: clear\n"
          "add test phones: test\n"
          "exit: exit")
    user_input=input()
    command = user_input.split()[0]
    args = user_input.split()[1:]

    match command:
        #creating a phone
        case "cr":
            print("Enter following values: [battery capacity],[name],[os]", end='')
            #adjusting a creation menu accordingly
            match args[0]:
                case "bp":
                    print()
                    user_input = input().split(',')
                    phones.append(p.ButtonPhone(int(user_input[0]), user_input[1], user_input[2]))
                case "sp":
                    print()
                    user_input = input().split(',')
                    phones.append(p.Smartphone(int(user_input[0]), user_input[1], user_input[2]))
                case "fp":
                    print(",[fold direction]")
                    user_input = input().split(',')
                    phones.append(p.FoldablePhone(int(user_input[0]), user_input[1], user_input[2], user_input[3]))
            print("Phone added successfully")


        #selecting a phone for operations
        case "sl":
            if int(args[0])-1<=len(phones) and int(args[0])>0:
                sel_phone = phones[int(args[0])-1]
                while True:
                    print(f"Selected phone: {sel_phone.name}")
                    print("exit selected phone: exit\n"
                          "press power switch: pow\n"
                          "call another phone: call [phone index]\n"
                          "show info: info")
                    #adjusting menu according to phone type
                    match type(sel_phone).__name__:
                        case "ButtonPhone":
                            print("press some buttons: btn")
                        case "Smartphone" | "FoldablePhone":
                            print("switch internet connection: int")
                            print("install an app: install [app name]")
                            print("delete an app: del [app name]")
                            if isinstance(sel_phone, p.FoldablePhone):
                                print("fold phone: fold")
                    user_input = input()
                    command = user_input.split()[0]
                    args = user_input.split()[1:]
                    match command:
                        case "btn":
                            if isinstance(sel_phone, p.ButtonPhone):
                                sel_phone.press_some_buttons()
                        case "pow":
                            if sel_phone.turned_on:
                                sel_phone.turn_off()
                            else:
                                sel_phone.turn_on()
                        case "call":
                            if int(args[0])-1<=len(phones) and int(args[0])>0:
                                sel_phone.call(phones[int(args[0])-1])
                            else:
                                print("Invalid index")
                        case "exit":
                            break
                        case "info":
                            sel_phone.show_info()
                        case "int":
                            if isinstance(sel_phone, p.Smartphone):
                                if sel_phone.internet_connection:
                                    sel_phone.disconnect_from_internet()
                                else: sel_phone.connect_to_internet()
                        case "install":
                            if isinstance(sel_phone, p.Smartphone):
                                sel_phone.download_app(args[0])
                        case "fold":
                            if isinstance(sel_phone, p.FoldablePhone):
                                sel_phone.fold()
                        case "del":
                            if isinstance(sel_phone, p.Smartphone):
                                sel_phone.uninstall_app(args[0])
                        case _:
                            print("Invalid command")
            else:
                print("Invalid index")
        #deleting a phone
        case "del":
            del_seq = []
            for i in range(len(args)):
                ind = int(args[i])-1
                if 0 <= ind < len(phones) and not ind in del_seq:
                    del_seq.append(ind)
            del_seq.sort(reverse=True)
            for i in del_seq:
                phones.pop(i)
        #clearing all
        case "clear":
            phones.clear()
            print("Phones cleared successfully")
        #exit
        case "exit":
            break
        case "test":
            phones.append(p.ButtonPhone(1000,'Nokia','NokiaOS'))
            phones.append(p.Smartphone(3000,'Xiaomi A15','MIUI'))
            phones.append(p.FoldablePhone(3500,'Galaxy Fold Z 6','OneUI','horizontal'))
        case _:
            print("No such command!")
