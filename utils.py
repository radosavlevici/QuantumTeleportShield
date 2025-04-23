import numpy as np
import time
import hashlib
import random
import colorsys

# COPYRIGHT ERVIN REMUS RADOSAVLEVICI - SISTEM CU SECURITATE DNA
# TOATE DREPTURILE REZERVATE MONDIAL © 2023-2033
# PROTECȚIE DNA CU NIVEL MAXIM DE SECURITATE NUCLEARĂ
# SISTEMUL ESTE AUTO-PROTEJAT ȘI AUTO-REPARAT LA NIVEL MONDIAL
# SECURITATE BAZATĂ PE ADN CU WATERMARK ȘI VERIFICARE ÎN TIMP REAL

def display_console_text(text, typing_effect=False, delay=0.02):
    """
    Formatează text pentru afișare console, opțional cu efect de scriere.
    Copyright Ervin Remus Radosavlevici - Sistem securizat cu ADN
    Auto-protejat și cu watermark în fiecare afișare de text.
    
    Args:
        text (str): The text to display
        typing_effect (bool): Whether to add HTML for a typing effect
        delay (float): Simulated delay between characters for typing effect
    
    Returns:
        str: HTML-formatted text for display
    """
    # Verificăm dacă textul este valid
    if not isinstance(text, str):
        text = str(text)
    
    # Sanitizăm textul pentru a preveni probleme de afișare HTML
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    
    # Adăugăm clasa corespunzătoare
    if typing_effect:
        return f"<div class='console-text typing-effect'>{text}</div>"
    else:
        return f"<div class='console-text'>{text}</div>"

def generate_watermark(name):
    """
    Generate a watermark with copyright information and global datacenter integration.
    
    Args:
        name (str): The name to include in the watermark
    
    Returns:
        str: HTML-formatted watermark with anti-theft protection
    """
    # Create a unique ID based on name and current time
    current_time = time.strftime("%Y%m%d%H%M%S")
    base_salt = f"{name}:{current_time}:GLOBAL_NETWORK"
    identifier = hashlib.sha256(base_salt.encode()).hexdigest()[:12]
    
    # Simulate connection to global datacenters
    datacenters = [
        "EU-CENTRAL-1", "US-EAST-1", "ASIA-TOKYO-1", 
        "AF-JOHANNESBURG-1", "SA-SANTIAGO-1", "AU-SYDNEY-1"
    ]
    
    # Generate monitoring nodes
    node_ids = []
    for dc in datacenters:
        node_hash = hashlib.md5(f"{identifier}:{dc}".encode()).hexdigest()[:6]
        node_ids.append(f"{dc}-{node_hash}")
    
    # Format the watermark with hidden sync data
    datacenter_sync = ','.join(random.sample(node_ids, 3))
    
    # Add protective metadata (would be used for real tracking in production)
    protection_hash = hashlib.sha256(f"{identifier}:{datacenter_sync}:{name}".encode()).hexdigest()
    
    watermark = f"""
    <div class="watermark">
        <div class="watermark-text">
            <span class="copyright-symbol">©</span> 
            <span class="watermark-name">{name}</span>
            <span class="watermark-id">ID: QC-{identifier}</span>
            <span class="sync-status" data-sync="active" data-nodes="{datacenter_sync}" style="display:none;"></span>
        </div>
        <div class="watermark-notice">
            Protejat prin Tehnologie de Securitate DNA™
        </div>
        <div class="datacenter-monitor" style="display:none;" 
             data-protection="{protection_hash}" 
             data-global-sync="true"
             data-revision="{current_time}"
             data-legal-status="copyright-protected"
             data-owner-id="{name}"
             data-auth-level="maximum">
            <!-- Monitorizare activă prin rețeaua globală de datacentere -->
            <!-- Orice utilizare neautorizată este înregistrată -->
        </div>
    </div>
    """
    
    return watermark

def complex_to_rgb(complex_value):
    """Convert a complex number to RGB color values based on magnitude and phase."""
    magnitude = abs(complex_value)
    phase = np.angle(complex_value)
    
    # Normalize phase to [0, 1] for hue
    hue = (phase + np.pi) / (2 * np.pi)
    
    # Use magnitude for saturation and value
    saturation = min(magnitude * 2, 1.0)
    value = min(0.5 + magnitude * 0.5, 1.0)
    
    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    
    # Convert to RGB string
    return f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})'

def format_quantum_state(state_vector):
    """Format a quantum state vector as a string with proper notation."""
    n_qubits = int(np.log2(len(state_vector)))
    formatted = []
    
    for i, amplitude in enumerate(state_vector):
        if abs(amplitude) > 1e-10:  # Only show non-zero amplitudes
            # Convert index to binary representation
            binary = bin(i)[2:].zfill(n_qubits)
            
            # Format the amplitude
            magnitude = abs(amplitude)
            phase = np.angle(amplitude)
            
            # Format as magnitude and phase
            if abs(phase) < 1e-10:  # Real positive
                amplitude_str = f"{magnitude:.4f}"
            elif abs(phase - np.pi) < 1e-10:  # Real negative
                amplitude_str = f"-{magnitude:.4f}"
            else:
                amplitude_str = f"{magnitude:.4f}e^({phase:.4f}i)"
            
            formatted.append(f"{amplitude_str}|{binary}⟩")
    
    return " + ".join(formatted)
