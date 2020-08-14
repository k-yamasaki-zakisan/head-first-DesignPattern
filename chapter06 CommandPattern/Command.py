from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def execute():
        pass

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

class SimpleRemoteControl():
    def setCommand(self, command):
        self.slot = command

    def buttonWasPressed(self):
        self.slot.execute()

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


class RemoteControlTest():
    def main():
        remote = SimpleRemoteControl()

        light = Light()
        lightOn = LighOnCommand(light)
        garageDoor = GarageDoor()
        garageDoorOpen = GarageDoorOpenCommnad(garageDoor)

        remote.setCommand(lightOn)
        remote.buttonWasPressed()
        remote.setCommand(garageDoorOpen)
        remote.buttonWasPressed()


    




RemoteControlTest.main()
        

