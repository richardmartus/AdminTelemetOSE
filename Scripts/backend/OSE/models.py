from django.db import models


class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45)
    id_region = models.ForeignKey('Regiones', on_delete=models.CASCADE, db_column='id_region')

    def __str__(self):
        return f"{self.departamento}"

    class Meta:
        managed = False
        verbose_name = 'Departamentos'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamentos'


class Localidades(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    localidad = models.CharField(max_length=45)
    id_departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, db_column='id_departamento')

    def __str__(self):
        return self.localidad

    class Meta:
        managed = False
        verbose_name = 'Localidades'
        verbose_name_plural = 'Localidades'
        db_table = 'localidades'


class Regiones(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=45)

    def __str__(self):
        return self.region

    class Meta:
        managed = False
        verbose_name = 'Regiones'
        verbose_name_plural = 'Regiones'
        db_table = 'regiones'


class Sectores(models.Model):
    id_sector = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=45)
    id_localidad = models.ForeignKey(Localidades, on_delete=models.CASCADE, db_column='id_localidad')
    licitacion = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Sectores'
        verbose_name_plural = 'Sectores'
        db_table = 'sectores'


#########################################################################
class Modulo(models.Model):
    modulo_id = models.AutoField(db_column='MODULO_ID', primary_key=True)
    modulo_address = models.CharField(db_column='MODULO_ADDRESS', unique=True, max_length=8)
    modulo_tipo = models.IntegerField(db_column='MODULO_TIPO')
    modulo_factor = models.FloatField(db_column='MODULO_FACTOR', blank=True, null=True)
    modulo_calle = models.CharField(db_column='MODULO_CALLE', max_length=100)
    modulo_numero = models.CharField(db_column='MODULO_NUMERO', max_length=10)
    modulo_letra = models.CharField(db_column='MODULO_LETRA', max_length=10, blank=True, null=True)
    modulo_piso = models.CharField(db_column='MODULO_PISO', max_length=10, blank=True, null=True)
    modulo_puerta = models.CharField(db_column='MODULO_PUERTA', max_length=10, blank=True, null=True)
    modulo_localidad = models.CharField(db_column='MODULO_LOCALIDAD', max_length=100)
    modulo_departamento = models.CharField(db_column='MODULO_DEPARTAMENTO', max_length=45)
    modulo_region = models.CharField(db_column='MODULO_REGION', max_length=45)
    modulo_sector = models.CharField(db_column='MODULO_SECTOR', max_length=45)
    modulo_latitud = models.CharField(db_column='MODULO_LATITUD', max_length=25)
    modulo_longitud = models.CharField(db_column='MODULO_LONGITUD', max_length=25)
    modulo_punto_en_plano = models.IntegerField(db_column='MODULO_PUNTO_EN_PLANO')
    modulo_cliente = models.CharField(db_column='MODULO_CLIENTE', max_length=100)
    modulo_suministro = models.CharField(db_column='MODULO_SUMINISTRO', max_length=45)
    modulo_cuenta = models.CharField(db_column='MODULO_CUENTA', max_length=45)
    modulo_medidor_numero = models.CharField(db_column='MODULO_MEDIDOR_NUMERO', unique=True, max_length=45)
    modulo_medidor_marca = models.CharField(db_column='MODULO_MEDIDOR_MARCA', max_length=45)
    modulo_medidor_modelo = models.CharField(db_column='MODULO_MEDIDOR_MODELO', max_length=45)
    modulo_medidor_diametro = models.CharField(db_column='MODULO_MEDIDOR_DIAMETRO', max_length=4)
    modulo_ultima_lectura_fyh = models.DateTimeField(db_column='MODULO_ULTIMA_LECTURA_FYH', blank=True, null=True)
    modulo_ultima_lectura_valor = models.IntegerField(db_column='MODULO_ULTIMA_LECTURA_VALOR', blank=True, null=True)
    modulo_alarmas = models.CharField(db_column='MODULO_ALARMAS', max_length=8, blank=True, null=True)

    def __str__(self):
        return f"{self.modulo_ultima_lectura_fyh}"

    class Meta:
        managed = False
        db_table = 'modulo'
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulo'


