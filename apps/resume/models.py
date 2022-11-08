from django.db import models


class Resume(models.Model):
    class GenderChoices(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'


    class WorkExperience(models.TextChoices):
        HAVE = 'Have work experience'
        HAVE_NOT = 'No work expirience'


    """Резюме"""

    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    email = models.EmailField(
        "Почта",
        unique=True
    )
    phone = models.CharField(
        "Телефон",
        max_length=11, 
        unique=True
    )
    hometown = models.CharField("Город проживания", max_length=100)
    data_of_birth= models.DateTimeField("Дата рождения")
    age = models.IntegerField("Возраст")
    gender = models.CharField(
        "Пол", 
        max_length=8, 
        choices=GenderChoices.choices, 
        default=GenderChoices.FEMALE
    )
    work_experience = models.CharField(
        "Опыт работы", 
        max_length=35, 
        choices=WorkExperience.choices,
        default=WorkExperience.HAVE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Резюме пользователя"
        verbose_name_plural = "Резюме пользователей"