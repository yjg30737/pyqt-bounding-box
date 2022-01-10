import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SelectionBox(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.__resizeEnabled = False
        self.__line_width = 3

        self.__top = False
        self.__bottom = False
        self.__left = False
        self.__right = False

        self.__default_width = 200.0
        self.__default_height = 200.0

        self.__min_width = 30
        self.__min_height = 30

        self.__cursor = QCursor()
        self.__initUi()

    def __initUi(self):
        self.setAcceptHoverEvents(True)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        self.__setStyleOfSelectionBox()

    def __setStyleOfSelectionBox(self):
        pen = QPen()
        pen.setStyle(Qt.DashLine)
        pen.setWidth(self.__line_width)
        self.setRect(QRectF(0.0, 0.0, self.__default_width, self.__default_height))
        self.setPen(pen)

    def setSizeCursor(self, p):
        # allow mouse cursor to change shape for scale more easily
        rect = self.rect()
        rect.setX(self.rect().x()+self.__line_width)
        rect.setY(self.rect().y()+self.__line_width)
        rect.setWidth(self.rect().width()-self.__line_width*2)
        rect.setHeight(self.rect().height()-self.__line_width*2)

        if rect.contains(p):
            # move
            self.setFlags(self.flags() | QGraphicsItem.ItemIsMovable)
            self.__cursor.setShape(Qt.SizeAllCursor)
            self.setCursor(self.__cursor)
            self.__cursor = self.cursor()
            self.__resizeEnabled = False

            self.__top = False
            self.__bottom = False
            self.__right = False
            self.__left = False
        else:
            # scale
            x = p.x()
            y = p.y()
            def setResizeEnabled():
                self.setFlags(self.flags() & ~QGraphicsItem.ItemIsMovable)
                self.setCursor(self.__cursor)
                self.__resizeEnabled = True

            x1 = self.rect().x()
            y1 = self.rect().y()
            x2 = self.rect().width()
            y2 = self.rect().height()

            # Top left
            if abs(x-x1) <= self.__line_width and abs(y-y1) <= self.__line_width:
                self.__cursor.setShape(Qt.SizeFDiagCursor)
                self.__top = True
                self.__left = True
                self.__bottom = False
                self.__right = False
                setResizeEnabled()

            # Top right
            elif abs(x-(x2+x1)) <= self.__line_width and abs(y-y1) <= self.__line_width:
                self.__cursor.setShape(Qt.SizeBDiagCursor)
                self.__top = True
                self.__right = True
                self.__bottom = False
                self.__left = False
                setResizeEnabled()

            # Bottom left
            elif abs(x-x1) <= self.__line_width and abs(y-(y2+y1)) <= self.__line_width:
                self.__cursor.setShape(Qt.SizeBDiagCursor)
                self.__bottom = True
                self.__left = True
                self.__top = False
                self.__right = False
                setResizeEnabled()

            # Bottom right
            elif abs(x-(x2+x1)) <= self.__line_width and abs(y-(y2+y1)) <= self.__line_width:
                self.__cursor.setShape(Qt.SizeFDiagCursor)
                self.__bottom = True
                self.__right = True
                self.__top = False
                self.__left = False
                setResizeEnabled()

            # Top
            elif abs(y-y1) <= self.__line_width:
                self.__top = True
                self.__right = False
                self.__left = False
                self.__bottom = False
                self.__cursor.setShape(Qt.SizeVerCursor)
                setResizeEnabled()

            # Bottom
            elif abs(y-(y2+y1)) <= self.__line_width:
                self.__bottom = True
                self.__right = False
                self.__left = False
                self.__top = False
                self.__cursor.setShape(Qt.SizeVerCursor)
                setResizeEnabled()

            # Left
            elif abs(x-x1) <= self.__line_width:
                self.__left = True
                self.__right = False
                self.__top = False
                self.__bottom = False
                self.__cursor.setShape(Qt.SizeHorCursor)
                setResizeEnabled()

            # Right
            elif abs(x-(x2+x1)) <= self.__line_width:
                self.__right = True
                self.__left = False
                self.__top = False
                self.__bottom = False
                self.__cursor.setShape(Qt.SizeHorCursor)
                setResizeEnabled()

    def mouseMoveEvent(self, e):
        if self.__resizeEnabled:
            rect = self.rect()
            p = e.pos()
            x = p.x()
            y = p.y()
            if self.__cursor.shape() == Qt.SizeHorCursor:
                if self.__left and rect.right()-x > self.__min_width:
                    rect.setLeft(x)
                elif self.__right and x > 30:
                    rect.setRight(x)
            elif self.__cursor.shape() == Qt.SizeVerCursor:
                if self.__top and rect.bottom()-y > self.__min_height:
                    rect.setTop(y)
                elif self.__bottom and y > self.__min_height:
                    rect.setBottom(y)
            elif self.__cursor.shape() == Qt.SizeBDiagCursor:
                if self.__top and self.__right and x > self.__min_width and rect.bottom()-y > self.__min_height:
                    rect.setTopRight(QPoint(x, y))
                elif self.__bottom and self.__left and rect.right()-x > self.__min_width and y > self.__min_height:
                    rect.setBottomLeft(QPoint(x, y))
            elif self.__cursor.shape() == Qt.SizeFDiagCursor:
                if self.__top and self.__left and rect.right()-x > self.__min_width and rect.bottom()-y > self.__min_height:
                    rect.setTopLeft(QPoint(x, y))
                elif self.__bottom and self.__right and x > self.__min_width and y > self.__min_height:
                    rect.setBottomRight(QPoint(x, y))

            self.setRect(rect)

        return super().mouseMoveEvent(e)

    def hoverMoveEvent(self, e):
        p = e.pos()

        if self.boundingRect().contains(p) or self.rect().contains(p):
            self.setSizeCursor(p)

        return super().hoverMoveEvent(e)

    # moving with arrow keys
    def keyPressEvent(self, e):
        tr = self.transform()
        if e.key() == Qt.Key_Up:
            tr.translate(0, -1)
        if e.key() == Qt.Key_Down:
            tr.translate(0, 1)
        if e.key() == Qt.Key_Left:
            tr.translate(-1, 0)
        if e.key() == Qt.Key_Right:
            tr.translate(1, 0)
        self.setTransform(tr)
        return super().keyPressEvent(e)

    def setLineWidth(self, n: int):
        self.__line_width = n
        self.__setStyleOfSelectionBox()