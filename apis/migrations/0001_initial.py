# Generated by Django 3.0.4 on 2020-04-11 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('Item_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('Item_Group_Code', models.IntegerField()),
                ('Company_Item_code', models.IntegerField()),
                ('Company_Code', models.IntegerField()),
                ('Photo', models.ImageField(upload_to='Item')),
                ('Description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Item_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('Item_Group_Code', models.IntegerField()),
                ('Company_Item_code', models.IntegerField()),
                ('Company_Code', models.IntegerField()),
                ('Photo', models.ImageField(upload_to='Item')),
                ('Description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemAssign',
            fields=[
                ('Item_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('Item_Group_Code', models.IntegerField()),
                ('Company_Item_code', models.IntegerField()),
                ('Company_Code', models.IntegerField()),
                ('Photo', models.ImageField(upload_to='Item')),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='managers')),
                ('Age', models.IntegerField()),
                ('user_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('Item_Ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Salesperson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='salesperson')),
                ('Age', models.IntegerField()),
                ('last_location_lat', models.FloatField()),
                ('last_location_long', models.FloatField()),
                ('Managed_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.Manager')),
                ('User_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assigned_Date', models.DateField()),
                ('Assigned_Time', models.TimeField()),
                ('Quantity', models.IntegerField()),
                ('Completed', models.BooleanField()),
                ('Notes', models.TextField()),
                ('Assigned_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.Manager')),
                ('Assigned_To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Salesperson')),
                ('Item_Ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Item_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('Item_Group_Code', models.IntegerField()),
                ('Company_Item_code', models.IntegerField()),
                ('Company_Code', models.IntegerField()),
                ('Photo', models.ImageField(upload_to='Item')),
                ('Description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('Issued_To', models.CharField(max_length=100)),
                ('Buyer_Contact', models.IntegerField()),
                ('Buyer_email', models.CharField(max_length=100)),
                ('SoftCopy', models.FileField(upload_to='Bills')),
                ('Salesperson_Ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.Salesperson')),
            ],
        ),
    ]
