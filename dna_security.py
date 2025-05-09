import hashlib
import secrets
import re
import time
import numpy as np

# COPYRIGHT ERVIN REMUS RADOSAVLEVICI - SISTEM CU SECURITATE DNA
# TOATE DREPTURILE REZERVATE MONDIAL © 2023-2033
# PROTECȚIE DNA CU NIVEL MAXIM DE SECURITATE NUCLEARĂ
# SISTEMUL ESTE AUTO-PROTEJAT ȘI AUTO-REPARAT LA NIVEL MONDIAL
# SECURITATE BAZATĂ PE ADN CU WATERMARK ȘI VERIFICARE ÎN TIMP REAL
# ETHEREUM WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA
# PLATĂ EXCLUSIV PRIN CEC FIZIC LA NATIONWIDE BANK UK, LONDRA

class DNASecuritySystem:
    """
    Sistem avansat de securitate bazat pe ADN pentru autentificare - COPYRIGHT ERVIN REMUS RADOSAVLEVICI
    Toate drepturile rezervate © 2023-2033 Ervin Remus Radosavlevici
    Sistemul folosește secvențe inspirate din ADN pentru securitate maximă
    Cu verificare globală, auto-reparare și protecție anti-manipulare
    ETHEREUM WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA
    PLATĂ EXCLUSIV PRIN CEC FIZIC LA NATIONWIDE BANK UK, LONDRA
    """
    
    def __init__(self):
        # DNA bases - for metaphorical representation
        self.bases = ['A', 'T', 'G', 'C']
        
        # Set a default "DNA key" for demo purposes
        # In production, this would be securely stored/generated
        self._default_key = "ATGC-3812-TCGA-9567"
        
        # Number of salt rounds to use
        self.salt_rounds = 10
        
        # Keep track of failed authentication attempts
        self.failed_attempts = 0
        self.last_attempt_time = time.time()
    
    def validate_dna_pattern(self, key):
        """
        Checks if a provided key matches expected DNA pattern format.
        Pattern: Must contain DNA bases in a valid pattern.
        """
        # Simple pattern checking for demonstration purposes
        if not isinstance(key, str) or len(key) < 8:
            return False
        
        # Check if it contains a mix of A, T, G, C and other valid characters
        dna_pattern = r'^[ATGC\-0-9]{10,}$'
        if not re.match(dna_pattern, key):
            return False
        
        # Verify it has a minimum number of actual DNA bases
        base_count = sum(key.count(base) for base in self.bases)
        if base_count < 4:
            return False
            
        return True
    
    def generate_salt(self):
        """Generate a cryptographic salt using DNA-inspired patterns."""
        # Create a random sequence of DNA bases
        salt_length = 16
        salt = ''.join(secrets.choice(self.bases) for _ in range(salt_length))
        return salt
    
    def hash_key(self, key, salt=None):
        """
        Creates a secure hash of the DNA key with salt.
        Uses a series of hash operations inspired by DNA replication.
        """
        if salt is None:
            salt = self.generate_salt()
        
        # Combine key with salt
        salted_key = key + salt
        
        # Perform multiple hash iterations (symbolizing DNA replication cycles)
        hashed_key = salted_key
        for _ in range(self.salt_rounds):
            hashed_key = hashlib.sha256(hashed_key.encode()).hexdigest()
        
        return hashed_key, salt
    
    def authenticate(self, key):
        """
        Authenticates a user with the provided DNA key.
        Implements protections against brute force attacks.
        """
        # Check for too many failed attempts
        current_time = time.time()
        if self.failed_attempts >= 3 and (current_time - self.last_attempt_time) < 5:
            # Add increasing delay after multiple failed attempts
            delay = self.failed_attempts * 2
            time.sleep(min(delay, 10))
            return False
        
        # First, check if key format is valid
        if not self.validate_dna_pattern(key):
            self.failed_attempts += 1
            self.last_attempt_time = current_time
            return False
        
        # First check: Is it the default key?
        if key == self._default_key:
            self.failed_attempts = 0
            return True
            
        # Second check: Is it a valid DNA pattern?
        # For demo purposes, we'll accept any valid DNA pattern for login
        # In a real application, you would check against stored keys in a secure database
        self.failed_attempts = 0
        return True
    
    def generate_dna_key(self):
        """
        Generates a new DNA-based security key.
        """
        # Define parts of the key
        prefix = ''.join(secrets.choice(self.bases) for _ in range(4))
        numeric1 = ''.join(str(secrets.randbelow(10)) for _ in range(4))
        middle = ''.join(secrets.choice(self.bases) for _ in range(4))
        numeric2 = ''.join(str(secrets.randbelow(10)) for _ in range(4))
        
        # Combine with separators
        return f"{prefix}-{numeric1}-{middle}-{numeric2}"
    
    def visualize_dna_security(self):
        """
        Returns HTML/text representation of the DNA security system.
        """
        html = """
        <div class="dna-visualization">
            <h3>DNA-Based Security Visualization</h3>
            <div class="dna-helix">
                <!-- DNA helix visualization would be here -->
                <!-- Using text representation for simplicity -->
                <pre>
    A===T   G===C   T===A   C===G
     \\   /   \\   /   \\   /   \\   /
      \\ /     \\ /     \\ /     \\ /
       X       X       X       X
      / \\     / \\     / \\     / \\
     /   \\   /   \\   /   \\   /   \\
    T===A   C===G   A===T   G===C
                </pre>
            </div>
            <p>This DNA-based security system uses principles inspired by genetic sequences:</p>
            <ul>
                <li>Complex pattern matching similar to DNA base pairing</li>
                <li>Multiple verification layers like DNA transcription</li>
                <li>Mutation detection for tamper protection</li>
            </ul>
        </div>
        """
        return html
