from ..逻辑门基类.BinaryGate import BinaryGate

class NorGate(BinaryGate):
    """模拟或非门"""

    def __init__(self, name):
        super().__init__(name=name)

    def performGateLogic(self):
        a_input = self.get_pinA()
        b_input = self.get_pinB()

        if a_input == 0 and b_input == 0:
            return 1
        else:
            return 0
