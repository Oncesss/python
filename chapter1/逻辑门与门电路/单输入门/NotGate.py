from ..逻辑门基类.LogicGate import LogicGate


class NotGate(LogicGate):
    """逻辑非门模拟"""

    def __init__(self, name):
        super().__init__(name=name)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + str(self.get_name()) + \
                         " -->"))
        else:
            return self.pin.get_from().get_output()

    def set_pin(self, gate):
        if self.pin is None:
            self.pin = gate

        else:
            raise ValueError("The pin has been connect!")

    def performGateLogic(self):
        gate_input = self.get_pin()
        if gate_input == 1:
            return 0
        elif gate_input == 0:
            return 1
        else:
            raise ValueError("逻辑值错误!")