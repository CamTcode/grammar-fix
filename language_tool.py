import language_tool_python
import os
import sys

# Initialize grammar tool
try:
    tool = language_tool_python.LanguageTool('en-US')
except Exception as e:
    print("❌ Failed to initialize grammar tool.")
    print(e)
    sys.exit(1)

# Use current working directory to locate email.txt
current_dir = os.getcwd()
email_file_path = os.path.join(current_dir, "email.txt")

# Load email content
try:
    with open(email_file_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("❌ Error: 'email.txt' not found. Make sure it's in the same folder where you run this program.")
    sys.exit(1)

if not text.strip():
    print("❌ Error: 'email.txt' is empty.")
    sys.exit(1)

# Check and correct grammar
matches = tool.check(text)
corrected_text = language_tool_python.utils.correct(text, matches)

# Save the corrected output
output_file_path = os.path.join(current_dir, "email_corrected.txt")
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(corrected_text)

# Display results
print("\n✅ Corrected Email:\n")
print(corrected_text)
print(f"\n✅ Saved as '{output_file_path}'.")
