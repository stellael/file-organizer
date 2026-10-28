import os
import shutil

# Βρίσκει αυτόματα το home directory του χρήστη (λειτουργεί σε κάθε PC!)
home_dir = os.path.expanduser("~")

# Ορίζει αυτόματα τα Downloads και το Desktop ανεξαρτήτως ονόματος χρήστη
source_folder = os.path.join(home_dir, "Downloads")
desktop_path = os.path.join(home_dir, "Desktop")

# Categories and their respective desktop folders
categories = {
    "Uni": os.path.join(desktop_path, "Uni"),
    "Work": os.path.join(desktop_path, "Work"),
    "Codes": os.path.join(desktop_path, "Codes"),
    "Gen": os.path.join(desktop_path, "Gen")
}

def setup_folders():
    for cat_name, folder_path in categories.items():
        os.makedirs(folder_path, exist_ok=True)

def smart_organizer():
    if not os.path.exists(source_folder):
        print("Downloads folder not found!")
        return

    setup_folders()
    
    files = os.listdir(source_folder)
    moved_count = 0
    
    for filename in files:
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            lower_name = filename.lower()
            target_folder = categories["Gen"]
            
            if "uni" in lower_name:
                target_folder = categories["Uni"]
            elif "work" in lower_name:
                target_folder = categories["Work"]
            elif "codes" in lower_name:
                target_folder = categories["Codes"]
            elif "gen" in lower_name:
                target_folder = categories["Gen"]
                
            dest_path = os.path.join(target_folder, filename)
            
            if not os.path.exists(dest_path):
                shutil.move(file_path, dest_path)
                print(f"Moved: '{filename}' -> to Desktop folder.")
                moved_count += 1

    print(f"\nProcess completed! Moved {moved_count} files.")

if __name__ == "__main__":
    smart_organizer()