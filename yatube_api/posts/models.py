from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        'Текст поста',
        help_text='Напишите содержание поста'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True,
        help_text='Выберите сообщество (опционально)'
    )

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return (
            self.text[:15] + ' ' + self.author.get_full_name()
            + ' ' + self.pub_date.strftime('%d.%m.%Y') + ' ' + str(self.group)
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(
        'Текст комментария.',
        help_text='Напишите текст комментария.'
    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    
    class Meta:
        ordering = ('-created', )
    
    def __str__(self):
        return self.text[:15]


class Group(models.Model):
    title = models.CharField(
        'Наименование сообщества',
        max_length=200,
        help_text='Напишите имя сообщества'
    )
    slug = models.SlugField(
        'Slug сообщества',
        unique=True,
        help_text=('Slug сообщества, заполняется автоматом')
    )
    description = models.TextField('Описание сообщества!')

    def __str__(self):
        return self.title[:15]

    class Meta:
        ordering = ('title', )


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             related_name='follower')
    following = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='user_author_constraint')
        ]
