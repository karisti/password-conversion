'''
	@Author: Kepa Aristi
	@Date: 30/11/2022
	@Links: https://github.com/karisti
'''

import sys, signal
import hashlib


############ Setup variables ############

WORDLIST_PATH = "rockyou.txt"
HASHES_FILE = "passwords_example.txt"

#########################################

def sig_handler(sig, frame):
	print("\n\nExiting... 👋👋")
	sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)



class PassClass:
	def __init__(self, md5):
		self.md5 = md5
		self.plain = ''
		self.sha256 = ''
	
	def print_pass(self):
		print("MD5: " + self.md5 + " // " + "Plain: " + self.plain + " // " + "SHA256: " + self.sha256)



def print_pass_array(passwd_array):
	for passwd in passwd_array:
		passwd.print_pass()


def load_hashes(hashes_file):
	pass_class_array = []
	with open(hashes_file, "r", encoding="utf-8", errors='ignore') as passwords_file:
		for password in passwords_file:
			pass_class_array.append(PassClass(password.strip()))

	return pass_class_array


def plain_to_md5(plain):
	encoded_password = plain.strip().encode('utf-8')
	md5 = hashlib.md5(encoded_password.strip()).hexdigest()
	return md5


def check_matches(rock_md5, rock_plain, pass_class_array):
	for pass_class in pass_class_array:
		if len(pass_class.plain) > 0:
			continue
		if pass_class.md5 == rock_md5:
			pass_class.plain = rock_plain
			# print(rock_md5 + " --- " + rock_plain)

	return pass_class_array


def save_plain_to_file(pass_class_array):
	print("\n💾 Saving to 'plain.txt' ...")

	with open('plain.txt', 'w') as f:
		for pass_class in pass_class_array:
			f.write(pass_class.plain + '\n')


def save_sha256_to_file(pass_class_array):
	print("\n💾 Saving to 'new_passwords.txt' ...")

	with open('new_passwords.txt', 'w') as f:
		for pass_class in pass_class_array:
			f.write(pass_class.sha256 + '\n')


def get_plain_from_md5(pass_class_array, wordlist_path):
	print("\n⚡ Bruteforcing MD5 hashes using '" + WORDLIST_PATH + "' ...")

	with open(wordlist_path, "r", encoding="utf-8", errors='ignore') as wordlist_file:
		for rock_plain in wordlist_file:
			rock_md5 = plain_to_md5(rock_plain.strip())
			pass_class_array = check_matches(rock_md5, rock_plain.strip(), pass_class_array)


def get_sha256_from_plain(pass_class_array):
	print("\n⚡ Hashing plain passwords to SHA256 with random salt ...")

	for idx, pass_class in enumerate(pass_class_array):
		if (len(pass_class.plain) > 0):
			salt = str(idx).encode('utf-8')
			key = hashlib.pbkdf2_hmac('sha256', pass_class.plain.encode('utf-8'), salt, 100000)
			pass_class.sha256 = key.hex()



def main():
	# Load hashes
	pass_class_array = load_hashes(HASHES_FILE)

	# Get plain text from MD5
	get_plain_from_md5(pass_class_array, WORDLIST_PATH)
	save_plain_to_file(pass_class_array)

	# Get SHA256 from plain text
	get_sha256_from_plain(pass_class_array)
	save_sha256_to_file(pass_class_array)

	print("\n✅ All done!! See created files :)")

	# Print data to console
	# print_pass_array(pass_class_array)



if __name__ == "__main__":
	main()
