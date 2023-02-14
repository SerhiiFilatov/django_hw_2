from django.db import models



class Type_of_car(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Car (models.Model):
    type_of_car = models.ForeignKey(Type_of_car, on_delete=models.PROTECT)
    age = models.PositiveIntegerField(default=0)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=32, null=True)
    engine = models.CharField(max_length=32, null=True)
    created = models.DateField(auto_now_add=True, verbose_name='Створено')

    def __str__(self):
        return '%s %s' % (self.type_of_car, self.model)

    class Meta:
        db_table = '1989'     # изменить название таблицы в бд
        verbose_name = 'Car' # изменить название таблицы в админке джанго
        unique_together = 'type_of_car', 'model' # делает значения уникальными сразу 2 атр


tasks = [
    {
        "id": 1,
        "title": "Descriptive ",
        "description": "Some long task description...",
        "created": '2022-01-24 12:00',
        "updated": "2022-01-25 12:00",
        "completed": False
    },
    {
        "id": 2,
        "title": "Descriptive task ",
        "description": "Some long task description...",
        "created": '2022-01-24 12:00',
        "updated": "2022-01-25 12:00",
        "completed": False
    },
    {
        "id": 3,
        "title": "Descriptive task title",
        "description": "Some long task description...",
        "created": '2022-01-24 12:00',
        "updated": "2022-01-25 12:00",
        "completed": True
    }
]


