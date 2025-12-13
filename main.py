from shortner import shorten_url, expand_url

while True:
    print("\n1. Shorten URL\n2. Expand URL\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        long_url = input("Enter URL: ")
        code = shorten_url(long_url)
        print(f"Short URL: short.ly/{code}")

    elif choice == "2":
        code = input("Enter code: ")
        url = expand_url(code)
        print(url if url else "❌ Not found")

    elif choice == "3":
        break
