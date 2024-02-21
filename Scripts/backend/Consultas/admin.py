from django.contrib import admin
from .models import GatewayActivo, ModuloUltimaLecturaCero, InformeTecnico, ModulosHuerfanos
from django.http import HttpResponseRedirect
from django.urls import reverse


class ModuloUltimaLecturaCeroAdmin(admin.ModelAdmin):
    list_display = ('get_modulo_id', 'get_modulo_address', 'get_modulo_ultima_lectura_valor')
    search_fields = ('modulo__modulo_id', 'modulo__modulo_address', 'modulo__modulo_ultima_lectura_valor')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(modulo__modulo_ultima_lectura_valor=0)

    def get_modulo_id(self, obj):
        return obj.modulo.modulo_id

    def get_modulo_address(self, obj):
        return obj.modulo.modulo_address

    def get_modulo_ultima_lectura_valor(self, obj):
        return obj.modulo.modulo_ultima_lectura_valor

    get_modulo_id.short_description = 'Módulo ID'
    get_modulo_address.short_description = 'Módulo Address'
    get_modulo_ultima_lectura_valor.short_description = 'Módulo Última Lectura Valor'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        modulo_id = ModuloUltimaLecturaCero.objects.get(pk=object_id).modulo.modulo_id
        url = reverse('admin:OSE_modulo_change', args=[modulo_id])
        return HttpResponseRedirect(url)


admin.site.register(ModuloUltimaLecturaCero, ModuloUltimaLecturaCeroAdmin)


class GatewayActivoAdmin(admin.ModelAdmin):
    list_display = ('get_gateway_address', 'get_gateway_nombre')
    search_fields = ('gateway__gateway_address', 'gateway__gateway_nombre')
    list_filter = ('gateway__gateway_address', 'gateway__gateway_nombre')
    ordering = ('gateway__gateway_address', 'gateway__gateway_nombre')

    def get_gateway_address(self, obj):
        return obj.gateway.gateway_address

    def get_gateway_nombre(self, obj):
        return obj.gateway.gateway_nombre

    get_gateway_address.short_description = 'Gateway Address'
    get_gateway_nombre.short_description = 'Gateway Nombre'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(gateway__gateway_address__startswith='100100')


admin.site.register(GatewayActivo, GatewayActivoAdmin)


class InformeTecnicoAdmin(admin.ModelAdmin):
    search_fields = ['modulo__modulo_localidad', 'modulo__modulo_address', 'modulo__modulo_cliente']
    list_filter = ['modulo__modulo_localidad']

    def get_modulo_address(self, obj):
        return obj.modulo.modulo_address

    def get_modulo_localidad(self, obj):
        return obj.modulo.modulo_localidad

    def get_modulo_calle(self, obj):
        return obj.modulo.modulo_calle

    def get_modulo_numero(self, obj):
        return obj.modulo.modulo_numero

    def get_modulo_punto_en_plano(self, obj):
        return obj.modulo.modulo_punto_en_plano

    def get_modulo_medidor_numero(self, obj):
        return obj.modulo.modulo_medidor_numero

    def get_modulo_cliente(self, obj):
        return obj.modulo.modulo_cliente

    def get_modulo_ultima_lectura_valor(self, obj):
        return obj.modulo.modulo_ultima_lectura_valor

    def get_modulo_ultima_lectura_fyh(self, obj):
        return obj.modulo.modulo_ultima_lectura_fyh

    def get_modulo_alarmas(self, obj):
        return obj.modulo.modulo_alarmas

    get_modulo_address.short_description = 'Modulo Address'
    get_modulo_localidad.short_description = 'Modulo Localidad'
    get_modulo_calle.short_description = 'Modulo Calle'
    get_modulo_numero.short_description = 'Modulo Numero'
    get_modulo_punto_en_plano.short_description = 'Modulo Punto en Plano'
    get_modulo_medidor_numero.short_description = 'Modulo Medidor Numero'
    get_modulo_cliente.short_description = 'Modulo Cliente'
    get_modulo_ultima_lectura_valor.short_description = 'Modulo Ultima Lectura Valor'
    get_modulo_ultima_lectura_fyh.short_description = 'Modulo Ultima Lectura FYH'
    get_modulo_alarmas.short_description = 'Modulo Alarmas'

    list_display = (
        'get_modulo_address', 'get_modulo_localidad', 'get_modulo_calle', 'get_modulo_numero',
        'get_modulo_punto_en_plano', 'get_modulo_medidor_numero', 'get_modulo_cliente',
        'get_modulo_ultima_lectura_valor', 'get_modulo_ultima_lectura_fyh', 'get_modulo_alarmas'
    )


admin.site.register(InformeTecnico, InformeTecnicoAdmin)

