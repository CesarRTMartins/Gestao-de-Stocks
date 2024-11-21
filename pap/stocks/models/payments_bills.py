from django.db import models

class PaymentType(models.Model):
    # Atributos da tabela
    paymentType = models.CharField(max_length=200)  # Tipo de Pagamento
    active = models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)  # Activo ou não