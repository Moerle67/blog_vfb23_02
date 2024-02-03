from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    header = models.CharField(("Überschrift"), max_length=50)
    contents = models.TextField(("Inhalt"))
    written = models.DateTimeField(("Geschrieben"), auto_now=False, auto_now_add=True)
    changed = models.DateTimeField(("Geändert"), auto_now=True, auto_now_add=False)
    rating = models.IntegerField(("Wertung (1-10)"), default = 5)
    author = models.ForeignKey(User, verbose_name=("Autor"), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Tagebuch")
        verbose_name_plural = ("Tagebücher")

    def __str__(self):
        return f"{self.header}/{self.author}({self.written})"  

    # def get_absolute_url(self):
    #     return reverse("Blog_detail", kwargs={"pk": self.pk})
