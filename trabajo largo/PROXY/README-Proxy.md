# PROXY
>Es un patrón de diseño el cual facilita un sustituto para otro objeto, en pocas palabras el proxy se encarga de controlar el acceso al objeto original, facilitando al objeto el poder hacer algo tanto antes como después de que la solicitud llegue al objeto original.
>Plaxy se puede utilizar en diversas ocasiones como por ejemplo: Cuando tengo un objeto el cual utiliza demasiados recursos del sistema debido a su constante funcionamiento, sin importar que se necesite pocas veces.
>Su estructuración se basa en: La interfaz de servicio, que es la interfaz que el proxy debe seguir para que este pueda encubrirse como si fuera un objeto de servicio.
Luego viene el servicio, que es la clase que proporciona la lógica del negocio útil.
>Después está la clase proxy que al finalizar su proceso genera una solicitud al objeto de servicio.
>Y por último el cliente, el cual funciona con ayuda de los servicios y proxies mediante una misma interfaz, generando así que se pueda pasar el proxy a cualquier código que espere a un objeto de servicio.
>image.png