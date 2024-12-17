import sys
from markitdown import MarkItDown

if len(sys.argv) ! 2:
  print("Usage: python mid.py <file_name>")
  sys.exit(1)

file_name = sys.argv[1]
markitdown = MarkItDown()
result = markitdown.convert(file_name)

output_file_name = file_name + ".md"
with open(output_file_name, "w", encoding="utf-8") as output_file:
  output_file.write(result.text_content)

print(f"Converted content writtent to {output_file_name}")
