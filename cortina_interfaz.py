import sys
import numpy as np
import serial
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QDialog , QApplication
from PyQt5.uic import loadUi
import pygame
import time

estado=0
delay = 250
mensaje="$RA,1,D"
subir="S"
bajar="B"
detener="D"

class tehseencode(QMainWindow):
	def __init__(self):
		global uart
		super(tehseencode,self).__init__()
		loadUi("cortina.ui", self)
		#self.setStyleSheet("background-color: black;")
		self.statusBar().showMessage("Bienvenid@")
		#self.showMaximized()
		self.show()
		self.setWindowTitle("cortina")

		self.subir_but.clicked.connect(self.subir)
		self.bajar_but.clicked.connect(self.bajar)
		self.detener_but.clicked.connect(self.detener)

		self.conect_label.setText('CONECTANDO')
		# self.conect_label.setStyleSheet("background-color: rgb(243, 244, 169); color: black")
		self.conect_label.setFont(QFont('Arial', 16))
		#self.SHOW.clicked.connect(self.onClicked)
		#self.CAPTURE.clicked.connect(self.CaptureClicked)

		uart = serial.Serial("COM10", 9600)
		self.cortina()
	@pyqtSlot()
	def cortina(self):
		global uart, detener, subir, bajar, estado, send, mensaje
		####### Initialise the pygame library #######
		#############################
		self.conect_label.setText('CONECTADO')
		count=0
		while True:
			try:
				if estado==0:
					mensaje="$RA,1,3\r\n"
				if estado==1:
					mensaje = "$RA,1,1\r\n"
				if estado==2:
					mensaje = "$RA,1,0\r\n"
				uart.write(str.encode(mensaje))
				print(mensaje)
				self.send_listWidget.addItem(mensaje[0:7])
				if count >6:
					count=0
					#self.send_listWidget.takeItem(1)
					self.send_listWidget.clear()
				loop = QEventLoop()
				QTimer.singleShot(delay, loop.quit)
				loop.exec_()
			except:
				print("error")
	def subir(self):
		global estado
		print("subir")
		estado=1
	def bajar(self):
		global estado
		print("bajar")
		estado = 2

	def detener(self):
		global estado
		print("detener")
		estado = 0


app =  QApplication(sys.argv)
window=tehseencode()
window.show()
#window.showFullScreen() #showFullScreen()

try:
	sys.exit(app.exec_())
except:
	print('excitng')
