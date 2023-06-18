# Generated by Django 3.2.5 on 2022-03-02 06:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0002_auto_20220302_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('middlename', models.TextField(blank=True, null=True)),
                ('lastname', models.TextField()),
                ('address', models.TextField()),
                ('contact', models.TextField()),
                ('email', models.TextField()),
                ('date_hired', models.DateField()),
                ('salary', models.FloatField(default=0)),
                ('status', models.IntegerField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('projet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.projet')),
                ('tache_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.tache')),
            ],
        ),
    ]
