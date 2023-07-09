import re

name = input("Whats your name? ").strip()

if matches := re.search("^(.+),\s*(.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello {name}")
