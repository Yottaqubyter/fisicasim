# Fisicasim

Estas son algunas simulaciones fisicas que he ido haciendo y haré en mi tiempo libre. 

Puedes descargar los binarios desde [este enlace](https://github.com/Yottaqubyter/fisicasim/releases).

## Pendulo
Esta simulacion controla un pendulo cualquiera (se asume masa=1 y longitud de cuerda igual), dejandote empujarlo con las teclas A y D.
<!-- Incluir imagen más tarde-->

### Formulas

Añadir más tarde.
<!-- Incluir mas tarde -->

## Gravedad
Esta simulacion esta en pantalla completa, y usa los datos de un archivo de configuración json (Admite comentarios) para calcular la posicion inicial y movimiento de cuerpos por la fuerza de la gravedad.
<!-- Incluir imagen más tarde 
![Formula euler](https://render.githubusercontent.com/render/math?math=e^{i\pi}=-1)
Este es el formato para usar latex (Si hay algún espacio en la formula, sustituirlo con un %20)
-->

Puedes moverte por el sistema usando las teclas de dirección

### Sintaxis del archivo de configuracion

```json
[
    /*
    Se pueden usar comentarios así
    */

    // O así

    {
        "masa":1000, 
        // Las unidades de masa equivalen a 10^12 kg
        "posicion":[1,4],
        // Las unidades de distancia son km
        "velocidad":[5,0],
        // Las unidades de velocidad son km/hora
        "radio":4
    },
    {···},
    {···}
] 
```

### Fórmulas

Añadir más tarde