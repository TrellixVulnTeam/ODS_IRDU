# Generated by Django 2.0.1 on 2018-01-03 12:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dept',
            name='user',
        ),
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rank',
            name='user',
        ),
        migrations.RemoveField(
            model_name='type',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='userDeptDR',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='user.Dept'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userGroupDR',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='user.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userRankDR',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.Rank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userTypeDR',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='user.Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dept',
            name='deptStDatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='group',
            name='groupStDatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='rankStDatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='type',
            name='typeStDatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userStDatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
    ]
