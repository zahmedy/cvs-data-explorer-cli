import re
import pandas as pd

def clean_phone(phone):
    if pd.isna(phone):
        return None
    
    # 1. Convert to string and strip spaces
    phone = str(phone).strip()

    # 2. Remove extensions: anything after 'x' or 'ext'
    phone = re.sub(r"(x.*$)|(ext.*$)", "", phone, flags=re.IGNORECASE)

    # 3. Keep only digits and '+'
    phone = re.sub(r"[^\d+]", "", phone)

    # 4. If it doesn't start with '+', assume +1
    if not phone.startswith('+') and phone != "":
        phone = '+1' + phone

    return phone