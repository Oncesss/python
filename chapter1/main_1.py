from 逻辑门与门电路.双输入门.NandGate import NandGate
from 逻辑门与门电路.双输入门.NorGate import NorGate


if __name__ == '__main__':
    g1 = NandGate("G1")
    g2 = NorGate("G2")
    print(g1.get_output())
    print(g2.get_output())