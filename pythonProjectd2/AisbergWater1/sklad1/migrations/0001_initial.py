# Generated by Django 4.2.14 on 2024-08-23 07:55

from decimal import Decimal
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(editable=False, max_length=50, unique=True)),
                ('production_date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(choices=[('g', 'Граммы'), ('pcs', 'Штуки'), ('l', 'Литры')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('gram', 'Грамм'), ('piece', 'Штука'), ('liter', 'Литр')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gtin', models.CharField(max_length=50)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.line')),
            ],
            options={
                'unique_together': {('name', 'line')},
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipment_date', models.DateField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.batch')),
                ('counterparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.counterparty')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('material', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sklad1.material')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.batch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.product')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sklad1.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='FinishedGoodsStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=50)),
                ('production_date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('is_used', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.product')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.line'),
        ),
        migrations.AddField(
            model_name='batch',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.product'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('material_warehouse_manager', 'Начальник склада материалов'), ('finished_goods_warehouse_manager', 'Начальник склада готовой продукции'), ('sales_director', 'Директор по продажам')], max_length=40)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad1.product')),
            ],
            options={
                'unique_together': {('product', 'material')},
            },
        ),
    ]
