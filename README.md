# Fisicasim

Estas son algunas simulaciones físicas que he ido haciendo y haré en mi tiempo libre. 

Puedes descargar los binarios desde [este enlace](https://github.com/Yottaqubyter/fisicasim/releases).

---
<br>
Todas las simulaciones funcionan calculando la aceleración de los objetos (Según el código que he escrito).

La velocidad y posiciones en el siguiente instante se calculan de esta manera:

><img src="https://render.githubusercontent.com/render/math?math=v_f%20=v_0+%2B+a\,dt">

><img src="https://render.githubusercontent.com/render/math?math=r_f%20=r_0+%2B+v\,dt">

<br>

Donde:

- <img src="https://render.githubusercontent.com/render/math?math=r_f"> y <img src="https://render.githubusercontent.com/render/math?math=v_f"> es la posición y velocidad en el instante simulado actual, mientras que <img src="https://render.githubusercontent.com/render/math?math=r_0"> y <img src="https://render.githubusercontent.com/render/math?math=v_0"> son sus respectivos en el previo instante simulado.

- <img src="https://render.githubusercontent.com/render/math?math=dt"> es el tiempo transcurrido entre iteraciones de la simulación (Entorno a 0.0167 segundos)

<br>

## Péndulo

Esta simulación controla un péndulo cualquiera (se asume masa=1 y longitud de cuerda igual), dejandote empujarlo con las teclas A y D.
<!-- Incluir imagen más tarde-->

### Formulas

Todavía no he incluido la explicación, aunque cabe notar que hago algunas cosas un poco extrañas para simplificar las ecuaciones.

</br>

## Gravedad
Esta simulación esta en pantalla completa, y usa los datos de un archivo de configuración json (Admite comentarios) para calcular la posición inicial y movimiento de cuerpos por la fuerza de la gravedad.
<!-- Incluir imagen más tarde 
![Formula euler](https://render.githubusercontent.com/render/math?math=e^{i\pi}=-1)
Este es el formato para usar latex (Si hay algún espacio en la formula, sustituirlo con un %20)
-->

Puedes moverte por el sistema usando las teclas de dirección

### Sintaxis del archivo de configuración

Esta información se escribe en el archivo AstralBodies.json, en config.

**Las unidades incluidas aquí no están implementadas en los binarios. Si quieres usar unidades reales, puedes usar las unidades del sistema internacional, pero para la masa tener en cuenta que 1 unidad de masa = 10^9/6.674 kg (Estará solucionado en la próxima actualización)**

**Además, la lista que hay en "grupo", es la que se usa como archivo de configuración en los binarios actuales**

```javascript
    /*
    Se pueden usar comentarios así
    */


    // O así

{
    "G":0.8649504 // Parametro opcional, para modificar la constante gravitacional. Por defecto 0.8649504 (En km^3/(Gt*h^2) )
    "grupo":[
        {
            "masa":1000, 
            // Las unidades de masa equivalen a 10^12 kg
            "posicion":[1,4],
            // Las unidades de distancia son km
            "velocidad":[5,0],
            // Las unidades de velocidad son km/hora
            "radio":4
            // El radio es algo puramente estético
        },
        {···},
        {···}]
} 
```

Las unidades que se muestran son las que se usan con la constante gravitacional que ya hay por defecto.

### Fórmulas

La ecuación para la aceleración de un cuerpo m es esta:

><img src="https://render.githubusercontent.com/render/math?math=a_m = G' \, \sum_{k=0}^{n} {\frac{\overrightarrow{AP_k}\,m_k}{\left|\overrightarrow{AP_k}\right|^3}}">

Donde:

- <img src="https://render.githubusercontent.com/render/math?math=n"> es el número de cuerpos en el espacio sin contar el propio
- <img src="https://render.githubusercontent.com/render/math?math=A"> es la posición del cuerpo propio y <img src="https://render.githubusercontent.com/render/math?math=P_k"> es la del otro cuerpo
-  <img src="https://render.githubusercontent.com/render/math?math=m_k"> es la masa del otro cuerpo
- <img src="https://render.githubusercontent.com/render/math?math=G'\, \frac{km^3}{Gt\,h^2}=G \, \frac{m^3}{kg\,s^2} \, \frac{10^12 \cdot 3600^2}{1000^3}"> es una simple conversión de unidades. No he usado la constante real porque era muy pequeña, y no creía que el ordenador pudiera manejar algo así (De todas formas, los cuerpos gravitatorios tienen mucha masa y se encuentran a mucha distancia entre sí, así que tampoco era muy necesario usar la constante real). Planeo incluir la posibilidad de cambiar la constante en el archivo de configuración en la próxima actualización.
