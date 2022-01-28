class Null:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Нельзя делить на нуль")


div = Null(33, 57)
print(Null.divide_by_null(3, 0))
print(Null.divide_by_null(6, 0.1))
print(div.divide_by_null(8, 0))