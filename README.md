# Proyecto Devops Semana 1 Grupo FOURBIDDEN

## Descripción
Una compañía multinacional está interesada en mejorar su proceso de gestión de listas negras de emails dado que en los últimos años ha recibido varias demandas y problemas legales por la mala gestión de sus listas negras de emails en los cientos de aplicaciones que utiliza para su día a día. Para lo anterior la compañía ha decidido que un equipo centralizado despliegue la primera versión de un nuevo microservicio que permita gestionar la lista negra global de la empresa. El objetivo de este microservicio es que cientos de sistemas internos puedan consultar si un email está en la lista negra global de la empresa o no, así como agregar emails a la lista negra global.

Para  realizar  la  implementación  inicial  del  microservicio,  es  necesario  desarrollar  las  siguientes actividades:

1.(45%)Desarrollar y exponer un servicio REST (POST) para agregar un email a la lista negra global. Este servicio permite agregar un email a la lista negra global. Para agregar un email a la lista negra global se necesita: el email del cliente a agregar a la lista negra global, el id de  la  app  cliente  (es  un  UUID  obligatorio),  el motivo  por  el  que  se  agrega  a  la  lista  negra (campo opcional de máximo 255 caracteres). Internamente el microservicio debe guardar la  dirección  IP  desde  donde  se  hace  la  solicitud  y  la  fecha/hora  en  la  que  se  realiza  la solicitud.

2.(25%) Desarrollar y exponer un servicio REST (GET) para consultar si un email está en la lista negra global o no. Este microservicio recibe como parámetro el email del cliente y retorna si ese email está en la lista negra global o no.

## Definición API REST
https://documenter.getpostman.com/view/5687446/UVyysCSn
