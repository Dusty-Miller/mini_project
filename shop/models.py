from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return f'{self.name} - {self.slug}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(null=True)
    size = models.CharField(max_length=10, null=True)
    shoulder= models.FloatField(null=True, blank=True)
    chest= models.FloatField(null=True, blank=True)
    somae= models.FloatField(null=True, blank=True)
    chongjang= models.FloatField(null=True, blank=True)
    waist= models.FloatField(null=True, blank=True)
    bottom_top= models.FloatField(null=True, blank=True)
    thigh= models.FloatField(null=True, blank=True)
    mit_dan= models.FloatField(null=True, blank=True)
    uploaded_image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.category}'

    @property
    def summary(self):
        field_labels = {
            "shoulder": "어깨",
            "chest": "가슴",
            "somae": "소매",
            "chongjang": "총장",
            "waist": "허리",
            "bottom_top": "밑위",
            "thigh": "허벅지",
            "mit_dan": "밑단",
        }
        parts = []
        for field, label in field_labels.items():
            v = getattr(self, field)
            if v not in (None, ""):
                parts.append(f"{label}: {v}")
        return " / ".join(parts)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Image for {self.post.title}'