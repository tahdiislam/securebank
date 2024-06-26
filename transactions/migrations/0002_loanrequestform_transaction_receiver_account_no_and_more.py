# Generated by Django 5.0.6 on 2024-05-23 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanRequestForm',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transactions.transaction')),
            ],
            bases=('transactions.transaction',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_account_no',
            field=models.IntegerField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_account_no',
            field=models.IntegerField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(2, 'Withdrawal'), (3, 'Loan'), (1, 'Deposit'), (4, 'Loan Paid'), (5, 'Money Transfer')], null=True),
        ),
    ]
