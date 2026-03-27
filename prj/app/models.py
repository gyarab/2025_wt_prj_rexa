from django.db import models


class Kategorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE_CHOICES = [
        ("noob", "Začátečník"),
        ("intermediate", "Pokročilý"),
        ("pro", "Profík"),
    ]

    name = models.CharField(max_length=100)
    minecraft_username = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.minecraft_username})"


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
    hotbar = models.TextField()
    options_txt = models.TextField()

    def __str__(self):
        return f"Settings pro {self.user.name}"


class Taktika(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField()  # 1–5
    effectivity = models.IntegerField()  # 1–10
    usefulness = models.IntegerField()  # 1–10

    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE, related_name="taktiky")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="taktiky")

    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
