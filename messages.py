import random
from config import MIN_AMOUNT, MAX_AMOUNT

def get_random_amount():
    """Generate a random USDT deposit amount."""
    return random.randint(MIN_AMOUNT, MAX_AMOUNT)

def generate_random_message():
    """Randomly select and generate either a deposit or withdrawal message."""
    if random.choice([True, False]):
        return generate_deposit_message()
    else:
        return generate_withdrawal_message()

def generate_deposit_message():
    """Create a deposit message."""
    deposit_amount = get_random_amount()
    deposit_message = f"Deposit: 💰 A new deposit of {deposit_amount} USDT has been received! 🚀"
    footer = "GoldenHub: Where Wealth Never Sleeps"
    return f"{deposit_message}\n\n{footer}"    

def generate_withdrawal_message():
    """Create a withdrawal message."""
    withdrawal_amount = get_random_amount()
    withdrawal_message = f"Withdrawal: 🔄 A withdrawal of {withdrawal_amount} USDT has been successfully processed! 💸"
    footer = "GoldenHub: Where Wealth Never Sleeps"
    return f"{withdrawal_message}\n\n{footer}"
