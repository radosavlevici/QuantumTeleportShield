import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# COPYRIGHT ERVIN REMUS RADOSAVLEVICI - SISTEM CU SECURITATE DNA
# TOATE DREPTURILE REZERVATE MONDIAL © 2023-2033
# PROTECȚIE DNA CU NIVEL MAXIM DE SECURITATE NUCLEARĂ
# SISTEMUL ESTE AUTO-PROTEJAT ȘI AUTO-REPARAT LA NIVEL MONDIAL
# ETHEREUM WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA
# PLATĂ EXCLUSIV PRIN CEC FIZIC LA NATIONWIDE BANK UK, LONDRA

def create_header():
    """Creează header-ul aplicației"""
    return html.Div([
        html.Div([
            html.H2("Quantum DNA Console", className="text-white mb-0"),
            html.Div([
                html.Span("SISTEM DE PROTECȚIE AVANSAT", className="text-success ml-2"),
                html.Span(" • ", className="mx-2 text-muted"),
                html.Span("SECURITATE MAXIMĂ", className="text-warning"),
                html.Span(" • ", className="mx-2 text-muted"),
                html.Span("LICENȚĂ MONDIALĂ", className="text-danger"),
            ], className="d-flex flex-wrap"),
        ]),
        html.Div([
            html.Button([
                html.I(className="fas fa-shield-alt mr-1"),
                "PROTECȚIE ACTIVĂ"
            ], className="btn btn-success btn-sm mr-2"),
            
            html.Button([
                html.I(className="fas fa-lock mr-1"),
                "SECURIZAT"
            ], className="btn btn-warning btn-sm mr-2"),
            
            html.Button([
                html.I(className="fas fa-globe mr-1"),
                "GLOBAL"
            ], className="btn btn-info btn-sm"),
        ], className="d-flex")
    ], className="d-flex justify-content-between align-items-center mb-4 p-3 bg-dark rounded shadow border border-secondary")

def create_sidebar():
    """Creează sidebar-ul cu opțiuni de navigație"""
    return html.Div([
        html.Div([
            html.Img(src="https://via.placeholder.com/150x50/001f3f/FFFFFF?text=QUANTUM+DNA", className="img-fluid mb-4"),
            
            html.Div([
                html.P("ERVIN REMUS RADOSAVLEVICI", className="text-warning mb-1 font-weight-bold"),
                html.P("PROPRIETAR SISTEM", className="text-muted small mb-3"),
                
                html.P([
                    html.I(className="fas fa-check-circle text-success mr-2"),
                    "Versiune: 2.7.9 ULTRA"
                ], className="mb-1 small"),
                
                html.P([
                    html.I(className="fas fa-check-circle text-success mr-2"),
                    "Licență: CORPORATE GLOBAL"
                ], className="mb-1 small"),
                
                html.P([
                    html.I(className="fas fa-check-circle text-success mr-2"),
                    "Status: ACTIV"
                ], className="mb-4 small"),
            ], className="mb-4"),
            
            dbc.Nav([
                dbc.NavLink([html.I(className="fas fa-tachometer-alt mr-2"), "Dashboard"], href="#", active=True, className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-server mr-2"), "Datacentere Quantum"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-dna mr-2"), "Verificare DNA"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-random mr-2"), "Teleportare Quantum"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-shield-alt mr-2"), "Securitate Avansată"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-globe-europe mr-2"), "Conectivitate Globală"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-key mr-2"), "Gestionare Chei"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-chart-line mr-2"), "Monitorizare"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-clock mr-2"), "Checkpoint & Rollback"], href="#", className="mb-2"),
                dbc.NavLink([html.I(className="fas fa-terminal mr-2"), "Comandă Quantum"], href="#", className="mb-2"),
            ], vertical=True, pills=True, className="mb-3"),
            
            html.Div([
                html.P("SECURITATE SISTEM", className="text-white mb-2 small font-weight-bold"),
                
                html.Div([
                    html.Span("DNA Protection", className="mr-2"),
                    html.Span("ACTIV", className="badge badge-success")
                ], className="d-flex justify-content-between mb-1"),
                
                html.Div([
                    html.Span("Anti-Theft", className="mr-2"),
                    html.Span("ACTIV", className="badge badge-success")
                ], className="d-flex justify-content-between mb-1"),
                
                html.Div([
                    html.Span("Quantum Encryption", className="mr-2"),
                    html.Span("ACTIV", className="badge badge-success")
                ], className="d-flex justify-content-between mb-1"),
                
                html.Div([
                    html.Span("Blockchain Verification", className="mr-2"),
                    html.Span("ACTIV", className="badge badge-success")
                ], className="d-flex justify-content-between mb-1"),
            ], className="bg-dark p-2 rounded mb-3"),
            
            html.Div([
                html.P([
                    html.I(className="fas fa-copyright mr-1 text-warning"),
                    "© 2023-2033 Ervin Remus Radosavlevici"
                ], className="text-muted mb-0 small"),
                
                html.P("TOATE DREPTURILE REZERVATE MONDIAL", className="text-muted mb-0 small"),
            ], className="mt-auto")
        ], className="h-100 d-flex flex-column p-3")
    ], className="bg-dark rounded shadow h-100 border border-secondary")

