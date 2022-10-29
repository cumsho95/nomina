# MEMENTO
>Es una patrón de diseño que permite guardar y restaurar estados previos de un objeto sin que se revelen sus detalles de implementación.
>Su estructura es la siguiente: La clase originadora, la cual tiene la capacidad de producir instantáneas del propio estado al igual que restaurar el mismo si es necesario con ayuda de instantáneas.
>El memento el cual es un objeto que actúa como una instantánea del estado original.
>La cuidadora, esta contiene la información de cuándo y por qué debería restaurarse el estado original.
>Y por último se lleva a cabo la implementación, entonces primero la clase de memento tiene que anidarse dentro de la original permitiéndole a ésta acceder a campos y métodos de la clase de memento, permitiendo que la cuidadora tenga un acceso limitado a estos campos y métodos lo que a su vez permite el almacenar mementos en una pila sin alterar su estado.
>Este patrón es utilizado cuando se quiere generar instantáneas del estado actual del objeto para así poder generar una restauración del estado previo del objeto.
>image.png