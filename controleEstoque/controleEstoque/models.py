from django.db import models


# comunicacao com o banco de dados 

#bd ESTOQUE
class estoqueinsert(models.Model):
    nome_pr=models.CharField(max_length=50)
    qtde_pr=models.IntegerField
    valor=models.DecimalField(max_digits=15, decimal_places=2,)
    class Meta:
        db_table="cEstoque"

#bd USUARIO
class usuarioinsert(models.Model):
    nome_user=models.CharField(max_length=50)
    email_user=models.CharField(max_length=50)
    senha_user=models.CharField(max_length=50)
    dn_user=models.DateField
    sexo_user=models.CharField(max_length=9)
    end_user=models.CharField(max_length=80)
    end_n_user=models.IntegerField(max_length=10)
    est_user=models.CharField(max_length=10)
    class Meta:
        db_table="cUser"