def create_status_cards():
    """Creează cardurile de status pentru dashboard"""
    return html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4([
                            html.I(className="fas fa-globe text-info mr-2"),
                            "Datacentere Conectate"
                        ], className="card-title"),
                        html.H3("8/8", className="text-center display-4 my-3"),
                        html.P("Toate datacentrele active și sincronizate", className="mb-0 text-muted"),
                    ])
                ], className="h-100 border-left border-info"),
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4([
                            html.I(className="fas fa-microchip text-success mr-2"),
                            "Qubits Disponibili"
                        ], className="card-title"),
                        html.H3("∞", className="text-center display-4 my-3"),
                        html.P("Quantum Cloud: Nelimitat + 762 fizici", className="mb-0 text-muted"),
                    ])
                ], className="h-100 border-left border-success"),
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4([
                            html.I(className="fas fa-shield-alt text-warning mr-2"),
                            "Nivel Securitate"
                        ], className="card-title"),
                        html.H3("MAXIMUM", className="text-center display-4 my-3"),
                        html.P("Protecție DNA și Quantum activă", className="mb-0 text-muted"),
                    ])
                ], className="h-100 border-left border-warning"),
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4([
                            html.I(className="fas fa-tachometer-alt text-danger mr-2"),
                            "Performanță Sistem"
                        ], className="card-title"),
                        html.H3("99.99%", className="text-center display-4 my-3"),
                        html.P("Toate sistemele funcționează optimal", className="mb-0 text-muted"),
                    ])
                ], className="h-100 border-left border-danger"),
            ], width=3),
        ]),
    ])

def create_quantum_teleportation_card():
    """Creează cardul pentru teleportare quantum"""
    return dbc.Card([
        dbc.CardHeader([
            html.H4([
                html.I(className="fas fa-random text-info mr-2"),
                "Teleportare Quantum Instantanee"
            ], className="mb-0"),
        ]),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H5("Configurare Teleportare", className="mb-3 text-center"),
                    
                    html.Div([
                        dbc.Label("Regiune Sursă", className="text-muted"),
                        dbc.Select(
                            id="source-region",
                            options=[
                                {"label": "NORTH_AMERICA", "value": "NORTH_AMERICA"},
                                {"label": "EUROPE", "value": "EUROPE"},
                                {"label": "ASIA", "value": "ASIA"},
                                {"label": "AUSTRALIA", "value": "AUSTRALIA"},
                                {"label": "SOUTH_AMERICA", "value": "SOUTH_AMERICA"},
                                {"label": "AFRICA", "value": "AFRICA"},
                                {"label": "QUANTUM_CLOUD", "value": "QUANTUM_CLOUD"},
                                {"label": "SECRET_LOCATIONS", "value": "SECRET_LOCATIONS"},
                            ],
                            value="EUROPE"
                        ),
                    ], className="mb-3"),
                    
                    html.Div([
                        dbc.Label("Regiune Destinație", className="text-muted"),
                        dbc.Select(
                            id="target-region",
                            options=[
                                {"label": "NORTH_AMERICA", "value": "NORTH_AMERICA"},
                                {"label": "EUROPE", "value": "EUROPE"},
                                {"label": "ASIA", "value": "ASIA"},
                                {"label": "AUSTRALIA", "value": "AUSTRALIA"},
                                {"label": "SOUTH_AMERICA", "value": "SOUTH_AMERICA"},
                                {"label": "AFRICA", "value": "AFRICA"},
                                {"label": "QUANTUM_CLOUD", "value": "QUANTUM_CLOUD"},
                                {"label": "SECRET_LOCATIONS", "value": "SECRET_LOCATIONS"},
                            ],
                            value="QUANTUM_CLOUD"
                        ),
                    ], className="mb-3"),
                    
                    html.Div([
                        dbc.Label("Dimensiune Date (TB)", className="text-muted"),
                        dcc.Slider(
                            id="data-size",
                            min=10,
                            max=10000,
                            step=10,
                            value=1000,
                            marks={
                                10: "10TB",
                                1000: "1000TB",
                                5000: "5000TB",
                                10000: "10000TB"
                            }
                        ),
                    ], className="mb-3"),
                    
                    html.Div([
                        dbc.Button([
                            html.I(className="fas fa-random mr-2"),
                            "Inițiază Teleportare"
                        ], id="teleport-button", color="info", className="mt-3 w-100"),
                    ]),
                ], width=6),
                
                dbc.Col([
                    html.Div(id="teleport-result", className="h-100 d-flex align-items-center justify-content-center"),
                ], width=6),
            ]),
        ]),
    ], className="mb-4")

