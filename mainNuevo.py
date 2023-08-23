import sys
from typing import Optional
from PySide6.QtCore import Qt, QDate, QAbstractTableModel
from PySide6.QtWidgets import ( QWidget, QHBoxLayout, QVBoxLayout, QStatusBar, QDateEdit, QTableView, QMainWindow, QLabel, QLineEdit, 
                               QPushButton, QTabWidget, QStackedLayout)
from PySide6.QtGui import QFont
from objetos.comunicacionNueva import Comunicacion
import pandas as pd

class TableModel( QAbstractTableModel ):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

class MainWindows( QMainWindow ):

    def window_chance( self ):
        button = self.sender()
        container_aux = QWidget()

        if button.text() == "Excel":

            container_aux.setLayout( self.stacked_layout_condominium.setCurrentIndex( 0 ) )

        elif button.text() == "Buscar Condominio": 

            self.table_name = "apartamentos"

            container_aux.setLayout( self.stacked_layout_condominium.setCurrentIndex( 1 ) )

        elif button.text() == "Editar Condominio":
            
            container_aux.setLayout( self.stacked_layout_condominium.setCurrentIndex( 2 ) )

        elif button.text() == "Eliminar Condominio":
            
            container_aux.setLayout( self.stacked_layout_condominium.setCurrentIndex( 3 ) )
        
        elif button.text() == "Agregar Servicio":
            
            container_aux.setLayout( self.stacked_layout_service.setCurrentIndex( 0 ) )
        
        elif button.text() == "Buscar Servicio":
         
            self.table_name = "bancos"
            container_aux.setLayout( self.stacked_layout_service.setCurrentIndex( 1 ) )
        
        elif button.text() == "Editar Servicio":
         
            container_aux.setLayout( self.stacked_layout_service.setCurrentIndex( 2 ) )
        
        elif button.text() == "Eliminar Servicio":
        
            container_aux.setLayout( self.stacked_layout_service.setCurrentIndex( 3 ) )
        
        elif button.text() == "Agregar Mantemiento":
        
            container_aux.setLayout( self.stacked_layout_maintenance.setCurrentIndex ( 0 ) )
        
        elif button.text() == "Buscar Mantemiento":
        
            self.table_name = "acumulados"
            container_aux.setLayout( self.stacked_layout_maintenance.setCurrentIndex ( 1 ) )
        
        elif button.text() == "Editar Mantemiento":
        
             container_aux.setLayout( self.stacked_layout_maintenance.setCurrentIndex ( 2 ) )
        
        elif button.text() == "Eliminar Mantemiento":
        
            container_aux.setLayout( self.stacked_layout_maintenance.setCurrentIndex ( 3 ) )
        
        elif button.text() == "Agregar Reparacion Menor":
        
            container_aux.setLayout( self.stacked_layout_minor_repairs.setCurrentIndex( 0 ) )
        
        elif button.text() == "Buscar Reparacion Menor":
            
            self.table_name = "transacciones_bancarias"
            container_aux.setLayout( self.stacked_layout_minor_repairs.setCurrentIndex( 1 ) )
        
        elif button.text() == "Editar Reparacion Menor":
        
            container_aux.setLayout( self.stacked_layout_minor_repairs.setCurrentIndex( 2 ) )
        
        elif button.text() == "Eliminar Reparacion Menor":
        
            container_aux.setLayout( self.stacked_layout_minor_repairs.setCurrentIndex( 3 ) )
        
        elif button.text() == "Agregar Aportes Fijos":
        
            container_aux.setLayout( self.stacked_layout_fixed_contributions.setCurrentIndex( 0 ) )
        
        elif button.text() == "Buscar Aportes Fijos":
            
            self.table_name = "cobrar1"
            container_aux.setLayout( self.stacked_layout_fixed_contributions.setCurrentIndex( 1 ) )
        
        elif button.text() == "Editar Aportes Fijos":
        
            container_aux.setLayout( self.stacked_layout_fixed_contributions.setCurrentIndex( 2 ) )
        
        elif button.text() == "Eliminar Aportes Fijos":
        
            container_aux.setLayout( self.stacked_layout_fixed_contributions.setCurrentIndex( 3 ) )
        
        elif button.text() == "Agregar Otros Gastos":
        
            container_aux.setLayout( self.stacked_layout_other_expenses.setCurrentIndex( 0 ) )
        
        elif button.text() == "Buscar Otros Gastos":

            self.table_name = "cobrar3"
            container_aux.setLayout( self.stacked_layout_other_expenses.setCurrentIndex( 1 ) )
        
        elif button.text() == "Editar Otros Gastos":
        
            container_aux.setLayout( self.stacked_layout_other_expenses.setCurrentIndex( 2 ) )
        
        elif button.text() == "Eliminar Otros Gastos":
        
            container_aux.setLayout( self.stacked_layout_other_expenses.setCurrentIndex( 3 ) )

    def build_panda_condominio( self, list ):
        
        xd = pd.DataFrame( list, columns=[ "codigo apartamento", "numero telefono", "direccion 1", "direccion 2", "tipo", "alicuota", "metros", 
                                "rif", "nombre dueño", "codigo apartamento 2", "sector", "alicuota2", "correo_electronico", "no se" ] )
        
        return xd
    
    def build_panda_servicio( self, list ):

        xd = pd.DataFrame( list, columns=[ "codigo", "nombre" ] )
        
        return xd

    def build_panda_mantenimiento( self, list ):

        xd = pd.DataFrame( list, columns=[ "fecha", "codigo_condominio", "acumulado", "tipo" ] )
        
        return xd
    
    def build_panda_repaciones_menores( self, list ):
        
        xd = pd.DataFrame( list, columns=[ "id", "numuero_cuenta", "ctnumtr", "cttipo", "fecha", "cdfeccob", "efectivo" , "cheques" , "monto" , 
                                          "nombre" , "concepto" , "estado_transaccion" , "ctcodcon" , "ctstatus" , "ctstatus2" , "ctstatus3" ] )
        
        return xd
    
    """def build_panda_aportes_fijos( self, list ):
        
        xd = pd.DataFrame( list, columns=[ "id", "codigo_apartamento", "codigo_operacion", "fecha_operacion", "fecha_vencimiento", "numero_referencia", 
                                          "monto", "saldo", "comentario", "estado", "cmint", "cmmul", "ctcue", "cmant", "ctnch", "ctfor", "ctban", 
                                          "cmsala", "ctsta2", "cttipoa", "cnidtra", "cmdesc", "cmant2" ] )
        
        return xd"""
    
    def build_panda_otros_gstos( self, list ):

        xd = pd.DataFrame( list, columns=[ "codigo_operacion", "numero_operacion", "codigo_operacion_2", "descricion_fecha", "comentario", 
                                          "codigo_condominio", "monto" ] )
        
        return xd

    def search_process( self ):
        
        list = self.conexion.buscar_datos( self.table_name )

        button = self.sender()

        list2 = []

        if button.text() == "Buscar Condominio":

            for i in list:
                if i[0] == self.condominium_name_input_search.text() :
                    list2.append(i)

            self.any_table_condominio.setModel( TableModel(  self.build_panda_condominio( list2 ) ) )
        
        elif button.text() == "Buscar Servicio":

            self.any_table_servicio.setModel( TableModel(  self.build_panda_servicio( list ) ) )
        
        elif button.text() == "Buscar Mantemiento":
            
            self.any_table_mantenimiento.setModel( TableModel(  self.build_panda_mantenimiento( list ) ) )
        
        elif button.text() == "Buscar Reparacion Menor":

            self.any_table_reparacion_menor.setModel( TableModel( self.build_panda_repaciones_menores( list ) ) )

        elif button.text() == "Buscar Otros Gastos":
           
           self.any_table_otros_gastos.setModel( TableModel( self.build_panda_otros_gstos( list ) ) )

        list2.clear()

        """elif button.text() == "Buscar Aportes Fijos":
           
            self.any_table_aportes_fijos.setModel( TableModel( self.build_panda_aportes_fijos( list ) ) )"""

    def window_condominium_tab( self ):
        
        excel_botton = QPushButton( "Excel" )
        excel_botton.clicked.connect( self.window_chance )
        
        search_botton = QPushButton( "Buscar Condominio" )
        search_botton.clicked.connect( self.window_chance )
        
        edit_botton = QPushButton( "Editar Condominio" )
        edit_botton.clicked.connect( self.window_chance )
        
        delete_botton = QPushButton( "Eliminar Condominio")
        delete_botton.clicked.connect( self.window_chance )

        bottons_group_condominium = QHBoxLayout()
        bottons_group_condominium.addWidget( excel_botton )
        bottons_group_condominium.addWidget( search_botton )
        bottons_group_condominium.addWidget( edit_botton )
        bottons_group_condominium.addWidget( delete_botton )

        #excel condominium
        titulo_principal_excel = QLabel( "Excel" )
        titulo_principal_excel.setFont( QFont( 'times new roman', 15 ) )
        titulo_principal_excel.setAlignment( Qt.AlignmentFlag.AlignCenter )

        condominium_name_label = QLabel( "Nombre de condominio" )
        condominium_name_label.setFont( QFont( 'times new roman', 13 ) )

        self.condominium_name_input = QLineEdit( self )

        condominium_fecha_label = QLabel( "Ingresa la fecha" )
        condominium_fecha_label.setFont( QFont( 'times new roman', 13 ) )
        self.date_excel = QDateEdit()
        self.date_excel.setDisplayFormat( "dd-MM-yyyy" )
        self.date_excel.setMaximumDate(
            QDate.currentDate()
        )
        self.date_excel.setCalendarPopup( True )
        self.date_excel.setDate( QDate.currentDate() )

        self.botton_search_excel = QPushButton( "Buscar" )
        
        self.botton_excel2 = QPushButton( "Generar Excel" )

        layout_H_1 = QHBoxLayout()
        layout_H_2 = QHBoxLayout()
        layout_V_1 = QVBoxLayout()

        layout_H_1.addWidget( condominium_name_label )
        layout_H_1.addWidget( self.condominium_name_input )

        layout_H_2.addWidget( condominium_fecha_label )
        layout_H_2.addWidget( self.date_excel )
        layout_H_2.addWidget( self.botton_search_excel )

        layout_V_1.addWidget( titulo_principal_excel )
        layout_V_1.addLayout( layout_H_1 )
        layout_V_1.addLayout( layout_H_2 )
        layout_V_1.addWidget( self.botton_excel2 )

        container_excel_condominium = QWidget()
        container_excel_condominium.setLayout( layout_V_1 )

        #search condominium

        titulo_principal_search = QLabel( "Buscar Condominio" )
        titulo_principal_search.setFont( QFont( 'times new roman', 15 ) )
        titulo_principal_search.setAlignment( Qt.AlignmentFlag.AlignCenter )

        condominium_name_label_search = QLabel( "Nombre de condominio" )
        condominium_name_label_search.setFont( QFont( 'times new roman', 13 ) )
        
        self.condominium_name_input_search = QLineEdit( self )
        
        self.botton_search_search = QPushButton( "Buscar Condominio" )
        self.botton_search_search.clicked.connect( self.search_process )

        layout_H_3 = QHBoxLayout()
        layout_V_2 = QVBoxLayout()

        layout_H_3.addWidget( condominium_name_label_search )
        layout_H_3.addWidget( self.condominium_name_input_search )
        layout_H_3.addWidget(  self.botton_search_search )

        layout_V_2.addWidget( titulo_principal_search )
        layout_V_2.addLayout( layout_H_3 )
        layout_V_2.addWidget( self.any_table_condominio )

        container_search_condominium = QWidget()
        container_search_condominium.setLayout( layout_V_2 )

        #edit condominium

        titulo_principal_edit = QLabel( "Editar Condominio" )
        titulo_principal_edit.setFont( QFont( 'times new roman', 15 ) )
        titulo_principal_edit.setAlignment( Qt.AlignmentFlag.AlignCenter )


        condominium_name_label_edit = QLabel( "Nombre de condominio" )
        condominium_name_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.condominium_name_input_edit = QLineEdit( self )
        
        self.botton_search_edit = QPushButton( "Buscar" )

        condominium_name_label_edit_aux = QLabel( "Nombre de condominio" )
        condominium_name_label_edit_aux.setFont( QFont( 'times new roman', 13 ) )
       
        self.condominium_name_input_edit_aux = QLineEdit( self )

        condominium_rif_label_edit = QLabel( "Rif" )
        condominium_rif_label_edit.setFont( QFont( 'times new roman', 13 ) )
       
        self.condominium_rif_input_edit = QLineEdit( self )

        self.botton_save_edit = QPushButton( "Guardar" )

        layout_H_4 = QHBoxLayout() 
        layout_H_5 = QHBoxLayout()
        layout_H_6 = QHBoxLayout()
        layout_V_3 = QVBoxLayout()

        layout_H_4.addWidget( condominium_name_label_edit )
        layout_H_4.addWidget( self.condominium_name_input_edit )
        layout_H_4.addWidget( self.botton_search_edit )

        layout_H_5.addWidget( condominium_name_label_edit_aux )
        layout_H_5.addWidget( self.condominium_name_input_edit_aux )

        layout_H_6.addWidget( condominium_rif_label_edit )
        layout_H_6.addWidget( self.condominium_rif_input_edit )

        layout_V_3.addWidget( titulo_principal_edit )
        layout_V_3.addLayout( layout_H_4 )
        layout_V_3.addLayout( layout_H_5 )
        layout_V_3.addLayout( layout_H_6 )
        layout_V_3.addWidget( self.botton_save_edit )

        container_edit_condominium = QWidget()
        container_edit_condominium.setLayout( layout_V_3 )

        #Delete condominio
        titulo_principal_delete = QLabel( "Eliminar Condominio" )
        titulo_principal_delete.setFont( QFont( 'times new roman', 15 ) )
        titulo_principal_delete.setAlignment( Qt.AlignmentFlag.AlignCenter )

        condominium_name_label_delete = QLabel( "Nombre de condominio" )
        condominium_name_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.condominium_name_input_delete = QLineEdit( self )

        self.botton_search_Delete = QPushButton( "Buscar" )

        self.botton_delete_delete = QPushButton( "Eleminar" )

        layout_H_7 = QHBoxLayout()
        layout_V_4 = QVBoxLayout()

        layout_H_7.addWidget( condominium_name_label_delete )
        layout_H_7.addWidget( self.condominium_name_input_delete )
        layout_H_7.addWidget( self.botton_search_Delete )

        layout_V_4.addWidget(  titulo_principal_delete )
        layout_V_4.addLayout( layout_H_7 )
        layout_V_4.addWidget( self.botton_delete_delete )

        container_delete_condominium = QWidget()
        container_delete_condominium.setLayout( layout_V_4 )

        #layout organization
        self.stacked_layout_condominium = QStackedLayout()
        self.stacked_layout_condominium.addWidget( container_excel_condominium )
        self.stacked_layout_condominium.addWidget( container_search_condominium )
        self.stacked_layout_condominium.addWidget( container_edit_condominium )
        self.stacked_layout_condominium.addWidget( container_delete_condominium )

        main_layout = QVBoxLayout()
        main_layout.addLayout( bottons_group_condominium )
        main_layout.addLayout( self.stacked_layout_condominium )
        
        self.condominium_container.setLayout( main_layout )

    def window_servicio_tab( self ):
        
        add_botton_service = QPushButton( "Agregar Servicio" )
        add_botton_service.clicked.connect( self.window_chance )
        
        search_botton_service = QPushButton( "Buscar Servicio" )
        search_botton_service.clicked.connect( self.window_chance )
        
        edit_botton_service = QPushButton( "Editar Servicio" )
        edit_botton_service.clicked.connect( self.window_chance )
        
        delete_botton_service = QPushButton( "Eliminar Servicio" )
        delete_botton_service.clicked.connect( self.window_chance )

        bottons_group_service = QHBoxLayout()
        bottons_group_service.addWidget( add_botton_service )
        bottons_group_service.addWidget( search_botton_service )
        bottons_group_service.addWidget( edit_botton_service )
        bottons_group_service.addWidget( delete_botton_service )

        #add service

        main_title_service_add = QLabel( "Agregar Servicio" )
        main_title_service_add.setFont( QFont( 'times new roman', 15 ) )
        main_title_service_add.setAlignment( Qt.AlignmentFlag.AlignCenter )

        service_condominium_name_label_add = QLabel( "Nombre de condominio" )
        service_condominium_name_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.service_condominium_name_input_add = QLineEdit( self )

        service_condominium_rif_label_add = QLabel( "Rif" )
        service_condominium_rif_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_rif_input_add = QLineEdit( self )

        service_date_label_add = QLabel( "Ingresa la fecha" )
        service_date_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.service_date_add = QDateEdit()
        self.service_date_add.setDisplayFormat( "dd-MM-yyyy" )
        self.service_date_add.setMaximumDate(
            QDate.currentDate()
        )
        self.service_date_add.setCalendarPopup( True )
        self.service_date_add.setDate( QDate.currentDate() )

        service_condominium_owner_label_add = QLabel( "Propietario" )
        service_condominium_owner_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_owner_input_add = QLineEdit( self )

        service_condominium_number_apartment_label_add = QLabel( "N° Apartamento" )
        service_condominium_number_apartment_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_number_apartment_input_add = QLineEdit( self )

        service_condominium_aliquot_separately_label_add = QLabel( "Alicuota Aparte" )
        service_condominium_aliquot_separately_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_aliquot_separately_input_add = QLineEdit( self )

        service_condominium_ordinary_expenses_label_add = QLabel( "Gastos Ordinarios" )
        service_condominium_ordinary_expenses_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.service_condominium_ordinary_expenses_input_add = QLineEdit( self )

        service_condominium_detail_label_add = QLabel( "Detalle" )
        service_condominium_detail_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_detail_input_add = QLineEdit( self )

        service_condominium_amount_label_add = QLabel( "Monto" )
        service_condominium_amount_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_amount_input_add = QLineEdit( self )

        self.botton_service_add_save = QPushButton( "Guardar" )

        layout_H_1 = QHBoxLayout()
        layout_H_2 = QHBoxLayout()
        layout_H_3 = QHBoxLayout()
        layout_H_4 = QHBoxLayout()
        layout_H_5 = QHBoxLayout()
        layout_H_6 = QHBoxLayout()
        layout_V_1 = QVBoxLayout()

        layout_H_1.addWidget( service_condominium_name_label_add )
        layout_H_1.addWidget( self.service_condominium_name_input_add )
        layout_H_1.addWidget( service_condominium_rif_label_add )
        layout_H_1.addWidget( self.service_condominium_rif_input_add )

        layout_H_2.addWidget( service_date_label_add )
        layout_H_2.addWidget( self.service_date_add )
        layout_H_2.addWidget( service_condominium_owner_label_add )
        layout_H_2.addWidget( self.service_condominium_owner_input_add )

        layout_H_3.addWidget( service_condominium_number_apartment_label_add )
        layout_H_3.addWidget( self.service_condominium_number_apartment_input_add )
        layout_H_3.addWidget( service_condominium_aliquot_separately_label_add )
        layout_H_3.addWidget( self.service_condominium_aliquot_separately_input_add )

        layout_H_4.addWidget( service_condominium_ordinary_expenses_label_add )
        layout_H_4.addWidget( self.service_condominium_ordinary_expenses_input_add )

        layout_H_5.addWidget( service_condominium_detail_label_add )
        layout_H_5.addWidget( self.service_condominium_detail_input_add )

        layout_H_6.addWidget( service_condominium_amount_label_add )
        layout_H_6.addWidget( self.service_condominium_amount_input_add )

        layout_V_1.addWidget( main_title_service_add )
        layout_V_1.addLayout( layout_H_1 )
        layout_V_1.addLayout( layout_H_2 )
        layout_V_1.addLayout( layout_H_3 )
        layout_V_1.addLayout( layout_H_4 )
        layout_V_1.addLayout( layout_H_5 )
        layout_V_1.addLayout( layout_H_6 )
        layout_V_1.addWidget( self.botton_service_add_save )

        container_add_service = QWidget()
        container_add_service.setLayout( layout_V_1 )

        #search service
        
        main_title_service_search = QLabel( "Buscar Servicio" )
        main_title_service_search.setFont( QFont( 'times new roman', 15 ) )
        main_title_service_search.setAlignment( Qt.AlignmentFlag.AlignCenter )

        service_condominium_name_label_search = QLabel( "Nombre de condominio" )
        service_condominium_name_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_name_input_search = QLineEdit( self )

        service_date_label_search = QLabel( "Ingresa la fecha" )
        service_date_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.service_date_search = QDateEdit()
        self.service_date_search.setDisplayFormat( "dd-MM-yyyy" )
        self.service_date_search.setMaximumDate(
            QDate.currentDate()
        )
        self.service_date_search.setCalendarPopup( True )
        self.service_date_search.setDate( QDate.currentDate() )

        self.botton_service_search_search = QPushButton( "Buscar Servicio" )
        self.botton_service_search_search.clicked.connect( self.search_process )

        layout_H_7 = QHBoxLayout()
        layout_V_2 = QVBoxLayout()

        layout_H_7.addWidget( service_condominium_name_label_search )
        layout_H_7.addWidget( self.service_condominium_name_input_search )
        layout_H_7.addWidget( service_date_label_search )
        layout_H_7.addWidget( self.service_date_search )
        layout_H_7.addWidget( self.botton_service_search_search )

        layout_V_2.addWidget( main_title_service_search )
        layout_V_2.addLayout( layout_H_7 )
        layout_V_2.addWidget( self.any_table_servicio )

        container_search_service = QWidget()
        container_search_service.setLayout( layout_V_2 )
        
        #edit service
        
        main_title_service_edit = QLabel( "Editar Servicio" )
        main_title_service_edit.setFont( QFont( 'times new roman', 15 ) )
        main_title_service_edit.setAlignment( Qt.AlignmentFlag.AlignCenter )

        service_condominium_code_label_edit = QLabel( "Ingrese el codigo a buscar" )
        service_condominium_code_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_code_input_edit = QLineEdit( self )

        self.botton_service_edit_search = QPushButton( "Buscar" )

        service_condominium_name_label_edit = QLabel( "Nombre de condominio" )
        service_condominium_name_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.service_condominium_name_input_edit = QLineEdit( self )

        service_condominium_rif_label_edit = QLabel( "Rif" )
        service_condominium_rif_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_rif_input_edit = QLineEdit( self )

        service_date_label_edit = QLabel( "Fecha" )
        service_date_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.service_date_edit = QDateEdit()
        self.service_date_edit.setDisplayFormat( "dd-MM-yyyy" )
        self.service_date_edit.setMaximumDate(
            QDate.currentDate()
        )
        self.service_date_add.setCalendarPopup( True )
        self.service_date_add.setDate( QDate.currentDate() )

        service_condominium_owner_label_edit = QLabel( "Propietario" )
        service_condominium_owner_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_owner_input_edit = QLineEdit( self )

        service_condominium_number_apartment_label_edit = QLabel( "N° Apartamento" )
        service_condominium_number_apartment_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_number_apartment_input_edit = QLineEdit( self )

        service_condominium_aliquot_separately_label_edit = QLabel( "Alicuota Aparte" )
        service_condominium_aliquot_separately_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_aliquot_separately_input_edit = QLineEdit( self )

        service_condominium_ordinary_expenses_label_edit = QLabel( "Gastos Ordinarios" )
        service_condominium_ordinary_expenses_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.service_condominium_ordinary_expenses_input_edit = QLineEdit( self )

        service_condominium_detail_label_edit = QLabel( "Detalle" )
        service_condominium_detail_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_detail_input_edit = QLineEdit( self )

        service_condominium_amount_label_edit = QLabel( "Monto" )
        service_condominium_amount_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_amount_input_edit = QLineEdit( self )

        service_condominium_amount2_label_edit = QLabel( "Importe" )
        service_condominium_amount2_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_amount2_input_edit = QLineEdit( self )

        self.botton_service_edit_save = QPushButton( "Guardar" )

        layout_H_8 = QHBoxLayout()
        layout_H_9 = QHBoxLayout()
        layout_H_10 = QHBoxLayout()
        layout_H_11 = QHBoxLayout()
        layout_H_12 = QHBoxLayout()
        layout_H_13 = QHBoxLayout()
        layout_H_14 = QHBoxLayout()
        layout_H_15 = QHBoxLayout()
        layout_V_3 = QVBoxLayout()

        layout_H_8.addWidget( service_condominium_code_label_edit )
        layout_H_8.addWidget( self.service_condominium_code_input_edit )
        layout_H_8.addWidget( self.botton_service_edit_search )

        layout_H_9.addWidget( service_condominium_name_label_edit )
        layout_H_9.addWidget( self.service_condominium_name_input_edit )
        layout_H_9.addWidget( service_condominium_rif_label_edit )
        layout_H_9.addWidget( self.service_condominium_rif_input_edit )

        layout_H_10.addWidget( service_date_label_edit )
        layout_H_10.addWidget( self.service_date_edit )
        layout_H_10.addWidget( service_condominium_owner_label_edit )
        layout_H_10.addWidget( self.service_condominium_owner_input_edit )

        layout_H_11.addWidget( service_condominium_number_apartment_label_edit )
        layout_H_11.addWidget( self.service_condominium_number_apartment_input_edit )
        layout_H_11.addWidget( service_condominium_aliquot_separately_label_edit )
        layout_H_11.addWidget( self.service_condominium_aliquot_separately_input_edit )

        layout_H_12.addWidget( service_condominium_ordinary_expenses_label_edit )
        layout_H_12.addWidget( self.service_condominium_ordinary_expenses_input_edit )

        layout_H_13.addWidget( service_condominium_detail_label_edit )
        layout_H_13.addWidget( self.service_condominium_detail_input_edit )

        layout_H_14.addWidget( service_condominium_amount_label_edit )
        layout_H_14.addWidget( self.service_condominium_amount_input_edit )

        layout_H_15.addWidget( service_condominium_amount2_label_edit )
        layout_H_15.addWidget( self.service_condominium_amount2_input_edit )


        layout_V_3.addWidget( main_title_service_edit )
        layout_V_3.addLayout( layout_H_8 )
        layout_V_3.addLayout( layout_H_9 )
        layout_V_3.addLayout( layout_H_10 )
        layout_V_3.addLayout( layout_H_11 )
        layout_V_3.addLayout( layout_H_12 )
        layout_V_3.addLayout( layout_H_13 )
        layout_V_3.addLayout( layout_H_14 )
        layout_V_3.addLayout( layout_H_15 )
        layout_V_3.addWidget( self.botton_service_edit_save )

        container_edit_service = QWidget()
        container_edit_service.setLayout( layout_V_3 )
        
        #delete service

        main_title_service_delete = QLabel( "Borrar Servicio" )
        main_title_service_delete.setFont( QFont( 'times new roman', 15 ) )
        main_title_service_delete.setAlignment( Qt.AlignmentFlag.AlignCenter )

        service_condominium_name_label_detele = QLabel( "Nombre de condominio" )
        service_condominium_name_label_detele.setFont( QFont( 'times new roman', 13 ) )

        self.service_condominium_name_input_delete = QLineEdit( self )

        service_date_label_delete = QLabel( "Ingresa la fecha" )
        service_date_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.service_date_delete = QDateEdit()
        self.service_date_delete.setDisplayFormat( "dd-MM-yyyy" )
        self.service_date_delete.setMaximumDate(
            QDate.currentDate()
        )
        self.service_date_delete.setCalendarPopup( True )
        self.service_date_delete.setDate( QDate.currentDate() )

        self.botton_service_delete_search = QPushButton( "Buscar" )

        self.botton_service_delete_delete = QPushButton( "Eliminar" )

        layout_H_16 = QHBoxLayout()
        layout_V_4 = QVBoxLayout()

        layout_H_16.addWidget( service_condominium_name_label_detele )
        layout_H_16.addWidget( self.service_condominium_name_input_delete )
        layout_H_16.addWidget( service_date_label_delete )
        layout_H_16.addWidget( self.service_date_delete )
        layout_H_16.addWidget( self.botton_service_delete_search )

        layout_V_4.addWidget( main_title_service_delete )
        layout_V_4.addLayout( layout_H_16 )
        layout_V_4.addWidget( self.botton_service_delete_delete )

        container_delete_service = QWidget()
        container_delete_service.setLayout( layout_V_4 )

        #layout organization
        self.stacked_layout_service = QStackedLayout()
        self.stacked_layout_service.addWidget( container_add_service )
        self.stacked_layout_service.addWidget( container_search_service )
        self.stacked_layout_service.addWidget( container_edit_service )
        self.stacked_layout_service.addWidget( container_delete_service )

        main_layout_service = QVBoxLayout()
        main_layout_service.addLayout( bottons_group_service )
        main_layout_service.addLayout( self.stacked_layout_service )

        self.servicion_container.setLayout( main_layout_service )

    def window_mantenimiento_tab( self ):

        add_botton_maintenance = QPushButton( "Agregar Mantemiento" )
        add_botton_maintenance.clicked.connect( self.window_chance )
        
        search_botton_maintenance = QPushButton( "Buscar Mantemiento" )
        search_botton_maintenance.clicked.connect( self.window_chance )
        
        edit_botton_maintenance = QPushButton( "Editar Mantemiento" )
        edit_botton_maintenance.clicked.connect( self.window_chance )
        
        delete_botton_maintenance = QPushButton( "Eliminar Mantemiento" )
        delete_botton_maintenance.clicked.connect( self.window_chance )

        bottons_group_maintenance = QHBoxLayout()
        bottons_group_maintenance.addWidget( add_botton_maintenance )
        bottons_group_maintenance.addWidget( search_botton_maintenance )
        bottons_group_maintenance.addWidget( edit_botton_maintenance )
        bottons_group_maintenance.addWidget( delete_botton_maintenance )

        #add maintenance 

        main_title_maintenance_add = QLabel( "Agregar Mantemiento" )
        main_title_maintenance_add.setFont( QFont( 'times new roman', 15 ) )
        main_title_maintenance_add.setAlignment( Qt.AlignmentFlag.AlignCenter )

        maintenance_condominium_ordinary_expenses_label_add = QLabel( "Gastos Ordinarios" )
        maintenance_condominium_ordinary_expenses_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.maintenance_condominium_ordinary_expenses_input_add = QLineEdit( self )

        maintenance_condominium_detail_label_add = QLabel( "Detalle" )
        maintenance_condominium_detail_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_detail_input_add = QLineEdit( self )

        maintenance_condominium_amount_label_add = QLabel( "Monto" )
        maintenance_condominium_amount_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_amount_input_add = QLineEdit( self )

        self.botton_maintenance_add_save = QPushButton( "Guardar" )

        layout_H_1 = QHBoxLayout()
        layout_H_2 = QHBoxLayout()
        layout_H_3 = QHBoxLayout()
        layout_V_1 = QVBoxLayout()

        layout_H_1.addWidget( maintenance_condominium_ordinary_expenses_label_add )
        layout_H_1.addWidget( self.maintenance_condominium_ordinary_expenses_input_add )

        layout_H_2.addWidget( maintenance_condominium_detail_label_add )
        layout_H_2.addWidget( self.maintenance_condominium_detail_input_add )

        layout_H_3.addWidget( maintenance_condominium_amount_label_add )
        layout_H_3.addWidget( self.maintenance_condominium_amount_input_add )

        layout_V_1.addWidget( main_title_maintenance_add )
        layout_V_1.addLayout( layout_H_1 )
        layout_V_1.addLayout( layout_H_2 )
        layout_V_1.addLayout( layout_H_3 )
        layout_V_1.addWidget( self.botton_maintenance_add_save )

        container_add_maintenance = QWidget()
        container_add_maintenance.setLayout( layout_V_1 )

        #search maintenance

        main_title_maintenance_search = QLabel( "Buscar Mantemiento" )
        main_title_maintenance_search.setFont( QFont( 'times new roman', 15 ) )
        main_title_maintenance_search.setAlignment( Qt.AlignmentFlag.AlignCenter )

        maintenance_condominium_name_label_search = QLabel( "Nombre de condominio" )
        maintenance_condominium_name_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_name_input_search = QLineEdit( self )

        maintenance_date_label_search = QLabel( "Ingresa la fecha" )
        maintenance_date_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_date_search = QDateEdit()
        self.maintenance_date_search.setDisplayFormat( "dd-MM-yyyy" )
        self.maintenance_date_search.setMaximumDate(
            QDate.currentDate()
        )
        self.maintenance_date_search.setCalendarPopup( True )
        self.maintenance_date_search.setDate( QDate.currentDate() )

        self.botton_maintenance_search_search = QPushButton( "Buscar Mantemiento" )
        self.botton_maintenance_search_search.clicked.connect( self.search_process )

        layout_H_4 = QHBoxLayout()
        layout_V_2 = QVBoxLayout()

        layout_H_4.addWidget( maintenance_condominium_name_label_search )
        layout_H_4.addWidget( self.maintenance_condominium_name_input_search )
        layout_H_4.addWidget( maintenance_date_label_search )
        layout_H_4.addWidget( self.maintenance_date_search )
        layout_H_4.addWidget( self.botton_maintenance_search_search ) 

        layout_V_2.addWidget( main_title_maintenance_search )
        layout_V_2.addLayout( layout_H_4 )
        layout_V_2.addWidget( self.any_table_mantenimiento )

        container_search_maintenance = QWidget()
        container_search_maintenance.setLayout( layout_V_2 )

        #edit maintenance
        
        main_title_maintenance_edit = QLabel( "Editar Mantemiento" )
        main_title_maintenance_edit.setFont( QFont( 'times new roman', 15 ) )
        main_title_maintenance_edit.setAlignment( Qt.AlignmentFlag.AlignCenter )

        maintenance_condominium_code_label_edit = QLabel( "Ingrese el codigo a buscar" )
        maintenance_condominium_code_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_code_input_edit = QLineEdit( self )

        self.botton_maintenance_edit_search = QPushButton( "Buscar" )

        maintenance_condominium_ordinary_expenses_label_edit = QLabel( "Gastos Ordinarios" )
        maintenance_condominium_ordinary_expenses_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.maintenance_condominium_ordinary_expenses_input_edit = QLineEdit( self )

        maintenance_condominium_detail_label_edit = QLabel( "Detalle" )
        maintenance_condominium_detail_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_detail_input_edit = QLineEdit( self )

        maintenance_condominium_amount_label_edit = QLabel( "Monto" )
        maintenance_condominium_amount_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_amount_input_edit = QLineEdit( self )

        maintenance_condominium_amount2_label_edit = QLabel( "Importe" )
        maintenance_condominium_amount2_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_amount2_input_edit = QLineEdit( self )

        self.botton_maintenance_edit_save = QPushButton( "Guardar" )

        layout_H_5 = QHBoxLayout()
        layout_H_6 = QHBoxLayout()
        layout_H_7 = QHBoxLayout()
        layout_V_3 = QVBoxLayout()

        layout_H_5.addWidget( maintenance_condominium_code_label_edit )
        layout_H_5.addWidget( self.maintenance_condominium_code_input_edit )
        layout_H_5.addWidget( self.botton_maintenance_edit_search )

        layout_H_6.addWidget( maintenance_condominium_ordinary_expenses_label_edit )
        layout_H_6.addWidget( self.maintenance_condominium_ordinary_expenses_input_edit )
        layout_H_6.addWidget( maintenance_condominium_detail_label_edit )
        layout_H_6.addWidget( self.maintenance_condominium_detail_input_edit )

        layout_H_7.addWidget( maintenance_condominium_amount_label_edit )
        layout_H_7.addWidget( self.maintenance_condominium_amount_input_edit )
        layout_H_7.addWidget( maintenance_condominium_amount2_label_edit )
        layout_H_7.addWidget( self.maintenance_condominium_amount2_input_edit )

        layout_V_3.addWidget( main_title_maintenance_edit )
        layout_V_3.addLayout( layout_H_5 )
        layout_V_3.addLayout( layout_H_6 )
        layout_V_3.addLayout( layout_H_7 )
        layout_V_3.addWidget( self.botton_maintenance_edit_save )

        container_edit_maintenance = QWidget()
        container_edit_maintenance.setLayout( layout_V_3 )

        #delete maintenance

        main_title_maintenance_delete = QLabel( "Eliminar Mantemiento" )
        main_title_maintenance_delete.setFont( QFont( 'times new roman', 15 ) )
        main_title_maintenance_delete.setAlignment( Qt.AlignmentFlag.AlignCenter )

        maintenance_condominium_name_label_detele = QLabel( "Nombre de condominio" )
        maintenance_condominium_name_label_detele.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_condominium_name_input_delete = QLineEdit( self )

        maintenance_date_label_delete = QLabel( "Ingresa la fecha" )
        maintenance_date_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.maintenance_date_delete = QDateEdit()
        self.maintenance_date_delete.setDisplayFormat( "dd-MM-yyyy" )
        self.maintenance_date_delete.setMaximumDate(
            QDate.currentDate()
        )
        self.maintenance_date_delete.setCalendarPopup( True )
        self.maintenance_date_delete.setDate( QDate.currentDate() )

        self.botton_maintenance_delete_search = QPushButton( "Buscar" )

        self.botton_maintenance_delete_delete = QPushButton( "Eliminar" )

        layout_H_8 = QHBoxLayout()
        layout_V_4 = QVBoxLayout()

        layout_H_8.addWidget( maintenance_condominium_name_label_detele )
        layout_H_8.addWidget( self.maintenance_condominium_name_input_delete )
        layout_H_8.addWidget( maintenance_date_label_delete )
        layout_H_8.addWidget( self.botton_maintenance_delete_search )

        layout_V_4.addWidget( main_title_maintenance_delete )
        layout_V_4.addLayout( layout_H_8 )
        layout_V_4.addWidget( self.botton_maintenance_delete_delete )

        container_delete_maintenance = QWidget()
        container_delete_maintenance.setLayout( layout_V_4 )

        #layout organization
        self.stacked_layout_maintenance = QStackedLayout()
        self.stacked_layout_maintenance.addWidget( container_add_maintenance )
        self.stacked_layout_maintenance.addWidget( container_search_maintenance )
        self.stacked_layout_maintenance.addWidget( container_edit_maintenance )
        self.stacked_layout_maintenance.addWidget( container_delete_maintenance )

        main_layout_maintenance = QVBoxLayout()
        main_layout_maintenance.addLayout( bottons_group_maintenance )
        main_layout_maintenance.addLayout( self.stacked_layout_maintenance )

        self.mantenimiento_container.setLayout( main_layout_maintenance )

    def window_reparaciones_menores_tab( self ):

        add_botton_minor_repairs = QPushButton( "Agregar Reparacion Menor" )
        add_botton_minor_repairs.clicked.connect( self.window_chance )
        
        search_botton_minor_repairs = QPushButton( "Buscar Reparacion Menor" )
        search_botton_minor_repairs.clicked.connect( self.window_chance )
        
        edit_botton_minor_repairs = QPushButton( "Editar Reparacion Menor" )
        edit_botton_minor_repairs.clicked.connect( self.window_chance )
        
        delete_botton_minor_repairs = QPushButton( "Eliminar Reparacion Menor" )
        delete_botton_minor_repairs.clicked.connect( self.window_chance )

        bottons_group_minor_repairs = QHBoxLayout()
        bottons_group_minor_repairs.addWidget( add_botton_minor_repairs )
        bottons_group_minor_repairs.addWidget( search_botton_minor_repairs )
        bottons_group_minor_repairs.addWidget( edit_botton_minor_repairs )
        bottons_group_minor_repairs.addWidget( delete_botton_minor_repairs )

        #add minor repairs

        main_title_minor_repairs_add = QLabel( "Agregar Reparacion Menor" )
        main_title_minor_repairs_add.setFont( QFont( 'times new roman', 15 ) )
        main_title_minor_repairs_add.setAlignment( Qt.AlignmentFlag.AlignCenter )

        minor_repairs_condominium_ordinary_expenses_label_add = QLabel( "Gastos Ordinarios" )
        minor_repairs_condominium_ordinary_expenses_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.minor_repairs_condominium_ordinary_expenses_input_add = QLineEdit( self )

        minor_repairs_condominium_detail_label_add = QLabel( "Detalle" )
        minor_repairs_condominium_detail_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_detail_input_add = QLineEdit( self )

        minor_repairs_condominium_amount_label_add = QLabel( "Monto" )
        minor_repairs_condominium_amount_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_amount_input_add = QLineEdit( self )

        self.botton_minor_repairs_add_save = QPushButton( "Guardar" )

        layout_H_1 = QHBoxLayout()
        layout_H_2 = QHBoxLayout()
        layout_H_3 = QHBoxLayout()
        layout_V_1 = QVBoxLayout()

        layout_H_1.addWidget( minor_repairs_condominium_ordinary_expenses_label_add )
        layout_H_1.addWidget( self.minor_repairs_condominium_ordinary_expenses_input_add )

        layout_H_2.addWidget( minor_repairs_condominium_detail_label_add )
        layout_H_2.addWidget( self.minor_repairs_condominium_detail_input_add )

        layout_H_3.addWidget( minor_repairs_condominium_amount_label_add )
        layout_H_3.addWidget( self.minor_repairs_condominium_amount_input_add )

        layout_V_1.addWidget( main_title_minor_repairs_add )
        layout_V_1.addLayout( layout_H_1 )
        layout_V_1.addLayout( layout_H_2 )
        layout_V_1.addLayout( layout_H_3 )
        layout_V_1.addWidget( self.botton_minor_repairs_add_save )

        container_add_minor_repairs = QWidget()
        container_add_minor_repairs.setLayout( layout_V_1 )

        #search minor repairs

        main_title_minor_repairs_search = QLabel( "Buscar Reparacion Menor" )
        main_title_minor_repairs_search.setFont( QFont( 'times new roman', 15 ) )
        main_title_minor_repairs_search.setAlignment( Qt.AlignmentFlag.AlignCenter )

        minor_repairs_condominium_name_label_search = QLabel( "Nombre de condominio" )
        minor_repairs_condominium_name_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_name_input_search = QLineEdit( self )

        minor_repairs_date_label_search = QLabel( "Ingresa la fecha" )
        minor_repairs_date_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_date_search = QDateEdit()
        self.minor_repairs_date_search.setDisplayFormat( "dd-MM-yyyy" )
        self.minor_repairs_date_search.setMaximumDate(
            QDate.currentDate()
        )
        self.minor_repairs_date_search.setCalendarPopup( True )
        self.minor_repairs_date_search.setDate( QDate.currentDate() )

        self.botton_minor_repairs_search_search = QPushButton( "Buscar Reparacion Menor" )
        self.botton_minor_repairs_search_search.clicked.connect( self.search_process )

        layout_H_4 = QHBoxLayout()
        layout_V_2 = QVBoxLayout()

        layout_H_4.addWidget( minor_repairs_condominium_name_label_search )
        layout_H_4.addWidget( self.minor_repairs_condominium_name_input_search )
        layout_H_4.addWidget( minor_repairs_date_label_search )
        layout_H_4.addWidget( self.minor_repairs_date_search )
        layout_H_4.addWidget( self.botton_minor_repairs_search_search ) 

        layout_V_2.addWidget( main_title_minor_repairs_search )
        layout_V_2.addLayout( layout_H_4 )
        layout_V_2.addWidget( self.any_table_reparacion_menor )

        container_search_minor_repairs = QWidget()
        container_search_minor_repairs.setLayout( layout_V_2 )

        #edit minor_repairs
        
        main_title_minor_repairs_edit = QLabel( "Editar Reparacion Menor" )
        main_title_minor_repairs_edit.setFont( QFont( 'times new roman', 15 ) )
        main_title_minor_repairs_edit.setAlignment( Qt.AlignmentFlag.AlignCenter )

        minor_repairs_condominium_code_label_edit = QLabel( "Ingrese el codigo a buscar" )
        minor_repairs_condominium_code_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_code_input_edit = QLineEdit( self )

        self.botton_minor_repairs_edit_search = QPushButton( "Buscar" )

        minor_repairs_condominium_ordinary_expenses_label_edit = QLabel( "Gastos Ordinarios" )
        minor_repairs_condominium_ordinary_expenses_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.minor_repairs_condominium_ordinary_expenses_input_edit = QLineEdit( self )

        minor_repairs_condominium_detail_label_edit = QLabel( "Detalle" )
        minor_repairs_condominium_detail_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_detail_input_edit = QLineEdit( self )

        minor_repairs_condominium_amount_label_edit = QLabel( "Monto" )
        minor_repairs_condominium_amount_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_amount_input_edit = QLineEdit( self )

        minor_repairs_condominium_amount2_label_edit = QLabel( "Importe" )
        minor_repairs_condominium_amount2_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_amount2_input_edit = QLineEdit( self )

        self.botton_minor_repairs_edit_save = QPushButton( "Guardar" )

        layout_H_5 = QHBoxLayout()
        layout_H_6 = QHBoxLayout()
        layout_H_7 = QHBoxLayout()
        layout_V_3 = QVBoxLayout()

        layout_H_5.addWidget( minor_repairs_condominium_code_label_edit )
        layout_H_5.addWidget( self.minor_repairs_condominium_code_input_edit )
        layout_H_5.addWidget( self.botton_minor_repairs_edit_search )

        layout_H_6.addWidget( minor_repairs_condominium_ordinary_expenses_label_edit )
        layout_H_6.addWidget( self.minor_repairs_condominium_ordinary_expenses_input_edit )
        layout_H_6.addWidget( minor_repairs_condominium_detail_label_edit )
        layout_H_6.addWidget( self.minor_repairs_condominium_detail_input_edit )

        layout_H_7.addWidget( minor_repairs_condominium_amount_label_edit )
        layout_H_7.addWidget( self.minor_repairs_condominium_amount_input_edit )
        layout_H_7.addWidget( minor_repairs_condominium_amount2_label_edit )
        layout_H_7.addWidget( self.minor_repairs_condominium_amount2_input_edit )

        layout_V_3.addWidget( main_title_minor_repairs_edit )
        layout_V_3.addLayout( layout_H_5 )
        layout_V_3.addLayout( layout_H_6 )
        layout_V_3.addLayout( layout_H_7 )
        layout_V_3.addWidget( self.botton_minor_repairs_edit_save )

        container_edit_minor_repairs = QWidget()
        container_edit_minor_repairs.setLayout( layout_V_3 )

        #delete minor repairs

        main_title_minor_repairs_delete = QLabel( "Eliminar Reparacion Menor" )
        main_title_minor_repairs_delete.setFont( QFont( 'times new roman', 15 ) )
        main_title_minor_repairs_delete.setAlignment( Qt.AlignmentFlag.AlignCenter )

        minor_repairs_condominium_name_label_detele = QLabel( "Nombre de condominio" )
        minor_repairs_condominium_name_label_detele.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_condominium_name_input_delete = QLineEdit( self )

        minor_repairs_date_label_delete = QLabel( "Ingresa la fecha" )
        minor_repairs_date_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.minor_repairs_date_delete = QDateEdit()
        self.minor_repairs_date_delete.setDisplayFormat( "dd-MM-yyyy" )
        self.minor_repairs_date_delete.setMaximumDate(
            QDate.currentDate()
        )
        self.minor_repairs_date_delete.setCalendarPopup( True )
        self.minor_repairs_date_delete.setDate( QDate.currentDate() )

        self.botton_minor_repairs_delete_search = QPushButton( "Buscar" )

        self.botton_minor_repairs_delete_delete = QPushButton( "Eliminar" )

        layout_H_8 = QHBoxLayout()
        layout_V_4 = QVBoxLayout()

        layout_H_8.addWidget( minor_repairs_condominium_name_label_detele )
        layout_H_8.addWidget( self.minor_repairs_condominium_name_input_delete )
        layout_H_8.addWidget( minor_repairs_date_label_delete )
        layout_H_8.addWidget( self.botton_minor_repairs_delete_search )

        layout_V_4.addWidget( main_title_minor_repairs_delete )
        layout_V_4.addLayout( layout_H_8 )
        layout_V_4.addWidget( self.botton_minor_repairs_delete_delete )

        container_delete_minor_repairs = QWidget()
        container_delete_minor_repairs.setLayout( layout_V_4 )

        #layout organization
        self.stacked_layout_minor_repairs = QStackedLayout()
        self.stacked_layout_minor_repairs.addWidget( container_add_minor_repairs )
        self.stacked_layout_minor_repairs.addWidget( container_search_minor_repairs )
        self.stacked_layout_minor_repairs.addWidget( container_edit_minor_repairs )
        self.stacked_layout_minor_repairs.addWidget( container_delete_minor_repairs )

        main_layout_minor_repairs = QVBoxLayout()
        main_layout_minor_repairs.addLayout( bottons_group_minor_repairs )
        main_layout_minor_repairs.addLayout( self.stacked_layout_minor_repairs )

        self.reparacione_menores_container.setLayout( main_layout_minor_repairs )

    def window_aportes_fijos_tab( self ):

        add_botton_fixed_contributions = QPushButton( "Agregar Aportes Fijos" )
        add_botton_fixed_contributions.clicked.connect( self.window_chance )
        
        search_botton_fixed_contributions = QPushButton( "Buscar Aportes Fijos" )
        search_botton_fixed_contributions.clicked.connect( self.window_chance )
        
        edit_botton_fixed_contributions = QPushButton( "Editar Aportes Fijos" )
        edit_botton_fixed_contributions.clicked.connect( self.window_chance )
        
        delete_botton_fixed_contributions = QPushButton( "Eliminar Aportes Fijos" )
        delete_botton_fixed_contributions.clicked.connect( self.window_chance )

        bottons_group_fixed_contributions = QHBoxLayout()
        bottons_group_fixed_contributions.addWidget( add_botton_fixed_contributions )
        bottons_group_fixed_contributions.addWidget( search_botton_fixed_contributions )
        bottons_group_fixed_contributions.addWidget( edit_botton_fixed_contributions )
        bottons_group_fixed_contributions.addWidget( delete_botton_fixed_contributions )

        #add fixed contributions

        main_title_fixed_contributions_add = QLabel( "Agregar Aportes Fijos" )
        main_title_fixed_contributions_add.setFont( QFont( 'times new roman', 15 ) )
        main_title_fixed_contributions_add.setAlignment( Qt.AlignmentFlag.AlignCenter )

        fixed_contributions_condominium_ordinary_expenses_label_add = QLabel( "Gastos Ordinarios" )
        fixed_contributions_condominium_ordinary_expenses_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.fixed_contributions_condominium_ordinary_expenses_input_add = QLineEdit( self )

        fixed_contributions_condominium_detail_label_add = QLabel( "Detalle" )
        fixed_contributions_condominium_detail_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_detail_input_add = QLineEdit( self )

        fixed_contributions_condominium_amount_label_add = QLabel( "Monto" )
        fixed_contributions_condominium_amount_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_amount_input_add = QLineEdit( self )

        self.botton_fixed_contributions_add_save = QPushButton( "Guardar" )

        layout_H_1 = QHBoxLayout()
        layout_H_2 = QHBoxLayout()
        layout_H_3 = QHBoxLayout()
        layout_V_1 = QVBoxLayout()

        layout_H_1.addWidget( fixed_contributions_condominium_ordinary_expenses_label_add )
        layout_H_1.addWidget( self.fixed_contributions_condominium_ordinary_expenses_input_add )

        layout_H_2.addWidget( fixed_contributions_condominium_detail_label_add )
        layout_H_2.addWidget( self.fixed_contributions_condominium_detail_input_add )

        layout_H_3.addWidget( fixed_contributions_condominium_amount_label_add )
        layout_H_3.addWidget( self.fixed_contributions_condominium_amount_input_add )

        layout_V_1.addWidget( main_title_fixed_contributions_add )
        layout_V_1.addLayout( layout_H_1 )
        layout_V_1.addLayout( layout_H_2 )
        layout_V_1.addLayout( layout_H_3 )
        layout_V_1.addWidget( self.botton_fixed_contributions_add_save )

        container_add_fixed_contributions = QWidget()
        container_add_fixed_contributions.setLayout( layout_V_1 )

        #search fixed_contributions

        main_title_fixed_contributions_search = QLabel( "Buscar Aportes Fijos" )
        main_title_fixed_contributions_search.setFont( QFont( 'times new roman', 15 ) )
        main_title_fixed_contributions_search.setAlignment( Qt.AlignmentFlag.AlignCenter )

        fixed_contributions_condominium_name_label_search = QLabel( "Nombre de condominio" )
        fixed_contributions_condominium_name_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_name_input_search = QLineEdit( self )

        fixed_contributions_date_label_search = QLabel( "Ingresa la fecha" )
        fixed_contributions_date_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_date_search = QDateEdit()
        self.fixed_contributions_date_search.setDisplayFormat( "dd-MM-yyyy" )
        self.fixed_contributions_date_search.setMaximumDate(
            QDate.currentDate()
        )
        self.fixed_contributions_date_search.setCalendarPopup( True )
        self.fixed_contributions_date_search.setDate( QDate.currentDate() )

        self.botton_fixed_contributions_search_search = QPushButton( "Buscar Aportes Fijos" )
        #self.botton_fixed_contributions_search_search.clicked.connect( self.search_process )

        layout_H_4 = QHBoxLayout()
        layout_V_2 = QVBoxLayout()

        layout_H_4.addWidget( fixed_contributions_condominium_name_label_search )
        layout_H_4.addWidget( self.fixed_contributions_condominium_name_input_search )
        layout_H_4.addWidget( fixed_contributions_date_label_search )
        layout_H_4.addWidget( self.fixed_contributions_date_search )
        layout_H_4.addWidget( self.botton_fixed_contributions_search_search ) 

        layout_V_2.addWidget( main_title_fixed_contributions_search )
        layout_V_2.addLayout( layout_H_4 )
        #layout_V_2.addLayout( self.any_table_aportes_fijos )

        container_search_fixed_contributions = QWidget()
        container_search_fixed_contributions.setLayout( layout_V_2 )

        #edit fixed contributions
        
        main_title_fixed_contributions_edit = QLabel( "Editar Aportes Fijos" )
        main_title_fixed_contributions_edit.setFont( QFont( 'times new roman', 15 ) )
        main_title_fixed_contributions_edit.setAlignment( Qt.AlignmentFlag.AlignCenter )

        fixed_contributions_condominium_code_label_edit = QLabel( "Ingrese el codigo a buscar" )
        fixed_contributions_condominium_code_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_code_input_edit = QLineEdit( self )

        self.botton_fixed_contributions_edit_search = QPushButton( "Buscar" )

        fixed_contributions_condominium_ordinary_expenses_label_edit = QLabel( "Gastos Ordinarios" )
        fixed_contributions_condominium_ordinary_expenses_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.fixed_contributions_condominium_ordinary_expenses_input_edit = QLineEdit( self )

        fixed_contributions_condominium_detail_label_edit = QLabel( "Detalle" )
        fixed_contributions_condominium_detail_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_detail_input_edit = QLineEdit( self )

        fixed_contributions_condominium_amount_label_edit = QLabel( "Monto" )
        fixed_contributions_condominium_amount_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_amount_input_edit = QLineEdit( self )

        fixed_contributions_condominium_amount2_label_edit = QLabel( "Importe" )
        fixed_contributions_condominium_amount2_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_amount2_input_edit = QLineEdit( self )

        self.botton_fixed_contributions_edit_save = QPushButton( "Guardar" )

        layout_H_5 = QHBoxLayout()
        layout_H_6 = QHBoxLayout()
        layout_H_7 = QHBoxLayout()
        layout_V_3 = QVBoxLayout()

        layout_H_5.addWidget( fixed_contributions_condominium_code_label_edit )
        layout_H_5.addWidget( self.fixed_contributions_condominium_code_input_edit )
        layout_H_5.addWidget( self.botton_fixed_contributions_edit_search )

        layout_H_6.addWidget( fixed_contributions_condominium_ordinary_expenses_label_edit )
        layout_H_6.addWidget( self.fixed_contributions_condominium_ordinary_expenses_input_edit )
        layout_H_6.addWidget( fixed_contributions_condominium_detail_label_edit )
        layout_H_6.addWidget( self.fixed_contributions_condominium_detail_input_edit )

        layout_H_7.addWidget( fixed_contributions_condominium_amount_label_edit )
        layout_H_7.addWidget( self.fixed_contributions_condominium_amount_input_edit )
        layout_H_7.addWidget( fixed_contributions_condominium_amount2_label_edit )
        layout_H_7.addWidget( self.fixed_contributions_condominium_amount2_input_edit )

        layout_V_3.addWidget( main_title_fixed_contributions_edit )
        layout_V_3.addLayout( layout_H_5 )
        layout_V_3.addLayout( layout_H_6 )
        layout_V_3.addLayout( layout_H_7 )
        layout_V_3.addWidget( self.botton_fixed_contributions_edit_save )

        container_edit_fixed_contributions = QWidget()
        container_edit_fixed_contributions.setLayout( layout_V_3 )

        #delete minor repairs

        main_title_fixed_contributions_delete = QLabel( "Eliminar Aportes Fijos" )
        main_title_fixed_contributions_delete.setFont( QFont( 'times new roman', 15 ) )
        main_title_fixed_contributions_delete.setAlignment( Qt.AlignmentFlag.AlignCenter )

        fixed_contributions_condominium_name_label_detele = QLabel( "Nombre de condominio" )
        fixed_contributions_condominium_name_label_detele.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_condominium_name_input_delete = QLineEdit( self )

        fixed_contributions_date_label_delete = QLabel( "Ingresa la fecha" )
        fixed_contributions_date_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.fixed_contributions_date_delete = QDateEdit()
        self.fixed_contributions_date_delete.setDisplayFormat( "dd-MM-yyyy" )
        self.fixed_contributions_date_delete.setMaximumDate(
            QDate.currentDate()
        )
        self.fixed_contributions_date_delete.setCalendarPopup( True )
        self.fixed_contributions_date_delete.setDate( QDate.currentDate() )

        self.botton_fixed_contributions_delete_search = QPushButton( "Buscar" )

        self.botton_fixed_contributions_delete_delete = QPushButton( "Eliminar" )

        layout_H_8 = QHBoxLayout()
        layout_V_4 = QVBoxLayout()

        layout_H_8.addWidget( fixed_contributions_condominium_name_label_detele )
        layout_H_8.addWidget( self.fixed_contributions_condominium_name_input_delete )
        layout_H_8.addWidget( fixed_contributions_date_label_delete )
        layout_H_8.addWidget( self.botton_fixed_contributions_delete_search )

        layout_V_4.addWidget( main_title_fixed_contributions_delete )
        layout_V_4.addLayout( layout_H_8 )
        layout_V_4.addWidget( self.botton_fixed_contributions_delete_delete )

        container_delete_fixed_contributions = QWidget()
        container_delete_fixed_contributions.setLayout( layout_V_4 )

        #layout organization
        self.stacked_layout_fixed_contributions = QStackedLayout()
        self.stacked_layout_fixed_contributions.addWidget( container_add_fixed_contributions )
        self.stacked_layout_fixed_contributions.addWidget( container_search_fixed_contributions )
        self.stacked_layout_fixed_contributions.addWidget( container_edit_fixed_contributions )
        self.stacked_layout_fixed_contributions.addWidget( container_delete_fixed_contributions )

        main_layout_fixed_contributions = QVBoxLayout()
        main_layout_fixed_contributions.addLayout( bottons_group_fixed_contributions )
        main_layout_fixed_contributions.addLayout( self.stacked_layout_fixed_contributions )

        self.aportes_fijos_container.setLayout( main_layout_fixed_contributions )

    def window_otros_gastos_tab( self ):

        add_botton_other_expenses = QPushButton( "Agregar Otros Gastos" )
        add_botton_other_expenses.clicked.connect( self.window_chance )
        
        search_botton_other_expenses = QPushButton( "Buscar Otros Gastos" )
        search_botton_other_expenses.clicked.connect( self.window_chance )
        
        edit_botton_other_expenses = QPushButton( "Editar Otros Gastos" )
        edit_botton_other_expenses.clicked.connect( self.window_chance )
        
        delete_botton_other_expenses = QPushButton( "Eliminar Otros Gastos" )
        delete_botton_other_expenses.clicked.connect( self.window_chance )

        bottons_group_other_expenses = QHBoxLayout()
        bottons_group_other_expenses.addWidget( add_botton_other_expenses )
        bottons_group_other_expenses.addWidget( search_botton_other_expenses )
        bottons_group_other_expenses.addWidget( edit_botton_other_expenses )
        bottons_group_other_expenses.addWidget( delete_botton_other_expenses )

        #add other expenses

        main_title_other_expenses_add = QLabel( "Agregar Otros Gastos" )
        main_title_other_expenses_add.setFont( QFont( 'times new roman', 15 ) )
        main_title_other_expenses_add.setAlignment( Qt.AlignmentFlag.AlignCenter )

        other_expenses_condominium_ordinary_expenses_label_add = QLabel( "Gastos Ordinarios" )
        other_expenses_condominium_ordinary_expenses_label_add.setFont( QFont( 'times new roman', 13 ) )
        
        self.other_expenses_condominium_ordinary_expenses_input_add = QLineEdit( self )

        other_expenses_condominium_detail_label_add = QLabel( "Detalle" )
        other_expenses_condominium_detail_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_detail_input_add = QLineEdit( self )

        other_expenses_condominium_amount_label_add = QLabel( "Monto" )
        other_expenses_condominium_amount_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_amount_input_add = QLineEdit( self )

        other_expenses_condominium_amount2_label_add = QLabel( "Importe" )
        other_expenses_condominium_amount2_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_amount2_input_add = QLineEdit( self )

        other_expenses_condominium_previous_balance_label_add = QLabel( "Saldo Anterior" )
        other_expenses_condominium_previous_balance_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_previous_balance_input_add = QLineEdit( self )

        other_expenses_condominium_USD_label_add = QLabel( "USD" )
        other_expenses_condominium_USD_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_USD_input_add = QLineEdit( self )

        other_expenses_condominium_mail_label_add = QLabel( "Correo del condominio" )
        other_expenses_condominium_mail_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_mail_input_add = QLineEdit( self )
        
        other_expenses_condominium_change_day_label_add = QLabel( "Taza del dia" )
        other_expenses_condominium_change_day_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_change_day_input_add = QLineEdit( self )

        other_expenses_condominium_effective_collection_label_add = QLabel( "Cobranza Efectiva" )
        other_expenses_condominium_effective_collection_label_add.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_effective_collection_input_add = QLineEdit( self )

        self.botton_other_expenses_add_save = QPushButton( "Guardar" )

        layout_H_1 = QHBoxLayout()
        layout_H_2 = QHBoxLayout()
        layout_H_3 = QHBoxLayout()
        layout_H_4 = QHBoxLayout()
        layout_H_5 = QHBoxLayout()
        layout_V_1 = QVBoxLayout()

        layout_H_1.addWidget( other_expenses_condominium_ordinary_expenses_label_add )
        layout_H_1.addWidget( self.other_expenses_condominium_ordinary_expenses_input_add )
        layout_H_1.addWidget( other_expenses_condominium_detail_label_add )
        layout_H_1.addWidget( self.other_expenses_condominium_detail_input_add )
        
        layout_H_2.addWidget( other_expenses_condominium_amount_label_add )
        layout_H_2.addWidget( self.other_expenses_condominium_amount_input_add )
        layout_H_2.addWidget( other_expenses_condominium_amount2_label_add )
        layout_H_2.addWidget( self.other_expenses_condominium_amount2_input_add )

        layout_H_3.addWidget( other_expenses_condominium_previous_balance_label_add )
        layout_H_3.addWidget( self.other_expenses_condominium_previous_balance_input_add )
        layout_H_3.addWidget( other_expenses_condominium_USD_label_add )
        layout_H_3.addWidget( self.other_expenses_condominium_USD_input_add )

        layout_H_4.addWidget( other_expenses_condominium_mail_label_add )
        layout_H_4.addWidget( self.other_expenses_condominium_mail_input_add )

        layout_H_5.addWidget( other_expenses_condominium_change_day_label_add )
        layout_H_5.addWidget( self.other_expenses_condominium_change_day_input_add )
        layout_H_5.addWidget( other_expenses_condominium_effective_collection_label_add )
        layout_H_5.addWidget( self.other_expenses_condominium_effective_collection_input_add )

        layout_V_1.addWidget( main_title_other_expenses_add )
        layout_V_1.addLayout( layout_H_1 )
        layout_V_1.addLayout( layout_H_2 )
        layout_V_1.addLayout( layout_H_3 )
        layout_V_1.addLayout( layout_H_4 )
        layout_V_1.addLayout( layout_H_5 )
        layout_V_1.addWidget( self.botton_other_expenses_add_save )

        container_add_other_expenses = QWidget()
        container_add_other_expenses.setLayout( layout_V_1 )

        #search other expenses

        main_title_other_expenses_search = QLabel( "Buscar Otros Gastos" )
        main_title_other_expenses_search.setFont( QFont( 'times new roman', 32 ) )
        main_title_other_expenses_search.setAlignment( Qt.AlignmentFlag.AlignCenter )

        other_expenses_condominium_name_label_search = QLabel( "Nombre de condominio" )
        other_expenses_condominium_name_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_name_input_search = QLineEdit( self )

        other_expenses_date_label_search = QLabel( "Ingresa la fecha" )
        other_expenses_date_label_search.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_date_search = QDateEdit()
        self.other_expenses_date_search.setDisplayFormat( "dd-MM-yyyy" )
        self.other_expenses_date_search.setMaximumDate(
            QDate.currentDate()
        )
        self.other_expenses_date_search.setCalendarPopup( True )
        self.other_expenses_date_search.setDate( QDate.currentDate() )

        self.botton_other_expenses_search_search = QPushButton( "Buscar Otros Gastos" )
        self.botton_other_expenses_search_search.clicked.connect( self.search_process )

        layout_H_6 = QHBoxLayout()
        layout_V_2 = QVBoxLayout()

        layout_H_6.addWidget( other_expenses_condominium_name_label_search )
        layout_H_6.addWidget( self.other_expenses_condominium_name_input_search )
        layout_H_6.addWidget( other_expenses_date_label_search )
        layout_H_6.addWidget( self.other_expenses_date_search )
        layout_H_6.addWidget( self.botton_other_expenses_search_search ) 

        layout_V_2.addWidget( main_title_other_expenses_search )
        layout_V_2.addLayout( layout_H_6 )
        layout_V_2.addWidget( self.any_table_otros_gastos )

        container_search_other_expenses = QWidget()
        container_search_other_expenses.setLayout( layout_V_2 )
        
        #edit other expenses

        main_title_other_expenses_edit = QLabel( "Editar Otros Gastos" )
        main_title_other_expenses_edit.setFont( QFont( 'times new roman', 15 ) )
        main_title_other_expenses_edit.setAlignment( Qt.AlignmentFlag.AlignCenter )

        other_expenses_condominium_code_label_edit = QLabel( "Ingrese el codigo a buscar" )
        other_expenses_condominium_code_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_code_input_edit = QLineEdit( self )

        self.botton_other_expenses_edit_search = QPushButton( "Buscar" )

        other_expenses_condominium_ordinary_expenses_label_edit = QLabel( "Gastos Ordinarios" )
        other_expenses_condominium_ordinary_expenses_label_edit.setFont( QFont( 'times new roman', 13 ) )
        
        self.other_expenses_condominium_ordinary_expenses_input_edit = QLineEdit( self )

        other_expenses_condominium_detail_label_edit = QLabel( "Detalle" )
        other_expenses_condominium_detail_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_detail_input_edit = QLineEdit( self )

        other_expenses_condominium_amount_label_edit = QLabel( "Monto" )
        other_expenses_condominium_amount_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_amount_input_edit = QLineEdit( self )

        other_expenses_condominium_amount2_label_edit = QLabel( "Importe" )
        other_expenses_condominium_amount2_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_amount2_input_edit = QLineEdit( self )

        other_expenses_condominium_previous_balance_label_edit = QLabel( "Saldo Anterior" )
        other_expenses_condominium_previous_balance_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_previous_balance_input_edit = QLineEdit( self )

        other_expenses_condominium_USD_label_edit = QLabel( "USD" )
        other_expenses_condominium_USD_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_USD_input_edit = QLineEdit( self )

        other_expenses_condominium_mail_label_edit = QLabel( "Correo del condominio" )
        other_expenses_condominium_mail_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_mail_input_edit = QLineEdit( self )
        
        other_expenses_condominium_change_day_label_edit = QLabel( "Taza del dia" )
        other_expenses_condominium_change_day_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_change_day_input_edit = QLineEdit( self )

        other_expenses_condominium_effective_collection_label_edit = QLabel( "Cobranza Efectiva" )
        other_expenses_condominium_effective_collection_label_edit.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_effective_collection_input_edit = QLineEdit( self )

        self.botton_other_expenses_edit_save = QPushButton( "Guardar" )

        layout_H_7 = QHBoxLayout()
        layout_H_8 = QHBoxLayout()
        layout_H_9 = QHBoxLayout()
        layout_H_10 = QHBoxLayout()
        layout_H_11 = QHBoxLayout()
        layout_H_12 = QHBoxLayout()
        layout_V_3 = QVBoxLayout()

        layout_H_7.addWidget( other_expenses_condominium_code_label_edit )
        layout_H_7.addWidget( self.other_expenses_condominium_code_input_edit )
        layout_H_7.addWidget( self.botton_other_expenses_edit_search )

        layout_H_8.addWidget( other_expenses_condominium_ordinary_expenses_label_edit )
        layout_H_8.addWidget( self.other_expenses_condominium_ordinary_expenses_input_edit )
        layout_H_8.addWidget( other_expenses_condominium_detail_label_edit )
        layout_H_8.addWidget( self.other_expenses_condominium_detail_input_edit )

        layout_H_9.addWidget( other_expenses_condominium_amount_label_edit )
        layout_H_9.addWidget( self.other_expenses_condominium_amount_input_edit )
        layout_H_9.addWidget( other_expenses_condominium_amount2_label_edit )
        layout_H_9.addWidget( self.other_expenses_condominium_amount2_input_edit )

        layout_H_10.addWidget( other_expenses_condominium_previous_balance_label_edit )
        layout_H_10.addWidget( self.other_expenses_condominium_previous_balance_input_edit )
        layout_H_10.addWidget( other_expenses_condominium_USD_label_edit )
        layout_H_10.addWidget( self.other_expenses_condominium_USD_input_edit )

        layout_H_11.addWidget( other_expenses_condominium_mail_label_edit )
        layout_H_11.addWidget( self.other_expenses_condominium_mail_input_edit )

        layout_H_12.addWidget( other_expenses_condominium_change_day_label_edit )
        layout_H_12.addWidget( self.other_expenses_condominium_change_day_input_edit )
        layout_H_12.addWidget( other_expenses_condominium_effective_collection_label_edit )
        layout_H_12.addWidget( self.other_expenses_condominium_effective_collection_input_edit )

        layout_V_3.addWidget( main_title_other_expenses_edit )
        layout_V_3.addLayout( layout_H_7 )
        layout_V_3.addLayout( layout_H_8 )
        layout_V_3.addLayout( layout_H_9 )
        layout_V_3.addLayout( layout_H_10 )
        layout_V_3.addLayout( layout_H_11 )
        layout_V_3.addLayout( layout_H_12 )
        layout_V_3.addWidget( self.botton_other_expenses_edit_save )

        container_edit_other_expenses = QWidget()
        container_edit_other_expenses.setLayout( layout_V_3 )

        #delete other expenses

        main_title_other_expenses_delete = QLabel( "Eliminar Otros Gastos" )
        main_title_other_expenses_delete.setFont( QFont( 'times new roman', 15 ) )
        main_title_other_expenses_delete.setAlignment( Qt.AlignmentFlag.AlignCenter )

        other_expenses_condominium_name_label_delete = QLabel( "Nombre de condominio" )
        other_expenses_condominium_name_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_condominium_name_input_delete = QLineEdit( self )

        other_expenses_date_label_delete = QLabel( "Ingresa la fecha" )
        other_expenses_date_label_delete.setFont( QFont( 'times new roman', 13 ) )

        self.other_expenses_date_delete = QDateEdit()
        self.other_expenses_date_delete.setDisplayFormat( "dd-MM-yyyy" )
        self.other_expenses_date_delete.setMaximumDate(
            QDate.currentDate()
        )
        self.other_expenses_date_delete.setCalendarPopup( True )
        self.other_expenses_date_delete.setDate( QDate.currentDate() )

        self.botton_other_expenses_search_delete = QPushButton( "Buscar" )

        self.botton_other_expenses_delete_delete = QPushButton( "eliminar" )

        layout_H_13 = QHBoxLayout()
        layout_V_4 = QVBoxLayout()

        layout_H_13.addWidget( other_expenses_condominium_name_label_delete )
        layout_H_13.addWidget( self.other_expenses_condominium_name_input_delete )
        layout_H_13.addWidget( other_expenses_date_label_delete )
        layout_H_13.addWidget( self.other_expenses_date_delete )
        layout_H_13.addWidget( self.botton_other_expenses_search_delete )

        layout_V_4.addWidget( main_title_other_expenses_delete )
        layout_V_4.addLayout( layout_H_13 )
        layout_V_4.addWidget( self.botton_other_expenses_delete_delete )

        container_delete_other_expenses = QWidget()
        container_delete_other_expenses.setLayout( layout_V_4 )


        #layout organization
        self.stacked_layout_other_expenses = QStackedLayout()
        self.stacked_layout_other_expenses.addWidget( container_add_other_expenses )
        self.stacked_layout_other_expenses.addWidget( container_search_other_expenses )
        self.stacked_layout_other_expenses.addWidget( container_edit_other_expenses )
        self.stacked_layout_other_expenses.addWidget( container_delete_other_expenses )

        main_layout_other_expenses = QVBoxLayout()
        main_layout_other_expenses.addLayout( bottons_group_other_expenses )
        main_layout_other_expenses.addLayout( self.stacked_layout_other_expenses )

        self.otros_gastos_container.setLayout( main_layout_other_expenses )

    def menuPrincipal( self ):
        self.setGeometry( 100, 100, 400, 400 )
        self.setWindowTitle( "Tucacas desktop" )

        self.conexion = Comunicacion()
        
        self.any_table_condominio =  QTableView()
        self.any_table_servicio =  QTableView()
        self.any_table_mantenimiento =  QTableView()
        self.any_table_reparacion_menor = QTableView()
        self.any_table_aportes_fijos = QTableView()
        self.any_table_otros_gastos = QTableView()

        tab_bar = QTabWidget()

        self.condominium_container = QWidget()
        self.servicion_container = QWidget()
        self.mantenimiento_container = QWidget()
        self.reparacione_menores_container = QWidget()
        self.aportes_fijos_container = QWidget()
        self.otros_gastos_container = QWidget()

        tab_bar.addTab( self.condominium_container, "Condomionio" )
        tab_bar.addTab( self.servicion_container, "Servicios" )
        tab_bar.addTab( self.mantenimiento_container, "Mantemiento" )
        tab_bar.addTab( self.reparacione_menores_container, "Reparaciones menores" )
        tab_bar.addTab( self.aportes_fijos_container, "Aportes fijos" ) 
        tab_bar.addTab( self.otros_gastos_container, "Otros gastos" )

        self.window_condominium_tab()
        self.window_servicio_tab()
        self.window_mantenimiento_tab()
        self.window_reparaciones_menores_tab()
        self.window_aportes_fijos_tab()
        self.window_otros_gastos_tab()

        tab_h_box = QHBoxLayout()
        tab_h_box.addWidget( tab_bar )

        main_container = QWidget()
        main_container.setLayout( tab_h_box )
        self.setCentralWidget( main_container )

    def __init__( self ):
        super().__init__()
        self.menuPrincipal()
        self.status_Bar = QStatusBar()
        self.setStatusBar( self.status_Bar ) 