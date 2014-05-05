
#-*- encoding utf-8 -*-
from osv import osv,fields

class directores (osv.model):
	_name='gid.cine.directores'

	_columns={

		'name':fields.char('Nombre',required=true,size=200),
		 'Nacionalidad':fields.char('Nacionalidad',required=true,size=100),


	}