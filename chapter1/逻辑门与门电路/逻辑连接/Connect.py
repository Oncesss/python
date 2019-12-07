class Connect:
    """元器件线，用来连接各逻辑门"""
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_pin(self)

    def get_from(self):
        return self.from_gate

    def to_target(self):
        return self.to_gate