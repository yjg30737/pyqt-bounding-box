# pyqt-selection-box
PyQt selection box for QGraphicsView

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-selection-box.git --upgrade```

## Feature
* Cursor shape changes properly for position (horizontal/vertical edge, etc.)
* Being able to resize horizontally/vertically/diagonally 
* Being able to move
* Being able to change the line width with ```setLineWidth(n: int)```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QGraphicsView, QVBoxLayout, QApplication, QGraphicsScene

from pyqt_selection_box.selectionBox import SelectionBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        view = QGraphicsView()
        self.__scene = QGraphicsScene()
        self.__scene.setSceneRect(0, 0, 400, 400)

        item = SelectionBox()
        # item.setLineWidth(8) If you want to change the edge line width, add the code.
        self.__scene.addItem(item)
        view.setScene(self.__scene)

        lay = QVBoxLayout()
        lay.addWidget(view)

        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = Example()
    example.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/148708740-cd1f0765-7768-44b6-88bb-770e2d34fe12.mp4

## Note
```SelectionBox``` class inherits ```QGraphicsRectItem```.

Default line width value is 3.
