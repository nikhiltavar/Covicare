from django.db import models

class Tags(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Tags'



class News(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateField()
    img = models.ImageField(upload_to='newsimgs')
    tags = models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='News'





