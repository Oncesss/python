class Fraction:
    """分数类"""

    def __init__(self,top , buttom):
        if not isinstance(top, int) or not isinstance(buttom, int):
            raise ValueError("分子分母必须为整数")
        self.top = top
        self.buttom = buttom
        if top != 0 and self.buttom != 0:
            self.gcd()

    def gcd(self):
        oldm = self.buttom
        oldn = self.top
        while oldm%oldn != 0:
            oldm, oldn = oldn, oldm%oldn
        self.buttom /= oldn
        self.top /= oldn

        self.buttom = int(self.buttom)
        self.top = int(self.top)


    def show(self):
        print("{}/{}".format(self.top, self.buttom))

    def __str__(self):
        return str(self.top) + "/" + str(self.buttom)

    def __add__(self, other):
        top = self.top * other.buttom + other.top*self.buttom
        buttom = self.buttom * other.buttom
        return Fraction(top, buttom)

    def __sub__(self, other):
        top = self.top * other.buttom - other.top*self.buttom
        buttom = self.buttom * other.buttom
        return Fraction(top=top, buttom=buttom)

    def __mul__(self, other):
        return Fraction(self.top * other.top, self.buttom * other.buttom)

    def __truediv__(self, other):
        return Fraction(self.top * other.buttom, self.buttom * other.top)

    def __gt__(self, other):
        """self > other"""
        new = self - other
        if new.top <= 0 :
            return False
        else:
            return True

    def __lt__(self, other):
        """self < other"""
        new = self - other
        if new.top < 0:
            return True
        else:
            return False

    def __ge__(self, other):
        """大于等于"""
        new = self - other
        if new.top < 0:
            return False
        else:
            return True

    def __le__(self, other):
        """小于等于"""
        new = self - other
        if new.top <=0:
            return True
        else:
            return False

    def __eq__(self, other):
        """等于"""
        if self.top == other.top and self.buttom == other.buttom:
            return True
        else:
            return False




if __name__ == '__main__':
    myfrac1 = Fraction(10,20)
    myfrac2 = Fraction(1, 3)
    myfrac3 = Fraction(20, 40)

    print(myfrac1,"+",myfrac2,"=",myfrac1 + myfrac2)
    print(myfrac1,"-",myfrac2,"=",myfrac1 - myfrac2)
    print(myfrac1,"*",myfrac2,"=",myfrac1 * myfrac2)
    print(myfrac1,"/",myfrac2,"=",myfrac1 / myfrac2)

    print(myfrac1 > myfrac2)
    print(myfrac1 < myfrac2)
    print(myfrac1 >= myfrac2)
    print(myfrac1 <= myfrac2)
    print(myfrac1 >= myfrac3)
    print(myfrac1 <= myfrac3)
    print(myfrac1 == myfrac3)

