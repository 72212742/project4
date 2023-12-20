def word_counter(text):
    words = text.split()
    return len(words)

# Example usage:
input_text = "This is a simple word counter program."
word_count = word_counter(input_text)
print(f"Word count: {word_count}")
