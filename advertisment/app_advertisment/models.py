from django.db import models


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата и время изменения', auto_now=True)

def __str__(self):
    return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"    
class Meta:
    db_table = "advertisements"    