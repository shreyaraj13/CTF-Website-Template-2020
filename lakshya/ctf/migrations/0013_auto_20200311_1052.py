# Generated by Django 2.2.5 on 2020-03-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0012_auto_20200310_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='clg',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='year',
        ),
        migrations.AddField(
            model_name='questions',
            name='category',
            field=models.CharField(choices=[('category_web', 'category_web'), ('category_reversing', 'category_reversing'), ('category_steg', 'category_steg'), ('category_pwning', 'category_pwning'), ('category_misc', 'category_misc'), ('category_crypt', 'category_crypt')], default='category_steg', max_length=2),
        ),
        migrations.AddField(
            model_name='questions',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='submission',
            name='curr_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='level',
            field=models.CharField(choices=[('E', 'easy'), ('M', 'medium'), ('H', 'hard')], default='H', max_length=2),
        ),
        migrations.AlterField(
            model_name='submission',
            name='sub_time',
            field=models.TimeField(default='00:00'),
        ),
    ]
