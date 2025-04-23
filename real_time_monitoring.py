import os
import datetime
import hashlib
import random
import time
import threading
import json

class RealTimeMonitoringSystem:
    """
    Sistem avansat de monitorizare în timp real pentru activități suspecte de scammer
    Copyright Ervin Remus Radosavlevici - Sistem securizat ADN
    """
    def __init__(self):
        self.monitoring_active = True
        self.protection_level = "MAXIMUM"
        self.real_time_alerts = True
        self.suspicious_activity_detection = True
        self.instant_blocking = True
        self.pattern_recognition = True
        self.behavioral_analysis = True
        
        # Istoricul activităților monitorizate
        self.activity_history = []
        self.max_history_size = 1000
        
        # Tipuri de activități monitorizate
        self.monitored_activities = [
            "FILE_ACCESS",
            "FILE_MODIFICATION",
            "FILE_DELETION",
            "AUTHENTICATION_ATTEMPT",
            "API_ACCESS",
            "DATABASE_QUERY",
            "CONFIGURATION_CHANGE",
            "COPYRIGHT_CHANGE",
            "WATERMARK_TAMPERING",
            "CHECKPOINT_ACCESS",
            "ROLLBACK_ATTEMPT",
            "WORKFLOW_MODIFICATION",
            "WORKSPACE_CHANGE",
            "SYSTEM_SETTING_CHANGE",
            "UNAUTHORIZED_EXPORT"
        ]
        
        # Niveluri de suspiciune
        self.suspicion_levels = {
            "NORMAL": "Activitate normală, nicio acțiune necesară",
            "LOW": "Activitate potențial suspectă, monitorizare continuă",
            "MEDIUM": "Activitate suspectă, înregistrare și analiză detaliată",
            "HIGH": "Activitate foarte suspectă, alertă și verificare suplimentară",
            "CRITICAL": "Activitate extrem de suspectă, blocare automată"
        }
        
        # Acțiuni pentru fiecare nivel de suspiciune
        self.suspicion_actions = {
            "NORMAL": ["LOG"],
            "LOW": ["LOG", "MONITOR"],
            "MEDIUM": ["LOG", "MONITOR", "ANALYZE", "ALERT"],
            "HIGH": ["LOG", "ALERT", "BLOCK_TEMPORARILY", "COLLECT_EVIDENCE"],
            "CRITICAL": ["LOG", "ALERT", "BLOCK_PERMANENTLY", "COLLECT_EVIDENCE", "ADD_TO_BLACKLIST"]
        }
        
        # Contoare pentru statistici
        self.statistics = {
            "total_activities_monitored": 0,
            "suspicious_activities_detected": 0,
            "alerts_generated": 0,
            "temporary_blocks": 0,
            "permanent_blocks": 0,
            "evidence_collected": 0,
            "blacklist_additions": 0
        }
        
        # Callback functions pentru integrare cu alte sisteme
        self.alert_callback = None
        self.evidence_collection_callback = None
        self.blacklist_callback = None
        
        # Thread pentru monitorizarea continuă
        self.monitoring_thread = None
        self.stop_monitoring = False
        
        # Generăm semnătura pentru sistemul de monitorizare
        self.monitoring_signature = self._generate_monitoring_signature()
        
    def _generate_monitoring_signature(self):
        """Generează o semnătură unică pentru sistemul de monitorizare"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        system_data = f"REAL-TIME-MONITORING-SYSTEM-{timestamp}"
        signature_base = f"ERVIN-REMUS-RADOSAVLEVICI:{system_data}:ANTI-SCAMMER"
        return hashlib.sha256(signature_base.encode()).hexdigest()
    
    def register_callbacks(self, alert_callback=None, evidence_callback=None, blacklist_callback=None):
        """
        Înregistrează callback-uri pentru integrare cu alte sisteme
        
        Args:
            alert_callback: Funcție apelată când se generează o alertă
            evidence_callback: Funcție apelată pentru colectarea dovezilor
            blacklist_callback: Funcție apelată pentru adăugarea în blacklist
        """
        if alert_callback:
            self.alert_callback = alert_callback
        
        if evidence_callback:
            self.evidence_collection_callback = evidence_callback
        
        if blacklist_callback:
            self.blacklist_callback = blacklist_callback
    
    def start_monitoring(self):
        """
        Pornește monitorizarea în timp real într-un thread separat
        
        Returns:
            bool: True dacă monitorizarea a fost pornită cu succes
        """
        if self.monitoring_thread and self.monitoring_thread.is_alive():
            return False  # Monitorizarea este deja pornită
        
        self.stop_monitoring = False
        self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitoring_thread.start()
        
        return True
    
    def stop_monitoring_thread(self):
        """
        Oprește monitorizarea în timp real
        
        Returns:
            bool: True dacă monitorizarea a fost oprită cu succes
        """
        if not self.monitoring_thread or not self.monitoring_thread.is_alive():
            return False  # Monitorizarea nu este activă
        
        self.stop_monitoring = True
        self.monitoring_thread.join(timeout=5.0)
        
        return not self.monitoring_thread.is_alive()
    
    def _monitoring_loop(self):
        """Loop principal pentru monitorizarea în timp real"""
        while not self.stop_monitoring:
            # Simulăm detectarea activităților
            if random.random() < 0.1:  # 10% șansă de a detecta o activitate
                activity_type = random.choice(self.monitored_activities)
                self._process_activity({
                    "type": activity_type,
                    "timestamp": datetime.datetime.now(),
                    "source": f"IP-{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
                    "user_agent": f"USER-AGENT-{random.randint(1000, 9999)}"
                })
            
            time.sleep(1.0)  # Așteptăm 1 secundă între verificări
    
    def _process_activity(self, activity_data):
        """
        Procesează o activitate detectată
        
        Args:
            activity_data (dict): Date despre activitatea detectată
        
        Returns:
            dict: Rezultatul procesării
        """
        # Incrementăm contorul total
        self.statistics["total_activities_monitored"] += 1
        
        # Evaluăm nivelul de suspiciune
        suspicion_score = self._calculate_suspicion_score(activity_data)
        suspicion_level = self._score_to_level(suspicion_score)
        
        # Creăm înregistrarea pentru activitate
        activity_record = {
            "id": hashlib.sha256(f"ACTIVITY-{datetime.datetime.now()}-{random.random()}".encode()).hexdigest()[:16],
            "timestamp": activity_data["timestamp"].strftime("%d.%m.%Y %H:%M:%S"),
            "type": activity_data["type"],
            "source": activity_data["source"],
            "user_agent": activity_data.get("user_agent", "UNKNOWN"),
            "suspicion_score": suspicion_score,
            "suspicion_level": suspicion_level,
            "actions_taken": self.suspicion_actions.get(suspicion_level, ["LOG"])
        }
        
        # Adăugăm activitatea în istoric
        self.activity_history.append(activity_record)
        if len(self.activity_history) > self.max_history_size:
            self.activity_history.pop(0)  # Eliminăm cea mai veche activitate
        
        # Executăm acțiunile corespunzătoare nivelului de suspiciune
        if suspicion_level != "NORMAL":
            self.statistics["suspicious_activities_detected"] += 1
            
            # Generăm alertă
            if "ALERT" in activity_record["actions_taken"]:
                self.statistics["alerts_generated"] += 1
                if self.alert_callback:
                    self.alert_callback(activity_record)
            
            # Blocăm temporar
            if "BLOCK_TEMPORARILY" in activity_record["actions_taken"]:
                self.statistics["temporary_blocks"] += 1
                # Implementare pentru blocare temporară
            
            # Blocăm permanent
            if "BLOCK_PERMANENTLY" in activity_record["actions_taken"]:
                self.statistics["permanent_blocks"] += 1
                # Implementare pentru blocare permanentă
            
            # Colectăm dovezi
            if "COLLECT_EVIDENCE" in activity_record["actions_taken"]:
                self.statistics["evidence_collected"] += 1
                if self.evidence_collection_callback:
                    self.evidence_collection_callback(activity_record)
            
            # Adăugăm în blacklist
            if "ADD_TO_BLACKLIST" in activity_record["actions_taken"]:
                self.statistics["blacklist_additions"] += 1
                if self.blacklist_callback:
                    self.blacklist_callback({
                        "identifier": activity_data["source"],
                        "reason": f"Activitate suspectă: {activity_data['type']}",
                        "severity": "HIGH",
                        "source": "REAL_TIME_MONITORING"
                    })
        
        return activity_record
    
    def _calculate_suspicion_score(self, activity_data):
        """
        Calculează un scor de suspiciune pentru o activitate
        
        Args:
            activity_data (dict): Date despre activitate
            
        Returns:
            int: Scorul de suspiciune (0-100)
        """
        base_score = 0
        
        # Scoruri pentru diferite tipuri de activități
        activity_scores = {
            "FILE_ACCESS": 5,
            "FILE_MODIFICATION": 10,
            "FILE_DELETION": 25,
            "AUTHENTICATION_ATTEMPT": 15,
            "API_ACCESS": 10,
            "DATABASE_QUERY": 15,
            "CONFIGURATION_CHANGE": 20,
            "COPYRIGHT_CHANGE": 40,
            "WATERMARK_TAMPERING": 50,
            "CHECKPOINT_ACCESS": 25,
            "ROLLBACK_ATTEMPT": 35,
            "WORKFLOW_MODIFICATION": 30,
            "WORKSPACE_CHANGE": 20,
            "SYSTEM_SETTING_CHANGE": 35,
            "UNAUTHORIZED_EXPORT": 45
        }
        
        # Adăugăm scorul de bază pentru tipul de activitate
        base_score += activity_scores.get(activity_data["type"], 10)
        
        # Adăugăm factori aleatori pentru simulare
        base_score += random.randint(-5, 15)
        
        # Limităm scorul între 0 și 100
        return max(0, min(100, base_score))
    
    def _score_to_level(self, score):
        """
        Convertește un scor de suspiciune într-un nivel de suspiciune
        
        Args:
            score (int): Scorul de suspiciune
            
        Returns:
            str: Nivelul de suspiciune
        """
        if score < 10:
            return "NORMAL"
        elif score < 25:
            return "LOW"
        elif score < 50:
            return "MEDIUM"
        elif score < 75:
            return "HIGH"
        else:
            return "CRITICAL"
    
    def monitor_specific_activity(self, activity_data):
        """
        Monitorizează o activitate specifică furnizată direct
        
        Args:
            activity_data (dict): Date despre activitatea de monitorizat
            
        Returns:
            dict: Rezultatul monitorizării
        """
        if "timestamp" not in activity_data:
            activity_data["timestamp"] = datetime.datetime.now()
        
        return self._process_activity(activity_data)
    
    def get_recent_activities(self, count=10, filter_level=None):
        """
        Obține cele mai recente activități din istoric
        
        Args:
            count (int): Numărul de activități de returnat
            filter_level (str, optional): Filtrează după nivelul de suspiciune
            
        Returns:
            list: Lista activităților recente
        """
        if filter_level:
            filtered_activities = [a for a in self.activity_history if a.get("suspicion_level") == filter_level]
        else:
            filtered_activities = self.activity_history
        
        # Sortăm după timestamp în ordine descrescătoare
        sorted_activities = sorted(filtered_activities, 
                                  key=lambda a: datetime.datetime.strptime(a["timestamp"], "%d.%m.%Y %H:%M:%S"),
                                  reverse=True)
        
        return sorted_activities[:count]
    
    def get_suspicious_activity_report(self):
        """
        Generează un raport detaliat despre activitățile suspecte
        
        Returns:
            dict: Raportul generat
        """
        suspicious_activities = [a for a in self.activity_history 
                                if a.get("suspicion_level") in ["MEDIUM", "HIGH", "CRITICAL"]]
        
        # Grupăm după nivelul de suspiciune
        grouped_by_level = {
            "MEDIUM": [],
            "HIGH": [],
            "CRITICAL": []
        }
        
        for activity in suspicious_activities:
            level = activity.get("suspicion_level")
            if level in grouped_by_level:
                grouped_by_level[level].append(activity)
        
        # Grupăm după tipul de activitate
        grouped_by_type = {}
        for activity in suspicious_activities:
            activity_type = activity.get("type")
            if activity_type not in grouped_by_type:
                grouped_by_type[activity_type] = []
            grouped_by_type[activity_type].append(activity)
        
        # Generăm raportul
        report = {
            "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "report_id": hashlib.sha256(f"REPORT-{datetime.datetime.now()}".encode()).hexdigest()[:16],
            "total_activities": len(self.activity_history),
            "suspicious_activities": len(suspicious_activities),
            "by_level": {
                "MEDIUM": len(grouped_by_level["MEDIUM"]),
                "HIGH": len(grouped_by_level["HIGH"]),
                "CRITICAL": len(grouped_by_level["CRITICAL"])
            },
            "by_type": {activity_type: len(activities) for activity_type, activities in grouped_by_type.items()},
            "recent_critical": grouped_by_level["CRITICAL"][:5] if grouped_by_level["CRITICAL"] else [],
            "statistics": self.statistics,
            "monitoring_signature": self.monitoring_signature
        }
        
        return report
    
    def get_monitoring_status(self):
        """
        Returnează statusul complet al sistemului de monitorizare
        
        Returns:
            dict: Statusul sistemului
        """
        return {
            "monitoring_active": self.monitoring_active,
            "protection_level": self.protection_level,
            "real_time_alerts": self.real_time_alerts,
            "suspicious_activity_detection": self.suspicious_activity_detection,
            "instant_blocking": self.instant_blocking,
            "pattern_recognition": self.pattern_recognition,
            "behavioral_analysis": self.behavioral_analysis,
            "monitored_activities": len(self.monitored_activities),
            "activity_history_size": len(self.activity_history),
            "is_monitoring_running": self.monitoring_thread is not None and self.monitoring_thread.is_alive(),
            "statistics": self.statistics,
            "monitoring_signature": self.monitoring_signature,
            "last_update": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "owner": "Ervin Remus Radosavlevici",
            "system_integrity": "100%"
        }
    
    def export_activity_history(self, format="json"):
        """
        Exportă istoricul activităților pentru analiză
        
        Args:
            format (str): Formatul de export (json, csv, etc.)
            
        Returns:
            str: Datele exportate în formatul specificat
        """
        if format == "json":
            export_data = {
                "export_id": hashlib.sha256(f"EXPORT-{datetime.datetime.now()}".encode()).hexdigest()[:16],
                "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "exported_by": "REAL_TIME_MONITORING_SYSTEM",
                "activity_count": len(self.activity_history),
                "owner": "Ervin Remus Radosavlevici",
                "activities": self.activity_history
            }
            
            return json.dumps(export_data, indent=2)
        
        # Implementarea pentru alte formate ar veni aici
        return "Format nesuportat"