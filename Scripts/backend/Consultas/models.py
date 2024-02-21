from django.db import models
from OSE.models import Gateway, Modulo, Lecturas


class GatewayActivo(models.Model):
    gateway = models.OneToOneField(Gateway, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = False
        db_table = 'gateway'
        verbose_name = 'Gateway Activo'
        verbose_name_plural = 'Gateways Activos'

    def __str__(self):
        return str(self.gateway)


class ModuloUltimaLecturaCero(models.Model):
    modulo = models.OneToOneField(Modulo, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = False
        db_table = 'modulo'
        verbose_name = 'Módulo Últ. Lectura 0'
        verbose_name_plural = 'Módulos Últ. Lectura 0'

    def __str__(self):
        return f"{self.modulo.modulo_address} (ID: {self.modulo.modulo_id})"


class InformeTecnico(models.Model):
    modulo = models.OneToOneField(Modulo, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = False
        db_table = 'modulo'
        verbose_name = 'Informe Tecnico'
        verbose_name_plural = 'Informe Tecnico'


class ModulosHuerfanos(models.Model):
    lecturas_modulo_id = models.PositiveIntegerField()
    lecturas_modulo_address = models.CharField(max_length=8)
    lecturas_medida = models.CharField(max_length=8)
    lecturas_alarmas = models.CharField(max_length=8)
    lecturas_gateway = models.OneToOneField(Gateway, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'modulos_huerfanos'
        unique_together = (('lecturas_modulo_id', 'lecturas_modulo_address'),)
        verbose_name = 'Modulos Huerfanos'
        verbose_name_plural = 'Modulos Huerfanos'
