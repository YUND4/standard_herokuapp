from django.db import models

class Contact(models.Model):
    firstname = models.CharField(max_length=55, verbose_name='✒️ Nombres')
    lastname = models.CharField(max_length=55, verbose_name='✒️ Apellidos')
    phone = models.BigIntegerField(verbose_name=' 📱 Telefono')
    email = models.EmailField(verbose_name='📫 Correo electronico')
    infromation = models.TextField(max_length=500, verbose_name='💬 Informacion adicional', blank=True, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname