# STRATEGY
>Es un patrón de diseño el cual permite definir a una familia de algoritmos, facilitando la distribución de estos en una clase separada para poder generar los unos objetos intercambiables.
>Su estructuración es: La clase contexto, esta clase es la que sostiene una referencia para una de las estrategias concretas para que solo se pueda comunicar con ese objeto por medio de la interfaz de estrategia.
>La interfaz estrategia, esta puede declarar un método que utiliza la clase contexto para poder ejecutar una estrategia.
>Las estrategias concretas. Son las que implementan diversas variaciones de un algoritmo el cual es utilizado por la clase contexto.
>Y el cliente, el cual se encarga de crear un objeto de estrategia para luego pasarlo a la clase de contexto par que así la clase contexto pueda utilizar un modificador (set) el cual le va a permitir a los clientes reemplazar la estrategia que está asociada al contexto (esto durante el proceso de ejecución).
>image.png