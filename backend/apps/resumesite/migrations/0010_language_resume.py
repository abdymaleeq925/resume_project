# Generated by Django 3.2.9 on 2022-07-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0009_alter_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='languagee', to='resumesite.cv'),
            preserve_default=False,
        ),
    ]