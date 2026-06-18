import masks

def mask_account_card(type_and_number: str) -> str:
    words = type_and_number.split()
    if len(words[-1]) == 16:
        return f"{" ".join(words[:-1])} {masks.get_mask_card_number(words[-1])}"
    else:
        return f"{" ".join(words[:-1])} {masks.get_mask_account(words[-1])}"

