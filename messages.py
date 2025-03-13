import random
from config import MIN_AMOUNT, MAX_AMOUNT

def get_deposit_amount():
    """Generate a random USDT deposit amount."""
    return random.randint(MIN_AMOUNT, MAX_AMOUNT)

def get_withdrawal_amount():
    """Generate a random USDT withdrawal amount."""
    min_withdrawal = MIN_AMOUNT
    max_withdrawal = MAX_AMOUNT

    # Ensure min_withdrawal does not exceed max_withdrawal
    if min_withdrawal > max_withdrawal:
        min_withdrawal = max_withdrawal  # Set to max to avoid empty range

    return random.randint(min_withdrawal, max_withdrawal)

def generate_messages():
    """Create deposit and corresponding withdrawal messages with proper spacing."""
    deposit_amount = get_deposit_amount()
    withdrawal_amount = get_withdrawal_amount()

    deposit_message = f"Deposit: 💰 A new deposit of {deposit_amount} USDT has been received! 🚀"
    withdrawal_message = f"Withdrawal: 🔄 A withdrawal of {withdrawal_amount} USDT has been successfully processed! 💸"
    
    footer = "GoldenHub: Where Wealth Never Sleeps"

    return f"{deposit_message}\n\n{withdrawal_message}\n\n{footer}"