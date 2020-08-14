from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def execute():
        pass

class LighOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()

class SimpleRemoteControl():
    def __init__(self, command):
        self.slot = command

    def buttonWasPressed(self):
        self.slot.execute()

class Light():
    def on(self):
        print("照明がついています")
    
    def off(self):
        pass

class RemoteControlTest():
    def main():
        light = Light()
        lightOn = LighOnCommand(light)

        remote = SimpleRemoteControl(lightOn)
        remote.buttonWasPressed()

RemoteControlTest.main()
        

