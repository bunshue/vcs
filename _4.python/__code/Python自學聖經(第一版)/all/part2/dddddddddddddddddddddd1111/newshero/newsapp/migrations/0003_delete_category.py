from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20170621_1700'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
