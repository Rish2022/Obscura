# Obscura
A Python and PyQt6 desktop file-encryption application using PBKDF2-HMAC-SHA-256 and AES-256-GCM.
# Obscura

A Python and PyQt6 desktop file-encryption application using PBKDF2-HMAC-SHA-256 and AES-256-GCM.

## Overview

Obscura is an educational desktop application that encrypts and decrypts local
files using a user-provided master password.

Its cryptographic core, Vanar Raksha Guhya, derives a 256-bit encryption key
using PBKDF2-HMAC-SHA-256 and protects file data using AES-256-GCM
authenticated encryption.

## Features

- PyQt6 desktop graphical interface
- Password-protected local file encryption and decryption
- PBKDF2-HMAC-SHA-256 password-based key derivation
- AES-256-GCM authenticated encryption
- Random salt and nonce generation
- `.vanar` encrypted-file format
- File selection and save dialogs
- Controlled handling of incorrect passwords and altered data
- Separate GUI and cryptographic-core files

## Run locally

```bash
pip install cryptography PyQt6
python Obscura.py
```

> If your GUI file has a different name, replace `Obscura.py` with that filename.

## Security Notice

This is an educational portfolio project. It has not undergone an independent
security audit and should not be used as the sole protection for critical,
regulated, financial, medical, legal, or irreplaceable data.

Always keep separate backups of original files.

## Licence

This project is licensed under the GNU General Public License v3.0.
See the [LICENSE](LICENSE) file for details.

## Author
Rishabh Narendra Pandey
- GitHub: https://github.com/Rish2022
- LinkedIn: https://www.linkedin.com/in/rishabh-pandey-baa62a16b
