# Generated by Django 4.2.3 on 2023-08-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelos", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-created"],
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="precio",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de creacion"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(verbose_name="Descripcion"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="project", verbose_name="Imagen"),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Titulo"),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion"),
        ),
    ]
