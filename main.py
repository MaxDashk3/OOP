import phone_classes as p

p1 = p.ButtonPhone(2000, 'Nokia', 'NokiaOS')
p1.turn_on()
p1.show_info()
p1.press_some_buttons()

p2 = p.Smartphone(3500, 'IPhone 14 Pro', 'iOS')
p2.turn_on()
p2.connect_to_internet()
p2.download_app('Facebook')
p2.uninstall_app('Instagram')
p2.show_info()

p1.call(p2)

p3 = p.FoldablePhone(3400, 'Galaxy Z Fold 6', "Android (One UI)", "horizontal")
p3.fold()
p3.show_info()

p3.call(p2)
p1.call(p3)