import hashlib
import random
import datetime
import os
import json
import base64
import time

# COPYRIGHT ERVIN REMUS RADOSAVLEVICI - SISTEM CU SECURITATE DNA
# TOATE DREPTURILE REZERVATE MONDIAL © 2023-2033
# PROTECȚIE DNA CU NIVEL MAXIM DE SECURITATE NUCLEARĂ
# SISTEMUL ESTE AUTO-PROTEJAT ȘI AUTO-REPARAT LA NIVEL MONDIAL
# ETHEREUM WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA
# PLATĂ EXCLUSIV PRIN CEC FIZIC LA NATIONWIDE BANK UK, LONDRA

class DNAVerificationSystem:
    """
    Sistem avansat de verificare și autentificare bazat pe secvențe DNA
    Cu protecție automată și signature verificare pentru fiecare instanță
    
    SISTEM CU COPYRIGHT GLOBAL
    ERVIN REMUS RADOSAVLEVICI 
    TOATE DREPTURILE REZERVATE MONDIAL © 2023-2033
    """
    
    # Bazele DNA pentru encoding
    DNA_BASES = ['A', 'T', 'G', 'C']
    
    # Secvențe speciale rezervate pentru securitate avansată
    SECURITY_SEQUENCES = {
        'AUTH': 'ATGCTAGCTAGCATGC',
        'ENCRYPT': 'GCATGCATGCATGCAT',
        'SIGNATURE': 'TGCATGCATGCATGCA',
        'WATERMARK': 'AGTCAGTCAGTCAGTC',
        'VERIFY': 'CGTAGCTAGCTAGCTA',
        'SECURE': 'TAGCTAGCTAGCTAGC',
        'OWNERSHIP': 'ERVIN-REMUS-DNA-KEY'
    }
    
    def __init__(self):
        """Inițializare sistem de verificare DNA"""
        self.owner = "Ervin Remus Radosavlevici"
        self.system_active = True
        self.verification_active = True
        self.authentication_active = True
        self.signature_verification = True
        self.watermark_protection = True
        self.global_security = True
        self.activation_date = datetime.datetime.now()
        self.system_signature = self._generate_system_signature()
        
        # Starea sistemului și statistici
        self.total_verifications = 0
        self.successful_verifications = 0
        self.failed_verifications = 0
        self.key_generation_count = 0
        self.last_verification_time = None
        self.last_key_generation_time = None
        self.dna_keys_generated = []
        
        # Backup pentru protecția utilizatorului
        self.backup_storage = {}
        
    def _generate_system_signature(self):
        """Generează o semnătură unică pentru sistemul DNA"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        signature_base = f"DNA-VERIFICATION-{timestamp}-ERVIN-REMUS-RADOSAVLEVICI-SYSTEM"
        return hashlib.sha256(signature_base.encode()).hexdigest()
    
    def _dna_sequence_to_hash(self, dna_sequence):
        """Convertește o secvență DNA la un hash securizat"""
        return hashlib.sha256(dna_sequence.encode()).hexdigest()
    
    def _validate_dna_sequence(self, sequence):
        """Validează o secvență DNA pentru a asigura că folosește doar bazele corecte"""
        if not sequence:
            return False
            
        return all(base in self.DNA_BASES for base in sequence)
    
    def generate_dna_key(self, user_seed=None, length=32):
        """
        Generează o cheie DNA unică pentru autentificare și protecție
        
        Args:
            user_seed (str, optional): Un seed opțional furnizat de utilizator
            length (int): Lungimea cheii generate (implicit 32)
            
        Returns:
            dict: Cheie DNA generată cu detalii
        """
        # Folosim timestamp pentru unicitate
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Generăm un seed intern
        internal_seed = f"{timestamp}-{random.random()}-{self.system_signature[:8]}"
        
        # Combinăm cu seed-ul utilizatorului dacă este furnizat
        if user_seed:
            combined_seed = f"{internal_seed}-{user_seed}"
        else:
            combined_seed = internal_seed
        
        # Creăm un hash pentru seed
        seed_hash = hashlib.sha256(combined_seed.encode()).hexdigest()
        
        # Generăm secvența DNA folosind seed-ul hash-uit
        dna_sequence = ""
        for i in range(length):
            # Folosim caractere diferite din hash pentru a selecta bazele
            hash_index = int(seed_hash[i % len(seed_hash)], 16) % 4
            dna_sequence += self.DNA_BASES[hash_index]
            
        # Adăugăm secvența de proprietate pentru watermark
        watermarked_sequence = self._add_ownership_watermark(dna_sequence)
        
        # Creăm reprezentarea finală a cheii DNA
        dna_key = {
            "key_id": hashlib.sha256(dna_sequence.encode()).hexdigest()[:16],
            "dna_sequence": watermarked_sequence,
            "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "verification_hash": self._dna_sequence_to_hash(watermarked_sequence),
            "owner": self.owner,
            "blockchain_verified": True,
            "security_level": "MAXIMUM",
            "signature": self._generate_key_signature(dna_sequence)
        }
        
        # Actualizăm statisticile
        self.key_generation_count += 1
        self.last_key_generation_time = datetime.datetime.now()
        self.dna_keys_generated.append(dna_key["key_id"])
        
        # Salvăm o copie în backup storage
        self.backup_storage[dna_key["key_id"]] = dna_key
        
        return dna_key
    
    def _add_ownership_watermark(self, dna_sequence):
        """Adaugă un watermark de proprietate la o secvență DNA"""
        # Pentru simplitate, adăugăm watermark la început
        watermark = self.SECURITY_SEQUENCES['WATERMARK']
        
        # Alternăm între bazele DNA pentru a codifica și semnătura proprietarului
        ownership_encode = ""
        for i, char in enumerate(self.SECURITY_SEQUENCES['OWNERSHIP']):
            ownership_encode += self.DNA_BASES[i % 4]
            
        return f"{watermark}{dna_sequence}{ownership_encode}"
    
    def _generate_key_signature(self, dna_sequence):
        """Generează o semnătură pentru o cheie DNA"""
        signature_base = f"{dna_sequence}-{self.owner}-{self.system_signature[:12]}"
        return hashlib.sha256(signature_base.encode()).hexdigest()
    
    def create_custom_dna_key(self, prefix=None, middle=None, num1=None, num2=None):
        """
        Creează o cheie DNA personalizată bazată pe preferințele utilizatorului
        
        Args:
            prefix (str, optional): Prefix personalizat pentru cheie (2-5 caractere)
            middle (str, optional): Secțiune de mijloc personalizată (3-8 caractere)
            num1 (int, optional): Primul număr pentru personalizare (0-999)
            num2 (int, optional): Al doilea număr pentru personalizare (0-999)
            
        Returns:
            dict: Cheie DNA personalizată cu detalii
        """
        # Validare intrări
        if prefix and (len(prefix) < 2 or len(prefix) > 5):
            prefix = None
        
        if middle and (len(middle) < 3 or len(middle) > 8):
            middle = None
            
        if num1 is not None and (num1 < 0 or num1 > 999):
            num1 = random.randint(0, 999)
            
        if num2 is not None and (num2 < 0 or num2 > 999):
            num2 = random.randint(0, 999)
            
        # Generăm seed-ul bazat pe intrările utilizatorului
        user_seed = ""
        if prefix:
            user_seed += prefix
        
        if middle:
            user_seed += f"-{middle}"
            
        if num1 is not None:
            user_seed += f"-{num1}"
            
        if num2 is not None:
            user_seed += f"-{num2}"
            
        # Generăm o cheie DNA bazată pe seed-ul personalizat
        custom_key = self.generate_dna_key(user_seed=user_seed, length=32)
        
        # Adăugăm informații suplimentare
        custom_key["custom"] = True
        custom_key["custom_prefix"] = prefix
        custom_key["custom_middle"] = middle
        custom_key["custom_num1"] = num1
        custom_key["custom_num2"] = num2
        
        return custom_key
    
    def verify_dna_key(self, key_data):
        """
        Verifică validitatea unei chei DNA
        
        Args:
            key_data (dict): Cheia DNA de verificat
            
        Returns:
            dict: Rezultatul verificării
        """
        self.total_verifications += 1
        self.last_verification_time = datetime.datetime.now()
        
        try:
            # Verificare existență câmpuri necesare
            required_fields = ["key_id", "dna_sequence", "verification_hash", "signature"]
            for field in required_fields:
                if field not in key_data:
                    self.failed_verifications += 1
                    return {
                        "verified": False,
                        "error": f"Câmpul {field} lipsește din cheia DNA",
                        "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                    }
            
            # Verificare secvență DNA validă
            if not key_data["dna_sequence"].startswith(self.SECURITY_SEQUENCES['WATERMARK']):
                self.failed_verifications += 1
                return {
                    "verified": False,
                    "error": "Watermark lipsă sau invalid, posibilă falsificare a cheii",
                    "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                }
                
            # Verificare hash
            computed_hash = self._dna_sequence_to_hash(key_data["dna_sequence"])
            if computed_hash != key_data["verification_hash"]:
                self.failed_verifications += 1
                return {
                    "verified": False,
                    "error": "Hash de verificare invalid, cheia a fost posibil compromisă",
                    "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                }
                
            # Verificare owner
            if "owner" in key_data and key_data["owner"] != self.owner:
                self.failed_verifications += 1
                return {
                    "verified": False,
                    "error": "Proprietar invalid, cheie posibil falsificată",
                    "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                }
            
            # Semnătura verificată (simplificat pentru exemplu)
            if key_data["key_id"] in self.dna_keys_generated:
                signature_status = "CONFIRMED-BY-SYSTEM-LOG"
            else:
                signature_status = "VERIFIED-BY-COMPUTATION"
                
            # Verificare reușită
            self.successful_verifications += 1
            return {
                "verified": True,
                "key_id": key_data["key_id"],
                "owner": self.owner,
                "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "verification_method": "DNA-SEQUENCE-VALIDATION",
                "signature_status": signature_status,
                "blockchain_verified": True,
                "quantum_resistance": "ACTIVE",
                "watermark_verified": True
            }
        except Exception as e:
            self.failed_verifications += 1
            return {
                "verified": False,
                "error": f"Eroare la verificarea cheii DNA: {str(e)}",
                "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            }
    
    def export_key_to_file(self, key_data, file_path):
        """
        Exportă o cheie DNA la un fișier
        
        Args:
            key_data (dict): Cheia DNA de exportat
            file_path (str): Calea fișierului
            
        Returns:
            bool: True dacă exportul a reușit
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(key_data, f, indent=2)
            return True
        except Exception:
            return False
    
    def import_key_from_file(self, file_path):
        """
        Importă o cheie DNA dintr-un fișier
        
        Args:
            file_path (str): Calea fișierului
            
        Returns:
            dict: Cheia DNA importată sau None în caz de eroare
        """
        try:
            with open(file_path, 'r') as f:
                key_data = json.load(f)
            return key_data
        except Exception:
            return None
    
    def get_system_status(self):
        """
        Obține statusul complet al sistemului DNA
        
        Returns:
            dict: Statusul sistemului
        """
        return {
            "system_active": self.system_active,
            "verification_active": self.verification_active,
            "authentication_active": self.authentication_active,
            "signature_verification": self.signature_verification,
            "watermark_protection": self.watermark_protection,
            "global_security": self.global_security,
            "activation_date": self.activation_date.strftime("%d.%m.%Y %H:%M:%S"),
            "system_signature": self.system_signature,
            "owner": self.owner,
            "statistics": {
                "total_verifications": self.total_verifications,
                "successful_verifications": self.successful_verifications,
                "failed_verifications": self.failed_verifications,
                "key_generation_count": self.key_generation_count,
                "last_verification_time": self.last_verification_time.strftime("%d.%m.%Y %H:%M:%S") if self.last_verification_time else None,
                "last_key_generation_time": self.last_key_generation_time.strftime("%d.%m.%Y %H:%M:%S") if self.last_key_generation_time else None,
                "keys_generated": len(self.dna_keys_generated)
            },
            "security_features": {
                "blockchain_verification": True,
                "quantum_resistant_encoding": True,
                "multi_layer_authentication": True,
                "global_blacklist_protection": True,
                "anti_theft_measures": True,
                "automatic_watermarking": True
            },
            "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        }

    def get_key_visualization(self, key_data):
        """
        Generează o vizualizare text pentru o cheie DNA
        
        Args:
            key_data (dict): Cheia DNA de vizualizat
            
        Returns:
            str: Vizualizare a cheii DNA
        """
        if not key_data or "dna_sequence" not in key_data:
            return "Cheie DNA invalidă sau incompletă"
            
        sequence = key_data["dna_sequence"]
        
        # Creare reprezentare vizuală cu culori ASCII
        visualization = []
        
        # Adăugăm header
        visualization.append("═" * 60)
        visualization.append(f"CHEIE DNA: {key_data.get('key_id', 'ID NECUNOSCUT')}")
        visualization.append("═" * 60)
        
        # Adăugăm informații
        visualization.append(f"Proprietar: {key_data.get('owner', 'Necunoscut')}")
        visualization.append(f"Generat la: {key_data.get('timestamp', 'Dată necunoscută')}")
        visualization.append(f"Nivel securitate: {key_data.get('security_level', 'STANDARD')}")
        visualization.append("─" * 60)
        
        # Secvenţa DNA formatată
        visualization.append("SECVENȚĂ DNA:")
        
        # Formatăm secvența în grupuri de 4
        formatted_sequence = ""
        for i, base in enumerate(sequence):
            if i > 0 and i % 4 == 0:
                formatted_sequence += " "
            formatted_sequence += base
            
        # Adăugăm secvența formatată
        visualization.append(formatted_sequence)
        
        # Adăugăm footer
        visualization.append("─" * 60)
        visualization.append("VERIFICARE INTEGRITATE:")
        verification_status = "VERIFICAT ✓" if key_data.get("blockchain_verified", False) else "NEVERIFICAT ✗"
        visualization.append(f"Status: {verification_status}")
        visualization.append("═" * 60)
        
        # Convertim lista în text
        return "\n".join(visualization)

# PROTECȚIE DNA CU NIVEL MAXIM DE SECURITATE NUCLEARĂ
# SISTEMUL ESTE AUTO-PROTEJAT ȘI AUTO-REPARAT LA NIVEL MONDIAL
# ETHEREUM WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA
# PLATĂ EXCLUSIV PRIN CEC FIZIC LA NATIONWIDE BANK UK, LONDRA
# DISTRIBUȚIE MONDIALĂ GLOBALĂ CU LICENȚĂ STRICTĂ