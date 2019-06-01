handler = open("test.txt", "a+")

# Append a line at the end
handler.write("\nAnother line")

new_lines = handler.readlines()

print(new_lines)
handler.close()
