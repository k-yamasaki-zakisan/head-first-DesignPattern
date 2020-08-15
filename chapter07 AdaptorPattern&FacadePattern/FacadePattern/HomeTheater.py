#統合されたインターフェースを作成してボタン一つで映画を見るのに必要な操作を行う
#必要クラスが多すぎて実装を断念

class HomethjeaterFacade():
    def __init__(self, amp, tuner, dvd, cd , projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watchMovie(self, move):
        print("映画を見る準備をします-------------------")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDvd(dvd)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play(movie)
    
    def endMovie(self):
        print("ムービーシアターを停止します--------------")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()


class HometheaterTestDrive():
    def main():
        homeTheater =  HomethjeaterFacade(amp, tuner, dvd, cd, projector,
                                          screen, lights, popper)
        homeTheater.watchMovie("（劇場版）ぐりとぐらとグフ")
        homeTheater.endMovie()