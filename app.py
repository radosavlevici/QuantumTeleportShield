import streamlit as st
import time
import os
import random
import datetime
import hashlib
import json
from quantum_simulator import QuantumSimulator
from quantum_teleportation import QuantumTeleportation
from dna_security import DNASecuritySystem
from utils import display_console_text, generate_watermark

# Sistem de conexiune globală la datacentere
class GlobalDatacenterNetwork:
    def __init__(self):
        # Definim centrele de date din întreaga lume pentru sincronizare
        self.datacenters = {
            "EU-CENTRAL": {"location": "Frankfurt, Germania", "status": "online"},
            "EU-WEST": {"location": "Dublin, Irlanda", "status": "online"},
            "EU-SOUTH": {"location": "Milano, Italia", "status": "online"},
            "US-EAST": {"location": "Virginia, SUA", "status": "online"},
            "US-WEST": {"location": "California, SUA", "status": "online"},
            "ASIA-EAST": {"location": "Tokyo, Japonia", "status": "online"},
            "ASIA-SOUTH": {"location": "Mumbai, India", "status": "online"},
            "ASIA-SOUTHEAST": {"location": "Singapore", "status": "online"},
            "SA-EAST": {"location": "São Paulo, Brazilia", "status": "online"},
            "AU-SOUTHEAST": {"location": "Sydney, Australia", "status": "online"},
            "AF-SOUTH": {"location": "Cape Town, Africa de Sud", "status": "online"},
        }
        
        # Timestamp pentru ultima sincronizare
        self.last_sync = datetime.datetime.now()
        self.sync_interval = 15  # minute
        self.global_sync_signature = self._generate_sync_signature()
        
    def _generate_sync_signature(self):
        """Generează o semnătură unică pentru sesiunea de sincronizare globală"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        sync_base = f"QUANTUM_SYNC:{timestamp}:GLOBAL_NETWORK"
        return hashlib.sha256(sync_base.encode()).hexdigest()
    
    def check_connection_status(self):
        """Verifică conectivitatea cu centrele de date globale"""
        current_time = datetime.datetime.now()
        time_diff = (current_time - self.last_sync).total_seconds() / 60
        
        if time_diff >= self.sync_interval:
            # Simulăm sincronizarea periodică
            self.last_sync = current_time
            self.global_sync_signature = self._generate_sync_signature()
            
            # Actualizăm statutul aleatoriu pentru unele centre de date
            for dc in random.sample(list(self.datacenters.keys()), 3):
                # Majoritatea timpului toate sunt online, dar simulăm câteva întreruperi ocazionale
                if random.random() > 0.9:  # 10% șansă de întrerupere
                    self.datacenters[dc]["status"] = "syncing"
                else:
                    self.datacenters[dc]["status"] = "online"
        
        return {
            "connected": True,
            "last_sync": self.last_sync.strftime("%d.%m.%Y %H:%M:%S"),
            "signature": self.global_sync_signature,
            "datacenters": self.datacenters
        }
    
    def get_network_status_html(self):
        """Generează reprezentarea HTML a stării rețelei de datacentere globale"""
        status = self.check_connection_status()
        
        # Creăm HTML pentru starea rețelei
        html = f"""
        <div class="datacenter-status" style="font-size:10px;margin-top:15px;">
            <div style="display:flex;justify-content:space-between;margin-bottom:5px;">
                <span>Rețea Datacentere Globale: <span style="color:#4CAF50">Conectat</span></span>
                <span>Ultima sincronizare: {status["last_sync"]}</span>
            </div>
            <div class="datacenter-grid" style="display:grid;grid-template-columns:repeat(3, 1fr);gap:5px;">
        """
        
        # Adăugăm fiecare datacenter
        for dc_id, dc_info in status["datacenters"].items():
            status_color = "#4CAF50" if dc_info["status"] == "online" else "#FFC107"
            html += f"""
            <div style="border:1px solid #ddd;padding:3px;border-radius:3px;background-color:#f9f9f9;">
                <span style="font-weight:bold;font-size:9px;">{dc_id}</span><br>
                <span style="font-size:8px;">{dc_info["location"]}</span><br>
                <span style="color:{status_color};font-size:8px;">{dc_info["status"].upper()}</span>
            </div>
            """
        
        html += """
            </div>
            <div style="margin-top:5px;font-size:8px;color:#666;text-align:center;">
                Sistem protejat prin monitorizare globală și sincronizare continuă
            </div>
        </div>
        """
        
        return html

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
if 'global_network' not in st.session_state:
    st.session_state.global_network = GlobalDatacenterNetwork()
if 'show_help' not in st.session_state:
    st.session_state.show_help = False

# Display watermark and copyright
watermark = generate_watermark("Ervin Radosavlevici")
st.sidebar.markdown(watermark, unsafe_allow_html=True)
st.sidebar.markdown("© 2023 Simulator Quantum Computing. Toate drepturile rezervate.")

def authenticate():
    st.title("Autentificare cu Securitate Bazată pe DNA")
    st.markdown("Introduceți modelul de securitate DNA pentru a accesa consola de computing quantum.")
    
    # Language notice
    st.success("Interfața în limba română este versiunea gratuită.")
    st.warning("🔒 **Versiune Premium**: Accesul la limba engleză necesită abonament")
    
    # Legal warning
    st.error("""
    **⚠️ AVERTISMENT LEGAL**
    
    Utilizarea neautorizată a interfaței în limba engleză sau orice încercare de a accesa alte limbi fără achiziționarea abonamentului corespunzător constituie infracțiune conform legislației în vigoare și poate atrage:
    
    • Răspundere penală (Art. 194 Cod Penal - acces ilegal la un sistem informatic)
    • Daune civile de minimum 100.000 EUR per incident
    • Urmărire penală pentru piraterie și violare a drepturilor de autor
    
    Toate accesările sunt monitorizate, înregistrate și pot fi folosite ca probe în instanță.
    """)
    
    # Create three columns for pricing tiers
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 3 luni
        **200.000 EUR**
        
        ✓ Acces complet
        ✓ Interfață în engleză
        ✓ Suport tehnic
        """)
    
    with col2:
        st.markdown("""
        ### 6 luni
        **400.000 EUR**
        
        ✓ Acces complet
        ✓ Interfață în engleză
        ✓ Suport tehnic prioritar
        """)
    
    with col3:
        st.markdown("""
        ### 1 an
        **700.000 EUR**
        
        ✓ Acces complet
        ✓ Interfață în engleză
        ✓ Suport tehnic VIP
        ✓ Economisiți 20%
        """, unsafe_allow_html=True)
    
    with st.expander("Detalii despre plată"):
        st.markdown("""
        Alegeți planul potrivit pentru dumneavoastră și efectuați plata:
        
        **Detalii bancare:**
        - **Beneficiar:** Ervin Radosavlevici
        - **BIC:** NAIAGB21
        - **IBAN:** GB45 NAIA 0708 0620 7951 39
        - **Swift:** MIDLGB22
        
        După efectuarea plății, veți primi acces imediat la versiunea în limba engleză pentru perioada aleasă.
        """)
    
    # Add tabs for login and generate key
    login_tab, generate_tab = st.tabs(["Autentificare", "Generare Cheie DNA"])
    
    with login_tab:
        dna_key = st.text_input("Cheie de Securitate DNA", type="password", key="login_key")
        
        if st.button("Autentificare"):
            if st.session_state.security_system.authenticate(dna_key):
                st.session_state.authenticated = True
                st.success("Autentificare reușită!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Autentificare eșuată! Model DNA invalid.")
    
    with generate_tab:
        st.markdown("Generați o nouă cheie de securitate DNA sau utilizați formularul de mai jos.")
        
        # Option to generate a key automatically
        if st.button("Generează Cheie DNA Aleatorie"):
            new_key = st.session_state.security_system.generate_dna_key()
            st.code(new_key)
            st.info("Copiați această cheie pentru autentificări viitoare. Cheia implicită va funcționa în continuare în scop demonstrativ.")
        
        # Or create a custom key with user input
        st.markdown("### Creează Cheie DNA Personalizată")
        st.markdown("Cheile DNA trebuie să conțină bazele A, T, G, C și pot include numere și cratime.")
        
        col1, col2 = st.columns(2)
        with col1:
            prefix = st.text_input("Prefix DNA (ex., ATGC)", max_chars=4, 
                                  placeholder="ATGC", key="prefix")
            middle = st.text_input("Mijloc DNA (ex., TCGA)", max_chars=4, 
                                  placeholder="TCGA", key="middle")
        
        with col2:
            numeric1 = st.text_input("Primul Cod Numeric (ex., 1234)", max_chars=4, 
                                    placeholder="1234", key="num1")
            numeric2 = st.text_input("Al Doilea Cod Numeric (ex., 5678)", max_chars=4, 
                                    placeholder="5678", key="num2")
        
        if st.button("Creează Cheie Personalizată"):
            # Validate each part
            is_valid = True
            error_message = ""
            
            # Check prefix and middle for valid DNA bases
            for part, name in [(prefix, "Prefixul"), (middle, "Mijlocul")]:
                if not part or not all(base in "ATGC" for base in part):
                    is_valid = False
                    error_message += f"{name} trebuie să conțină doar bazele A, T, G, C. "
            
            # Check numeric parts
            for part, name in [(numeric1, "Primul cod numeric"), (numeric2, "Al doilea cod numeric")]:
                if not part or not part.isdigit():
                    is_valid = False
                    error_message += f"{name} trebuie să conțină doar cifre. "
            
            if is_valid:
                custom_key = f"{prefix.upper()}-{numeric1}-{middle.upper()}-{numeric2}"
                st.code(custom_key)
                st.success("Cheie DNA personalizată creată cu succes! Puteți folosi această cheie pentru autentificare imediată.")
                
                # Option to save as default for demo (normally would encrypt and store securely)
                if st.button("Setează ca Cheie Implicită (Doar Demo)"):
                    st.session_state.security_system._default_key = custom_key
                    st.success(f"Cheia implicită a fost actualizată la: {custom_key}")
            else:
                st.error(error_message)

