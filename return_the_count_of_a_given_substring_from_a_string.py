# Return the count of a given substring from a string

def count_substring(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

str_x = "Emma is good developer. Emma is a writer"
substring = "Emma"
count = count_substring(str_x, substring)

print(f"'{substring}' appears {count} times in this given string.")
