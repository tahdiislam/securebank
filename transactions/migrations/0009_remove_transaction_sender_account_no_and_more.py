# Generated by Django 5.0.6 on 2024-05-23 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('transactions', '0008_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='sender_account_no',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver_account_no',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userbankaccount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(3, 'Loan'), (1, 'Deposit'), (5, 'Money Transfer'), (4, 'Loan Paid'), (2, 'Withdrawal')], null=True),
        ),
    ]
