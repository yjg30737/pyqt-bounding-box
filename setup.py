from setuptools import setup, find_packages

setup(
    name='pyqt-selection-box',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt selection box for QGraphicsView',
    url='https://github.com/yjg30737/pyqt-selection-box.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)