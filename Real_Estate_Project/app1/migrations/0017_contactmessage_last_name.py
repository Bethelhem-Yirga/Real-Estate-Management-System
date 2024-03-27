

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_merge_0014_contactmessage_0015_application_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='last_name',
            field=models.CharField(default='Your Default Value', max_length=100),
        ),
    ]
