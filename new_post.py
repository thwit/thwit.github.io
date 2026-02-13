import os
from datetime import datetime
import subprocess
import sys
import platform

def create_post():
    # Get today's date
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    
    # Get verb from user
    print("Creating a new blog post for Today I {verbed}")
    verb = input("Title: Today I ").strip()
    
    if not verb:
        print("Verb cannot be empty!")
        sys.exit(1)
    
    content = "Write your post here..."
    
    # Read template
    with open("_template.md", "r") as f:
        template = f.read()
    
    # Fill in template
    post_content = template.format(
        verb=verb,
        date=date_str,
        content=content
    )
    
    # Create filename
    filename = f"_posts/{date_str}-Today I {verb}.md"
    
    # Write file
    with open(filename, "w") as f:
        f.write(post_content)
    
    print(f"\n? Created: {filename}")


if __name__ == "__main__":
    create_post()