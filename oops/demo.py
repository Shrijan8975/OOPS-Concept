class Fan():
    def __init__(self,sp=1500,cl="copper",input=230):
        self.speed= sp
        self.coil = cl
        self.input_voltage=input

    def setdata(self):
        self.speed=int(input("enter speed of fan: "))
        self.coil=input("enter coil did you need: ")
        self.input_voltage=int(input("enter input voltage: "))

    def getData(self):
         print("speed: {0}".format(self.speed))
         print("coil: {0}".format(self.coil))
         print("input_voltage: {0}".format(self.input_voltage))

s1=Fan(1600,"copper",230)
s1.getData()

print("__________________________")

s2=Fan()
s2.getData()

print("___________________________")
s3=Fan()
s3.getData()