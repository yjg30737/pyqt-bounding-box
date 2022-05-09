from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SelectionBox(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.__resizeEnabled = False
        self.__line_width = 3

        self.__default_width = 200.0
        self.__default_height = 200.0

        self.__min_width = 30
        self.__min_height = 30

        self.__cursor = QCursor()

        self.__initPosition()
        self.__initUi()

    def __initUi(self):
        self.setAcceptHoverEvents(True)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        self.__setStyleOfSelectionBox()

    # init the edge direction for set correct reshape cursor based on it
    def __initPosition(self):
        self.__top = False
        self.__bottom = False
        self.__left = False
        self.__right = False

    def __setStyleOfSelectionBox(self):
        pen = QPen()
        pen.setStyle(Qt.DashLine)
        pen.setWidth(self.__line_width)
        self.setRect(QRectF(0.0, 0.0, self.__default_width, self.__default_height))
        self.setPen(pen)

    def __setCursorShapeForCurrentPoint(self, p):
        # allow mouse cursor to change shape for scale more easily
        rect = self.rect()
        rect.setX(self.rect().x() + self.__line_width)
        rect.setY(self.rect().y() + self.__line_width)
        rect.setWidth(self.rect().width() - self.__line_width * 2)
        rect.setHeight(self.rect().height() - self.__line_width * 2)

        if rect.contains(p):
            # move
            self.setFlags(self.flags() | QGraphicsItem.ItemIsMovable)
            self.__cursor.setShape(Qt.SizeAllCursor)
            self.setCursor(self.__cursor)
            self.__cursor = self.cursor()
            self.__resizeEnabled = False
            self.__initPosition()
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

            self.__left = abs(x - x1) <= self.__line_width  # if mouse cursor is at the almost far left
            self.__top = abs(y - y1) <= self.__line_width  # far top
            self.__right = abs(x - (x2 + x1)) <= self.__line_width  # far right
            self.__bottom = abs(y - (y2 + y1)) <= self.__line_width  # far bottom

            # set the cursor shape based on flag above
            if self.__top or self.__left or self.__bottom or self.__right:
                if self.__top and self.__left:
                    self.__cursor.setShape(Qt.SizeFDiagCursor)
                elif self.__top and self.__right:
                    self.__cursor.setShape(Qt.SizeBDiagCursor)
                elif self.__bottom and self.__left:
                    self.__cursor.setShape(Qt.SizeBDiagCursor)
                elif self.__bottom and self.__right:
                    self.__cursor.setShape(Qt.SizeFDiagCursor)
                elif self.__left:
                    self.__cursor.setShape(Qt.SizeHorCursor)
                elif self.__top:
                    self.__cursor.setShape(Qt.SizeVerCursor)
                elif self.__right:
                    self.__cursor.setShape(Qt.SizeHorCursor)
                elif self.__bottom:
                    self.__cursor.setShape(Qt.SizeVerCursor)
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
                    rect.setTopRight(p)
                elif self.__bottom and self.__left and rect.right()-x > self.__min_width and y > self.__min_height:
                    rect.setBottomLeft(p)
            elif self.__cursor.shape() == Qt.SizeFDiagCursor:
                if self.__top and self.__left and rect.right()-x > self.__min_width and rect.bottom()-y > self.__min_height:
                    rect.setTopLeft(p)
                elif self.__bottom and self.__right and x > self.__min_width and y > self.__min_height:
                    rect.setBottomRight(p)

            self.setRect(rect)

        return super().mouseMoveEvent(e)

    def hoverMoveEvent(self, e):
        p = e.pos()

        if self.boundingRect().contains(p) or self.rect().contains(p):
            self.__setCursorShapeForCurrentPoint(p)

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