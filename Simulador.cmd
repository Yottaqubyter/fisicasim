@echo off
rem NO USAR EL cd
rem El programa deja de funcionar bien

rem POR HACER:
rem  Que te de varias opciones de programas de simulacion a escoger
:inicio
cls
echo Para ejecutar alguno de los siguientes programas, debes introducir su numero correspondiente
echo Programas de simulacion disponibles para ejecutar:
echo 1) Pendulo
echo 2) Gravedad
echo 3) Salir
rem añadir simulador de cuerpos celestes
rem echo 
rem echo 
rem echo 

set /p input=Numero: 
if %input%==1 (
	echo Usa las teclas A y D para empujar hacia la agujas del reloj y contrario a estas, respectivamente
	pause
	python ".\src\pendulum.py"
	.\bin\pendulum.exe
	goto inicio
)
if %input%==2 (
	echo Usa las teclas de direccion para mover tu punto de vista
	echo Pulsa escape para salir
	echo Puedes editar el archivo AstralBodies.json en config para colocar tus propios cuerpos en la simulacion
	pause
	python ".\src\AstralBodies.py" ".\config\AstralBodies.json"
	.\bin\AstralBodies.exe .\config\AstralBodies.json
	goto inicio
)
if %input%==3 (
	exit
)
echo Numero Invalido
pause
goto inicio