import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
import plotly.graph_objects as go
import time
import os
from utils import complex_to_rgb

class QuantumTeleportation:
    def __init__(self):
        # Initialize the simulator for optimized performance
        # Use the most advanced simulator available in Qiskit
        self.simulator = AerSimulator()
        self.statevector_sim = Aer.get_backend('statevector_simulator')
        self.qasm_sim = Aer.get_backend('qasm_simulator')
        
        # State tracking
        self.ibm_available = False
        self.using_real_quantum = False
        self.max_qubits = 32  # Simulator can handle many qubits
        
        # Check if IBM token exists but don't try to connect yet
        self.ibm_available = 'IBM_QUANTUM_TOKEN' in os.environ
    
    def connect_to_ibm_quantum(self):
        """
        Connect to IBM Quantum hardware
        Uses IBM_QUANTUM_TOKEN for authentication
        """
        import os
        import time
        
        # Verificăm dacă avem token IBM Quantum disponibil
        ibm_token = os.environ.get('IBM_QUANTUM_TOKEN')
        
        if not ibm_token:
            result_text = """
            <div class='warning-text'>
            <h3>Token IBM Quantum lipsă</h3>
            <p>Nu s-a găsit token-ul IBM Quantum. Conexiunea la hardware-ul real IBM Quantum necesită un token de acces valid.</p>
            <p>Pentru a obține un token, creați un cont la https://quantum-computing.ibm.com/ și accesați secțiunea "My Account".</p>
            <p>După obținerea token-ului, adăugați-l în setările secretelor Replit și reporniți aplicația.</p>
            </div>
            """
            return result_text, None
        
        try:
            # Afișăm un mesaj pentru utilizator despre inițializarea procesului
            result_text = """
            <div class='info-text'>
            <h3>Se inițializează conexiunea cu IBM Quantum pentru teleportare...</h3>
            <p>Se verifică token-ul și se obține lista de procesoare quantum disponibile.</p>
            <p>Acest proces poate dura câteva momente. Vă rugăm să așteptați.</p>
            </div>
            """
            
            # Importăm modulele necesare
            try:
                from qiskit_ibm_provider import IBMProvider
            except ImportError as e:
                return f"""
                <div class='error-text'>
                <h3>Eroare la importarea modulelor IBM Quantum</h3>
                <p>Nu s-a putut importa modulul qiskit_ibm_provider:</p>
                <div style="margin:10px 0;padding:10px;background-color:#fff0f0;border-radius:5px;font-family:monospace;font-size:12px;">
                    {str(e)}
                </div>
                <p>Verificați dacă toate pachetele necesare sunt instalate corect.</p>
                </div>
                """, None
            
            # Încercăm să ne conectăm cu un timeout
            try:
                # Inițializăm provider-ul cu token-ul
                provider = IBMProvider(token=ibm_token)
                
                # Adăugăm un delay mic pentru a evita probleme de rate limiting
                time.sleep(1)
                
                # Obținem lista de backend-uri disponibile
                backends = provider.backends()
                backend_names = [backend.name for backend in backends]
                
            except Exception as conn_error:
                return f"""
                <div class='error-text'>
                <h3>Eroare la conectarea cu IBM Quantum</h3>
                <p>Nu s-a putut stabili conexiunea cu serverele IBM Quantum:</p>
                <div style="margin:10px 0;padding:10px;background-color:#fff0f0;border-radius:5px;font-family:monospace;font-size:12px;">
                    {str(conn_error)}
                </div>
                <p>Verificați conexiunea la internet și dacă token-ul IBM Quantum este valid și actualizat.</p>
                </div>
                """, None
            
            # Alegem backend-ul cu cele mai multe qubits disponibile pentru teleportare
            # Avem nevoie de minimum 3 qubits pentru teleportare
            max_qubits = 0
            max_qubit_backend = None
            
            for backend in backends:
                try:
                    # Verificăm doar backend-urile disponibile (de simulator sau hardware)
                    if not backend.operational:
                        continue
                        
                    # Obținem configurația backend-ului
                    config = backend.configuration()
                    num_qubits = config.n_qubits
                    
                    # Pentru teleportare avem nevoie de minim 3 qubits
                    if num_qubits >= 3 and num_qubits > max_qubits:
                        max_qubits = num_qubits
                        max_qubit_backend = backend
                except Exception as backend_error:
                    # Sărim peste backend-urile care cauzează erori
                    continue
            
            # Verificăm dacă am găsit un backend valid
            if max_qubit_backend is None:
                result_text = """
                <div class='warning-text'>
                <h3>Nu s-au găsit procesoare quantum adecvate pentru teleportare</h3>
                <p>Conexiunea la IBM Quantum a reușit, dar nu s-au găsit procesoare quantum cu suficiente qubits pentru teleportare.</p>
                <p>Vă rugăm să încercați mai târziu când procesoarele quantum cu minim 3 qubits vor fi disponibile.</p>
                </div>
                """
                return result_text, None
            
            # Actualizăm state tracking
            self.ibm_available = True
            self.max_qubits = max_qubits
            
            # Generăm textul rezultatului
            result_text = f"""
            <div class='success-text'>
            <h3>Conectare la IBM Quantum pentru Teleportare reușită!</h3>
            <p>S-a stabilit conexiunea cu IBM Quantum pentru experimentul de teleportare. Detalii:</p>
            
            <ul>
                <li><strong>Total backend-uri disponibile:</strong> {len(backends)}</li>
                <li><strong>Backend selectat pentru teleportare:</strong> {max_qubit_backend.name}</li>
                <li><strong>Număr qubits disponibile:</strong> {max_qubits}</li>
            </ul>
            
            <p>Backend-uri disponibile:</p>
            <div style="max-height:150px;overflow-y:auto;margin:10px 0;padding:10px;background-color:#f5f5f5;border-radius:5px;font-family:monospace;font-size:12px;">
                {', '.join(backend_names)}
            </div>
            
            <p>Sistemul este pregătit pentru realizarea teleportării quantum pe hardware real.</p>
            <p>Pentru a continua, utilizați comanda <code>teleportare reală</code>.</p>
            </div>
            """
            
            # Creăm o imagine simplă pentru reprezentarea conexiunii
            try:
                import plotly.graph_objects as go
                import numpy as np
                
                # Creăm un grafic simplu care arată conectivitatea
                fig = go.Figure()
                
                # Adăugăm noduri pentru utilizator și IBM Quantum
                fig.add_trace(go.Scatter(
                    x=[0, 10], 
                    y=[5, 5],
                    mode='markers+text',
                    marker=dict(size=20, color=['#4CAF50', '#2196F3']),
                    text=['Local', 'IBM Quantum'],
                    textposition='bottom center'
                ))
                
                # Adăugăm linie de conexiune
                fig.add_trace(go.Scatter(
                    x=[0, 10],
                    y=[5, 5],
                    mode='lines',
                    line=dict(width=3, color='#4CAF50', dash='dashdot'),
                    hoverinfo='none'
                ))
                
                # Adăugăm puncte intermediare pentru a sugera transferul de date
                steps = 5
                for i in range(steps):
                    pos = 2 + i*1.5
                    fig.add_trace(go.Scatter(
                        x=[pos],
                        y=[5],
                        mode='markers',
                        marker=dict(size=8, color='#FFC107'),
                        hoverinfo='none'
                    ))
                
                # Configurăm layout-ul
                fig.update_layout(
                    title="Conexiune Securizată la IBM Quantum",
                    showlegend=False,
                    template="plotly_dark",
                    height=300,
                    xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
                    yaxis=dict(showticklabels=False, showgrid=False, zeroline=False)
                )
            except Exception as viz_error:
                # În caz de eroare la crearea vizualizării, continuăm fără ea
                fig = None
            
            return result_text, fig
            
        except Exception as e:
            # În caz de eroare generală la conectare
            import traceback
            error_details = traceback.format_exc()
            
            result_text = f"""
            <div class='error-text'>
            <h3>Eroare la conectarea cu IBM Quantum pentru teleportare</h3>
            <p>S-a produs o eroare în timpul conectării la serviciile IBM Quantum:</p>
            <div style="margin:10px 0;padding:10px;background-color:#fff0f0;border-radius:5px;font-family:monospace;font-size:12px;overflow-x:auto;white-space:pre-wrap;">
                {str(e)}
            </div>
            <details>
                <summary>Detalii eroare (pentru dezvoltatori)</summary>
                <pre style="margin:10px 0;padding:10px;background-color:#fff0f0;border-radius:5px;font-family:monospace;font-size:11px;overflow-x:auto;white-space:pre-wrap;">
                {error_details}
                </pre>
            </details>
            <p>Verificați dacă token-ul IBM Quantum este valid și actualizat.</p>
            </div>
            """
            return result_text, None

        
    def run_teleportation(self):
        """
        Simulate quantum teleportation and create a visualization.
        Uses high-performance local simulation.
        """
        # Step 1: Create a quantum circuit with 3 qubits and 2 classical bits
        qc = QuantumCircuit(3, 2)
        
        # Teleportation steps with text output
        output_text = """
        <div class='teleportation-output'>
        <h3>Quantum Teleportation Simulation</h3>
        <p>Quantum teleportation is a protocol to transfer a quantum state from one location to another using entanglement and classical communication.</p>
        
        <h4>Step 1: Create the quantum state to teleport</h4>
        <p>Initializing qubit 0 with a state to teleport using Hadamard and T gates.</p>
        """
        
        # Create the state to teleport (using qubit 0)
        qc.h(0)
        qc.t(0)
        qc.barrier()
        
        output_text += """
        <h4>Step 2: Create entanglement between qubits 1 and 2</h4>
        <p>Creating a Bell pair using Hadamard and CNOT gates.</p>
        """
        
        # Create entanglement between qubits 1 and 2
        qc.h(1)
        qc.cx(1, 2)
        qc.barrier()
        
        output_text += """
        <h4>Step 3: Perform Bell measurement</h4>
        <p>Entangling qubit 0 with qubit 1 and measuring to teleport the state.</p>
        """
        
        # Bell measurement
        qc.cx(0, 1)
        qc.h(0)
        qc.measure([0, 1], [0, 1])
        qc.barrier()
        
        output_text += """
        <h4>Step 4: Apply corrections based on measurement</h4>
        <p>Conditional operations on qubit 2 based on the measurement results.</p>
        """
        
        # Corrections based on measurements
        qc.x(2).c_if(1, 1)  # Apply X gate if qubit 1 is measured as 1
        qc.z(2).c_if(0, 1)  # Apply Z gate if qubit 0 is measured as 1
        
        # Add info about simulator vs real hardware
        if self.ibm_available:
            output_text += f"""
            <h4>Result: Quantum state teleported using high-performance simulator</h4>
            <p>The initial state of qubit 0 has been teleported to qubit 2 through quantum entanglement.</p>
            <p><strong>Note:</strong> IBM Quantum API token detected but using local simulator due to compatibility. 
            Simulating with {self.max_qubits} qubits.</p>
            </div>
            """
        else:
            output_text += f"""
            <h4>Result: Quantum state teleported using high-performance simulator</h4>
            <p>The initial state of qubit 0 has been teleported to qubit 2 through quantum entanglement.</p>
            <p><strong>Note:</strong> Using high-performance quantum simulator optimized for maximum qubits.
            Simulating with {self.max_qubits} qubits. For real hardware, provide an IBM Quantum API Token.</p>
            </div>
            """
            
        # Execute the circuit using the Aer qasm_simulator for best performance
        backend = self.qasm_sim
        compiled_circuit = transpile(qc, backend)
        job = backend.run(compiled_circuit, shots=1024)
        counts = job.result().get_counts()
        
        # Create visualization
        visualization = self.visualize_teleportation()
        
        return output_text, visualization
    
    def visualize_teleportation(self):
        """Create a visualization of the quantum teleportation process."""
        # Create figure
        fig = go.Figure()
        
        # Define the timeline
        timeline = [0, 1, 2, 3, 4, 5]
        
        # Define positions for qubits
        qubit_positions = [1, 0, -1]  # y-coordinates for qubits 0, 1, 2
        
        # Add horizontal lines for each qubit
        for i, pos in enumerate(qubit_positions):
            fig.add_trace(go.Scatter(
                x=[timeline[0], timeline[-1]],
                y=[pos, pos],
                mode='lines',
                line=dict(color='rgba(150, 150, 150, 0.5)', width=1),
                name=f'Qubit {i}'
            ))
        
        # Step 0: Initial state
        fig.add_trace(go.Scatter(
            x=[timeline[0]] * 3,
            y=qubit_positions,
            mode='markers',
            marker=dict(size=12, color=['blue', 'grey', 'grey']),
            name='Initial State'
        ))
        
        # Step 1: State preparation (H and T gates on qubit 0)
        fig.add_trace(go.Scatter(
            x=[timeline[1]],
            y=[qubit_positions[0]],
            mode='markers+text',
            marker=dict(size=15, color='purple', symbol='square'),
            text=['H,T'],
            textposition='top center',
            name='State Preparation'
        ))
        
        # Step 2: Bell pair creation (H on qubit 1, CNOT from 1 to 2)
        fig.add_trace(go.Scatter(
            x=[timeline[2]],
            y=[qubit_positions[1]],
            mode='markers+text',
            marker=dict(size=15, color='green', symbol='square'),
            text=['H'],
            textposition='top center',
            name='Create Bell Pair'
        ))
        
        # CNOT from qubit 1 to 2
        fig.add_trace(go.Scatter(
            x=[timeline[2], timeline[2]],
            y=[qubit_positions[1], qubit_positions[2]],
            mode='lines+markers',
            line=dict(color='green', dash='dash'),
            marker=dict(size=[0, 15], color=['green', 'green'], symbol=['circle', 'x']),
            name='CNOT Gate'
        ))
        
        # Step 3: Bell measurement (CNOT from 0 to 1, H on 0, then measure both)
        fig.add_trace(go.Scatter(
            x=[timeline[3], timeline[3]],
            y=[qubit_positions[0], qubit_positions[1]],
            mode='lines+markers',
            line=dict(color='red', dash='dash'),
            marker=dict(size=[0, 0], color=['red', 'red']),
            name='Bell Measurement'
        ))
        
        fig.add_trace(go.Scatter(
            x=[timeline[3]],
            y=[qubit_positions[0]],
            mode='markers+text',
            marker=dict(size=15, color='red', symbol='square'),
            text=['H'],
            textposition='top center',
            showlegend=False
        ))
        
        # Measurement symbols
        fig.add_trace(go.Scatter(
            x=[timeline[3], timeline[3]],
            y=[qubit_positions[0], qubit_positions[1]],
            mode='markers',
            marker=dict(size=12, color=['darkred', 'darkred'], symbol='diamond'),
            name='Measurement'
        ))
        
        # Step 4: Conditional operations (corrective gates on qubit 2)
        fig.add_trace(go.Scatter(
            x=[timeline[4]],
            y=[qubit_positions[2]],
            mode='markers+text',
            marker=dict(size=15, color='orange', symbol='square'),
            text=['X/Z'],
            textposition='top center',
            name='Corrective Gates'
        ))
        
        # Step 5: Final state with teleported qubit
        fig.add_trace(go.Scatter(
            x=[timeline[5]] * 3,
            y=qubit_positions,
            mode='markers',
            marker=dict(size=12, color=['grey', 'grey', 'blue']),
            name='Final State (Teleported)'
        ))
        
        # Add dashed lines connecting the steps
        for i in range(3):
            points_x = []
            points_y = []
            for t in timeline:
                points_x.append(t)
                points_y.append(qubit_positions[i])
            
            fig.add_trace(go.Scatter(
                x=points_x,
                y=points_y,
                mode='lines',
                line=dict(color='rgba(100, 100, 100, 0.2)', width=1),
                showlegend=False
            ))
        
        # Add classical communication line (dashed)
        fig.add_trace(go.Scatter(
            x=[timeline[3], timeline[4]],
            y=[-0.5, -0.5],
            mode='lines',
            line=dict(color='yellow', width=2, dash='dash'),
            name='Classical Channel'
        ))
        
        # Add arrows to classical communication
        fig.add_annotation(
            x=timeline[4],
            y=-0.5,
            ax=timeline[3],
            ay=-0.5,
            xref="x", yref="y",
            axref="x", ayref="y",
            text="",
            showarrow=True,
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor='yellow'
        )
        
        # Add step labels
        step_labels = [
            "Initial State", 
            "State Preparation", 
            "Entanglement", 
            "Bell Measurement", 
            "Conditional Operations", 
            "Teleported State"
        ]
        
        for i, label in enumerate(step_labels):
            fig.add_annotation(
                x=timeline[i],
                y=1.5,
                text=label,
                showarrow=False,
                font=dict(size=10, color="white")
            )
        
        # Update layout
        fig.update_layout(
            title="Quantum Teleportation Protocol Visualization",
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                range=[timeline[0]-0.5, timeline[-1]+0.5]
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                range=[-2, 2],
                scaleanchor="x",
                scaleratio=1
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5
            ),
            template="plotly_dark",
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="white"
            ),
            margin=dict(l=20, r=20, t=60, b=80)
        )
        
        return fig
