import pyglet
from math import cos, sin
from time import sleep
win = pyglet.window.Window(fullscreen=False,resizable=True,caption='Pendulo')

global alpha, valpha, g, counter
g = -9.8
alpha = 1.57
valpha = 0
counter = 0
pendulum = pyglet.shapes.Circle(100*sin(alpha)+win.width/2,win.height-150-100*cos(alpha),10)
cord = pyglet.shapes.Line(win.width/2,win.height-150,pendulum.x,pendulum.y)
def update(dt):
	global alpha, valpha, counter
	if counter <= 2:
		counter +=1
		# print(alpha,',', valpha)
		# print(dt)
		return 0
	# Las formulas (como voy a tratar valores pequeños, y asumir que la longitud de la cuerda es 1, la velocidad angular se asume que es igual a la velocidad)
	alpha += valpha*dt
	# La posicion cambia por la velocidad * el tiempo entre cada instante simulado
	valpha += sin(alpha)*g*dt
	valpha *= 1-0.034*valpha**2*dt/abs(valpha) 

	# valpha_f = valpha_0 - cte*vaplha_0**3*dt/abs(valpha_0) => valpha_f = valpha_0*(1 - cte*vaplha_0**2*dt/abs(valpha_0))
	# => para modificar correctamente valpha: valpha *= 1- cte*valpha**2*dt/abs(valpha)

	# cte. = densidad aire * coeficiente de rozamiento (de esfera en este caso) * area de seccion del objeto * 1/2 = 
	# cte. = 1.1839        * 0.47                                               * 3.14*0.2**2                * 0.5 =~0.035 (El radio se asume que es 0.2 (Y que es una esfera))

	pendulum.x = 100*sin(alpha)+win.width/2
	pendulum.y = win.height-150-100*cos(alpha)
	cord.x = win.width/2
	cord.y = win.height-150
	cord.x2 = pendulum.x
	cord.y2 = pendulum.y



pyglet.clock.schedule_interval(update,1/60)

@win.event
def on_key_press(symbol, modifiers):
	#Al presionar las teclas, la velocidad se modifica
	global valpha
	if symbol==pyglet.window.key.D:
		valpha += 2
	elif symbol == pyglet.window.key.A:
		valpha -= 2


@win.event
def on_draw():
	win.clear()
	cord.draw()
	pendulum.draw()

pyglet.app.run()