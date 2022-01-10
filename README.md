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

https://user-images.githubusercontent.com/55078043/148641700-1a2994a9-c536-40b1-a6c0-575c2ca9be76.mp4

## Note
```SelectionBox``` class inherits ```QGraphicsRectItem```.

