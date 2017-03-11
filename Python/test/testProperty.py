class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height = height
    @property
    def resolution(self):
        return self.__width * self.__height

if __name__ == '__main__':
     s = Screen()
     s.width = 4
     s.height = 8
     print(s.resolution)
