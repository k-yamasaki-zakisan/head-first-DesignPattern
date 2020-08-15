from abc import ABCMeta, abstractmethod

#コマンドクラス
##抽象パート
class Command(metaclass=ABCMeta):
    def execute():
        pass

    def undo():
        pass

##具象パート
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()

class GarageDoorUpCommnad(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.up()
    
    def undo(self):
        self.garageDoor.down()

class GarageDoorDownCommnad(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.down()
    
    def undo():
        self.garageDoor.up()


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


#リモコンボタンのセットクラス
class RemoteControl():
    def __init__(self):
        self.onCommands = []
        self.offCommands = []

        nocommand = Nocommand()
        for _ in range(7):
            self.onCommands.append(nocommand)
            self.offCommands.append(nocommand)
        
        self.undocommand = nocommand

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
    
    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undocommand = self.onCommands[slot]
    
    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undocommand = self.offCommands[slot]
    
    def undoButtonWaspushed(self):
        self.undocommand.undo()
    
    def toString(self):
        self.stringBuff = []
        self.stringBuff.append("---------リモコン一覧----------")
        for i in range(len(self.onCommands)):
            self.stringBuff.append("[スロット"+ str(i) + "]" + str(self.onCommands[i]) + " " + str(self.offCommands[i]))
        
        return str(self.stringBuff)


#設定されていないボタン用の実装を無効化するクラス
class Nocommand(Command):
    def execute(self):
        pass


#実行パート
class RemoteLoader():
    def mainTest():
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

    def mainUndoTest():
        remoteControl = RemoteControl()

        lightRoomLight = Light("リビングルーム")

        lightRoomLightOn = LightOnCommand(lightRoomLight)
        lightRoomLightOff = LightOffCommand(lightRoomLight)

        remoteControl.setCommand(0, lightRoomLightOn, lightRoomLightOff)

        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました
        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました

        print(remoteControl.onCommands, remoteControl.undocommand)

        remoteControl.undoButtonWaspushed()   #リビングルームの照明をつけました

        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました
        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました

        remoteControl.undoButtonWaspushed()   #リビングルームの照明を消しました


#実行
RemoteLoader.mainTest()
RemoteLoader.mainUndoTest()