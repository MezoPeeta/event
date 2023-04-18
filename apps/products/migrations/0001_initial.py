# Generated by Django 4.2 on 2023-04-13 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=15)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=7, null=True),
                ),
                ("start_date", models.DateTimeField(null=True)),
                ("end_date", models.DateTimeField(null=True)),
                ("active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("device", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date_ordered", models.DateTimeField(auto_now_add=True)),
                ("complete", models.BooleanField(default=False)),
                ("transaction_id", models.CharField(max_length=100, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShippingAddress",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.CharField(max_length=200)),
                ("phone_number", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("zipcode", models.CharField(max_length=200)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.customer",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(default="Product Name", max_length=200)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="product_default.jpg", upload_to="products"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=7, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField(blank=True, default=0, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageProducts",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="products")),
                ("default", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
        ),
    ]