from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import DateTimeWidget

from .models import Departamentos, Regiones, Localidades, Sectores, Modulo, Gateway, Trasmisiones, MarcasMedidores, \
    ModelosMedidores, Lecturas


class DepartamentosResource(resources.ModelResource):
    class Meta:
        model = Departamentos
        import_id_fields = ('id_departamento',)


class DepartamentosAdmin(ImportExportModelAdmin):
    resource_class = DepartamentosResource

    list_display = ('departamento', 'region_name')
    list_filter = ('departamento', 'id_region__region')
    search_fields = ('departamento', 'id_region__region')
    ordering = ['id_region__region']
    raw_id_fields = ['id_region']

    def region_name(self, obj):
        return obj.id_region.region

    region_name.short_description = 'Región'


admin.site.register(Departamentos, DepartamentosAdmin)


class LocalidadesResource(resources.ModelResource):
    class Meta:
        model = Localidades
        import_id_fields = ('id_localidad',)


class LocalidadesAdmin(ImportExportModelAdmin):
    resource_class = LocalidadesResource
    list_display = ('localidad', 'departamento_name')
    list_filter = ('localidad', 'id_departamento__departamento')
    search_fields = ('localidad', 'id_departamento__departamento')
    ordering = ['id_departamento']

    def departamento_name(self, obj):
        return obj.id_departamento.departamento

    departamento_name.short_description = 'Departamento'


admin.site.register(Localidades, LocalidadesAdmin)


class SectoresResource(resources.ModelResource):
    class Meta:
        model = Sectores
        import_id_fields = ('id_sector', 'id_localidad')


class SectoresAdmin(ImportExportModelAdmin):
    resource_class = SectoresResource
    list_display = ('sector', 'localidad', 'licitacion')
    list_filter = ('id_localidad', 'licitacion')
    search_fields = ('id_localidad', 'licitacion')
    ordering = ['id_sector']
    raw_id_fields = ['id_localidad']

    def localidad(self, obj):
        return obj.id_localidad.localidad

    localidad.short_description = 'Localidad'


admin.site.register(Sectores, SectoresAdmin)


class RegionesResource(resources.ModelResource):
    class Meta:
        model = Regiones
        import_id_fields = ('id_region',)


class RegionesAdmin(ImportExportModelAdmin):
    resource_class = RegionesResource
    list_display = ('id_region', 'region')
    list_filter = ('region',)
    search_fields = ('region',)
    ordering = ['region', ]

    def localidad(self, obj):
        return obj.id_localidad.localidad

    localidad.short_description = 'Región'


admin.site.register(Regiones, RegionesAdmin)


#########################################################################################
class ModuloResource(resources.ModelResource):
    # modulo_ultima_lectura_fyh = Field(
    #     column_name='modulo_ultima_lectura_fyh',
    #     attribute='modulo_ultima_lectura_fyh',
    #     widget=DateTimeWidget(format="%Y-%m-%d %H:%M:%S")
    # )
    #
    # def get_export_value(self, field, obj):
    #     if field.attribute == 'modulo_ultima_lectura_fyh':
    #         value = getattr(obj, field.attribute)
    #
    #         return value.strftime("%Y-%m-%d %H:%M:%S") if value else None
    #     return super().get_export_value(field, obj)

    class Meta:
        model = Modulo
        import_id_fields = ('modulo_id',)


class ModuloAdmin(ImportExportModelAdmin):
    resource_class = ModuloResource
    list_display = (
        'modulo_id', 'modulo_localidad', 'modulo_sector', 'modulo_address', 'modulo_tipo', 'modulo_factor',
        'modulo_calle',
        'modulo_numero', 'modulo_letra', 'modulo_piso', 'modulo_puerta', 'modulo_departamento', 'modulo_region',
        'modulo_latitud', 'modulo_longitud', 'modulo_punto_en_plano', 'modulo_cliente', 'modulo_suministro',
        'modulo_cuenta', 'modulo_medidor_numero', 'modulo_medidor_marca', 'modulo_medidor_modelo',
        'modulo_medidor_diametro', 'modulo_ultima_lectura_fyh', 'modulo_ultima_lectura_valor', 'modulo_alarmas')
    list_filter = (
        'modulo_id', 'modulo_address', 'modulo_localidad', 'modulo_sector', 'modulo_region', 'modulo_departamento',
        'modulo_suministro', 'modulo_tipo', 'modulo_medidor_numero')
    search_fields = (
        'modulo_localidad__localidad', 'modulo_sector', 'modulo_address', 'modulo_cliente', 'modulo_suministro',
        'modulo_cuenta', 'modulo_medidor_numero', 'modulo_alarmas')
    ordering = ['modulo_region', 'modulo_departamento', 'modulo_localidad', 'modulo_sector', 'modulo_address']

    def modulo_localidad(self, obj):
        return obj.modulo_localidad.localidad

    modulo_localidad.short_description = 'Localidad'


