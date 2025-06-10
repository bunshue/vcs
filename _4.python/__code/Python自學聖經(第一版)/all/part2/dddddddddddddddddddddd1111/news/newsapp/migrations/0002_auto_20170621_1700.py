from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsunit',
            name='catego',
            field=models.CharField(max_length=10),
        ),
    ]
