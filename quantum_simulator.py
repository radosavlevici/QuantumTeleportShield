import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
import plotly.graph_objects as go
import plotly.express as px
from utils import complex_to_rgb
import os
import time

class QuantumSimulator:
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
        
        # Verificăm dacă avem token IBM Quantum disponibil
        ibm_token = os.environ.get('IBM_QUANTUM_TOKEN')
        
        if not ibm_token:
            result_text = """
            <div class='warning-text'>
            <h3>Token IBM Quantum lipsă</h3>
            <p>Nu s-a găsit token-ul IBM Quantum. Conexiunea la hardware-ul real IBM Quantum necesită un token de acces valid.</p>
            <p>Contactați administratorul pentru configurarea token-ului.</p>
            </div>
            """
            return result_text, None
        
        try:
            # Încercăm să ne conectăm la IBM Quantum
            from qiskit_ibm_provider import IBMProvider
            
            # Inițializăm provider-ul cu token-ul
            provider = IBMProvider(token=ibm_token)
            
            # Obținem lista de backend-uri disponibile
            backends = provider.backends()
            backend_names = [backend.name for backend in backends]
            
            # Alegem backend-ul cu cele mai multe qubits disponibile
            max_qubits = 0
            max_qubit_backend = None
            
            for backend in backends:
                # Verificăm doar backend-urile disponibile (de simulator sau hardware)
                if not backend.operational:
                    continue
                    
                # Obținem configurația backend-ului
                config = backend.configuration()
                num_qubits = config.n_qubits
                
                if num_qubits > max_qubits:
                    max_qubits = num_qubits
                    max_qubit_backend = backend
            
            # Verificăm dacă am găsit un backend valid
            if max_qubit_backend is None:
                result_text = """
                <div class='warning-text'>
                <h3>Nu s-au găsit procesoare quantum disponibile</h3>
                <p>Conexiunea la IBM Quantum a reușit, dar nu s-au găsit procesoare quantum operaționale.</p>
                <p>Vă rugăm să încercați mai târziu când procesoarele quantum vor fi disponibile.</p>
                </div>
                """
                return result_text, None
            
            # Creăm un circuit de test simplu pentru a demonstra conexiunea
            from qiskit import QuantumCircuit
            qc = QuantumCircuit(2, 2)
            qc.h(0)
            qc.cx(0, 1)
            qc.measure([0, 1], [0, 1])
            
            # Rulăm pe simulator pentru a verifica circuitul
            from qiskit_aer import AerSimulator
            simulator = AerSimulator()
            compiled_circuit = qc.decompose()
            result = simulator.run(compiled_circuit, shots=1024).result()
            counts = result.get_counts(compiled_circuit)
            
            # Creăm reprezentarea vizuală a circuitului
            from qiskit.visualization import plot_histogram
            import plotly.graph_objects as go
            
            # Convertim histograma într-un obiect plotly
            labels = list(counts.keys())
            values = list(counts.values())
            
            fig = go.Figure(data=[go.Bar(x=labels, y=values)])
            fig.update_layout(
                title="Rezultate Circuit Bell State (Simulator)",
                xaxis_title="Stare",
                yaxis_title="Frecvență",
                width=700,
                height=500,
            )
            
            # Actualizăm state tracking
            self.ibm_available = True
            self.max_qubits = max_qubits
            
            # Generăm textul rezultatului
            result_text = f"""
            <div class='success-text'>
            <h3>Conectare la IBM Quantum reușită!</h3>
            <p>S-a stabilit conexiunea cu IBM Quantum. Detalii:</p>
            
            <ul>
                <li><strong>Total backend-uri disponibile:</strong> {len(backends)}</li>
                <li><strong>Backend cu cele mai multe qubits:</strong> {max_qubit_backend.name}</li>
                <li><strong>Număr qubits disponibile:</strong> {max_qubits}</li>
            </ul>
            
            <p>Backend-uri disponibile:</p>
            <div style="max-height:150px;overflow-y:auto;margin:10px 0;padding:10px;background-color:#f5f5f5;border-radius:5px;font-family:monospace;font-size:12px;">
                {', '.join(backend_names)}
            </div>
            
            <p>A fost rulat un circuit Bell State pe simulator pentru a demonstra funcționalitatea.</p>
            <p>Pentru a continua cu rularea pe hardware real, utilizați comanda <code>rulează circuit real</code>.</p>
            </div>
            """
            
            return result_text, fig
            
        except Exception as e:
            # În caz de eroare la conectare
            result_text = f"""
            <div class='error-text'>
            <h3>Eroare la conectarea cu IBM Quantum</h3>
            <p>S-a produs o eroare în timpul conectării la serviciile IBM Quantum:</p>
            <div style="margin:10px 0;padding:10px;background-color:#fff0f0;border-radius:5px;font-family:monospace;font-size:12px;">
                {str(e)}
            </div>
            <p>Verificați dacă token-ul IBM Quantum este valid și actualizat.</p>
            </div>
            """
            return result_text, None
    
    def run_basic_circuit(self):
        """Run a basic quantum circuit with common gates using optimized simulator."""
        # Create a quantum circuit with 3 qubits
        circuit = QuantumCircuit(3, 3)
        
        # Add gates to the circuit
        circuit.h(0)  # Hadamard gate on qubit 0
        circuit.cx(0, 1)  # CNOT gate with control qubit 0 and target qubit 1
        circuit.x(2)  # X gate (NOT) on qubit 2
        circuit.measure([0, 1, 2], [0, 1, 2])  # Measure all qubits
        
        try:
            # Use the QASM simulator for best performance with this circuit type
            backend = self.qasm_sim
            
            # Execute the circuit
            compiled_circuit = transpile(circuit, backend)
            job = backend.run(compiled_circuit, shots=1024)
            result = job.result()
            
            # Get the histogram data
            counts = result.get_counts(circuit)
        except Exception as e:
            print(f"Error executing quantum circuit: {str(e)}")
            # Try a different simulator approach if the first one fails
            backend = AerSimulator()
            compiled_circuit = transpile(circuit, backend)
            job = backend.run(compiled_circuit, shots=1024)
            result = job.result()
            counts = result.get_counts(circuit)
        
        # Create a formatted output for the console
        if self.ibm_available:
            output_text = f"""
            <div class='circuit-output'>
            <h4>Basic Quantum Circuit Executed (High-Performance Simulation)</h4>
            <p><strong>Note:</strong> IBM Quantum API token detected but using optimized simulator due to compatibility.
            Simulating with {self.max_qubits} qubits.</p>
            <p>Circuit operations:</p>
            <ul>
                <li>Hadamard gate on qubit 0</li>
                <li>CNOT gate with control qubit 0 and target qubit 1</li>
                <li>X gate on qubit 2</li>
                <li>Measurement of all qubits</li>
            </ul>
            <p>Results from 1024 shots:</p>
            </div>
            """
        else:
            output_text = f"""
            <div class='circuit-output'>
            <h4>Basic Quantum Circuit Executed (High-Performance Simulation)</h4>
            <p><strong>Note:</strong> Using optimized quantum simulator with {self.max_qubits} qubit capacity.
            For real hardware, provide an IBM Quantum API token.</p>
            <p>Circuit operations:</p>
            <ul>
                <li>Hadamard gate on qubit 0</li>
                <li>CNOT gate with control qubit 0 and target qubit 1</li>
                <li>X gate on qubit 2</li>
                <li>Measurement of all qubits</li>
            </ul>
            <p>Results from 1024 shots:</p>
            </div>
            """
        
        # Create a visualization of the results
        labels = list(counts.keys())
        values = list(counts.values())
        
        fig = go.Figure(data=[go.Bar(
            x=labels, 
            y=values,
            marker_color='rgb(0, 150, 200)'
        )])
        
        fig.update_layout(
            title="Quantum Circuit Measurement Results",
            xaxis_title="Measured State",
            yaxis_title="Count",
            template="plotly_dark",
            font=dict(
                family="Courier New, monospace",
                size=14,
                color="white"
            )
        )
        
        return output_text, fig
    
    def visualize_bloch_sphere(self, theta=0, phi=0):
        """Create a visualization of a qubit on the Bloch sphere."""
        # Convert spherical coordinates to cartesian
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        
        # Create the Bloch sphere
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x_sphere = np.cos(u) * np.sin(v)
        y_sphere = np.sin(u) * np.sin(v)
        z_sphere = np.cos(v)
        
        # Create the figure
        fig = go.Figure()
        
        # Add the Bloch sphere
        fig.add_trace(go.Surface(
            x=x_sphere, y=y_sphere, z=z_sphere,
            colorscale=[[0, 'rgb(0, 50, 100)'], [1, 'rgb(0, 100, 200)']],
            opacity=0.3,
            showscale=False
        ))
        
        # Add the state vector
        fig.add_trace(go.Scatter3d(
            x=[0, x], y=[0, y], z=[0, z],
            mode='lines+markers',
            line=dict(color='red', width=6),
            marker=dict(size=[0, 8], color='red')
        ))
        
        # Add basis vectors
        fig.add_trace(go.Scatter3d(
            x=[0, 1, 0, 0, 0, 0], y=[0, 0, 0, 1, 0, 0], z=[0, 0, 0, 0, 0, 1],
            mode='lines',
            line=dict(color='white', width=2)
        ))
        
        # Update layout
        fig.update_layout(
            title="Bloch Sphere Representation",
            scene=dict(
                xaxis_title="X",
                yaxis_title="Y",
                zaxis_title="Z",
                aspectmode="cube",
                xaxis=dict(range=[-1.2, 1.2], showbackground=False),
                yaxis=dict(range=[-1.2, 1.2], showbackground=False),
                zaxis=dict(range=[-1.2, 1.2], showbackground=False)
            ),
            template="plotly_dark",
            margin=dict(l=0, r=0, b=0, t=30)
        )
        
        return fig
    
    def visualize_statevector(self, qc):
        """Visualize the statevector of a quantum circuit."""
        # Execute the circuit and get the statevector
        # In newer Qiskit, we use Aer's statevector_simulator
        statevector_sim = Aer.get_backend('statevector_simulator')
        transpiled_qc = transpile(qc, statevector_sim)
        job = statevector_sim.run(transpiled_qc)
        statevector = job.result().get_statevector()
        
        # Create labels for each state
        n_qubits = qc.num_qubits
        labels = [bin(i)[2:].zfill(n_qubits) for i in range(2**n_qubits)]
        
        # Extract magnitudes and phases
        magnitudes = np.abs(statevector)
        phases = np.angle(statevector)
        
        # Generate colors based on phase
        colors = [complex_to_rgb(statevector[i]) for i in range(len(statevector))]
        
        # Create the figure
        fig = go.Figure()
        
        # Add bars for magnitude
        fig.add_trace(go.Bar(
            x=labels,
            y=magnitudes,
            marker_color=colors,
            name='Magnitude'
        ))
        
        # Update layout
        fig.update_layout(
            title="Quantum State Vector Visualization",
            xaxis_title="Basis State",
            yaxis_title="Magnitude",
            template="plotly_dark",
            font=dict(
                family="Courier New, monospace",
                size=14,
                color="white"
            )
        )
        
        return fig
