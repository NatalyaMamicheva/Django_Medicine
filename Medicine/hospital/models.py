from django.db import models


class Doctor(models.Model):
    first_last_middle_name = models.CharField(
        max_length=100,
        verbose_name='ФИО')
    age = models.CharField(max_length=3,
                           verbose_name='Возраст')
    position = models.CharField(
        max_length=60,
        verbose_name='Должность')

    def __str__(self):
        return f'{self.first_last_middle_name}({self.position}).'

    class Meta:
        verbose_name_plural = 'Доктор'


class Patient(models.Model):
    first_last_middle_name = models.CharField(
        max_length=100,
        verbose_name='ФИО')
    age = models.CharField(max_length=3,
                           verbose_name='Возраст')
    address = models.TextField(
        verbose_name='Адрес_проживания')
    gender = models.CharField(
        max_length=1,
        verbose_name='Пол')

    def __str__(self):
        return f'{self.first_last_middle_name}({self.age} лет)'

    class Meta:
        verbose_name_plural = 'Пациент'


class Reception(models.Model):
    date = models.DateField(verbose_name='Дата_приема')
    disease = models.TextField(
        verbose_name='Заболевание')
    cost = models.FloatField(
        verbose_name='Стоимость_приема')
    doctor_name = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name='Доктор'
    )
    patient_name = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='Пациент'
    )

    def __str__(self):
        return f'Дата: {self.date}. {self.doctor_name}.  ' \
               f'{self.patient_name}.'

    class Meta:
        verbose_name_plural = 'Прием'
