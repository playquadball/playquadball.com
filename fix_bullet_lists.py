#!/usr/bin/env python3
import os
import re
import glob

def fix_bullet_lists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: Bold text followed immediately by bullet list
    pattern1 = r'(\*\*[^*]+\*\*)\n(- \*\*)'
    replacement1 = r'\1\n\n\2'
    
    # Pattern 2: Question followed immediately by bullet list
    pattern2 = r'(\?)\n(- \*\*)'
    replacement2 = r'\1\n\n\2'
    
    new_content = re.sub(pattern1, replacement1, content, flags=re.MULTILINE)
    new_content = re.sub(pattern2, replacement2, new_content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {file_path}")
        return True
    return False

# Process all markdown files
markdown_files = glob.glob('/home/dev/playquadball.com/docs/**/*.md', recursive=True)
fixed_count = 0

for file_path in markdown_files:
    if fix_bullet_lists(file_path):
        fixed_count += 1

print(f"Fixed {fixed_count} files")