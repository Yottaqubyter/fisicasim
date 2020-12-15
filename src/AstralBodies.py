from stdprojectlib import *
import sys
from os import system as cmd
try:
	import pyglet as pg
	import jstyleson as json
except ModuleNotFoundError:
	_ = cmd("pip install pyglet")
	_ = cmd("pip install jstyleson")
	import pyglet as pg
	import jstyleson as json

try:
	config_file = open(sys.argv[1], 'r')
except IndexError as err:
	print("Uso: astralBodies.exe config_file.json\n")
	# config = open(input("Introduce la dirección del archivo de configuración: "),'r')
else:
	config = json.load(config_file)
	config_file.close()
	win = pg.window.Window(fullscreen=True,caption='Gravitacion')
	wdata = vector(win.width/2, win.height/2)
	d_wdata = +null_vector
	# coord = [
	# vector(-20,0),
	# vector(0,195),
	# vector(0,200),
	# vector(20,0),
	# vector(30,0),
	# ]
	# vel = [
	# vector(0,-20),
	# vector(25,0),
	# vector(20,0),
	# vector(0,20),
	# vector(0,80),
	# ]
	# mass=(4000000,1,10000,4000000,1)
	# pgSpace = [
	# pg.shapes.Circle(0,0,20),
	# pg.shapes.Circle(0,0,4),
	# pg.shapes.Circle(0,0,7),
	# pg.shapes.Circle(0,0,20),
	# pg.shapes.Circle(0,0,4),
	# ]

	astralSpace = []
	# tempSpace = []
	pygletSpace = []
	for c in config:
		pygletSpace += [pg.shapes.Circle(0,0,c["radio"]*3)]
		astralSpace += [astralBody(c["masa"], astralSpace, vector(*c["posicion"]), vector(*c["velocidad"]))]
	# tempSpace = [
	# 	astralBody(
	# 		pg.shapes.Circle(0,0,c["radio"]),
	# 		wdata,
	# 		c["masa"],
	# 		astralSpace,
	# 		vector(c["posicion"][0],c["posicion"][1]),
	# 		vector(c["velocidad"][0],c["velocidad"][1]))
	# 		 for c in config]

	# astralSpace += tempSpace
	# del tempSpace

	counter = 0

	def update(dt):
		global astralSpace, counter, wdata, d_wdata, pygletSpace
		if counter<=2:
			counter+=1
			return None
		for b in astralSpace:
			b.update(dt)
		wdata += d_wdata
		for pygletBody, astralBody in zip(pygletSpace,astralSpace):
			pygletBody.x = astralBody.get_dnr_dtn(0).x*3 + wdata.x
			pygletBody.y = astralBody.get_dnr_dtn(0).y*3 + wdata.y

	pg.clock.schedule_interval(update,1/60)


	@win.event
	def on_key_release(symbol, modifiers):
		d_wdata.x = 0
		d_wdata.y = 0

	@win.event
	def on_key_press(symbol, modifiers): # Añadir soporte para salir de pantalla completa (Y para zoom)
		if pg.window.key.UP==symbol:
			d_wdata.y = -10
		if pg.window.key.DOWN==symbol:
			d_wdata.y =  10
		if pg.window.key.LEFT==symbol:
			d_wdata.x =  10
		if pg.window.key.RIGHT==symbol:
			d_wdata.x = -10

	@win.event
	def on_draw():
		win.clear()
		for pygletBody in pygletSpace:
			pygletBody.draw()
	pg.app.run()