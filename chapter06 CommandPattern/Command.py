from abc import ABCMeta, abstractmethod

#コマンドクラス
##抽象パート
class Command(metaclass=ABCMeta):
    def execute():
        pass

##具象パート
class LighOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()

class GarageDoorOpenCommnad(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor
    
    def execute(self):
        self.garageDoor.up()


#コマンド実行クラス(具象)
class SimpleRemoteControl():
    def setCommand(self, command):
        self.slot = command

    def buttonWasPressed(self):
        self.slot.execute()

#セットされるコマンド(具象)
class Light():
    def on(self):
        print("照明をつけました")
    
    def off(self):
        print("照明を消しました")

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


#実行処理の記述
class RemoteControlTest():
    def main():
        #実行コマンドクラスの宣言
        remote = SimpleRemoteControl()

        #コマンドインスタンスを作成
        light = Light()
        lightOn = LighOnCommand(light)
        garageDoor = GarageDoor()
        garageDoorOpen = GarageDoorOpenCommnad(garageDoor)

        #コマンドをセットして実行
        remote.setCommand(lightOn)
        remote.buttonWasPressed()
        remote.setCommand(garageDoorOpen)
        remote.buttonWasPressed()


#実行パート
RemoteControlTest.main()
        