class Gateway(models.Model):
    gateway_id = models.AutoField(db_column='GATEWAY_ID', primary_key=True)
    gateway_address = models.CharField(db_column='GATEWAY_ADDRESS', unique=True, max_length=8)
    gateway_nombre = models.CharField(db_column='GATEWAY_NOMBRE', unique=True, max_length=16)
    gateway_latitud = models.CharField(db_column='GATEWAY_LATITUD', max_length=25)
    gateway_longitud = models.CharField(db_column='GATEWAY_LONGITUD', max_length=25)
    gateway_ubicacion = models.CharField(db_column='GATEWAY_UBICACION', max_length=100)
    gateway_ntrasmisiones = models.IntegerField(db_column='GATEWAY_NTRASMISIONES')
    gateway_nactividad = models.IntegerField(db_column='GATEWAY_NACTIVIDAD')
    gateway_nfalla = models.IntegerField(db_column='GATEWAY_NFALLA')
    gateway_password = models.CharField(db_column='GATEWAY_PASSWORD', max_length=32)

    def __str__(self):
        return self.gateway_address

    class Meta:
        managed = False
        verbose_name = 'Gateway'
        verbose_name_plural = 'Gateway'
        db_table = 'gateway'


class Trasmisiones(models.Model):
    trasmisiones_id = models.AutoField(db_column='TRASMISIONES_ID', primary_key=True)
    trasmisiones_gateway = models.IntegerField(db_column='TRASMISIONES_GATEWAY', blank=True, null=True)
    trasmisiones_signal = models.CharField(db_column='TRASMISIONES_SIGNAL', max_length=5)
    trasmisiones_fyh = models.DateTimeField(db_column='TRASMISIONES_FYH')
    trasmisiones_nlecturas = models.IntegerField(db_column='TRASMISIONES_NLECTURAS')
    trasmisiones_lecturas_mod0 = models.IntegerField(db_column='TRASMISIONES_LECTURAS_MOD0')
    trasmisiones_lecturas_mod1 = models.IntegerField(db_column='TRASMISIONES_LECTURAS_MOD1')
    trasmisiones_lecturas_mod2 = models.IntegerField(db_column='TRASMISIONES_LECTURAS_MOD2')

    class Meta:
        managed = False
        db_table = 'trasmisiones'
        verbose_name = 'Trasmisiones'
        verbose_name_plural = 'Trasmisiones'


class MarcasMedidores(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'marcas_medidores'
        verbose_name = 'Marcas de Medidores'
        verbose_name_plural = 'Marcas de Medidores'


class ModelosMedidores(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'modelos_medidores'
        verbose_name = 'Modelos de Medidores'
        verbose_name_plural = 'Modelos de Medidores'


class Lecturas(models.Model):
    lecturas_id = models.AutoField(db_column='LECTURAS_ID', primary_key=True)  # Field name made lowercase.
    lecturas_modulo_id = models.PositiveIntegerField(db_column='LECTURAS_MODULO_ID')  # Field name made lowercase.
    lecturas_modulo_address = models.CharField(db_column='LECTURAS_MODULO_ADDRESS',
                                               max_length=8)  # Field name made lowercase.
    lecturas_signal = models.CharField(db_column='LECTURAS_SIGNAL', max_length=2)  # Field name made lowercase.
    lecturas_fyh = models.DateTimeField(db_column='LECTURAS_FYH')  # Field name made lowercase.
    lecturas_medida = models.CharField(db_column='LECTURAS_MEDIDA', max_length=8)  # Field name made lowercase.
    lecturas_bateria = models.CharField(db_column='LECTURAS_BATERIA', max_length=4)  # Field name made lowercase.
    lecturas_gateway = models.IntegerField(db_column='LECTURAS_GATEWAY')  # Field name made lowercase.
    lecturas_alarmas = models.CharField(db_column='LECTURAS_ALARMAS', max_length=8)  # Field name made lowercase.
    lecturas_procesada = models.CharField(db_column='LECTURAS_PROCESADA', max_length=1, blank=True,
                                          null=True)  # Field name made lowercase.
    lecturas_fyhrx = models.DateTimeField(db_column='LECTURAS_FYHRX')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lecturas'
        unique_together = (('lecturas_fyh', 'lecturas_modulo_address'),)
        verbose_name = 'Lecturas'
        verbose_name_plural = 'Lecturas'
