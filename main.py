from ATM import BasicATM, ProtectedATM, CreditCard, Collector, Bank

card_list = [CreditCard(1020304910117658, 2025, 160043),
             CreditCard(4039180945839820, 5324, 1123020)]
collector_list = [Collector("Oppenheimer", [50,50,50,50,50]),
         Collector("Maria", [150,200,300,430,220])]

bank = Bank([BasicATM("NextLVL", [1, 2, 3, 4, 5]),
             ProtectedATM("SafeBank24", [500,300,400,300,400]),
             BasicATM("Bankbank.UA", [100, 200, 300, 203, 433])])

bill_numbers = [1000, 500, 200, 100, 50]

while True:
    print("Available ATMs:")
    index = 1
    for i in bank:
        print(f"{index}. {i.name}")
        index += 1
    print("Credit cards:")
    index = 1
    for i in card_list:
        print(f"{index}. number: {i.get_number()}, pin {i.get_pin()}, money: {i.money}")
        index += 1
    print("Collectors:")
    index = 1
    for i in collector_list:
        bills_string = ""
        for a in range(len(bill_numbers)):
            bills_string+=f"{str(i.bills[a])} for {bill_numbers[a]}, "
        bills_string = bills_string[:-2]
        print(f"{index}. {i.name}, bills: {bills_string}")
        index += 1

    print("Choose a command:\n"
          f"add an object: add [batm, patm, card, coll]\n"
          f"remove an object: rm [atm, card, coll] [index]\n"
          f"withdraw money: wdraw [atm_index] [card_index]\n"
          f"replenish money: repl [atm_index] [collector_index]\n"
          f"view info about atms: inf\n"
          f"set amount of bills for a collector: set [collector_index] [1000_uah_bills] [500_uah_bills] [200_uah_bills] [100_uah_bills] [50_uah_bills]\n"
          f"clear all: clear\n"
          f"exit: exit\n")
    user_input = input()
    command = user_input.split()[0]
    args = user_input.split()[1:]
    match command:
        case "add":
            match args[0]:
                case "batm" | "patm":
                    user_input = input("enter ATM name and amount of bills (optional): [name] [1000_uah_bills] [500_uah_bills] [200_uah_bills] [100_uah_bills] [50_uah_bills]\n")
                    if len(user_input.split()) not in [1, 6]:
                        raise ValueError("Incorrect number of arguments!")
                    name = user_input.split()[0]
                    bills = []
                    for i in user_input.split()[1:]:
                        bills.append(int(i))
                    match args[0]:
                        case "batm":
                            if bills:
                                bank.add(BasicATM(name, bills))
                            else: bank.add(BasicATM(name))
                        case "patm":
                            if bills:
                                bank.add(ProtectedATM(name, bills))
                            else:
                                bank.add(ProtectedATM(name))
                case "card":
                    user_input = input("enter card number, pin code and amount of money: [number] [pin] [money_amount]\n")
                    if len(user_input.split()) != 3:
                        raise ValueError("Incorrect number of arguments!")
                    number = int(user_input.split()[0])
                    pin = int(user_input.split()[1])
                    money = int(user_input.split()[2])

                    card_list.append(CreditCard(number, pin, money))
                case "coll":
                    user_input = input("enter collector name and bill amount, [name] [1000_uah_bills] [500_uah_bills] [200_uah_bills] [100_uah_bills] [50_uah_bills]\n")
                    if len(user_input.split()) not in [6]:
                        raise ValueError("Incorrect number of arguments!")
                    bills = []
                    for i in user_input.split()[1:]:
                        bills.append(int(i))
                    name = user_input.split()[0]
                    collector_list.append(Collector(name, bills))
            pass
        case "rm":
            if len(args) != 2:
                raise ValueError("Incorrect number of arguments!")
            match args[0]:
                case "atm":
                    del bank[int(args[1]) - 1]
                case "coll":
                    del collector_list[int(args[1])-1]
                case "card":
                    del card_list[int(args[1])-1]
        case "wdraw":
            if len(args) != 2:
                raise ValueError("Incorrect number of arguments!")
            bank[int(args[0]) - 1].get_bills(card_list[int(args[1]) - 1])
        case "repl":
            if len(args) != 2:
                raise ValueError("Incorrect number of arguments!")
            bank[int(args[0]) - 1].get_replenished(collector_list[int(args[1]) - 1])
        case "inf":
            bank.info()
        case "set":
            if len(args) != 6:
                raise ValueError("Incorrect number of arguments!")
            bills = []
            for i in args[1:]:
                bills.append(int(i))
            collector_list[int(args[0])-1].bills = bills
        case "clear":
            bank = Bank()
            card_list = []
            collector_list = []
        case "exit":
            break
        case _:
            print("Error! Unknown command!")