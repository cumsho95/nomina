# OBSERVER
>Es un patrón de diseño que permite definir dependencias de tipo (1:M) entre los objetos, generando de esta manera que si alguno de los objetos cambia su estado se notifique a todos los dependientes de este.
>Su estructura se basa en: El sujeto, el cual es el que proporciona una interfaz para poder agregar y eliminar observadores.
>El observador, que es el que define el método que utilizará el sujeto para que se puedan notificar los cambios de su estado.
>El sujeto concreto, Este mantiene un estado beneficioso para los observadores concretos y así mismo los notifica si su estado se altera.
>Y los observadores concretos, que son los que mantienen referenciado al sujeto concreto para poder implementar la interfaz de actualización, en pocas palabras guardan información de este objeto que observan para que puedan preguntar sobre algún cambio en este.
>Normalmente se utiliza cuando los cambios de estado de algún objeto necesitan cambiar a otros objetos desconocidos del grupo.
>image.png