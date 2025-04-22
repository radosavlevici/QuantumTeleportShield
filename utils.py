import numpy as np
import time
import hashlib
import random
import colorsys

def display_console_text(text, typing_effect=False, delay=0.02):
    """
    Formats text for console display, optionally with a typing effect simulation.
    
    Args:
        text (str): The text to display
        typing_effect (bool): Whether to add HTML for a typing effect
        delay (float): Simulated delay between characters for typing effect
    
    Returns:
        str: HTML-formatted text for display
    """
    if typing_effect:
        # Add span with typing effect class
        return f"<span class='typing-effect'>{text}</span>"
    else:
        return f"<span class='console-text'>{text}</span>"

def generate_watermark(name):
    """
    Generate a watermark with copyright information.
    
    Args:
        name (str): The name to include in the watermark
    
    Returns:
        str: HTML-formatted watermark
    """
    # Create a unique ID based on name
    identifier = hashlib.md5(name.encode()).hexdigest()[:8]
    
    # Format the watermark
    watermark = f"""
    <div class="watermark">
        <div class="watermark-text">
            <span class="copyright-symbol">©</span> 
            <span class="watermark-name">{name}</span>
            <span class="watermark-id">ID: QC-{identifier}</span>
        </div>
        <div class="watermark-notice">
            Protected by DNA Security™ Technology
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
