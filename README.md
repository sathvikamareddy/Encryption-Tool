<div align="center">
  
# 🔐 Python Text Encryption & Decryption Tool

</div>

A simple Python-based application that encrypts and decrypts text using a **Substitution Cipher technique**.
The program replaces each character in a message with another character from a randomly shuffled key, making the original message unreadable without the correct mapping.

This project demonstrates fundamental concepts of **Python programming, string manipulation, randomization, and basic cryptography**.

---

# 📌 Features

* Encrypts text messages using a randomly generated substitution key
* Decrypts encrypted messages back into the original text
* Supports:

  * Uppercase letters (A–Z)
  * Lowercase letters (a–z)
  * Numbers (0–9)
  * Special characters
  * Spaces
* Simple and beginner-friendly Python implementation
* Demonstrates a basic cryptographic substitution method

---

# 🛠 Technologies Used

* **Python 3**
* Built-in Python libraries:

  * `random`
  * `string`

No external dependencies are required.

---

# 📂 Project Structure

```
text-encryption-tool
│
├── encryption.py
├── README.md
├── requirements.txt
├── .gitignore

```

### File Description

| File               | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| encryption.py      | Main Python program that performs encryption and decryption |
| README.md          | Documentation explaining the project                        |
| requirements.txt   | Lists project dependencies                                  |
| .gitignore         | Prevents unnecessary files from being uploaded to GitHub    |
                          

---

# ⚙️ How the Program Works

### Step 1 — Character Set Creation

The program first creates a list of characters including:

* Letters
* Digits
* Punctuation
* Spaces

```
characters = " " + string.punctuation + string.ascii_letters + string.digits
```

---

### Step 2 — Key Generation

A copy of the character list is created and shuffled randomly to generate a **secret encryption key**.

```
key = characters.copy()
random.shuffle(key)
```

Each character now has a corresponding encrypted substitute.

Example mapping:

| Original | Encrypted |
| -------- | --------- |
| a        | @         |
| b        | #         |
| c        | Z         |
| 1        | %         |

---

### Step 3 — Encryption

Each character in the input text is replaced with its corresponding character in the shuffled key.

```
encrypted_text += key[index]
```

---

### Step 4 — Decryption

The encrypted characters are mapped back to their original characters using the same key.

```
decrypted_text += characters[index]
```

---

# ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/sathvikamareddy/text-encryption-tool.git
```

---

### 2. Navigate to the project directory

```
cd text-encryption-tool
```

---

### 3. Run the program

```
python encryption.py
```

---

# 💻 Example

### Input

```
Enter text to encrypt: Hello123
```

### Output

```
Encrypted Message: #@9L$p2!
Decrypted Message: Hello123
```
 # sample output

 
---

# ⚠️ Important Note

The encryption key is generated randomly every time the program runs.

This means:

* If the program is restarted, the same encrypted message **cannot be decrypted** unless the original key is preserved.
* In real-world cryptographic systems, encryption keys are stored securely.

---

# 🚀 Future Improvements

Possible enhancements for this project:

* Save encryption keys to a file
* Allow users to load previously generated keys
* Implement file encryption
* Build a graphical user interface (GUI)
* Implement stronger encryption algorithms
* Convert the program into a command-line tool

---

# 📚 Learning Outcomes

This project helps in understanding:

* Python lists and indexing
* String manipulation
* Randomization techniques
* Basic encryption and decryption logic
* Substitution cipher methods
* Python program structuring

---

# 👩‍💻 Author

**Sathvi Reddy**

B.Tech – Computer Science Engineering
Specialization: Artificial Intelligence & Machine Learning

---

⭐ If you find this project useful, feel free to star the repository.
