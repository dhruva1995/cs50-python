import re


url = input("Enter your twitter url: ").strip()

if matches := re.search(
    r"(?:https?://)?(?:www\.)?twitter.com/([\w]+)", url, re.IGNORECASE
):
    print(f"Username: {matches.group(1)}")
