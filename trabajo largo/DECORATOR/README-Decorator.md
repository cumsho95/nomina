# DECORATOR
>Es un patrón de diseño el cual permite añadir unas funcionalidades dentro de unos objetos los cuales estarán dentro de otros objetos encapsulados especiales, los cuales contienen a su vez estas funcionalidades.
>Su estructuración es la siguiente: El componente, que se encarga de declarar una interfaz común para wrappers y objetos.
>El componente concreto, el cual se compone por una serie de objetos envueltos, y este define el comportamiento básico, que los decoradores pueden alterar.
>La clase (Decorada-base), esta cuenta con un campo definido para poder referenciar un objeto envuelto, este tipo de campo se declara como una interfaz del componente para que así esta pueda contener los decoradores y los componentes. Esta clase puede delegar las operaciones de un objeto envuelto.
>Luego vienen los Decoradores concretos, los cuales definen las funcionalidades adicionales que se permiten agregar de manera dinámica a los componentes, estos decoradores sobreescriben métodos y ejecutan su comportamiento.
>y por último el cliente, que es el que tiene la posibilidad de envolver los componentes en varias capas de decoradores, con la condición de que en todo momento se trabaje con todos los objetos a través de la interfaz denominada del componente.
>image.png