


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_contactmessage_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
