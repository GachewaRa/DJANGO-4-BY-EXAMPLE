def inspect_non_utf8_char(file_path, position, context=10):
    with open(file_path, 'rb') as f:
        f.seek(position - context)
        surrounding_bytes = f.read(context * 2 + 1)
        return surrounding_bytes

# Replace 'mysite_data.json' with the path to your JSON file and 15029 with the position
file_path = 'mysite_data.json'
position = 15029
context_bytes = inspect_non_utf8_char(file_path, position)

print(f"Surrounding bytes at position {position}:")
print(context_bytes)
