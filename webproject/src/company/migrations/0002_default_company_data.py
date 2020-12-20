# Generated by Django 2.2.4 on 2019-11-22 11:47

from django.db import migrations

def load_company_data(apps,schema_editor):
    """
    These creates the initial company details used as default placeholder.
    """
    DefaultCompany = apps.get_model("company", "Company")
    DefaultUser = apps.get_model("accounts", "User")

    comp = DefaultCompany.objects.create(
        name="Superrecord Management System",
        address="P.O.Box xxx, Kampala",
        company_tel="+2567xxxxxxxx",
        created_by= DefaultUser.objects.get(username="admin")
        )
    comp.save()

class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_company_data)
    ]
