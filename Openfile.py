# Open input.txt for reading
file = open("input.txt", "r")
content = file.read()  # Read the entire content
file.close()           # Close the file after reading

# Convert content to uppercase
processed_content = content.upper()

# Count words
word_count = len(content.split())

# Prepare final content with word count
final_content = processed_content + f"\n\nWord Count: {word_count}"

# Open output.txt for writing
file = open("output.txt", "w")
file.write(final_content)  # Write the processed content
file.close()                # Close the file after writing

# Print a success message
print("✅ 'output.txt' has been created successfully!")
