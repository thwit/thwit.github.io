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
    print("Creating a new blog post for Today I <verbed>")
    verb = input("Title: Today I ").strip()
    
    if not verb:
        print("Verb cannot be empty!")
        sys.exit(1)
    
    # Ask if they want to add content now or later
    add_content = input("Add content now? (y/n, default: n): ").strip().lower()
    
    if add_content == 'y':
        print("Enter your content (press Ctrl+D or Ctrl+Z when done):")
        content_lines = []
        try:
            while True:
                line = input()
                content_lines.append(line)
        except EOFError:
            pass
        content = "\n".join(content_lines)
    else:
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
    
    # Ask if they want to open in editor
    open_editor = input("Open in editor? (y/n, default: y): ").strip().lower()
    
    if open_editor != 'n':
        # Check if running in VS Code
        is_vscode = (
            os.environ.get('TERM_PROGRAM') == 'vscode' or
            os.environ.get('VSCODE_INJECTION') or
            os.environ.get('VSCODE_GIT_IPC_HANDLE')
        )
        
        if is_vscode:
            # Running in VS Code - open in VS Code
            try:
                subprocess.run(['code', filename])
                print(f"Opening in VS Code...")
            except FileNotFoundError:
                print("VS Code detected but 'code' command not found!")
        else:
            # Not in VS Code - use notepad (or default editor on non-Windows)
            if platform.system() == 'Windows':
                subprocess.run(['notepad', filename])
            else:
                # Fallback for macOS/Linux
                editors = ['nano', 'vim', 'vi']
                for editor in editors:
                    try:
                        subprocess.run([editor, filename])
                        break
                    except FileNotFoundError:
                        continue

if __name__ == "__main__":
    create_post()