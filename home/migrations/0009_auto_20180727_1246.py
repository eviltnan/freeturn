# Generated by Django 2.0.7 on 2018-07-27 12:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailimages', '0020_add-verbose-name'),
        ('home', '0008_technologiespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', wagtail.core.fields.RichTextField()),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='taggit.Tag')),
            ],
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='technologies',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='projects', through='home.ProjectTechnology', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]