from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=120, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    avatar_url = models.URLField(blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Skill(models.Model):
    name = models.CharField(max_length=120)
    level = models.CharField(max_length=80, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]


class Experience(models.Model):
    company = models.CharField(max_length=160)
    title = models.CharField(max_length=160)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} @ {self.company}"

    class Meta:
        ordering = ["order", "-start_date"]


class Education(models.Model):
    institution = models.CharField(max_length=160)
    degree = models.CharField(max_length=160)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

    class Meta:
        ordering = ["order", "-start_date"]


class Project(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    link = models.URLField(blank=True)
    repo = models.URLField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    image_url = models.URLField(blank=True)
    show_in_portfolio = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order", "title"]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ["-created_at"]
