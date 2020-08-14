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
    def on():
        pass
    
    def off():
        pass

class RemoteControlTest():
    def main():
        light = light()
        lightOn = LighOnCommand(light)

        remote = SimpleRemoteControl(lightOn)
        remote.buttonWasPressed()

RemoteControlTest()
        

