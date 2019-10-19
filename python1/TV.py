class TV:
    def __init__(self, name:str, channel:int=1, volumn:int=15):
        self.name = name
        self.channel = channel
        self.volumn = volumn
        self.isOn = False

    def start(self):
        self.isOn = True
        #print('TV : '+ self.name + 'has started ' + 'channel number : '+ str(self.channel) + ' volumn : '+ str(self.volumn))

    def changeChannel(self, channel:int):
        if self.isOn == True:
            self.channel = channel
        else:
            print('Please trun on the TV')

    def changeVolumn(self, volumn:int):
        if self.isOn == True:
            self.volumn = volumn
        else:
            print('Please trun on the TV')

    def display(self):
        if self.isOn == True:
            print('TV Name '+ self.name + ' Channel : '+ str(self.channel) + ' volumn : '+ str(self.volumn))
        else:
            print('Please trun on the TV')

tv1 = TV('LG')
tv2 = TV('Samsung')
tv1.start()
tv1.display()
tv2.display()
tv1.changeChannel(5)
tv1.changeVolumn(100)
tv1.display()
tv2.display()