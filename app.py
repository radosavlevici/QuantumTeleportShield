import streamlit as st
import time
import os
from quantum_simulator import QuantumSimulator
from quantum_teleportation import QuantumTeleportation
from dna_security import DNASecuritySystem
from utils import display_console_text, generate_watermark

# Set page configuration
st.set_page_config(
    page_title="Quantum Computing Simulation Console",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
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
    
    dna_key = st.text_input("DNA Security Key", type="password")
    
    if st.button("Authenticate"):
        if st.session_state.security_system.authenticate(dna_key):
            st.session_state.authenticated = True
            st.success("Authentication successful!")
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.error("Authentication failed! Invalid DNA pattern.")

def run_console():
    # Sidebar with info and controls
    st.sidebar.title("Quantum Terminal")
    st.sidebar.info("This is a simulation console for quantum computing with teleportation visualization.")
    
    # Help toggle
    if st.sidebar.button("Toggle Help"):
        st.session_state.show_help = not st.session_state.show_help
    
    # Main content area
    st.title("Quantum Computing Simulation Console")
    
    # Display help if enabled
    if st.session_state.show_help:
        with st.expander("Available Commands", expanded=True):
            st.markdown("""
            - `help` - Display this help message
            - `clear` - Clear console history
            - `run circuit` - Run a basic quantum circuit
            - `teleport` - Demonstrate quantum teleportation
            - `about` - Show information about quantum computing
            - `security` - Show DNA security information
            - `exit` - Log out of the console
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
    command = st.text_input("Enter command:", key="command_input")
    
    if st.button("Execute") or command:
        if command:
            process_command(command)
            # Clear the input field after execution
            st.session_state.current_command = ""
            # Rerun to update the UI
            st.experimental_rerun()

def process_command(command):
    # Add command to history
    st.session_state.console_history.append({'type': 'command', 'text': command})
    
    # Process command
    command = command.lower().strip()
    
    if command == "help":
        help_text = """
        <div class='help-text'>
        <h3>Available Commands:</h3>
        <ul>
            <li><code>help</code> - Display this help message</li>
            <li><code>clear</code> - Clear console history</li>
            <li><code>run circuit</code> - Run a basic quantum circuit</li>
            <li><code>teleport</code> - Demonstrate quantum teleportation</li>
            <li><code>about</code> - Show information about quantum computing</li>
            <li><code>security</code> - Show DNA security information</li>
            <li><code>exit</code> - Log out of the console</li>
        </ul>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': help_text})
    
    elif command == "clear":
        st.session_state.console_history = []
        st.session_state.console_history.append({'type': 'output', 'text': "Console cleared."})
    
    elif command == "run circuit":
        output, visualization = st.session_state.quantum_simulator.run_basic_circuit()
        st.session_state.console_history.append({'type': 'output', 'text': output})
        if visualization:
            st.session_state.console_history.append({'type': 'visualization', 'chart': visualization})
    
    elif command == "teleport":
        output = display_console_text("Initializing quantum teleportation simulation...")
        st.session_state.console_history.append({'type': 'output', 'text': output})
        
        # Simulate loading
        output = display_console_text("Setting up quantum registers...")
        st.session_state.console_history.append({'type': 'output', 'text': output})
        
        # Run the teleportation simulation
        output, visualization = st.session_state.teleportation_sim.run_teleportation()
        st.session_state.console_history.append({'type': 'output', 'text': output})
        if visualization:
            st.session_state.console_history.append({'type': 'visualization', 'chart': visualization})
    
    elif command == "about":
        quantum_info = """
        <div class='info-text'>
        <h3>Quantum Computing Basics</h3>
        <p>Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform computation.</p>
        
        <h4>Key Concepts:</h4>
        <ul>
            <li><strong>Qubit</strong>: The quantum equivalent of a bit, capable of existing in multiple states simultaneously.</li>
            <li><strong>Superposition</strong>: The ability of a quantum system to be in multiple states at once.</li>
            <li><strong>Entanglement</strong>: A quantum phenomenon where pairs of particles become connected and the state of one instantly influences the other.</li>
            <li><strong>Quantum Teleportation</strong>: A process that transmits the quantum state of a particle over a distance using entanglement.</li>
        </ul>
        
        <p>This simulator demonstrates these concepts in a simplified way for educational purposes.</p>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': quantum_info})
    
    elif command == "security":
        security_info = """
        <div class='info-text'>
        <h3>DNA-Based Security System</h3>
        <p>This system uses principles inspired by DNA sequences to create secure authentication.</p>
        
        <h4>Features:</h4>
        <ul>
            <li><strong>Sequence Patterns</strong>: Similar to DNA base pairs, the security system uses complex pattern matching.</li>
            <li><strong>Mutation Resistance</strong>: The system can detect and prevent unauthorized access attempts.</li>
            <li><strong>Cryptographic Integration</strong>: DNA patterns are combined with modern cryptography.</li>
        </ul>
        
        <p>The DNA-based security approach offers a metaphorical representation of biological security mechanisms.</p>
        </div>
        """
        st.session_state.console_history.append({'type': 'output', 'text': security_info})
    
    elif command == "exit":
        st.session_state.authenticated = False
        st.session_state.console_history = []
        st.experimental_rerun()
    
    else:
        st.session_state.console_history.append({'type': 'output', 'text': f"Command not recognized: '{command}'. Type 'help' for available commands."})

# Main app flow
if st.session_state.authenticated:
    run_console()
else:
    authenticate()

# Footer with copyright
st.markdown("""
<div class='footer'>
    <p>© 2023 Quantum Computing Simulator by Ervin Radosavlevici. Protected by DNA-based security technology.</p>
</div>
""", unsafe_allow_html=True)
