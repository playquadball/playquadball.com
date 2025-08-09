#!/usr/bin/env python3
import os
import re
import glob

def check_bullet_lists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    issues = []
    for i, line in enumerate(lines):
        # Check for bold text or question followed immediately by bullet list
        if (line.strip().endswith('**') or line.strip().endswith('?')) and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if re.match(r'^-\s+\*\*', next_line):  # Bullet list starting with bold
                issues.append(f"Line {i+1}: '{line.strip()}' followed immediately by '{next_line}'")
    
    return issues

# Check all markdown files
markdown_files = glob.glob('/home/dev/playquadball.com/docs/**/*.md', recursive=True)
total_issues = 0

for file_path in markdown_files:
    issues = check_bullet_lists(file_path)
    if issues:
        print(f"\n{file_path}:")
        for issue in issues:
            print(f"  {issue}")
        total_issues += len(issues)

if total_issues == 0:
    print("✅ All bullet lists are properly formatted!")
else:
    print(f"\n❌ Found {total_issues} bullet list formatting issues")