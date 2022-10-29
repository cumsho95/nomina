# ABSTRACT FACTORY
>Es una interfaz gráfica la cual tiene como propósito agrupar un conjunto de clases las cuales tienen un funcionamiento en común que se llaman familias las cuales se crean por medio de un (Factory).  
>Se utiliza normalmente cuando en el código se emplean varias familias de productos relacionadas las cuales no queremos que dependan de las clases concretas de los productos.
>Su estructura se basa en: Primero la interfaz que se encarga de definir la estructura de los objetos que crearan las familias.
>Segundo, las clases que van a heredar el Abstract Product para que se puedan implementar las familias a objetos específicos.
>Tercero, El concrete Factory que es el que representa las creaciones específicas que servirán para poder crear todas las
instancias de clases de la familia, y por último se define la estructura de estas creaciones las cuales deberán proporcionar una método para cada una de las clases de la familia.
>image.jpg