# Password Conversion

## Description
This project is about creating a program that converts passwords hashed in MD5 to plaintext, and then hashes them back to SHA256. To do this, it uses a wordlist to brute-force the MD5 hashes.

This is used to migrate the password format of an application from MD5 to SHA256, increasing security without requiring all users to re-enter the password.

## Prerequisites
- `rockyou.txt` wordlist
- `passwords.txt` md5 hashes list

## Usage
1. Run `python ./password_conversion.py`
2. Wait until `plain.txt` is created
3. Wait until `new_passwords.txt` is created
4. Be patient pls :)

## Lessons
- MD5 hashes
- SHA256 hashes
- Brute force

## Resources
- [hashlib](https://docs.python.org/3/library/hashlib.html "hashlib")
- [Decrypt MD5 Hash using Python](https://www.youtube.com/watch?v=H_Yx73upCuY "Decrypt MD5 Hash using Python")
- [How To Hash Passwords In Python](https://nitratine.net/blog/post/how-to-hash-passwords-in-python/ "How To Hash Passwords In Python")
- [rockyou.txt wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt "rockyou.txt wordlist")