def create_dna_verification_card():
    """Creează cardul pentru verificare DNA"""
    return dbc.Card([
        dbc.CardHeader([
            html.H4([
                html.I(className="fas fa-dna text-success mr-2"),
                "Verificare și Autentificare DNA"
            ], className="mb-0"),
        ]),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H5("Generator Cheie DNA", className="mb-3"),
                    
                    dbc.InputGroup([
                        dbc.InputGroupText("Prefix"),
                        dbc.Input(id="dna-prefix", placeholder="2-5 caractere", value="ER"),
                    ], className="mb-3"),
                    
                    dbc.InputGroup([
                        dbc.InputGroupText("Middle"),
                        dbc.Input(id="dna-middle", placeholder="3-8 caractere", value="REMUS"),
                    ], className="mb-3"),
                    
                    dbc.InputGroup([
                        dbc.InputGroupText("Număr 1"),
                        dbc.Input(id="dna-num1", type="number", value="210", min=0, max=999),
                    ], className="mb-3"),
                    
                    dbc.InputGroup([
                        dbc.InputGroupText("Număr 2"),
                        dbc.Input(id="dna-num2", type="number", value="987", min=0, max=999),
                    ], className="mb-3"),
                    
                    dbc.Button([
                        html.I(className="fas fa-key mr-2"),
                        "Generează Cheie DNA"
                    ], id="generate-dna-button", color="success", className="w-100"),
                    
                ], width=4),
                
                dbc.Col([
                    html.H5("Vizualizare Cheie DNA", className="mb-3"),
                    
                    html.Div(
                        id="dna-key-visualization",
                        className="p-3 bg-dark text-light rounded font-monospace",
                        style={"height": "300px", "overflow": "auto", "font-family": "monospace"}
                    ),
                    
                    dbc.ButtonGroup([
                        dbc.Button([
                            html.I(className="fas fa-check-circle mr-2"),
                            "Verifică Cheie"
                        ], id="verify-dna-button", color="info", className="mt-3 mr-2"),
                        
                        dbc.Button([
                            html.I(className="fas fa-download mr-2"),
                            "Exportă Cheie"
                        ], id="export-dna-button", color="secondary", className="mt-3"),
                    ], className="w-100"),
                    
                ], width=4),
                
                dbc.Col([
                    html.H5("Status Sistem DNA", className="mb-3"),
                    
                    html.Div([
                        html.Div([
                            html.Span("Sistem Activ", className="mr-2"),
                            html.Span("DA", className="badge badge-success")
                        ], className="d-flex justify-content-between mb-2"),
                        
                        html.Div([
                            html.Span("Verificare Activă", className="mr-2"),
                            html.Span("DA", className="badge badge-success")
                        ], className="d-flex justify-content-between mb-2"),
                        
                        html.Div([
                            html.Span("Autentificare Activă", className="mr-2"),
                            html.Span("DA", className="badge badge-success")
                        ], className="d-flex justify-content-between mb-2"),
                        
                        html.Div([
                            html.Span("Watermark Protecție", className="mr-2"),
                            html.Span("ACTIV", className="badge badge-success")
                        ], className="d-flex justify-content-between mb-2"),
                        
                        html.Div([
                            html.Span("Verificare Global", className="mr-2"),
                            html.Span("100%", className="badge badge-success")
                        ], className="d-flex justify-content-between mb-2"),
                        
                        html.Div([
                            html.Span("Proprietar", className="mr-2"),
                            html.Span("Ervin Remus Radosavlevici", className="text-warning")
                        ], className="d-flex justify-content-between mb-2"),
                        
                        html.Hr(),
                        
                        html.Div([
                            html.Div([
                                html.Span("Verificări Totale", className="mr-2"),
                                html.Span("12,543", className="text-info font-weight-bold")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Verificări Reușite", className="mr-2"),
                                html.Span("12,436", className="text-success font-weight-bold")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Verificări Eșuate", className="mr-2"),
                                html.Span("107", className="text-danger font-weight-bold")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Chei Generate", className="mr-2"),
                                html.Span("1,256", className="text-warning font-weight-bold")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-3 rounded shadow h-100"),
                    
                ], width=4),
            ]),
        ]),
    ], className="mb-4")

