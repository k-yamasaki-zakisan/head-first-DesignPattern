from abc import ABCMeta, abstractmethod

#コマンドクラス
##抽象パート
class Command(metaclass=ABCMeta):
    def execute():
        pass

    def undo():
        pass

class MacroCommand(Command):
    def __init__(self, commands):
        self.__commands = commands
    
    def execute(self):
        for i in range(len(self.__commands)):
            self.__commands[i].execute()


##具象パート
class LightOnCommand(Command):
    def __init__(self, light):
        self.__light = light
    
    def execute(self):
        self.__light.on()
    
    def undo(self):
        self.__light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.__light = light
    
    def execute(self):
        self.__light.off()
    
    def undo(self):
        self.__light.on()

class GarageDoorUpCommnad(Command):
    def __init__(self, garageDoor):
        self.__garageDoor = garageDoor
    
    def execute(self):
        self.__garageDoor.up()
    
    def undo(self):
        self.__garageDoor.down()

class GarageDoorDownCommnad(Command):
    def __init__(self, garageDoor):
        self.__garageDoor = garageDoor
    
    def execute(self):
        self.__garageDoor.down()
    
    def undo(self):
        self.__garageDoor.up()

class CeillingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        self.__ceilingFan = ceilingFan
    
    def execute(self):
        preSpeed = self.__ceilingFan.getSpeed()
        self.__ceilingFan.high()

    def undo(self):
        if preSpeed == self.__ceilingFan.checkHigh():
            self.__ceilingFan.high()
        elif preSpeed == self.__ceilingFan.checkMedium():
            self.__ceilingFan.medium()
        elif preSpeed == self.__ceilingFan.checkLow():
            self.__ceilingFan.low()
        elif preSpeed == self.__ceilingFan.checkOff():
            self.__ceilingFan.off()

class CeillingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        self.__ceilingFan = ceilingFan
        self.preSpeed = self.__ceilingFan.checkOff()
    
    def execute(self):
        self.preSpeed = self.__ceilingFan.getSpeed()
        self.__ceilingFan.medium()

    def undo(self):
        if self.preSpeed == self.__ceilingFan.checkHigh():
            self.__ceilingFan.high()
        elif self.preSpeed == self.__ceilingFan.checkMedium():
            self.__ceilingFan.medium()
        elif self.preSpeed == self.__ceilingFan.checkLow():
            self.__ceilingFan.low()
        elif self.preSpeed == self.__ceilingFan.checkOff():
            self.__ceilingFan.off()

class CeillingFanLowCommand(Command):
    def __init__(self, ceilingFan):
        self.__ceilingFan = ceilingFan
        self.preSpeed = self.__ceilingFan.checkOff()
    
    def execute(self):
        self.preSpeed = self.__ceilingFan.getSpeed()
        self.__ceilingFan.low()

    def undo(self):
        if self.preSpeed == self.__ceilingFan.checkHigh():
            self.__ceilingFan.high()
        elif self.preSpeed == self.__ceilingFan.checkMedium():
            self.__ceilingFan.medium()
        elif self.preSpeed == self.__ceilingFan.checkLow():
            self.__ceilingFan.low()
        elif self.preSpeed == self.__ceilingFan.checkOff():
            self.__ceilingFan.off()

class CeillingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        self.__ceilingFan = ceilingFan
        self.preSpeed = self.__ceilingFan.checkOff()
    
    def execute(self):
        self.preSpeed = self.__ceilingFan.getSpeed()
        self.__ceilingFan.off()

    def undo(self):
        if self.preSpeed == self.__ceilingFan.checkHigh():
            self.__ceilingFan.high()
        elif self.preSpeed == self.__ceilingFan.checkMedium():
            self.__ceilingFan.medium()
        elif self.preSpeed == self.__ceilingFan.checkLow():
            self.__ceilingFan.low()
        elif self.preSpeed == self.__ceilingFan.checkOff():
            self.__ceilingFan.off()


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

class CeilingFan():
    def __init__(self, location):
        self.__HIGH = 3
        self.__MEDIUM = 2
        self.__LOW = 1
        self.__OFF = 0
        self.__location = location
        self.speed = 0
    
    def high(self):
        self.speed = self.__HIGH
        print("扇風機の強さは「強」です")
    
    def medium(self):
        self.speed = self.__MEDIUM
        print("扇風機の強さは「中」です")
    
    def low(self):
        self.speed = self.__LOW
        print("扇風機の強さは「弱」です")
    
    def off(self):
        self.speed = self.__OFF
        print("扇風機を切りました")
    
    def checkHigh(self):
        return self.__HIGH
    
    def checkMedium(self):
        return self.__MEDIUM

    def checkLow(self):
        return self.__LOW
    
    def checkOff(self):
        return self.__OFF

    def getSpeed(self):
        return self.speed

#リモコンボタンのセットクラス
#抽象パート
class RemoteControl():
    def __init__(self):
        self.__onCommands = []
        self.__offCommands = []

        nocommand = Nocommand()
        for _ in range(7):
            self.__onCommands.append(nocommand)
            self.__offCommands.append(nocommand)
        
        self.__undocommand = nocommand

    def setCommand(self, slot, onCommand, offCommand):
        self.__onCommands[slot] = onCommand
        self.__offCommands[slot] = offCommand
    
    def onButtonWasPushed(self, slot):
        self.__onCommands[slot].execute()
        self.__undocommand = self.__onCommands[slot]
    
    def offButtonWasPushed(self, slot):
        self.__offCommands[slot].execute()
        self.__undocommand = self.__offCommands[slot]
    
    def undoButtonWaspushed(self):
        self.__undocommand.undo()
    
    def toString(self):
        self.__stringBuff = []
        self.__stringBuff.append("---------リモコン一覧----------")
        for i in range(len(self.onCommands)):
            self.__stringBuff.append("[スロット"+ str(i) + "]" + str(self.__onCommands[i]) + " " + str(self.__offCommands[i]))
        
        return str(self.__stringBuff)

