# Generated by Django 4.1 on 2022-08-11 05:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=20, null=True)),
                ('account_balance', models.IntegerField()),
                ('account_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=20, null=True)),
                ('symbol', models.CharField(max_length=20, null=True)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=20, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_currency', to='wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_ref', models.CharField(max_length=20, null=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_name', models.CharField(max_length=20, null=True)),
                ('transaction_type', models.CharField(max_length=20, null=True)),
                ('transaction_charge', models.IntegerField()),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_account', models.IntegerField()),
                ('receipt', models.CharField(max_length=20, null=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('amount', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Third_party_account', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Third_party_currency', to='wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=20, null=True)),
                ('customer_id', models.IntegerField()),
                ('points', models.IntegerField()),
                ('gender', models.CharField(max_length=20, null=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_third_party', to='wallet.third_party')),
            ],
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciept_type', models.CharField(max_length=20, null=True)),
                ('date', models.DateField()),
                ('bill_number', models.CharField(max_length=20, null=True)),
                ('balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('receipt_file', models.FileField(upload_to='')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reciept_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_description', models.CharField(max_length=20, null=True)),
                ('transaction_id', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Notifications_recipient', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('date_and_time', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('loan_status', models.CharField(max_length=20, null=True)),
                ('interest_rate', models.IntegerField()),
                ('loan_term', models.CharField(max_length=20, null=True)),
                ('payment_due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('loan_balance', models.IntegerField()),
                ('guarantor', models.CharField(max_length=20, null=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('card_name', models.CharField(max_length=20, null=True)),
                ('date_issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('card_type', models.CharField(max_length=20, null=True)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('security_code', models.IntegerField()),
                ('issuer', models.CharField(max_length=20, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]
