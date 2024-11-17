import re


def get_user_number(filename: str, number: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # # bilan boshlangan sarlavhalar va ularning matnlarini ajratish
    headers_and_texts = []
    current_header = None
    current_text = []

    for index, line in enumerate(lines):
        line = line.strip()
        if line.startswith("#"):
            # Agar yangi sarlavha topilsa, avvalgi sarlavhani saqlaymiz
            if current_header:
                headers_and_texts.append((current_header, ''.join(current_text).strip()))
            # Yangi sarlavhani o'rnatamiz
            current_header = line
            current_text = []
        else:
            # Agar sarlavhadan keyingi matn bo'lsa, uni yig'ish
            current_text.append(line)

    # Oxirgi sarlavha va matnni ham saqlaymiz
    if current_header:
        headers_and_texts.append((current_header, ''.join(current_text).strip()))

    # Natijani chiqarish
    for header, text in headers_and_texts:
        numbers = re.findall(r'#(\d+)', header)
        if numbers[0] == number:
            return f"Header: {header}\nText: {text}"
        else:
            return f"Sizning life_numberingizga mos ta'rif numerologiya jadvalida topilmadi!"
