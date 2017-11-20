from django.db import models


class category(models.Model):
    QUESTION = 'Q'
    SOLUTION = 'S'
    UNKNOWN = 'U'
    CATEGORY_CHOICE = (
        ('quiz', (
            (QUESTION, 'Question'),
            (SOLUTION, 'Solution'),
        )
         ),
        (UNKNOWN, 'Unknown'),
    )
    name = models.CharField(max_length=1, choices=CATEGORY_CHOICE)
    image = models.ImageField(upload_to='uploads/category/', default='anonymous.jpg')

    def __str__(self):
        return self.name


class question(models.Model):
    category = models.ForeignKey(to=category, on_delete=models.CASCADE, related_name='question_set')
    title = models.CharField(max_length=20, default='unknown')
    number_of_options = models.IntegerField(default=0)
    options = models.ManyToManyField(to='option', related_name='options_set')  # alternative for options_set
    correct_option = models.OneToOneField(to='option', on_delete=models.CASCADE, default=None,
                                          related_name='correct_option_set')  # alternative for correct_option_set

    @classmethod
    def create_f_j(cls, quetsion):
        j2m = {'title'}
    def __str__(self):
        return "{0}------{1}-----{2}".format(self.title, self.category.name, self.pk)


class option(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class story(models.Model):
    title = models.CharField(max_length=20, default='unknown')
    category = models.ForeignKey(to=category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/story/', default='anonymous.jpg')
    content = models.TextField()
    author = models.CharField(max_length=20, default='anonymous')
    description = models.TextField(default='anonymous')

    def __str__(self):
        return "{0}-------{1}------{2}".format(self.id, self.title, self.description)