from django.db import models



class Music(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to="images/",default="")
    Sname = models.CharField(max_length=70,default="")
    pub_date = models.DateField(default="")
    Singer = models.CharField(max_length=20,default="")
    disc = models.CharField(max_length=500,default="")
    link = models.URLField(max_length=150)
    song = models.FileField(upload_to='songs/',default="")

    def __str__(self):
        return self.Sname


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20,default="")
    Email = models.CharField(max_length=30,default="")
    Phone = models.CharField(max_length=10,default="")
    desc = models.CharField(max_length=700,default="")

    def __str__(self):
        return self.Name



