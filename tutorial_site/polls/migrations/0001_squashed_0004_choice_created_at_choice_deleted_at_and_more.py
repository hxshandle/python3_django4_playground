# Generated by Django 4.2.4 on 2023-08-20 06:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [
        ("polls", "0001_initial"),
        ("polls", "0002_group_person_membership_group_members"),
        ("polls", "0003_person_groups"),
        ("polls", "0004_choice_created_at_choice_deleted_at_and_more"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("question_text", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, default=django.utils.timezone.now
                    ),
                ),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
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
                ("date_joined", models.DateField()),
                ("invite_reason", models.CharField(max_length=64)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.group"
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.person"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(through="polls.Membership", to="polls.person"),
        ),
        migrations.AddField(
            model_name="person",
            name="groups",
            field=models.ManyToManyField(through="polls.Membership", to="polls.group"),
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("choice_text", models.CharField(max_length=200)),
                ("votes", models.PositiveIntegerField(default=0)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.question"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, default=django.utils.timezone.now
                    ),
                ),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="group",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="group",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="person",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
