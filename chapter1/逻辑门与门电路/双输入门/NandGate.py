from ..逻辑门基类.BinaryGate import BinaryGate


class NandGate(BinaryGate):
    """模拟与非门"""

    def __init__(self, name):
        super().__init__(name=name)

    def performGateLogic(self):
        a_input = self.get_pinA()
        b_input = self.get_pinB()

        if a_input == 1 and b_input == 1:
            return 0
        else:
            return 1

