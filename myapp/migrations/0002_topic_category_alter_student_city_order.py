# Generated by Django 4.0.5 on 2022-06-05 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(choices=[('WS', 'Windsor'), ('CG', 'Calgary'), ('MR', 'Montreal'), ('VC', 'Vancouver')], default='WS', max_length=2),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.PositiveIntegerField()),
                ('order_status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Order Confirmed')], default=1)),
                ('order_date', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myapp.student')),
            ],
        ),
    ]
