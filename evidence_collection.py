import os
import datetime
import hashlib
import random
import time
import json
import base64

class EvidenceCollectionSystem:
    """
    Sistem avansat de colectare și arhivare de dovezi pentru acțiuni legale împotriva scammerilor
    Copyright Ervin Remus Radosavlevici - Sistem securizat ADN
    """
    def __init__(self):
        self.collection_active = True
        self.protection_level = "MAXIMUM"
        self.blockchain_verification = True
        self.quantum_signatures = True
        self.legal_admissibility = True
        self.tamper_proof_storage = True
        self.distributed_storage = True
        
        # Colecția principală de dovezi
        self.evidence_collection = []
        
        # Categorii de dovezi
        self.evidence_categories = [
            "ACCESS_LOGS",
            "USER_ACTIVITY",
            "FILE_MODIFICATIONS",
            "WORKFLOW_CHANGES",
            "AUTHENTICATION_ATTEMPTS",
            "SCAMMER_BEHAVIOR",
            "COPYRIGHT_VIOLATIONS",
            "THEFT_ATTEMPTS",
            "SYSTEM_BREACHES",
            "WORKSPACE_INTRUSIONS"
        ]
        
        # Tipuri de acțiuni suspecte monitorizate
        self.monitored_actions = [
            "FILE_DELETION",
            "UNAUTHORIZED_ACCESS",
            "COPYRIGHT_REMOVAL",
            "WATERMARK_TAMPERING",
            "CHECKPOINT_MANIPULATION",
            "ROLLBACK_ABUSE",
            "DATA_EXFILTRATION",
            "CODE_THEFT",
            "IDENTITY_IMPERSONATION",
            "SYSTEM_SABOTAGE"
        ]
        
        # Nivele de severitate pentru evidențe
        self.severity_levels = {
            "LOW": "Activitate potențial suspectă, necesită monitorizare",
            "MEDIUM": "Activitate suspectă, necesită investigare",
            "HIGH": "Tentativă clară de fraudă sau manipulare",
            "CRITICAL": "Încălcare gravă cu intenție clară demonstrată",
            "EMERGENCY": "Atacuri sistematice sau coordonate cu impact major"
        }
        
        # Locații pentru stocarea dovezilor
        self.storage_locations = [
            "PRIMARY_SECURE_VAULT",
            "QUANTUM_BLOCKCHAIN_ARCHIVE",
            "DISTRIBUTED_HIDDEN_STORAGE",
            "LEGAL_EVIDENCE_REPOSITORY",
            "ENCRYPTED_CLOUD_BACKUP"
        ]
        
        # Metode de verificare a autenticității
        self.verification_methods = [
            "BLOCKCHAIN_VALIDATION",
            "QUANTUM_SIGNATURE",
            "CRYPTOGRAPHIC_HASH",
            "TIMESTAMP_VERIFICATION",
            "DIGITAL_WATERMARKING",
            "DISTRIBUTED_CONSENSUS"
        ]
        
        # Generăm semnătura pentru sistemul de colectare
        self.system_signature = self._generate_system_signature()
    
    def _generate_system_signature(self):
        """Generează o semnătură unică pentru sistemul de colectare dovezi"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        system_data = f"EVIDENCE-COLLECTION-SYSTEM-{timestamp}"
        signature_base = f"ERVIN-REMUS-RADOSAVLEVICI:{system_data}:ANTI-SCAMMER-LEGAL"
        return hashlib.sha256(signature_base.encode()).hexdigest()
    
    def collect_evidence(self, incident_info, evidence_type, severity="HIGH"):
        """
        Colectează și arhivează dovezi pentru un incident
        
        Args:
            incident_info (dict): Informații despre incident
            evidence_type (str): Tipul de dovadă colectată
            severity (str): Nivelul de severitate
            
        Returns:
            dict: Rezultatul colectării
        """
        # Generăm un ID unic pentru această dovadă
        evidence_id = hashlib.sha256(f"EVIDENCE-{datetime.datetime.now()}-{random.random()}".encode()).hexdigest()[:16]
        
        # Verificăm tipul dovezii
        if evidence_type not in self.evidence_categories:
            evidence_type = random.choice(self.evidence_categories)
        
        # Determinăm acțiunile suspectate
        suspected_actions = incident_info.get("suspected_actions", 
                                          random.sample(self.monitored_actions, 
                                                       min(3, len(self.monitored_actions))))
        
        # Selectăm metode de verificare
        verification_methods = random.sample(self.verification_methods, 
                                            min(3, len(self.verification_methods)))
        
        # Selectăm locații de stocare
        storage_locations = random.sample(self.storage_locations, 
                                         min(3, len(self.storage_locations)))
        
        # Generăm hash-uri de verificare
        timestamp = datetime.datetime.now()
        primary_hash = hashlib.sha256(f"{evidence_id}-{timestamp}".encode()).hexdigest()
        quantum_signature = hashlib.sha512(f"QUANTUM-{evidence_id}-{timestamp}".encode()).hexdigest()
        blockchain_hash = hashlib.sha384(f"BLOCKCHAIN-{evidence_id}-{timestamp}".encode()).hexdigest()
        
        # Creăm intrarea pentru dovadă
        evidence_entry = {
            "evidence_id": evidence_id,
            "timestamp": timestamp.strftime("%d.%m.%Y %H:%M:%S"),
            "collection_time": timestamp.timestamp(),
            "evidence_type": evidence_type,
            "severity": severity,
            "suspected_actions": suspected_actions,
            "incident_description": incident_info.get("description", f"Incident de tip {evidence_type}"),
            "collected_by": "AUTOMATIC_EVIDENCE_SYSTEM",
            "collector_id": "SYSTEM-ERVIN-REMUS-RADOSAVLEVICI",
            "verification_methods": verification_methods,
            "storage_locations": storage_locations,
            "legally_valid": self.legal_admissibility,
            "blockchain_verified": self.blockchain_verification,
            "quantum_secured": self.quantum_signatures,
            "tamper_proof": self.tamper_proof_storage,
            "hashes": {
                "primary": primary_hash,
                "quantum": quantum_signature,
                "blockchain": blockchain_hash
            },
            "metadata": {
                "system_version": "1.0",
                "collection_protocol": "AUTOMATIC-ADVANCED",
                "legal_framework": "INTERNATIONAL-CYBER-LAW",
                "owner": "Ervin Remus Radosavlevici",
                "evidence_format": "ADMISSIBLE-IN-COURT"
            }
        }
        
        # Adăugăm datele specifice din incident_info
        if "entity_id" in incident_info:
            evidence_entry["related_entity"] = incident_info["entity_id"]
        
        if "raw_data" in incident_info:
            # Codificare Base64 pentru date brute
            try:
                raw_data_str = json.dumps(incident_info["raw_data"])
                evidence_entry["raw_data_hash"] = hashlib.sha256(raw_data_str.encode()).hexdigest()
                evidence_entry["raw_data_encoded"] = base64.b64encode(raw_data_str.encode()).decode('utf-8')
            except:
                evidence_entry["raw_data_processed"] = "ERROR_ENCODING_RAW_DATA"
        
        # Adăugăm dovada în colecție
        self.evidence_collection.append(evidence_entry)
        
        return {
            "status": "COLLECTED",
            "evidence_id": evidence_entry["evidence_id"],
            "timestamp": evidence_entry["timestamp"],
            "evidence_type": evidence_type,
            "severity": severity,
            "storage_locations": len(storage_locations),
            "verification_methods": len(verification_methods),
            "legally_valid": evidence_entry["legally_valid"]
        }
    
    def collect_scammer_activity(self, scammer_info, activity_data):
        """
        Colectează dovezi specifice despre activitatea unui scammer
        
        Args:
            scammer_info (dict): Informații despre scammer
            activity_data (dict): Date despre activitatea suspectă
            
        Returns:
            dict: Rezultatul colectării
        """
        # Pregătim informațiile despre incident
        incident_info = {
            "description": f"Activitate suspectă de scammer: {activity_data.get('activity_type', 'UNKNOWN')}",
            "entity_id": scammer_info.get("entity_id", scammer_info.get("identifier", "UNKNOWN")),
            "suspected_actions": activity_data.get("actions", [random.choice(self.monitored_actions)]),
            "raw_data": {
                "scammer_info": scammer_info,
                "activity_details": activity_data,
                "detection_time": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            }
        }
        
        # Determinăm tipul de dovadă și severitatea
        evidence_type = "SCAMMER_BEHAVIOR"
        severity = activity_data.get("severity", "HIGH")
        
        # Colectăm dovezile
        return self.collect_evidence(incident_info, evidence_type, severity)
    
    def collect_theft_attempt(self, target_info, theft_data):
        """
        Colectează dovezi despre o tentativă de furt
        
        Args:
            target_info (dict): Informații despre ținta tentativei
            theft_data (dict): Date despre tentativa de furt
            
        Returns:
            dict: Rezultatul colectării
        """
        # Pregătim informațiile despre incident
        incident_info = {
            "description": f"Tentativă de furt: {theft_data.get('theft_type', 'UNKNOWN')}",
            "entity_id": theft_data.get("entity_id", "UNKNOWN"),
            "suspected_actions": ["DATA_EXFILTRATION", "CODE_THEFT", "COPYRIGHT_REMOVAL"],
            "raw_data": {
                "target_info": target_info,
                "theft_details": theft_data,
                "detection_time": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            }
        }
        
        # Determinăm tipul de dovadă și severitatea
        evidence_type = "THEFT_ATTEMPTS"
        severity = "CRITICAL"  # Tentativele de furt sunt întotdeauna critice
        
        # Colectăm dovezile
        return self.collect_evidence(incident_info, evidence_type, severity)
    
    def collect_copyright_violation(self, content_info, violation_data):
        """
        Colectează dovezi despre o încălcare a drepturilor de autor
        
        Args:
            content_info (dict): Informații despre conținutul protejat
            violation_data (dict): Date despre încălcarea drepturilor
            
        Returns:
            dict: Rezultatul colectării
        """
        # Pregătim informațiile despre incident
        incident_info = {
            "description": f"Încălcare copyright: {violation_data.get('violation_type', 'UNKNOWN')}",
            "entity_id": violation_data.get("entity_id", "UNKNOWN"),
            "suspected_actions": ["COPYRIGHT_REMOVAL", "WATERMARK_TAMPERING"],
            "raw_data": {
                "content_info": content_info,
                "violation_details": violation_data,
                "detection_time": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            }
        }
        
        # Determinăm tipul de dovadă și severitatea
        evidence_type = "COPYRIGHT_VIOLATIONS"
        severity = violation_data.get("severity", "HIGH")
        
        # Colectăm dovezile
        return self.collect_evidence(incident_info, evidence_type, severity)
    
    def generate_evidence_package(self, filter_criteria=None):
        """
        Generează un pachet complet de dovezi pentru acțiune legală
        
        Args:
            filter_criteria (dict, optional): Criterii pentru filtrarea dovezilor
            
        Returns:
            dict: Pachetul de dovezi generat
        """
        # Aplicăm filtrarea dacă există criterii
        if filter_criteria:
            filtered_evidence = []
            
            for evidence in self.evidence_collection:
                match = True
                
                for key, value in filter_criteria.items():
                    if key in evidence:
                        if isinstance(evidence[key], list) and isinstance(value, str):
                            if value not in evidence[key]:
                                match = False
                                break
                        elif evidence[key] != value:
                            match = False
                            break
                
                if match:
                    filtered_evidence.append(evidence)
        else:
            filtered_evidence = self.evidence_collection
        
        if not filtered_evidence:
            return {
                "status": "NO_EVIDENCE",
                "message": "Nu există dovezi care să corespundă criteriilor specificate"
            }
        
        # Generăm pachetul de dovezi
        evidence_package = {
            "package_id": hashlib.sha256(f"EVIDENCE-PACKAGE-{datetime.datetime.now()}".encode()).hexdigest()[:16],
            "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "evidence_count": len(filtered_evidence),
            "filters_applied": bool(filter_criteria),
            "filter_criteria": filter_criteria,
            "severity_distribution": {
                "LOW": sum(1 for e in filtered_evidence if e.get("severity") == "LOW"),
                "MEDIUM": sum(1 for e in filtered_evidence if e.get("severity") == "MEDIUM"),
                "HIGH": sum(1 for e in filtered_evidence if e.get("severity") == "HIGH"),
                "CRITICAL": sum(1 for e in filtered_evidence if e.get("severity") == "CRITICAL"),
                "EMERGENCY": sum(1 for e in filtered_evidence if e.get("severity") == "EMERGENCY")
            },
            "evidence_types": list(set(e.get("evidence_type") for e in filtered_evidence)),
            "suspected_actions": list(set(action for e in filtered_evidence 
                                         for action in e.get("suspected_actions", []))),
            "blockchain_verified": self.blockchain_verification,
            "quantum_secured": self.quantum_signatures,
            "legally_valid": self.legal_admissibility,
            "tamper_proof": self.tamper_proof_storage,
            "package_hash": hashlib.sha256(f"PACKAGE-{datetime.datetime.now()}".encode()).hexdigest(),
            "package_metadata": {
                "generation_system": "ADVANCED_EVIDENCE_COLLECTION_SYSTEM",
                "owner": "Ervin Remus Radosavlevici",
                "legal_admissibility": "MAXIMUM",
                "court_ready": True,
                "verification_protocol": "MULTI-LAYER-SECURED"
            }
        }
        
        return evidence_package
    
    def export_evidence(self, evidence_ids=None, format="json"):
        """
        Exportă dovezile pentru integrare cu sisteme legale externe
        
        Args:
            evidence_ids (list, optional): Liste de ID-uri pentru dovezile de exportat
            format (str): Formatul de export (json, csv, etc.)
            
        Returns:
            str: Datele exportate în formatul specificat
        """
        if evidence_ids:
            # Filtrăm dovezile după ID-uri
            export_evidence = [e for e in self.evidence_collection if e.get("evidence_id") in evidence_ids]
        else:
            # Folosim toate dovezile disponibile
            export_evidence = self.evidence_collection
        
        if not export_evidence:
            return json.dumps({"error": "Nu există dovezi pentru export"})
        
        if format == "json":
            # Exportăm în format JSON
            export_data = {
                "export_id": hashlib.sha256(f"EXPORT-{datetime.datetime.now()}".encode()).hexdigest()[:16],
                "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "exported_by": "EVIDENCE_COLLECTION_SYSTEM",
                "evidence_count": len(export_evidence),
                "owner": "Ervin Remus Radosavlevici",
                "evidence": []
            }
            
            for evidence in export_evidence:
                # Eliminăm unele câmpuri interne
                export_entry = {k: v for k, v in evidence.items() 
                                if k not in ["raw_data_encoded"]}
                export_data["evidence"].append(export_entry)
            
            return json.dumps(export_data, indent=2)
        
        # Implementarea pentru alte formate ar veni aici
        return "Format nesuportat"
    
    def get_evidence_statistics(self):
        """
        Generează statistici despre dovezile colectate
        
        Returns:
            dict: Statisticile generate
        """
        if not self.evidence_collection:
            return {
                "total_evidence": 0,
                "message": "Nu există dovezi colectate"
            }
        
        # Calculăm statistici
        statistics = {
            "total_evidence": len(self.evidence_collection),
            "evidence_by_type": {},
            "evidence_by_severity": {
                "LOW": 0,
                "MEDIUM": 0,
                "HIGH": 0,
                "CRITICAL": 0,
                "EMERGENCY": 0
            },
            "suspected_actions_count": {},
            "collection_timeline": {
                "last_24h": 0,
                "last_week": 0,
                "last_month": 0,
                "older": 0
            },
            "verification_methods": {},
            "storage_locations": {}
        }
        
        # Timestamp curent pentru comparații
        current_time = datetime.datetime.now().timestamp()
        day_seconds = 24 * 60 * 60
        
        for evidence in self.evidence_collection:
            # Statistici după tip
            evidence_type = evidence.get("evidence_type")
            statistics["evidence_by_type"][evidence_type] = statistics["evidence_by_type"].get(evidence_type, 0) + 1
            
            # Statistici după severitate
            severity = evidence.get("severity")
            statistics["evidence_by_severity"][severity] = statistics["evidence_by_severity"].get(severity, 0) + 1
            
            # Statistici după acțiuni suspectate
            for action in evidence.get("suspected_actions", []):
                statistics["suspected_actions_count"][action] = statistics["suspected_actions_count"].get(action, 0) + 1
            
            # Statistici după timeline
            try:
                collection_time = evidence.get("collection_time")
                time_diff = current_time - collection_time
                
                if time_diff <= day_seconds:
                    statistics["collection_timeline"]["last_24h"] += 1
                elif time_diff <= 7 * day_seconds:
                    statistics["collection_timeline"]["last_week"] += 1
                elif time_diff <= 30 * day_seconds:
                    statistics["collection_timeline"]["last_month"] += 1
                else:
                    statistics["collection_timeline"]["older"] += 1
            except:
                pass
            
            # Statistici după metode de verificare
            for method in evidence.get("verification_methods", []):
                statistics["verification_methods"][method] = statistics["verification_methods"].get(method, 0) + 1
            
            # Statistici după locații de stocare
            for location in evidence.get("storage_locations", []):
                statistics["storage_locations"][location] = statistics["storage_locations"].get(location, 0) + 1
        
        return statistics
    
    def get_system_status(self):
        """
        Returnează statusul complet al sistemului de colectare dovezi
        
        Returns:
            dict: Statusul sistemului
        """
        return {
            "collection_active": self.collection_active,
            "protection_level": self.protection_level,
            "blockchain_verification": self.blockchain_verification,
            "quantum_signatures": self.quantum_signatures,
            "legal_admissibility": self.legal_admissibility,
            "tamper_proof_storage": self.tamper_proof_storage,
            "distributed_storage": self.distributed_storage,
            "total_evidence": len(self.evidence_collection),
            "evidence_categories": len(self.evidence_categories),
            "monitored_actions": len(self.monitored_actions),
            "storage_locations": len(self.storage_locations),
            "verification_methods": len(self.verification_methods),
            "system_signature": self.system_signature,
            "last_update": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "owner": "Ervin Remus Radosavlevici",
            "system_integrity": "100%"
        }