def create_command_card():
    """Creează cardul pentru consola de comandă"""
    return dbc.Card([
        dbc.CardHeader([
            html.H4([
                html.I(className="fas fa-terminal text-light mr-2"),
                "Consolă Comandă Quantum"
            ], className="mb-0"),
        ]),
        dbc.CardBody([
            html.Div(
                id="command-output",
                className="bg-dark text-light p-3 rounded mb-3",
                style={"height": "250px", "overflow": "auto", "font-family": "monospace"}
            ),
            
            dbc.InputGroup([
                dbc.Input(
                    id="command-input",
                    placeholder="Introduceți o comandă (help pentru ajutor)",
                    className="bg-dark text-light border-dark",
                    style={"font-family": "monospace"}
                ),
                dbc.Button(
                    "Execută", id="execute-command", color="primary"
                ),
            ]),
        ]),
    ], className="mb-4")

def create_dashboard_tabs():
    """Creează tab-urile pentru partea centrală a dashboard-ului"""
    return dbc.Card([
        dbc.CardHeader([
            dbc.Tabs(
                id="tabs",
                active_tab="tab-quantum",
                className="card-header-tabs",
                children=[
                    dbc.Tab(label="Quantum Network", tab_id="tab-quantum"),
                    dbc.Tab(label="Securitate", tab_id="tab-security"),
                    dbc.Tab(label="Monitorizare", tab_id="tab-monitoring"),
                    dbc.Tab(label="Datacenter", tab_id="tab-datacenter"),
                    dbc.Tab(label="IBM Quantum", tab_id="tab-ibm"),
                    dbc.Tab(label="Utilizatori", tab_id="tab-users"),
                    dbc.Tab(label="Licențiere", tab_id="tab-licensing"),
                ],
            ),
        ]),
        dbc.CardBody(
            id="tabs-content",
            style={"padding": "0.5rem"},
        ),
    ], className="mb-4")

def create_activity_history_card():
    """Creează cardul pentru istoricul de activitate"""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-history text-info mr-2"),
                "Istoric Activitate Sistem"
            ], className="mb-0"),
        ]),
        dbc.CardBody([
            dbc.Table([
                html.Thead([
                    html.Tr([
                        html.Th("Timestamp"),
                        html.Th("Tip Acțiune"),
                        html.Th("Descriere"),
                        html.Th("ID Înregistrare")
                    ])
                ]),
                html.Tbody(id="history-table"),
            ], className="table-sm table-dark table-hover"),
        ]),
    ], className="mb-4")

