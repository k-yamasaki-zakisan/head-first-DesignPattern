from abc import ABCMeta, abstractmethod

#コマンドクラス
##抽象パート
class Command(metaclass=ABCMeta):
    def execute():
        pass

##具象パート
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()

class GarageDoorUpCommnad(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.up()

class GarageDoorDownCommnad(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.down()


# class StereOnWithCDCommand(Command):
#     def __init__(self, stereo):
#         self.stereo = stereo
    
#     def execute(self):
#         self.stereo.on()
#         self.stereo.setCD()
#         self.stereo.setVolume(11)


#セットされるコマンド(具象)
class Light():
    def __init__(self, type):
        self.type = type

    def on(self):
        print(self.type + "の照明をつけました")
    
    def off(self):
        print(self.type + "の照明を消しました")

class GarageDoor():
    def up(self):
        print("ガレージを開けました")
    
    def down(self):
        print("ガレージを閉じました")
    
    def stop(self):
        print("ガレージのシャッターを閉じました")
    
    def lightOn(self):
        print("ガレージの照明をつけました")
    
    def lightOff(self):
        print("ガレージの照明を消しました")


class RemoteControl():
    def __init__(self):
        self.onCommands = [None]*7
        self.offCommands = [None]*7

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
    
    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
    
    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
    
    def toString(self):
        self.stringBuff = []
        self.stringBuff.append("---------リモコン----------")
        for i in range(len(self.onCommands)):
            self.stringBuff.append("[スロット"+ str(i) + "]" + str(self.onCommands[i]) + " " + str(self.offCommands[i]))
        
        return str(self.stringBuff)


class RemoteLoader():
    def main():
        remoteControl = RemoteControl()

        lightRoomLight = Light("リビングルーム")
        kitchenLight = Light("キッチン")
        garageDoor = GarageDoor()

        lightRoomLightOn = LightOnCommand(lightRoomLight)
        lightRoomLightOff = LightOffCommand(lightRoomLight)

        kitchenRoomLightOn = LightOnCommand(kitchenLight)
        kitchenRoomLightOff = LightOffCommand(kitchenLight)

        garageDoorUpCommnad = GarageDoorUpCommnad(garageDoor)
        garageDoorDownCommnad = GarageDoorDownCommnad(garageDoor)

        remoteControl.setCommand(0, lightRoomLightOn, lightRoomLightOff)
        remoteControl.setCommand(1, kitchenRoomLightOn, kitchenRoomLightOff)
        remoteControl.setCommand(2, garageDoorUpCommnad, garageDoorDownCommnad)

        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました
        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました

        remoteControl.onButtonWasPushed(1)    #キッチンの照明をつけました
        remoteControl.offButtonWasPushed(1)   #キッチンの照明を消しました

        remoteControl.onButtonWasPushed(2)    #ガレージを開けました
        remoteControl.offButtonWasPushed(2)   #ガレージを閉じました


RemoteLoader.main()