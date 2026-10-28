# Smart File Organizer🗂️

A simple Python automation script that keeps your Desktop clean by automatically organizing downloaded files from your `Downloads` folder into specific categories on your `Desktop`.

## Features
- **Zero Configuration needed for users:** Dynamically finds the user's home directory (`os.path.expanduser("~")`), making it fully cross-platform and secure.
- **Auto-Setup:** Automatically creates destination folders (`Uni`, `Work`, `Codes`, `Gen`) on the Desktop if they don't already exist.
- **Keyword Sorting:** Scans filenames for specific tags and moves them accordingly.
- **Safety First:** Prevents file overwriting by checking if a file with the same name already exists in the destination folder.

## How to Use
When downloading files, simply include one of the following keywords in your filename:
- `uni` ➔ Moves to **Uni** folder
- `work` ➔ Moves to **Work** folder
- `codes` ➔ Moves to **Codes** folder
- `gen` (or anything else) ➔ Moves to **Gen** folder (General)

## Requirements
- Python 3.x installed on your system.
