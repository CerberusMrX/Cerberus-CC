import requests
import random
import string
import re
from datetime import datetime, timedelta
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

# ASCII Art Banner
ASCII_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Define prompt_toolkit style
style = Style.from_dict({
    'prompt': '#00ff00 bold',
    'header': '#ffffff bold',
    'error': '#ff0000',
    'result': '#00ffff',
})

# Create PromptSession for styled input
session = PromptSession(style=style)

def luhn_checksum(card_number):
    """Check if a card number is valid using the Luhn algorithm."""
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    if not digits:
        return False
    checksum = 0
    is_even = False
    for digit in digits[::-1]:
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_even = not is_even
    return checksum % 10 == 0

def generate_card_number(bin_prefix, length=16):
    """Generate a valid test card number based on a BIN prefix."""
    if not (6 <= len(bin_prefix) <= 8):
        return "Error: BIN prefix must be 6-8 digits."
    card_number = bin_prefix
    remaining_length = length - len(card_number)
    card_number += ''.join(random.choice(string.digits) for _ in range(remaining_length - 1))
    digits = [int(d) for d in card_number]
    checksum = 0
    is_even = False
    for digit in digits[::-1]:
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_even = not is_even
    check_digit = (10 - (checksum % 10)) % 10
    card_number += str(check_digit)
    return card_number

def generate_expiry_date():
    """Generate a random future expiry date (MM/YY)."""
    current_year = datetime.now().year % 100
    expiry_year = random.randint(current_year + 1, current_year + 5)
    expiry_month = random.randint(1, 12)
    return f"{expiry_month:02d}/{expiry_year:02d}"

def generate_cvv():
    """Generate a random 3-digit CVV."""
    return ''.join(random.choice(string.digits) for _ in range(3))

def bin_lookup(bin_number):
    """Perform a BIN lookup using binlist.net API."""
    url = f"https://lookup.binlist.net/{bin_number}"
    headers = {"Accept-Version": "3"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {
                "Bank": data.get("bank", {}).get("name", "Unknown"),
                "Brand": data.get("brand", "Unknown"),
                "Type": data.get("type", "Unknown"),
                "Country": data.get("country", {}).get("name", "Unknown")
            }
        elif response.status_code == 404:
            return "Error: BIN not found."
        else:
            return "Error: API request failed."
    except requests.RequestException:
        return "Error: Network issue during BIN lookup."

def validate_card_input(card_number):
    """Validate card number input (remove spaces, check digits)."""
    card_number = re.sub(r'\D', '', card_number)
    if not (13 <= len(card_number) <= 19):
        return None, "Error: Card number must be 13-19 digits."
    return card_number, None

def validate_cvv(cvv, bin_number=None):
    """Validate CVV format (3 or 4 digits based on card type)."""
    if not cvv.isdigit():
        return "Error: CVV must contain only digits."
    if bin_number and bin_number.startswith(("34", "37")):  # Amex
        if len(cvv) != 4:
            return "Error: Amex CVV must be 4 digits."
    else:  # Visa, Mastercard, etc.
        if len(cvv) != 3:
            return "Error: CVV must be 3 digits."
    return "CVV is valid."

def validate_expiry_date(expiry):
    """Validate expiry date format (MM/YY) and check if not expired."""
    if not re.match(r"^(0[1-9]|1[0-2])/\d{2}$", expiry):
        return "Error: Expiry date must be in MM/YY format (e.g., 12/25)."
    month, year = map(int, expiry.split("/"))
    current_date = datetime.now()
    expiry_date = datetime(2000 + year, month, 1) + timedelta(days=31)
    if expiry_date < current_date:
        return "Error: Expiry date has passed."
    return "Expiry date is valid."

def check_sk_non_sk(card_number):
    """Placeholder for SK/Non-SK checking (only non-SK supported)."""
    card_number, error = validate_card_input(card_number)
    if error:
        return error
    if luhn_checksum(card_number):
        return "Non-SK Check: Card number is valid (passes Luhn check)."
    return "Non-SK Check: Card number is invalid (fails Luhn check). SK checking is not supported due to legal restrictions."

def check_sk_demo(card_number, cvv, expiry):
    """Mock SK check for demonstration purposes only."""
    results = []
    
    # Validate card number format
    card_number, error = validate_card_input(card_number)
    if error:
        results.append(error)
    else:
        results.append("SK Demo: Card number format is valid." if luhn_checksum(card_number) else "SK Demo: Card number format is invalid.")
    
    # Mock SK validation (simulated, no real check)
    results.append("SK Demo: Secret key check simulated (no real validation performed for legal reasons).")
    
    # Validate CVV and expiry for completeness
    results.append(validate_cvv(cvv, card_number[:6] if card_number else None))
    results.append(validate_expiry_date(expiry))
    
    return {
        "Card Number": results[0],
        "SK Status": results[1],
        "CVV": results[2],
        "Expiry Date": results[3]
    }

def validate_full_card(card_number, cvv, expiry):
    """Validate card number, CVV, and expiry date together."""
    results = []
    
    # Validate card number
    card_number, error = validate_card_input(card_number)
    if error:
        results.append(error)
    else:
        results.append("Card number is valid (passes Luhn check)." if luhn_checksum(card_number) else "Card number is invalid (fails Luhn check).")
    
    # Validate CVV
    bin_number = card_number[:6] if card_number else None
    results.append(validate_cvv(cvv, bin_number))
    
    # Validate expiry date
    results.append(validate_expiry_date(expiry))
    
    return {
        "Card Number": results[0],
        "CVV": results[1],
        "Expiry Date": results[2]
    }

def print_result(result):
    """Print result in a formatted table-like structure."""
    print("┌" + "─" * 50 + "┐")
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"│ {key:<20} : {value:<27} │")
    else:
        print(f"│ {result:<48} │")
    print("└" + "─" * 50 + "┘")

