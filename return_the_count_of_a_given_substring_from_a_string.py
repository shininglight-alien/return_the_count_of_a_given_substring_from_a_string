# Return the count of a given substring from a string

def count_substring(string, substring):
    return string.count(substring)

str_x = "Emma is good developer. Emma is a writer"
substring = "Emma"
count = count_substring(str_x, substring)

print(f"'{substring}' appears {count} times in this given string.")
