from setuptools import setup, find_packages

setup(
    name='pyqt-bounding-box',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt bounding box for graphic design software',
    url='https://github.com/yjg30737/pyqt-bounding-box.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)