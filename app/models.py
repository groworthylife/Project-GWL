from django.db import models
from base.models import BaseModel


class ContactUsModel(BaseModel):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    msg = models.TextField()
    def __str__(self):
        return self.name


class ClassModel(BaseModel):
    std = models.CharField(max_length=10)
    def __str__(self):
        return self.std
    class Meta:
        db_table = 'class'


class SubjectsModel(BaseModel):
    std = models.ForeignKey(ClassModel, related_name="class_subjects", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name
    class Meta:
        db_table = 'subject-name'


class ChapterModel(BaseModel):
    subject = models.ForeignKey(SubjectsModel, related_name="subject_notes", on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    def __str__(self):
        return self.chapter_name
    class Meta:
        db_table = 'chapter'
