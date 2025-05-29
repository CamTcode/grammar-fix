import language_tool_python
import requests

# Initialize grammar tool
try:
    tool = language_tool_python.LanguageTool('en-US')
except Exception as e:
    print("❌ Failed to initialize grammar tool.")
    print(e)
    exit(1)

# Load email content
try:
    with open("email.txt", "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("❌ Error: 'email.txt' not found.")
    exit(1)

if not text.strip():
    print("❌ Error: 'email.txt' is empty.")
    exit(1)

# Check and correct grammar
matches = tool.check(text)
corrected_text = language_tool_python.utils.correct(text, matches)

# Save and print
with open("email_corrected.txt", "w", encoding="utf-8") as f:
    f.write(corrected_text)

print("\n✅ Corrected Email:\n")
print(corrected_text)
print("\n✅ Saved as 'email_corrected.txt'.")
