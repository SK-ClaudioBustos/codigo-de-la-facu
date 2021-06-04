# codigo-de-la-facu
***
Este repositorio esta hecho para hacer un backup de archivos personales

* RECORDATORIO PARA PODER SUBIR ARCHIVOS(SIEMPRE SE ME OLVIDA)
  * git add <lo que queramos añadir>
  * git status (para confirmar que se añadio)
  * git commit -m "comentario"
  * git push
* EN EL CASO DE QUE NO ME DEJE 
  * git pull && git push
  * git pull master && git push origin master(segunda opcion)
***
* PARA VER LOS COMMITS
  * git log
  * git log --stat(para ver la cantidad de cambios en el archivo) 
* EN EL CASO QUE HAYA HECHO UN COMMIT ERRONEO
  * git rm --cached "nombre archivo,sin comillas" 
* PARA VIAJAR ENTRE VERSIONES DE NUESTRO PROYECTOS(ATENCION:CUANDO SE VIAJA A UNA VERSION ANTERIOR,SE PIERDE EL COMMIT OSEA LOS CAMBIOS)
  * git log --oneline(con esto obtenemos los hash de las versiones)
  * git checkout "aca va el hash de la version a la cual queremos viajar,sin comillas"
***
* RAMAS 
  * git branch(para ver ramas)   
  * git checkout "nombre rama,sin comillas"(cambiar de rama)
  * git checkout -b "nombre rama,sin comillas"(crear rama)
  * git merged "nombre rama,sin comillas"(para unir dos ramas,primero se necesita ubicar en una de las ramas y luego hacer la combinacion con la otra rama)
  * git branch -d "nombre rama,sin comillas"(eliminar rama,al eliminar una rama se envian todos sus logs a otra rama)
***
* CLONAR
  * git clone "direccion repositorio,sin comillas"(se debe situar en la carpeta de destino) 
* BORRAR
  * git rm "nombre archivo" 
  * git rm -r "nombre carpeta"(eliminar carpeta)
