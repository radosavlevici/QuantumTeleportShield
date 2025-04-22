import streamlit as st
import time
import os
from quantum_simulator import QuantumSimulator
from quantum_teleportation import QuantumTeleportation
from dna_security import DNASecuritySystem
from utils import display_console_text, generate_watermark

# Set page configuration
st.set_page_config(
    page_title="Consolă de Simulare Quantum Computing Premium",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = True  # Auto-authenticate for easy access
if 'console_history' not in st.session_state:
    st.session_state.console_history = []
if 'current_command' not in st.session_state:
    st.session_state.current_command = ""
if 'quantum_simulator' not in st.session_state:
    st.session_state.quantum_simulator = QuantumSimulator()
if 'teleportation_sim' not in st.session_state:
    st.session_state.teleportation_sim = QuantumTeleportation()
if 'security_system' not in st.session_state:
    st.session_state.security_system = DNASecuritySystem()
if 'show_help' not in st.session_state:
    st.session_state.show_help = False

# Display watermark and copyright
watermark = generate_watermark("Ervin Radosavlevici")
st.sidebar.markdown(watermark, unsafe_allow_html=True)
st.sidebar.markdown("© 2023 Quantum Computing Simulator. All Rights Reserved.")

def authenticate():
    st.title("DNA-Based Security Authentication")
    st.markdown("Enter your DNA security pattern to access the quantum computing console.")
    
    # Add tabs for login and generate key
    login_tab, generate_tab = st.tabs(["Login", "Generate DNA Key"])
    
    with login_tab:
        dna_key = st.text_input("DNA Security Key", type="password", key="login_key")
        
        if st.button("Authenticate"):
            if st.session_state.security_system.authenticate(dna_key):
                st.session_state.authenticated = True
                st.success("Authentication successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Authentication failed! Invalid DNA pattern.")
    
    with generate_tab:
        st.markdown("Generate a new DNA security key or use the custom form below.")
        
        # Option to generate a key automatically
        if st.button("Generate Random DNA Key"):
            new_key = st.session_state.security_system.generate_dna_key()
            st.code(new_key)
            st.info("Copy this key for future logins. The default key will still work for demo purposes.")
        
        # Or create a custom key with user input
        st.markdown("### Create Custom DNA Key")
        st.markdown("DNA keys must have A, T, G, C bases and can include numbers and hyphens.")
        
        col1, col2 = st.columns(2)
        with col1:
            prefix = st.text_input("DNA Prefix (e.g., ATGC)", max_chars=4, 
                                  placeholder="ATGC", key="prefix")
            middle = st.text_input("DNA Middle (e.g., TCGA)", max_chars=4, 
                                  placeholder="TCGA", key="middle")
        
        with col2:
            numeric1 = st.text_input("First Number Code (e.g., 1234)", max_chars=4, 
                                    placeholder="1234", key="num1")
            numeric2 = st.text_input("Second Number Code (e.g., 5678)", max_chars=4, 
                                    placeholder="5678", key="num2")
        
        if st.button("Create Custom Key"):
            # Validate each part
            is_valid = True
            error_message = ""
            
            # Check prefix and middle for valid DNA bases
            for part, name in [(prefix, "Prefix"), (middle, "Middle")]:
                if not part or not all(base in "ATGC" for base in part):
                    is_valid = False
                    error_message += f"{name} must contain only A, T, G, C bases. "
            
            # Check numeric parts
            for part, name in [(numeric1, "First number code"), (numeric2, "Second number code")]:
                if not part or not part.isdigit():
                    is_valid = False
                    error_message += f"{name} must contain only digits. "
            
            if is_valid:
                custom_key = f"{prefix.upper()}-{numeric1}-{middle.upper()}-{numeric2}"
                st.code(custom_key)
                st.success("Custom DNA key created successfully! You can use this key to log in right away.")
                
                # Option to save as default for demo (normally would encrypt and store securely)
                if st.button("Set as Default Key (Demo Only)"):
                    st.session_state.security_system._default_key = custom_key
                    st.success(f"Default key updated to: {custom_key}")
            else:
                st.error(error_message)

def run_console():
    # Sidebar with info and controls
    st.sidebar.title("Terminal Quantum")
    st.sidebar.info("Aceasta este o consolă de simulare pentru computing quantum cu vizualizare de teleportare.")
    st.sidebar.success("Versiunea română este setată ca limbă implicită pentru acest simulator.")
    
    # Help toggle
    if st.sidebar.button("Comutare Ajutor"):
        st.session_state.show_help = not st.session_state.show_help
    
    # Main content area
    st.title("Consolă de Simulare Quantum Computing")
    
    # Display help if enabled
    if st.session_state.show_help:
        with st.expander("Comenzi Disponibile", expanded=True):
            st.markdown("""
            - `ajutor` - Afișează acest mesaj de ajutor
            - `șterge` - Șterge istoricul consolei
            - `rulează circuit` - Rulează un circuit quantum de bază
            - `teleportare` - Demonstrează teleportarea quantum
            - `generează cheie dna` - Generează o nouă cheie de securitate DNA
            - `despre` - Arată informații despre quantum computing
            - `securitate` - Arată informații despre sistemul de securitate DNA
            - `ieșire` - Șterge consola și resetează
            """)
    
    # Console output area with scrolling
    console_container = st.container()
    with console_container:
        for entry in st.session_state.console_history:
            if entry['type'] == 'command':
                st.markdown(f"<div class='console-prompt'>&gt; {entry['text']}</div>", unsafe_allow_html=True)
            elif entry['type'] == 'output':
                st.markdown(f"<div class='console-output'>{entry['text']}</div>", unsafe_allow_html=True)
            elif entry['type'] == 'visualization':
                st.plotly_chart(entry['chart'], use_container_width=True)
    
    # Command input
    command = st.text_input("Introduceți comanda:", key="command_input")
    
    if st.button("Execută") or command:
        if command:
            process_command(command)
            # Clear the input field after execution
            st.session_state.current_command = ""
            # Rerun to update the UI
            st.rerun()

def process_command(command):
    # Add command to history
    st.session_state.console_history.append({'type': 'command', 'text': command})
    
    # Process command
    command = command.lower().strip()
    
    if command == "help" or command == "ajutor":
        help_text = """
        <div class='help-text'>
        <h3>Comenzi Disponibile:</h3>
        <ul>
            <li><code>ajutor</code> - Afișează acest mesaj de ajutor</li>
            <li><code>șterge</code> - Șterge istoricul consolei</li>
            <li><code>rulează circuit</code> - Rulează un circuit quantum de bază</li>
            <li><code>teleportare</code> - Demonstrează teleportarea quantum</li>
            <li><code>generează cheie dna</code> - Generează o nouă cheie de securitate DNA</li>
            <li><code>despre</code> - Arată informații despre quantum computing</li>
            <li><code>securitate</code> - Arată informații despre sistemul de securitate DNA</li>
            <li><code>ieșire</code> - Șterge consola și resetează</li>
        </ul>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': help_text})
    
    elif command == "clear" or command == "șterge":
        st.session_state.console_history = []
        st.session_state.console_history.append({'type': 'output', 'text': "Consola a fost ștearsă."})
    
    elif command == "run circuit" or command == "rulează circuit":
        output, visualization = st.session_state.quantum_simulator.run_basic_circuit()
        st.session_state.console_history.append({'type': 'output', 'text': output})
        if visualization:
            st.session_state.console_history.append({'type': 'visualization', 'chart': visualization})
    
    elif command == "teleport" or command == "teleportare":
        output = display_console_text("Se inițializează simularea teleportării quantum...")
        st.session_state.console_history.append({'type': 'output', 'text': output})
        
        # Simulate loading
        output = display_console_text("Se configurează registrele quantum...")
        st.session_state.console_history.append({'type': 'output', 'text': output})
        
        # Run the teleportation simulation
        output, visualization = st.session_state.teleportation_sim.run_teleportation()
        st.session_state.console_history.append({'type': 'output', 'text': output})
        if visualization:
            st.session_state.console_history.append({'type': 'visualization', 'chart': visualization})
            
    elif command == "generate dna key" or command == "generează cheie dna":
        output = display_console_text("Se generează model de cheie DNA securizată...")
        st.session_state.console_history.append({'type': 'output', 'text': output})
        
        # Generate a new DNA key
        new_key = st.session_state.security_system.generate_dna_key()
        
        # Create decorative output
        dna_key_output = f"""
        <div class='info-text'>
        <h3>Cheie DNA de Securitate Generată</h3>
        <p>O nouă cheie de securitate bazată pe DNA a fost generată pentru tine:</p>
        <div class="code-block">
            <code>{new_key}</code>
        </div>
        <p>Această cheie urmează modelul perechilor de baze DNA combinat cu identificatori numerici.</p>
        <p>Poți folosi această cheie pentru autentificare în sesiunile viitoare.</p>
        
        <h4>Structura Cheii:</h4>
        <ul>
            <li><strong>Primul segment</strong>: Baze DNA (A, T, G, C)</li>
            <li><strong>Al doilea segment</strong>: Identificator numeric</li>
            <li><strong>Al treilea segment</strong>: Baze DNA (A, T, G, C)</li>
            <li><strong>Al patrulea segment</strong>: Identificator numeric</li>
        </ul>
        
        <p><em>Notă: Pentru demonstrație, poți folosi în continuare cheia implicită: ATGC-3812-TCGA-9567</em></p>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': dna_key_output})
    
    elif command == "about" or command == "despre":
        quantum_info = """
        <div class='info-text'>
        <h3>Elemente de Bază în Quantum Computing</h3>
        <p>Quantum computing folosește fenomene cuantice, precum superpoziția și entanglement-ul, pentru a efectua calcule.</p>
        
        <h4>Concepte Cheie:</h4>
        <ul>
            <li><strong>Qubit</strong>: Echivalentul cuantic al unui bit, capabil să existe în mai multe stări simultan.</li>
            <li><strong>Superpoziție</strong>: Abilitatea unui sistem cuantic de a fi în mai multe stări în același timp.</li>
            <li><strong>Entanglement</strong>: Un fenomen cuantic în care perechi de particule devin conectate și starea uneia influențează instantaneu pe cealaltă.</li>
            <li><strong>Teleportare Cuantică</strong>: Un proces care transmite starea cuantică a unei particule pe o distanță folosind entanglement-ul.</li>
        </ul>
        
        <p>Acest simulator demonstrează aceste concepte într-un mod simplificat, în scopuri educaționale.</p>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': quantum_info})
    
    elif command == "security" or command == "securitate":
        security_info = """
        <div class='info-text'>
        <h3>Sistem de Securitate Bazat pe DNA</h3>
        <p>Acest sistem utilizează principii inspirate din secvențele DNA pentru a crea autentificare securizată.</p>
        
        <h4>Caracteristici:</h4>
        <ul>
            <li><strong>Modele de Secvență</strong>: Similar perechilor de baze DNA, sistemul de securitate folosește potrivirea complexă de modele.</li>
            <li><strong>Rezistență la Mutații</strong>: Sistemul poate detecta și preveni încercările neautorizate de acces.</li>
            <li><strong>Integrare Criptografică</strong>: Modelele DNA sunt combinate cu criptografia modernă.</li>
        </ul>
        
        <p>Abordarea securității bazată pe DNA oferă o reprezentare metaforică a mecanismelor biologice de securitate.</p>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': security_info})
    
    elif command == "exit" or command == "ieșire":
        # Just clear the console instead of logging out
        st.session_state.console_history = []
        st.session_state.console_history.append({'type': 'output', 'text': "Consola a fost ștearsă. Tastează 'ajutor' pentru comenzile disponibile."})
    
    else:
        st.session_state.console_history.append({'type': 'output', 'text': f"Comandă nerecunoscută: '{command}'. Tastează 'ajutor' pentru comenzile disponibile."})

# Main app flow
if st.session_state.authenticated:
    run_console()
else:
    authenticate()

# Footer with copyright
st.markdown("""
<div class='footer'>
    <p>© 2023 Simulator Quantum Computing de Ervin Radosavlevici. Protejat prin tehnologie de securitate DNA.</p>
    <p style="font-size:11px;color:#4a6577;">Interfața în limba română este gratuită. Pentru alte limbi, vă rugăm să contactați pentru detalii de plată.</p>
</div>
""", unsafe_allow_html=True)
