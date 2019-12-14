from django.test import TestCase

# Create your tests here.

class article(models.model):
    author = models.Foreignkey("auth.User",on_delete = models.CASCADE)
    Ttitle = models.CharField(max_length = 50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)