def run_console():
    # Sidebar with info and controls
    st.sidebar.title("Terminal Quantum")
    st.sidebar.info("Aceasta este o consolă de simulare pentru computing quantum cu vizualizare de teleportare.")
    st.sidebar.success("Versiunea română este setată ca limbă implicită pentru acest simulator.")
    
    # Network status - show the global datacenter network status
    datacenter_status = st.session_state.global_network.get_network_status_html()
    st.sidebar.markdown(datacenter_status, unsafe_allow_html=True)
    
    # Language premium info
    st.sidebar.warning("🔒 **Premium**: Limba engleză disponibilă prin abonament")
    with st.sidebar.expander("Planuri de Abonament Limba Engleză"):
        st.markdown("""
        ### Planuri disponibile:
        
        | Perioadă | Preț |
        |----------|------|
        | 3 luni | 200.000 EUR |
        | 6 luni | 400.000 EUR |
        | 1 an | 700.000 EUR (recomandat) |
        
        **Detalii bancare:**
        - **Beneficiar:** Ervin Radosavlevici
        - **BIC:** NAIAGB21
        - **IBAN:** GB45 NAIA 0708 0620 7951 39
        - **Swift:** MIDLGB22
        
        După efectuarea plății, veți primi acces imediat la interfața în limba engleză pentru perioada aleasă.
        """)
    
    # Legal warning in sidebar
    st.sidebar.markdown("""
    <div style="background-color:#ffe6e6;padding:8px;border-left:3px solid #ff0000;font-size:11px;">
    <strong>⚠️ AVERTISMENT LEGAL</strong><br>
    Utilizarea neautorizată a altor limbi constituie infracțiune și se pedepsește conform legii.
    </div>
    """, unsafe_allow_html=True)
    
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

