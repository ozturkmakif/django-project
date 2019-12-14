from django.db import models

# Create your models here.

class article(models.Model):
    author =models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "yazar")
    title = models.CharField(max_length =50,verbose_name = "başlık")
    content = models.TextField(verbose_name = "içerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "oluşturma tarihi")
    def __str__(self):
        return self.title