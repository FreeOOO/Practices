class Aminal(object):
    #def __init__(self,name):
    #    self.name = name
    #def run(self):
    #    print('{0} is running'.format(self.name))
    def printInfo(self):
        print('aminal is running')

class Dog(Aminal):
    def __init__(self,name):
        self.__name = name
    def printInfo(self):
        print('{0} is running'.format(self.__name))
    #def __init__(self,eat):
    #    Aminal.__init__(self,'dog')
    #    self.__eat = eat
    #def printInfo(self):
    #    print('{0} {1}'.format(self.name,self.__eat))

if __name__ == '__main__':
    dog = Dog('dog')
    #dog.run()
    dog.printInfo()
    #print(dog.name)