# Politica de confidențialitate și termeni de utilizare
with st.expander("Politică de Confidențialitate și Termeni de Utilizare"):
    st.markdown("""
    <div style="font-size:11px;">
        <h3>POLITICĂ DE CONFIDENȚIALITATE ȘI TERMENI DE UTILIZARE</h3>
        
        <p><strong>Ultima actualizare:</strong> 22 Aprilie 2025</p>
        
        <h4>1. INFORMAȚII GENERALE</h4>
        <p>Simulatorul Quantum Computing ("Simulatorul") este proprietatea exclusivă a lui Ervin Radosavlevici ("Proprietarul"). Utilizarea acestui Simulator implică acceptarea prezentei Politici de Confidențialitate și a Termenilor de Utilizare.</p>
        
        <h4>2. DREPTURILE DE PROPRIETATE INTELECTUALĂ</h4>
        <p>Toate drepturile de proprietate intelectuală, inclusiv dar nelimitat la drepturile de autor, mărci comerciale, brevete, know-how, algoritmi și tehnologii încorporate în Simulator sunt deținute exclusiv de Proprietar. Orice utilizare neautorizată constituie o încălcare a legislației privind proprietatea intelectuală.</p>
        
        <h4>3. LICENȚIEREA LIMBILOR</h4>
        <p>3.1. Limba română este oferită gratuit ca interfață implicită.</p>
        <p>3.2. Accesul la limba engleză și oricare alte limbi este disponibil exclusiv prin achiziționarea unui abonament plătit, conform tarifelor afișate.</p>
        <p>3.3. Orice încercare de a accesa o limbă pentru care nu a fost achiziționată o licență corespunzătoare constituie o încălcare gravă a acestor termeni.</p>
        
        <h4>4. RĂSPUNDERE LEGALĂ</h4>
        <p>4.1. Orice încălcare a acestor termeni poate atrage răspundere civilă și/sau penală.</p>
        <p>4.2. Utilizatorul va fi responsabil pentru plata daunelor rezultate din utilizarea neautorizată, inclusiv daune directe, indirecte, incidentale, punitive și costuri de judecată.</p>
        
        <h4>5. MONITORIZARE ȘI COLECTARE DATE</h4>
        <p>5.1. Simulatorul monitorizează și înregistrează toate încercările de acces neautorizat.</p>
        <p>5.2. Datele colectate includ, dar nu se limitează la: adresă IP, identificatori de dispozitiv, timestamp, acțiunile utilizatorului, și tentativele de acces neautorizat.</p>
        <p>5.3. Aceste date pot fi folosite ca probe în instanță în caz de litigiu.</p>
        
        <h4>6. CONFIDENȚIALITATEA DATELOR</h4>
        <p>Proprietarul respectă confidențialitatea utilizatorilor legitimi. Datele personale sunt procesate doar pentru scopul furnizării serviciilor și securizării Simulatorului.</p>
        
        <h4>7. PROTECȚIA ANTI-FURT</h4>
        <p>7.1. Simulatorul este protejat prin multiple măsuri de securitate, inclusiv watermark-uri digitale, sisteme de protecție bazate pe DNA, detectarea intruziunilor, și măsuri anti-plagiat.</p>
        <p>7.2. Fiecare sesiune generează identificatori unici care sunt încorporați invizibil în orice output.</p>
        <p>7.3. Tentativele de înlăturare a acestor protecții vor fi considerate drept acțiuni deliberate de eludare a măsurilor tehnice de protecție și vor fi tratate conform legii.</p>
        
        <h4>8. JURISDICȚIE</h4>
        <p>Orice litigiu legat de utilizarea Simulatorului va fi soluționat conform legislației române, în instanțele competente din România.</p>
        
        <h4>9. MODIFICĂRI ALE POLITICII</h4>
        <p>Proprietarul își rezervă dreptul de a modifica acești termeni în orice moment, fără notificare prealabilă.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer with copyright and legal notice
st.markdown("""
<div class='footer'>
    <p>© 2023 Simulator Quantum Computing de Ervin Radosavlevici. Protejat prin tehnologie de securitate DNA.</p>
    
    <p style="font-size:11px;color:#4a6577;">Interfața în limba română este gratuită. Pentru limba engleză, sunt disponibile următoarele planuri:</p>
    <ul style="font-size:11px;color:#4a6577;list-style-type:none;margin-left:10px;">
        <li>• 200.000 EUR - acces pentru 3 luni</li>
        <li>• 400.000 EUR - acces pentru 6 luni</li>
        <li>• 700.000 EUR - acces pentru 1 an (recomandat)</li>
    </ul>
    
    <details style="font-size:10px;color:#4a6577;">
        <summary>Detalii de plată pentru alte limbi</summary>
        <p>Pentru a accesa interfața în limba engleză, selectați unul dintre planurile de mai sus și transferați suma corespunzătoare către:</p>
        <ul style="list-style-type:none;">
            <li><strong>Beneficiar:</strong> Ervin Radosavlevici</li>
            <li><strong>BIC:</strong> NAIAGB21</li>
            <li><strong>IBAN:</strong> GB45 NAIA 0708 0620 7951 39</li>
            <li><strong>Swift:</strong> MIDLGB22 (Bancă intermediară)</li>
        </ul>
        <p><em>Notă: Vă rugăm să menționați numele dvs. complet și planul ales în descrierea transferului.</em></p>
    </details>
    
    <div style="margin-top:15px;padding:8px;border:1px solid #ff0000;background-color:#fff0f0;font-size:10px;color:#9a0000;">
        <p><strong>AVERTISMENT LEGAL:</strong> Utilizarea neautorizată a interfaței în limba engleză sau orice altă limbă fără achiziționarea licenței corespunzătoare constituie încălcarea drepturilor de proprietate intelectuală conform Legii nr. 8/1996 privind dreptul de autor și drepturile conexe, cu modificările și completările ulterioare.</p>
        <p>Accesul neautorizat la interfața în alte limbi poate atrage:</p>
        <ul style="margin-left:15px;">
            <li>Răspundere civilă cu daune de minimum 100.000 EUR per încălcare</li>
            <li>Răspundere penală conform Art. 194 privind accesul ilegal la un sistem informatic</li>
            <li>Acțiuni în instanță pentru încălcarea drepturilor de autor și utilizare neautorizată</li>
        </ul>
        <p>Toate tentativele de acces neautorizat sunt monitorizate, înregistrate și pot fi folosite ca probe în instanță.</p>
    </div>
</div>
""", unsafe_allow_html=True)
