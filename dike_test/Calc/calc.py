
class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b

    def seki(self):
        return self.a*self.b

    def shou(self):
        return self.a/self.b


if __name__ == "__main__":
    a = Calc(1, 2)               # MyClass のインスタンスを生成
    print("test", a.add())          # 変数 value に文字列 "abc" を代入 