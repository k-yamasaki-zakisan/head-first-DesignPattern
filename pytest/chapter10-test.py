import sys
sys.path.append("../chapter10 StatePattern/NewStateMachine/")
from Client import GumballMachine

def test_gumballMachineTestDrive():
    Client.gumballMachineTestDrive(5)
    assert (gumballMachineTestDrive.count == 5)


if __name__ == '__main__':
    pytest.main()

    