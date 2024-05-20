def find_non_utf8_chars(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    try:
        content.decode('utf-8')
        print("No non-UTF-8 characters found.")
    except UnicodeDecodeError as e:
        print(f"Non-UTF-8 character found at position {e.start}: {e.reason}")

# Replace 'mysite_data.json' with the path to your JSON file
find_non_utf8_chars('mysite_data.json')
