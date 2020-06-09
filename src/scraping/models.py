from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City name',unique=True)
    slug = models.CharField(max_length=50,blank=True, unique=True)

    class Meta:
        verbose_name = 'City name'
        verbose_name_plural = 'City names'
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = str(self.name).upper()
        super().save(*args,**kwargs)

class Language(models.Model):
    name = models.CharField(max_length=50,verbose_name='Language',unique=True)
    slug = models.CharField(max_length=50,blank=True, unique=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languagies'
    
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Title')
    company = models.CharField(max_length=250, verbose_name='From company')
    discription = models.TextField(verbose_name='Discription')
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    timeStamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
    
    def __str__(self):
        return self.title