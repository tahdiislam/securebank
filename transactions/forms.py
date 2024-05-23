from typing import Any
from django import forms
from .models import Transaction

BANK_IS_BANKRUPT = True
class TransactionForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']
    
    def __init__(self, *args, **kwargs):
        self.user_account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit: bool = True) -> Any:
        self.instance.account = self.user_account
        self.instance.balance_after_transaction = self.instance.account.balance
        return super().save(commit)

class DepositForm(TransactionForm):
    def clean_amount(self):
        if BANK_IS_BANKRUPT:
            raise forms.ValidationError(f'Bank is bankrupt!!!')
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')

        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount}$'
            )
        return amount

class TransferMoneyForm(TransactionForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type','receiver_account_no']
    def clean_amount(self):
        if BANK_IS_BANKRUPT:
            raise forms.ValidationError(f'Bank is bankrupt!!!')
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')

        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount}$'
            )
        return amount
    def save(self, commit: bool = True) -> Any:
        self.instance.account = self.user_account
        self.instance.balance_after_transaction = self.instance.account.balance
        return super().save(commit)

class WithDrawalForm(TransactionForm):
    def clean_amount(self):
        if BANK_IS_BANKRUPT:
            raise forms.ValidationError(f'Bank is bankrupt!!!')
        account = self.user_account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount}$'
            )
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount}$'
            )
        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance}$ in your account. '
                'You can not withdraw more than your account balance'
            )
        return amount

class LoanRequestForm(Transaction):
    def clean_amount(self):
        if BANK_IS_BANKRUPT:
            raise forms.ValidationError(f'Bank is bankrupt!!!')
        amount = self.cleaned_data["amount"]    
        return amount