class Pen:
    ''' Pen init method takes three parameters name, ink_quantity and colour'''
    def __init__(self, name:str, inkQ:int, colour:str):
        self.__name__ = name
        self.__intkQ__ = inkQ
        self.__colour__ = colour

    def write(self):
        if self.getInkQ() > 0:
            print('Pen ' + self.getName() + ' is writing, '
                                        'it has Ink Quntity : ' + str(self.getInkQ()) + ' ml and color :' + self.getColour())
        else:
            print('There is no int int the ' + self.getName()+ ' pen')

    def getInkQ(self) -> int:
        return self.__intkQ__

    def getName(self) -> str:
        return self.__name__

    def getColour(self) -> str:
        return self.__colour__

