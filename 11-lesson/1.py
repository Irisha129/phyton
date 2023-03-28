# sys - модуль, который обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(300,300)
#     w.setWindowTitle("Hello World")
#     w.show()
#     sys.exit(app.exec_())

# ________________________________________
import sys
from PyQt5.QtWidgets import *
if __name__ == '__main__':
    app = QApplication([])
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("QboxLayout")

    btn1 = QPushButton("Bird")
    btn2 = QPushButton("Animal")
    btn3 = QPushButton("Fish")
    hbox = QVBoxLayout(w)

    hbox.addWidget(btn1)
    hbox.addWidget(btn2)
    hbox.addWidget(btn3)

    w.show()
    sys.exit(app.exec_())


# ________________________
# import numpy as np
# n1 = np.array([1,2,3,4,5])
# n2 = n1 + 2
# print(n2)
