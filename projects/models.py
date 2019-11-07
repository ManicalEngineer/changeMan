from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Project(models.Model):
    PROJ_TYPES = (
        ('RD', 'Research & Development'),
        ('PJ', 'Improvement Project'),
        ('CS', 'Custom Variation'),
    )

    title = models.CharField(max_length=40)
    create_date = models.DateField(auto_now_add=True)
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Project")
    engineer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.CharField(max_length=300)
    proj_type = models.CharField(max_length=3, choices=PROJ_TYPES, default='RD')


class Requirement(models.Model):
    create_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    description = models.CharField(max_length=40)
    justification = models.CharField(max_length=300)
    shall = models.BooleanField(default=False)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    approved = models.BooleanField(default=False)
    approved_date = models.DateField()

    def __str__(self):
        return self.description


class Specification(models.Model):
    VALUE_TYPE = (
        ("BOO", "True or False"),
        ("LESS", "Less Than"),
        ("MORE", "More Than"),
        ("RANGE", "Between"),
    )
    create_date = models.DateField(auto_now_add=True)
    requirements = models.ManyToManyField("Requirement", verbose_name="Satisfies Requirement(s)")
    value_type = models.CharField(max_length=5, choices=VALUE_TYPE, default='LESS')
    goal_value = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    approved = models.BooleanField(default=False)
    approved_date = models.DateField()


class Concept(models.Model):
    create_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    media = models.FileField(upload_to='projects/')
    grade = models.DecimalField(decimal_places=2, max_digits=5)
    selected = models.BooleanField(default=False)


class Rating(models.Model):
    concept = models.ForeignKey('Concept', on_delete=models.CASCADE)
    requirement = models.ForeignKey('Requirement', on_delete=models.CASCADE)
    value = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Idea(models.Model):
    create_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)


class Feedback(models.Model):
    STAGE_OPS = (
        ('RQ', 'Requirements/Specifications'),
        ('CON', 'Concept Design'),
        ('PT', 'Construction/Prototype'),
    )
    create_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    stage = models.CharField(max_length=3, choices=STAGE_OPS, default='RQ')
    resolved = models.BooleanField(default=False)
