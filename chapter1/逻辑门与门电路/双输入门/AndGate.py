from ..逻辑门基类.BinaryGate import BinaryGate


class AndGate(BinaryGate):
    """模拟与门"""
    def __init__(self, name):
        super().__init__(name=name)

    def performGateLogic(self):
        a_input = self.get_pinA()
        b_input = self.get_pinB()

        return a_input&b_input