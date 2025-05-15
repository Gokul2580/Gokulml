import requests
import os
import sys
import subprocess

ascii_art = """
   ____        _   _       _                 
  |  _ \\ _   _| |_| |__   | | ___  _ __ ___  
  | |_) | | | | __| '_ \\  | |/ _ \\| '_ ` _ \\ 
  |  __/| |_| | |_| | | | | | (_) | | | | | |
  |_|    \\__, |\\__|_| |_| |_|\\___/|_| |_| |_|
         |___/                               
     -- Gok's Python Program Hub --
"""

programs = [
    ("Hello World", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/hello_world/hello.py"),
    ("Bubble Sort", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/bubble_sort.py"),
    ("Binary Search", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/searches/binary_search.py"),
    ("Factorial", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/math/factorial.py"),
    ("Fibonacci", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/math/fibonacci.py"),
    ("Palindrome", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/strings/is_palindrome.py"),
    ("Linear Search", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/searches/linear_search.py"),
    ("Quick Sort", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/quick_sort.py"),
    ("Selection Sort", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/selection_sort.py"),
    ("Dijkstra", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/graphs/dijkstra.py"),
    ("Queue", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/data_structures/queue.py"),
    ("Stack", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/data_structures/stack.py"),
    ("Merge Sort", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/merge_sort.py"),
    ("GCD", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/math/gcd.py"),
    ("LCM", "https://raw.githubusercontent.com/TheAlgorithms/Python/master/math/lcm.py"),
]

def download_file(name, url):
    filename = f"{name.replace(' ', '_')}.py"
    try:
        r = requests.get(url, stream=True)
        total = int(r.headers.get('content-length', 0))
        downloaded = 0
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = int((downloaded / total) * 100)
                    print(f"\rDownloading {name}: {percent}% complete", end="")
        print(f"\n{name} downloaded successfully!")

        # Open in IDLE
        if sys.platform.startswith('win'):
            subprocess.Popen(['pythonw', '-m', 'idlelib', filename])
        else:
            subprocess.Popen(['idle', filename])

    except Exception as e:
        print("Download failed:", e)

def main():
    print(ascii_art)
    print("Select a program to download:\n")
    for i, (name, _) in enumerate(programs, 1):
        print(f"{i}. {name}")
    print("\n0. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                print("Goodbye!")
                break
            elif 1 <= choice <= len(programs):
                name, url = programs[choice - 1]
                download_file(name, url)
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
