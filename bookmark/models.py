from django.db import models


# Create your models here.
class BookMark(models.Model):
    TAG = (
        ('product', 'product'),
        ('bookmark', 'bookmark'),
        ('docs', 'docs'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField('名称', max_length=255)
    desc = models.CharField('描述', max_length=255)
    pic = models.CharField('图片', max_length=255)
    url = models.CharField('链接', max_length=255)
    tag = models.CharField('标签', choices=TAG, max_length=255)

    class Meta:
        verbose_name = '我的书签'
        verbose_name_plural = verbose_name
        db_table = 'bookmark'
        ordering = ['id']

    def __unicode__(self):
        return f"{self.name}"
