
import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag
from PyQt6.QtWidgets import QMessageBox

class Vanar_Guhya_Raksha:

    def __init__(self, Master_Password: str ,Salt: bytes = None):  # IF there is no salt provided create random
        # Establish the mathematical stretching parameters using PBKDF2
        self.Vault_Salt = Salt if Salt else os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.Vault_Salt,
            iterations=600000)

        self.Master_Key = kdf.derive(Master_Password.encode("utf-8"))
        self.aesgcm = AESGCM(self.Master_Key)

    def Guhya_Data(self, Raw_Data: bytes):
        """UNIVERSAL CRYPTOGRAPHIC VAULT CORE for everything """

        Guhya_Nonce = os.urandom(12)

        Encrypted_Bytes = self.aesgcm.encrypt(
            nonce=Guhya_Nonce,
            data=Raw_Data,
            associated_data=None
        )

        Final_Bytes = (self.Vault_Salt) + Guhya_Nonce + Encrypted_Bytes

        return Final_Bytes

    def Rahasya_Bhedan(Gopaniya_Data: bytes, Master_Password: str) -> bytes:
        """Strips Base64 armor, perfectly slices the components, and decrypts."""
        try:
            Final_Bytes = Gopaniya_Data
            Vault_Salt_Check = Final_Bytes[:16]

            Guhya_Nonce_Check = Final_Bytes[16:28]
            Guhya_Data = Final_Bytes[28:]

            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=Vault_Salt_Check,
                iterations=600000
            )

            Final_Master_Key = kdf.derive(Master_Password.encode("utf-8"))
            Temp_aesgcm = AESGCM(Final_Master_Key)

            # 4. Decrypt and verify Galois Tag

            Rahasya_Bhedan_Data = Temp_aesgcm.decrypt(
                nonce=Guhya_Nonce_Check,
                data=Guhya_Data,
                associated_data=None
            )
            return Rahasya_Bhedan_Data

        except InvalidTag:
            return b"TAMPER_DETECTED"
        except Exception as e:
            print(f"Vault_Error: {e}")
            return b"ERROR"
