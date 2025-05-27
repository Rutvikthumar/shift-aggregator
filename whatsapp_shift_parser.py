import re

def parse_whatsapp_shifts(file_path):
    shifts = []
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            if re.search(r'shift|duty', line, re.IGNORECASE):
                shifts.append(line.strip())
    return shifts

if __name__ == '__main__':
    shifts = parse_whatsapp_shifts('WhatsAppChat.txt')
    for s in shifts:
        print(s)
