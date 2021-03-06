# Generated by Django 2.1.5 on 2019-01-22 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagulous.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casehistory',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_histories', to=settings.AUTH_USER_MODEL, verbose_name='Editor'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Region', verbose_name='User Region'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Type', verbose_name='Case Type'),
        ),
        migrations.AddField(
            model_name='case',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='cases.Region', verbose_name='User Region'),
        ),
        migrations.AddField(
            model_name='case',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, help_text='Enter a comma-separated tag string', to='cases.Tagulous_Case_tags', verbose_name='Case Tags'),
        ),
        migrations.AddField(
            model_name='case',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='cases.Type', verbose_name='Case Type'),
        ),
    ]
