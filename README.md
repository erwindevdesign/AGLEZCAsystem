# Aglezca-System :card_index:

# Sistema de gestión de datos en producción AGLEZCA S.A. de C.V. (México)

## Indice

1. [Visión general y alcances](#id1)
2. [Sistema de gestión de datos en producción AGLEZCA S.A. de C.V.](#id2)

## Visión general y alcances <a name="id1"></a>

El sistema de gestión de datos - **SGD** -, se desarrolla como metodo para en la recabación, almacenamiento y consulta de datos en busca del desarrollo de indicadores clave **(KPI´s)** y el alcance de objetivos y resultados **(OKR´s)** en funsion de la integración de la información en la toma de desiciones en un entorno de producción real.

### Fase 1

La implementación de formularios para la recabación de datos mediante macros implementadas en hojas de calculo  **VBA** (visual basic for application). Esto nos permitira crear las tablas a normailizar que posteriormente crearán la base de datos relacionando entidades y dependencias, eliminando información inecesaria para estructurar un sistema de gestión de procesos dando seguimiento a los siguientes requerimientos de gestión:

> Seguimiento de producción

	- Impresión JV33
	- impresión UV
	- corte cg-160
	- corte cama plana

> Seguimiento de consumo

	- Materiales en rollo / hoja
	- Materiales rigídos
	- consumibles
	- componentes
	- 

> Uso de  EPP

	- mascarilla-antigases 	

> Seguimiento de mantenimientos en equipos

	- Mantt. de uso 
	- residuos
	- Mantt. preventivo
	- Mantt. correctivo
	- Temp. & Hum.

SGDP (sistema de gestion de datos en produción)

Se desarrolla formularios para cada requerimiento con la siguiente nomenclatura técnica:

> Seguimiento de producción (RP: registro de producción,)

	- RP-1-v0.0.1.xlsm
	- RP-2-v0.0.1.xlsm
	- RP-3-v0.0.1.xlsm
	- RP-UV-v0.0.1.xlsm

> Seguimiento de consumo (RC: registro de consumo)

	- RC-MAT-R-v0.0.1.xlsm

> Uso de  EPP (RU: registro de uso)

	- RU-EPP-FAJA-v0.0.1.xlsm
	- RU-EPP-LENTES-v0.0.1.xlsm
	- RU-EPP-GUANTES-v0.0.1.xlsm
	- RU-EPP-MASCARILLA-v0.0.1.xlsm
	- RU-EPP-TAPONES-v0.0.1.xlsm
	- RU-EPP-CALZADO-v0.0.1.xlsm

> Seguimiento de mantenimientos en equipos (RM: registro de matenimiento)

	- RM-U-PLOT-JV33-v0.0.1.xlsm


### Sistema de gestión de datos en producción. :floppy_disk: <a name="id2"></a>

<!-- COMENTARIOS -->

#### Diagrama entidad-relación simbology

~~~sh

[ Entidad ]

[[ Entidad debil ]]

< Relación >

( Atributo )

( _Atributo Key_ )

(( Atributo Multivalue ))

( Atributo compuesto ( 1 ) ( 2 ) ( 3 ) )

{ Atributo calculado / deribado }

[ entidad ] -- < relación > -- | 1:1 | -- [ entidad ]

[ entidad ] -- < relación > --> | 1:N | --> [ entidad ]

[ entidad ] <-- < relación > --> | N:N | --> [ entidad ]

~~~

#### System diagram

~~~sh

  [ Orden de producción ] ------------- < recibe > --| 1:N |--> [ operador ]
			^					|									 ^					
   _________|__________			|					           	 ____|____
   |		|		  |			|								|		  |
( OP )    ( OC ) ( cliente )  	|						    ( firma ) ( coment )
								|
								|
								|
								|
						 [ filenameIMP ] ----------------------- < implica > -- | 1:1 | -- [ perfilColor ]	                     
								^							|									   ^
			  __________________|__________________			|					  _________________|___________________				   
  			  |		   |		|		  |   	   |		| 					  |		  |		   |         |        |
          ( name ) ( cant ) ( ancho ) ( alto ) ( largo )    |				  ( pass ) ( dir ) ( speed ) ( MAPS ) ( comp )
															|					  |_______|________|
														    |							  |
															|                       ( PerfilColor )*
															|
															|
															|
															|
															|--- < crea > -- | M:1 | -- [ NoSerie ]*	    
															|								 |
															|		 ( SKU (equipo:P1) (op:633) (client:FEM) (count:001) )
															|
															|
															|
															|
													  < requiere >
															|
															|
														 | 1:1 |
															|
															|
													  [ material ] --------------------------------- < requiere > --| 1:N |--> [ NoVale ]
													  		^									|									^
									   _____________________|_________________________		   	| 							        |	
									   |		|			|   		|			 |		   	|						 ( No. Vale de Almacen )
									( tipo ) ( base ) ( descrip1 ) ( descrip2 ) ( descrip3 )    |
																							    |
																								|
																								|
																								|--- < proviene > --| N:N |--> [ proveedor ]
																								|									 ^
																								|									 |
																								|							   ( proveedor )
																								|
																								|
																								|
																								|
																								---- < proviene > --| N:1 |--> [ lote ]
																																   ^
																																   |
																										     ( lote (index:VBB) (base:Bco) (count:001) )

~~~

#### Tables

| | VIEW |
| -- | -- |
| + | Publico |
| - | Privado |
| # | Protegido |
| / | Deribado |
| ~ | Paquete |

> estructure

| Class name |
| -- |
| Atibutes |
| Operation & methods |




| | OP | dataType |
| -- | -- | -- |
| # | id | int |
| + | op | string |
| 




#### Version


    1. [] > Versionamiento de sistema
    2. [] Documentación de sistema 
		- instructivo de uso de plataforma ASANA
    	- instructivo de uso de formularios de recabación de data
    	-  indicadores, metricas, rubricas y graficación.
    3. [] > Formularios
    

    


1. Versionamiento de sistema. :pushpin: 

    * Versionamiento de sistema ***"Alpha"*** actual. 
	> (Alapha, Beta, RC)
    * Usar la estructura de ramas en github para la gestión de versiones en prueba.
		
		* main = carpeta con versión en producción (final/respaldo), - **v1.0** -
		* develop = carpeta con versión en desarrollo (creación) - **v0.0.11** -
		* relase = carpeta con versión en depliegue para optimización y/o prueba en uso real para depuración de interfase (prueba) - **v0.1** -
		* hotfix = carpeta con versiones de arreglos de las versiones - relase - **v0.1H** -
		* features = carpeta con versiones a las cuales se les agrrega caracteristicas de las versiones - relase - main - hotfix - **v0.1F** - *Solicitadas por los usuarios*.
	* 

2. Documentación del sistema. :clipboard:

    * 
    * Documentación de sistema.* "Alpha".

3. Formularios. :speech_balloon:









> Desarrollo de sistema de gestión de datos en un ecosistema real de producción.
> Implementado en *Impresos AGLEZCA S.A. de C.V.* Cuernavaca Mor. Mexico (2022)