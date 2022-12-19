# pyqt-bounding-box
PyQt bounding box for graphic design software

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-bounding-box`

## Feature
* Cursor shape changes properly for position (horizontal/vertical edge, etc.)
* Being able to resize the box horizontally/vertically/diagonally 
* Being able to move the box with either mouse cursor or arrow keys
* Being able to change the attribute of the box

## Methods Overview
* setLineWidth(self, n: int) - Default width is 3
* setColor(self, color: QColor) - Default color is black
* setStyle(self, style: Qt.PenStyle) - Default style is Qt.DashLine (You can see more about this style in <a href="https://doc.qt.io/qt-6/qt.html#PenStyle-enum">here</a>)

## Example
Code Sample

```python
from PyQt5.QtWidgets import QWidget, QGraphicsView, QVBoxLayout, QApplication, QGraphicsScene

from pyqt_bounding_box.boundingBox import BoundingBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        view = QGraphicsView()
        self.__scene = QGraphicsScene()
        self.__scene.setSceneRect(0, 0, 400, 400)

        item = BoundingBox()
        # item.setLineWidth(8) If you want to change the edge line width, add the code.
        # item.setColor(QColor(255, 255, 255)) If you want to change the color of the line to white, add the code.
        # item.setStyle(Qt.SolidLine) If you want to change the style of line from dashed to solid line, add the code.
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

## See Also
* <a href="https://github.com/yjg30737/pyqt-hbounding-box.git">pyqt-hbounding-box</a>
* <a href="https://github.com/yjg30737/pyqt-vbounding-box.git">pyqt-vbounding-box</a>
