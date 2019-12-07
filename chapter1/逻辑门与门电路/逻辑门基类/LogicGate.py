class LogicGate:
    """逻辑门基类，定义逻辑门类型及获取输出"""

    def __init__(self, name):
        self.name = name
        self.output = None

    def get_name(self):

        return self.name

    def get_output(self):

        self.output = self.performGateLogic()
        return self.output

    def performGateLogic(self):
        pass