#-*- encoding utf-8 -*-
from osv import osv,fields

class pelicula  (osv.model)

Genero[
('Accion','Accion')
('Terror', 'Terror')
('Comedia','Comedia')
('ciencia ficcion','ciencia ficcion')
('suspenso','suspenso')
('infantil','infantil')
]

_name = 'gid.cine.pelicula'

_columns = {
	'name': fields.char('Nombre',required=true,size=200),
	'duracion': fields.char('Duracion',required=true,size=100),
	'Genero':fields.selection(Genero,'Generos cinematrograficos'),
	'sinopsis':fields.text('Sinopsis',required=true,size=300),
	'imagen': fields.binary(String='imagen', filters='*.png,*jpeg'), 

}
