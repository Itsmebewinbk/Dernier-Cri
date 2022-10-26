# Generated by Django 4.1.2 on 2022-10-08 13:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=120, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=120, unique=True)),
                ("img", models.ImageField(max_length=120, null=True, upload_to="")),
                ("price", models.PositiveIntegerField()),
                ("description", models.CharField(max_length=120, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="owner.categories",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comments", models.CharField(max_length=120)),
                (
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="owner.products"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("order-placed", "order-placed"),
                            ("dispatch", "dispatch"),
                            ("in-transit", "in-transit"),
                            ("delivered", "delivered"),
                            ("cancelled", "cancelled"),
                        ],
                        default="order-placed",
                        max_length=120,
                    ),
                ),
                ("delivery_address", models.CharField(max_length=180, null=True)),
                ("expected_delivery_date", models.DateTimeField(null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="owner.products"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Carts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in-cart", "in-cart"),
                            ("order-placed", "order-placed"),
                            ("cancelled", "cancelled"),
                        ],
                        default="in-cart",
                        max_length=120,
                    ),
                ),
                ("qty", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="owner.products"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]