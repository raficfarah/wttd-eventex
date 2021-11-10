# Generated by Django 3.1.7 on 2021-11-10 20:53

from django.db import migrations
import uuid

class Migration(migrations.Migration):
    def gen_uuid(apps, schema_editor):
        MyModel = apps.get_model('subscriptions', 'subscription')
        for row in MyModel.objects.all():
            row.uuid = uuid.uuid4()
            row.save(update_fields=['hashid'])

    dependencies = [
        ('subscriptions', '0012_alter_uuid_null'),
    ]

    operations = [
        migrations.RunPython(gen_uuid,
        reverse_code=migrations.RunPython.noop),
    ]