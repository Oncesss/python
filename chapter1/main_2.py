from 逻辑门与门电路.双输入门.NandGate import NandGate
from 逻辑门与门电路.双输入门.AndGate import AndGate
from 逻辑门与门电路.双输入门.NorGate import NorGate
from 逻辑门与门电路.逻辑连接.Connect import Connect


if __name__ == '__main__':
    g1 = AndGate('G1')
    g2 = AndGate("G2")
    g3 = NorGate("G3")
    c1 = Connect(g1, g3)
    c2 = Connect(g2, g3)

    f1 = NandGate('F1')
    f2 = NandGate("F2")
    f3 = AndGate('F3')
    c3 = Connect(f1, f3)
    c4 = Connect(f2, f3)

    print(g3.get_output())
    print()
    print(f3.get_output())