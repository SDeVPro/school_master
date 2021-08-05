from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm,TextInput,Textarea,EmailInput
from django.utils.safestring import mark_safe


class SchoolSetting(models.Model):
    title = models.CharField(max_length=222)#nomlanishi 159-maktab
    keywords = models.CharField(max_length=222)#kalit so'zlar rus tilida dars beruvchi maktab
    description = models.CharField(max_length=222)#qisqacha mazmundagi ma'lumot bizda 2000 dan oshiq o'quvchi mavjud
    aboutus = RichTextUploadingField()
    contactus = RichTextUploadingField()
    facebook = models.CharField(max_length=222,blank=True)
    instagram = models.CharField(max_length=222,blank=True)
    email = models.CharField(max_length=222,blank=True)
    tiktok = models.CharField(max_length=222,blank=True)
    youtube = models.CharField(max_length=222,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=222)
    keywords = models.CharField(max_length=222)
    description = models.CharField(max_length=222)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='images')
    author = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))
    image_tag.short_description = 'image'

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    level_years = models.IntegerField()
    image = models.ImageField(upload_to='images')
    classes = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name + self.surname + self.lastname

class Student(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    level_years = models.IntegerField()
    image = models.ImageField(upload_to='images')
    classes = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  self.name + self.surname + self.lastname

class ContactMessage(models.Model):
    STATUS  = (
        ('Yangi','Yangi'),
        ("O'qildi","O'qildi"),
        ("Yopilgan","Yopilgan"),
    )
    name = models.CharField(blank=True,max_length=222)
    email = models.EmailField(blank=True, max_length=222)
    subject = models.TextField(blank=True, max_length=222)
    message = models.TextField(blank=True, max_length=1000)
    status = models.CharField(max_length=15,default='Yangi',choices=STATUS)
    ip = models.CharField(blank=True, max_length=222)
    note = models.CharField(blank=True, max_length=222)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class ContactForm(ModelForm):
    class Meta:#bizni metama'lumotlarimizni ustida ishlovchi class
        model = ContactMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name':TextInput(attrs={'class':'input','placeholder':'Name&Surname'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'Email Address'}),
            'message':Textarea(attrs={'class':'input','placeholder':'Your Message Here','rows':'5'})
        }











