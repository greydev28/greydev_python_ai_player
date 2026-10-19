# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 1 — Thinking in Files

> *"Memory is what separates a script from an application."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Explain why programs use files
✅ Understand persistent storage
✅ Distinguish between RAM and files
✅ Understand text vs binary files
✅ Understand file paths

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

███████████████████████████████████████████░ 92%

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming

🟢 Files & Python Ecosystem

    ⏳ Thinking in Files
    ⬜ Reading Files
    ⬜ Writing Files
    ⬜ Context Managers
    ⬜ Modules & Imports
    ⬜ Packages
```

---

# 🤔 The Problem

Imagine your Football Academy AI.

You add three players.

```text
James

David

Samuel
```

Everything looks good.

Then you close the program.

Tomorrow...

You open it again.

Your players are gone.

Why?

Because they only existed in **RAM** (computer memory).

---

# 🧠 RAM vs Files

Think of RAM as a whiteboard.

```text
Write Notes

↓

Use Them

↓

Erase Board
```

When the program ends...

Everything written on the whiteboard disappears.

---

A file is different.

Think of it as a notebook.

```text
Write Notes

↓

Close Notebook

↓

Open Tomorrow

↓

Notes Still There
```

That's persistence.

---

# ⚽ Football Academy Example

Without files:

```text
Start Program

↓

Create Players

↓

Exit

↓

Players Lost
```

With files:

```text
Start Program

↓

Load Players

↓

Add New Player

↓

Save Players

↓

Exit

↓

Everything is remembered
```

Now your academy behaves like real software.

---

# 📄 What Is a File?

A file is simply a collection of data stored on your computer.

Examples:

```text
players.txt

notes.md

image.png

music.mp3

report.pdf
```

Different extensions often indicate different file formats.

---

# 📝 Text vs Binary Files

## Text Files

Designed for humans to read.

Examples:

```text
.txt
.csv
.py
.md
.json
```

Open them in a text editor and you'll see readable characters.

---

## Binary Files

Designed primarily for computers.

Examples:

```text
.png
.jpg
.mp3
.mp4
.exe
```

Open one in a text editor and you'll mostly see unreadable symbols because the data isn't plain text.

---

# 📂 File Paths

Your computer organizes files in folders.

Example:

```text
Projects/
    FootballAcademy/
        players.txt
```

The location of a file is its **path**.

Python needs that path to find the file.

---

# 🗂️ Relative vs Absolute Paths

Relative path

```text
players.txt
```

Means:

"Look in the current folder."

---

Another relative path

```text
data/players.txt
```

Means:

"Go into the `data` folder."

---

Absolute path

Windows example:

```text
C:\Users\Valerian\Projects\FootballAcademy\players.txt
```

Absolute paths start from the root of the computer.

For most of your projects, relative paths are preferred because they make your code easier to move between computers.

---

# 🤖 Why AI Engineers Care

Machine learning projects almost always begin with data stored in files.

Examples:

```text
train.csv

players.json

images/

model.pkl
```

Your code reads those files before it can learn from the data.

---

# 🌱 Real-World Examples

A game saves your progress.

↓

File

---

A browser remembers bookmarks.

↓

File

---

A password manager stores encrypted passwords.

↓

File

---

Your Python script stores football players.

↓

File

---

# 💡 Chapter Summary

You learned

- RAM is temporary.
- Files provide persistent storage.
- Text files are human-readable.
- Binary files store other kinds of data.
- File paths tell Python where to find a file.

---

# 🏃 Practice

## Think About It

1. Why would storing players in a list alone not be enough for a real application?

2. Give three examples of programs that rely on files every day.

3. Name two text file formats and two binary file formats.

4. What's the difference between a relative path and an absolute path?

---

# 🌱 Growth Log

Reflect honestly.

- Can I explain persistence in my own words?

- Why do programs lose their data when they close?

- Why are relative paths usually a better choice for projects?

If yes...

You're ready to actually open your first file.

---

> 🚀 Coming Up

## 📖 Batch 2 — Reading Files

You'll learn how to use `open()`, `read()`, `readline()`, `readlines()`, and understand how Python moves through a file one character at a time.

## Greydev Advanced Challenge — No Step-by-Step Hints

Complete these as small, testable programs. State assumptions, handle failure cases, and explain your design in a short `DESIGN.md`.

1. **Crash-safe JSON repository:** Build a repository for records with unique IDs. It must distinguish a missing file from malformed JSON, validate loaded data, avoid silently overwriting corrupted data, write updates safely using a temporary file and replacement, and preserve the original file if validation fails. Demonstrate recovery from a deliberately corrupted file.
2. **Import architecture:** Refactor a single-file CLI into `models`, `services`, `storage`, and `cli` modules. Prevent circular imports, keep input/output at the CLI boundary, and make business logic testable without interactive input. Explain what belongs in each module.
3. **Path portability:** Make file paths work when the program is launched from a different current working directory. Add tests for missing directories, Unicode text, empty files, and permission errors where practical.
4. **Environment and dependencies:** Create a virtual environment, install one third-party package, record dependencies reproducibly, and document setup for a clean machine. Explain why the interpreter and `pip` must refer to the same environment.
5. **Git investigation:** Make five meaningful commits, inspect a previous version, create a branch, introduce a bug, identify the commit that introduced it with history/diff tools, fix it, and merge the branch. Do not rewrite shared history.

