"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entry point script that writes a specific satirical quote about office printers
to an output file located in $MAKEFUN_OUTPUT_DIR (defaulting to 'out').
"""

import os
import sys

LINE = "The office printer operates exclusively on the spiritual energy of pure desperation and refuses to touch paper if anyone is watching."

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content failed validation checks.")
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(output_path)
    print(len(content))

if __name__ == "__main__":
    main()
