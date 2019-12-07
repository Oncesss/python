from .LogicGate import LogicGate


class BinaryGate(LogicGate):
    """二输入逻辑门基类"""

    def __init__(self, name):
        super().__init__(name=name)
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + str(self.get_name()) + \
                             " -->"))

        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + str(self.get_name()) + \
                             " -->"))

        else:
            return self.pinB.get_from().get_output()

    def set_pin(self, gate):
        if self.pinA is None:
            self.pinA = gate

        elif self.pinB is None:
            self.pinB = gate

        else:
            raise ValueError("pins has been connect!")
