class Smartphone:

    marka_phone = "Iphone"
    model_phone = "001"
    number_phone = "7 900 000 00 00"

    def __init__(self, marka, model, number):
        self.marka_phone = marka
        self.model_phone = model
        self.number_phone = number

    def info(self):
        print(self.marka_phone, "-", self.model_phone + ".", self.number_phone + ".")
