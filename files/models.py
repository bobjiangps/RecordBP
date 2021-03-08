from django.db import models
from django.utils import timezone
# from ckeditor_uploader.fields import RichTextUploadingField
import os


class Files(models.Model):
    name = models.CharField(max_length=100, verbose_name="文件名")
    path = models.CharField(max_length=500, verbose_name="文件路径")
    content = models.TextField(verbose_name="文件内容")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=timezone.now, verbose_name="更新时间")

    def __str__(self):
        return self.name

    def save(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        file_full_path = os.path.join(self.path, self.name)
        with open(file_full_path, "w") as f:
            f.write(self.content)
        super().save()

    class Meta:
        verbose_name_plural = "文件"