#設定されていないボタン用の実装を無効化するクラス
class Nocommand(Command):
    def execute(self):
        pass


#実行パート
class RemoteLoader():
    def mainTest():
        #実行コマンドクラスの宣言
        remoteControl = RemoteControl()

        #コマンドインスタンスを作成
        lightRoomLight = Light("リビングルーム")
        kitchenLight = Light("キッチン")
        garageDoor = GarageDoor()

        lightRoomLightOn = LightOnCommand(lightRoomLight)
        lightRoomLightOff = LightOffCommand(lightRoomLight)
        kitchenRoomLightOn = LightOnCommand(kitchenLight)
        kitchenRoomLightOff = LightOffCommand(kitchenLight)
        garageDoorUpCommnad = GarageDoorUpCommnad(garageDoor)
        garageDoorDownCommnad = GarageDoorDownCommnad(garageDoor)

         #コマンドをセット
        remoteControl.setCommand(0, lightRoomLightOn, lightRoomLightOff)
        remoteControl.setCommand(1, kitchenRoomLightOn, kitchenRoomLightOff)
        remoteControl.setCommand(2, garageDoorUpCommnad, garageDoorDownCommnad)

        #コマンド実行
        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました
        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました

        remoteControl.onButtonWasPushed(1)    #キッチンの照明をつけました
        remoteControl.offButtonWasPushed(1)   #キッチンの照明を消しました

        remoteControl.onButtonWasPushed(2)    #ガレージを開けました
        remoteControl.offButtonWasPushed(2)   #ガレージを閉じました

    def mainUndoTest():
        #実行コマンドクラスの宣言
        remoteControl = RemoteControl()

        #コマンドインスタンスを作成
        lightRoomLight = Light("リビングルーム")
        lightRoomLightOn = LightOnCommand(lightRoomLight)
        lightRoomLightOff = LightOffCommand(lightRoomLight)

        #コマンドをセット
        remoteControl.setCommand(0, lightRoomLightOn, lightRoomLightOff)

        #コマンド実行
        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました
        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました

        print(remoteControl.onCommands, remoteControl.undocommand)

        remoteControl.undoButtonWaspushed()   #リビングルームの照明をつけました

        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました
        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました

        remoteControl.undoButtonWaspushed()   #リビングルームの照明を消しました
    
    def mainCeilingFanTest():
        #実行コマンドクラスの宣言
        remoteControl = RemoteControl()

        #コマンドインスタンスを作成
        ceillingFan = CeilingFan("リビングルーム")

        ceillingFanHigh = CeillingFanHighCommand(ceillingFan)
        ceillingFanMedium = CeillingFanMediumCommand(ceillingFan)
        ceillingFanLow = CeillingFanLowCommand(ceillingFan)
        ceillingFanOff = CeillingFanOffCommand(ceillingFan)

        #コマンドをセット
        remoteControl.setCommand(2, ceillingFanHigh, ceillingFanOff)
        remoteControl.setCommand(1, ceillingFanMedium, ceillingFanOff)
        remoteControl.setCommand(0, ceillingFanLow, ceillingFanOff)

        #コマンド実行
        remoteControl.onButtonWasPushed(0)    #扇風機の強さは「弱」です
        remoteControl.offButtonWasPushed(0)   #扇風機を切りました

        remoteControl.undoButtonWaspushed()   #扇風機の強さは「弱」です

        remoteControl.onButtonWasPushed(1)    #扇風機の強さは「中」です

        remoteControl.undoButtonWaspushed()   #扇風機の強さは「弱」です

        remoteControl.offButtonWasPushed(2)   #扇風機を切りました
        remoteControl.onButtonWasPushed(2)    #扇風機の強さは「強」です

    def mainMacroTest():
        #実行コマンドクラスの宣言
        remoteControl = RemoteControl()

        #コマンドインスタンスを作成
        lightRoomLight = Light("リビングルーム")
        kitchenLight   = Light("キッチン")
        garageDoor     = GarageDoor()

        lightRoomLightOn      = LightOnCommand(lightRoomLight)
        lightRoomLightOff     = LightOffCommand(lightRoomLight)
        kitchenRoomLightOn    = LightOnCommand(kitchenLight)
        kitchenRoomLightOff   = LightOffCommand(kitchenLight)
        garageDoorUpCommnad   = GarageDoorUpCommnad(garageDoor)
        garageDoorDownCommnad = GarageDoorDownCommnad(garageDoor)

        #コマンドをセット(マクロ化するために配列でひとまとめにする)
        partyOn  = [lightRoomLightOn, kitchenRoomLightOn, garageDoorUpCommnad]
        partyOff = [lightRoomLightOff, kitchenRoomLightOff, garageDoorDownCommnad]

        partyOnMacro  = MacroCommand(partyOn)
        partyOffMacro = MacroCommand(partyOff)
        remoteControl.setCommand(0, partyOnMacro, partyOffMacro)

        #コマンド実行
        remoteControl.onButtonWasPushed(0)    #リビングルームの照明をつけました キッチンの照明をつけました ガレージを開けました
        remoteControl.offButtonWasPushed(0)   #リビングルームの照明を消しました キッチンの照明を消しました ガレージを閉じました

#実行
#RemoteLoader.mainTest()
#RemoteLoader.mainUndoTest()
#RemoteLoader.mainCeilingFanTest()
RemoteLoader.mainMacroTest()