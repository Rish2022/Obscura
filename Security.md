# Security Policy

## Project Status

Obscura is an educational portfolio project demonstrating local file encryption
with PBKDF2-HMAC-SHA-256 and AES-256-GCM.

It has not undergone an independent security audit. Do not use it as the sole
protection for critical, regulated, financial, medical, legal, or irreplaceable data.

## Reporting a Security Issue

Please do not post possible security vulnerabilities in public GitHub issues.

Report security concerns privately to:

**rishabhpandey728@gmail.com**

Include:

Short description:
Obscura crashes when I try to decrypt a damaged .vanar file.

Steps to reproduce:
1. Encrypt a small .txt file with Obscura.
2. Open the resulting .vanar file in a text editor or hex editor.
3. Change one character/byte near the end.
4. Try to decrypt the modified .vanar file in Obscura.

Affected file or feature:
Rahasya_Bhedan / decrypt_file function.

Expected behavior:
The app should show a controlled message explaining that the password may be
incorrect or the encrypted file may be corrupted.

Actual behavior:
The application closes unexpectedly / displays an unhandled error.

## Scope

This project is intended for educational and portfolio purposes. Always retain
separate backups of original files before encryption or decryption.