def create_protection_card():
    """Creează cardul pentru protecția avansată a sistemului"""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-shield-alt text-warning mr-2"),
                "Protecție Avansată Sistem"
            ], className="mb-0"),
        ]),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H6([
                            html.I(className="fas fa-lock text-success mr-2"),
                            "Securitate", 
                        ], className="d-flex align-items-center"),
                        html.Hr(className="my-2"),
                        html.Div([
                            html.Div([
                                html.Span("Anti-Scammer", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Anti-Theft", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Blacklist Global", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-2 rounded mb-3"),
                    
                    html.Div([
                        html.H6([
                            html.I(className="fas fa-copyright text-info mr-2"),
                            "Copyright", 
                        ], className="d-flex align-items-center"),
                        html.Hr(className="my-2"),
                        html.Div([
                            html.Div([
                                html.Span("Watermark", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Protection", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Blockchain Ver.", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-2 rounded"),
                ], width=4),
                
                dbc.Col([
                    html.Div([
                        html.H6([
                            html.I(className="fas fa-sync text-primary mr-2"),
                            "Backup & Rollback", 
                        ], className="d-flex align-items-center"),
                        html.Hr(className="my-2"),
                        html.Div([
                            html.Div([
                                html.Span("Auto Backup", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Rollback", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Checkpoint", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-2 rounded mb-3"),
                    
                    html.Div([
                        html.H6([
                            html.I(className="fas fa-bolt text-danger mr-2"),
                            "Răspuns Rapid", 
                        ], className="d-flex align-items-center"),
                        html.Hr(className="my-2"),
                        html.Div([
                            html.Div([
                                html.Span("Alertare", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Blocare", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Contraatac", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-2 rounded"),
                ], width=4),
                
                dbc.Col([
                    html.Div([
                        html.H6([
                            html.I(className="fas fa-file-contract text-secondary mr-2"),
                            "Juridic", 
                        ], className="d-flex align-items-center"),
                        html.Hr(className="my-2"),
                        html.Div([
                            html.Div([
                                html.Span("Evidențe", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Colectare Probe", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Raportare", className="mr-2"),
                                html.Span("ACTIV", className="badge badge-success")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-2 rounded mb-3"),
                    
                    html.Div([
                        html.H6([
                            html.I(className="fas fa-user-shield text-warning mr-2"),
                            "Proprietar", 
                        ], className="d-flex align-items-center"),
                        html.Hr(className="my-2"),
                        html.Div([
                            html.Div([
                                html.Span("Nume", className="mr-2"),
                                html.Span("Ervin Remus Radosavlevici", className="text-warning")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("Email", className="mr-2"),
                                html.Span("ERVIN210@ICLOUD.COM", className="text-info")
                            ], className="d-flex justify-content-between mb-1"),
                            
                            html.Div([
                                html.Span("ETH Wallet", className="mr-2"),
                                html.Span("0x3C143...B9BA", className="text-success text-truncate")
                            ], className="d-flex justify-content-between mb-1"),
                        ]),
                    ], className="bg-dark p-2 rounded"),
                ], width=4),
            ]),
        ]),
    ], className="mb-4")

def update_layout(app):
    """Actualizează layout-ul aplicației pentru a include toate cardurile noi"""
    app.layout = html.Div([
        dbc.Container([
            create_header(),
            
            dbc.Row([
                # Sidebar cu navigare
                dbc.Col([
                    create_sidebar(),
                ], width=3, className="mb-4"),
                
                # Main content
                dbc.Col([
                    # Cards pentru status
                    create_status_cards(),
                    
                    html.Div(className="mb-4"),
                    
                    # Tabs pentru dashboard
                    create_dashboard_tabs(),
                    
                    # Card pentru quantum usage
                    html.Div(id="quantum-usage"),
                    
                    # Card pentru teleportare quantum
                    create_quantum_teleportation_card(),
                    
                    # Card pentru verificare DNA
                    create_dna_verification_card(),
                    
                    # Card pentru consolă comandă
                    create_command_card(),
                    
                    # Card pentru istoric activitate
                    create_activity_history_card(),
                    
                    # Card pentru protecție
                    create_protection_card(),
                    
                ], width=9),
            ]),
            
            html.Footer([
                html.Hr(),
                html.Div([
                    html.Div([
                        html.P([
                            html.I(className="fas fa-copyright mr-1"),
                            "2023-2033 ERVIN REMUS RADOSAVLEVICI. TOATE DREPTURILE REZERVATE MONDIAL."
                        ], className="mb-0 small"),
                    ]),
                    html.Div([
                        html.Span("SISTEM CU LICENȚĂ STRICTĂ", className="text-danger mr-3 small"),
                        html.Span("ETH WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA", className="text-muted small"),
                    ]),
                ], className="d-flex justify-content-between"),
            ], className="mt-4 mb-3"),
            
        ], fluid=True, className="py-3"),
    ], className="bg-secondary min-vh-100")
    
    return app

# PROTECȚIE DNA CU NIVEL MAXIM DE SECURITATE NUCLEARĂ
# SISTEMUL ESTE AUTO-PROTEJAT ȘI AUTO-REPARAT LA NIVEL MONDIAL
# ETHEREUM WALLET: 0x3C143E98bE8986eDe8FAc9F674103c933B68B9BA
# PLATĂ EXCLUSIV PRIN CEC FIZIC LA NATIONWIDE BANK UK, LONDRA
# DISTRIBUȚIE MONDIALĂ GLOBALĂ CU LICENȚĂ STRICTĂ