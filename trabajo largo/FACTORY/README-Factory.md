# FACTORY
>Es un patrón de diseño el cual facilita una interfaz que permite crear objetos en superclases, y a la vez le permite a estas alterar el tipo de objetos que se van a crear.
>Su estructuración se basa en: el producto que es el que declara la interfaz.
>Los productos concretos lo cual se refiere a las diversas implementaciones de la interfaz del producto.
>La clase (creadora) que se encarga de declarar el método de fábrica que devuelve los datos nuevos del producto.
>Los creadores concretos son los que se encargan de sobrescribir el Factory para que se pueda retornar un producto con (tipo) diferente. 
>image.png