def main():
    """Main function with enhanced terminal UI."""
    print(ASCII_ART)
    print("Cerberus CC - Developed by Sudeepa Wanigarathne")
    print("=" * 50)

    while True:
        print("\nCerberus CC Menu:")
        print("1. Validate Card Number")
        print("2. Generate Test Card Number")
        print("3. BIN Lookup")
        print("4. SK/Non-SK Check")
        print("5. Full Card Check")
        print("6. SK Demo (For Educational Purposes)")
        print("7. Exit")
        
        choice = session.prompt("Enter choice (1-7): ")

        if choice == "1":
            card_number = session.prompt("Enter card number: ")
            card_number, error = validate_card_input(card_number)
            if error:
                print_result(error)
            else:
                result = "Card number is valid (passes Luhn check)." if luhn_checksum(card_number) else "Card number is invalid (fails Luhn check)."
                print_result(result)

        elif choice == "2":
            bin_prefix = session.prompt("Enter BIN prefix (6-8 digits): ")
            if not bin_prefix.isdigit() or not (6 <= len(bin_prefix) <= 8):
                print_result("Error: BIN prefix must be 6-8 digits.")
                continue
            length = session.prompt("Enter card length (13-19, default 16): ", default="16")
            if not length.isdigit() or not (13 <= int(length) <= 19):
                print_result("Error: Card length must be 13-19.")
                continue
            card_number = generate_card_number(bin_prefix, int(length))
            expiry = generate_expiry_date()
            cvv = generate_cvv()
            print_result({
                "Generated Card": card_number,
                "Expiry Date": expiry,
                "CVV": cvv
            })

        elif choice == "3":
            bin_number = session.prompt("Enter BIN (6-8 digits): ")
            if not bin_number.isdigit() or not (6 <= len(bin_number) <= 8):
                print_result("Error: BIN must be 6-8 digits.")
                continue
            result = bin_lookup(bin_number)
            print_result(result)

        elif choice == "4":
            card_number = session.prompt("Enter card number for SK/Non-SK check: ")
            result = check_sk_non_sk(card_number)
            print_result(result)

        elif choice == "5":
            card_number = session.prompt("Enter card number: ")
            cvv = session.prompt("Enter CVV (3-4 digits): ")
            expiry = session.prompt("Enter expiry date (MM/YY): ")
            result = validate_full_card(card_number, cvv, expiry)
            print_result(result)

        elif choice == "6":
            print("\nNote: SK Demo is for educational purposes only and does not perform real SK validation.")
            card_number = session.prompt("Enter card number: ")
            cvv = session.prompt("Enter CVV (3-4 digits): ")
            expiry = session.prompt("Enter expiry date (MM/YY): ")
            result = check_sk_demo(card_number, cvv, expiry)
            print_result(result)

        elif choice == "7":
            print("Exiting Cerberus CC...")
            break
        else:
            print_result("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