admin.site.register(Modulo, ModuloAdmin)


class GatewayResource(resources.ModelResource):
    class Meta:
        model = Gateway
        import_id_fields = ('gateway_address',)


class GatewayAdmin(ImportExportModelAdmin):
    resource_class = GatewayResource

    list_display = ('gateway_address', 'gateway_nombre', 'display_gateway_latitud', 'display_gateway_longitud',
                    'display_gateway_ubicacion', 'gateway_ntrasmisiones', 'gateway_nactividad', 'gateway_nfalla')
    search_fields = ('gateway_address', 'gateway_nombre', 'gateway_latitud', 'gateway_longitud', 'gateway_ubicacion')
    list_filter = ('gateway_address', 'gateway_nombre')

    def display_gateway_latitud(self, obj):
        return obj.gateway_latitud

    display_gateway_latitud.short_description = 'Latitud'

    display_gateway_latitud.admin_order_field = 'gateway_latitud'
    display_gateway_latitud.allow_tags = False
    display_gateway_latitud.empty_value_display = '-empty-'

    def display_gateway_longitud(self, obj):
        return obj.gateway_longitud

    display_gateway_longitud.short_description = 'Longitud'

    display_gateway_longitud.admin_order_field = 'gateway_longitud'
    display_gateway_longitud.allow_tags = False
    display_gateway_longitud.empty_value_display = '-empty-'

    def display_gateway_ubicacion(self, obj):
        return obj.gateway_ubicacion

    display_gateway_ubicacion.short_description = 'Ubicación'

    display_gateway_ubicacion.admin_order_field = 'gateway_ubicacion'
    display_gateway_ubicacion.allow_tags = False
    display_gateway_ubicacion.empty_value_display = '-empty-'


admin.site.register(Gateway, GatewayAdmin)


class TrasmisionesAdmin(admin.ModelAdmin):
    list_display = (
        'trasmisiones_id', 'trasmisiones_gateway', 'trasmisiones_signal', 'trasmisiones_fyh', 'trasmisiones_nlecturas',
        'trasmisiones_lecturas_mod0', 'trasmisiones_lecturas_mod1', 'trasmisiones_lecturas_mod2')
    search_fields = ('trasmisiones_gateway', 'trasmisiones_fyh')
    list_filter = ('trasmisiones_gateway', 'trasmisiones_fyh')


admin.site.register(Trasmisiones, TrasmisionesAdmin)


class MarcasMedidoresResource(resources.ModelResource):
    class Meta:
        model = MarcasMedidores
        import_id_fields = ('id_marca',)


class MarcasMedidoresAdmin(ImportExportModelAdmin):
    resource_class = MarcasMedidoresResource
    list_display = ['marca']
    search_fields = ['marca']


admin.site.register(MarcasMedidores, MarcasMedidoresAdmin)


class ModelosMedidoresResource(resources.ModelResource):
    class Meta:
        model = ModelosMedidores
        import_id_fields = ('id_modelo',)


class ModelosMedidoresAdmin(ImportExportModelAdmin):
    resource_class = ModelosMedidoresResource
    list_display = ['modelo']
    search_fields = ['modelo']


admin.site.register(ModelosMedidores, ModelosMedidoresAdmin)


class LecturasAdmin(admin.ModelAdmin):
    list_display = ('lecturas_id', 'lecturas_modulo_id', 'lecturas_modulo_address', 'lecturas_signal', 'lecturas_fyh',
                    'lecturas_medida', 'lecturas_bateria', 'lecturas_gateway', 'lecturas_alarmas', 'lecturas_procesada',
                    'lecturas_fyhrx')
    search_fields = ('lecturas_id', 'lecturas_modulo_id', 'lecturas_modulo_address', 'lecturas_signal', 'lecturas_fyh',
                     'lecturas_medida', 'lecturas_bateria', 'lecturas_gateway', 'lecturas_alarmas',
                     'lecturas_procesada', 'lecturas_fyhrx')

    list_filter = ('lecturas_id', 'lecturas_modulo_id', 'lecturas_modulo_address')


admin.site.register(Lecturas, LecturasAdmin)
