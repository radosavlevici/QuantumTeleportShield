import os
import datetime
import hashlib
import random
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertSystem:
    """
    Sistem avansat de alerte și notificări pentru activități suspecte și tentative de fraudă
    Copyright Ervin Remus Radosavlevici - Sistem securizat ADN
    """
    def __init__(self):
        self.alert_system_active = True
        self.protection_level = "MAXIMUM"
        self.email_alerts = True
        self.sms_alerts = False  # Necesită configurare suplimentară
        self.dashboard_alerts = True
        self.critical_alerts = True
        
        # Setări de email
        self.email_settings = {
            "enabled": True,
            "notification_email": "ERVIN210@ICLOUD.COM",
            "email_frequency": "REAL-TIME",  # Alternativ: "DAILY", "HOURLY", "SUMMARY"
            "include_details": True,
            "include_evidence": True
        }
        
        # Setări pentru alertele din dashboard
        self.dashboard_settings = {
            "show_realtime_alerts": True,
            "alert_history_size": 100,
            "auto_refresh": True,
            "refresh_interval_seconds": 30,
            "highlight_critical": True
        }
        
        # Alerte și notificări recente
        self.recent_alerts = []
        self.max_alert_history = 500
        
        # Niveluri de alertă
        self.alert_levels = {
            "INFO": "Informație generală, fără acțiune necesară",
            "WARNING": "Avertisment pentru activitate potențial suspectă",
            "ALERT": "Alertă pentru activitate suspectă confirmată",
            "CRITICAL": "Alertă critică pentru activitate malițioasă imediată",
            "EMERGENCY": "Urgență de securitate, activitate malițioasă severă"
        }
        
        # Tipuri de alerte
        self.alert_types = [
            "SUSPICIOUS_ACTIVITY",
            "AUTHENTICATION_FAILURE",
            "FILE_MANIPULATION",
            "COPYRIGHT_VIOLATION",
            "UNAUTHORIZED_ACCESS",
            "CONFIGURATION_CHANGE",
            "CHECKPOINT_MANIPULATION",
            "ROLLBACK_ABUSE",
            "SCAMMER_DETECTED",
            "BLACKLIST_ADDITION",
            "SYSTEM_TAMPERING",
            "EMERGENCY_PROTOCOL_ACTIVATED",
            "DATA_THEFT_ATTEMPT",
            "WORKSPACE_VIOLATION",
            "WORKFLOW_TAMPERING"
        ]
        
        # Statistici
        self.alert_statistics = {
            "total_alerts": 0,
            "by_level": {
                "INFO": 0,
                "WARNING": 0,
                "ALERT": 0,
                "CRITICAL": 0,
                "EMERGENCY": 0
            },
            "by_type": {},
            "emails_sent": 0,
            "sms_sent": 0,
            "dashboard_alerts": 0
        }
        
        # Generăm semnătura pentru sistemul de alerte
        self.alert_system_signature = self._generate_alert_signature()
    
    def _generate_alert_signature(self):
        """Generează o semnătură unică pentru sistemul de alerte"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        system_data = f"ALERT-SYSTEM-{timestamp}"
        signature_base = f"ERVIN-REMUS-RADOSAVLEVICI:{system_data}:ANTI-SCAMMER-ALERTS"
        return hashlib.sha256(signature_base.encode()).hexdigest()
    
    def generate_alert(self, alert_data):
        """
        Generează o alertă pentru o activitate suspectă
        
        Args:
            alert_data (dict): Informații despre alertă
            
        Returns:
            dict: Alertă generată
        """
        if "timestamp" not in alert_data:
            alert_data["timestamp"] = datetime.datetime.now()
        
        if "level" not in alert_data:
            alert_data["level"] = "WARNING"
        
        if "type" not in alert_data:
            alert_data["type"] = "SUSPICIOUS_ACTIVITY"
        
        # Creăm alerta
        alert = {
            "alert_id": hashlib.sha256(f"ALERT-{datetime.datetime.now()}-{random.random()}".encode()).hexdigest()[:16],
            "timestamp": alert_data["timestamp"].strftime("%d.%m.%Y %H:%M:%S"),
            "level": alert_data["level"],
            "type": alert_data["type"],
            "message": alert_data.get("message", f"Alertă de {alert_data['type']}"),
            "details": alert_data.get("details", {}),
            "source": alert_data.get("source", "ALERT_SYSTEM"),
            "generated_by": "ALERT_SYSTEM",
            "signature": hashlib.sha256(f"ALERT-{alert_data['timestamp']}-{alert_data['level']}-{alert_data['type']}".encode()).hexdigest()
        }
        
        # Adăugăm alerta în istoric
        self.recent_alerts.append(alert)
        if len(self.recent_alerts) > self.max_alert_history:
            self.recent_alerts.pop(0)  # Eliminăm cea mai veche alertă
        
        # Actualizăm statisticile
        self.alert_statistics["total_alerts"] += 1
        self.alert_statistics["by_level"][alert["level"]] = self.alert_statistics["by_level"].get(alert["level"], 0) + 1
        self.alert_statistics["by_type"][alert["type"]] = self.alert_statistics["by_type"].get(alert["type"], 0) + 1
        
        # Procesăm alerta
        self._process_alert(alert)
        
        return alert
    
    def _process_alert(self, alert):
        """
        Procesează o alertă și realizează acțiunile necesare
        
        Args:
            alert (dict): Alerta de procesat
        """
        # Alertă pe dashboard
        if self.dashboard_alerts and self.dashboard_settings["show_realtime_alerts"]:
            self.alert_statistics["dashboard_alerts"] += 1
            # Implementare pentru afișarea alertei pe dashboard
        
        # Alertă prin email
        if self.email_alerts and self.email_settings["enabled"]:
            if self._should_send_email_alert(alert):
                self._send_email_alert(alert)
                self.alert_statistics["emails_sent"] += 1
        
        # Alertă prin SMS
        if self.sms_alerts:
            if alert["level"] in ["CRITICAL", "EMERGENCY"]:
                self._send_sms_alert(alert)
                self.alert_statistics["sms_sent"] += 1
    
    def _should_send_email_alert(self, alert):
        """
        Determină dacă trebuie trimisă o alertă prin email
        
        Args:
            alert (dict): Alerta de evaluat
            
        Returns:
            bool: True dacă trebuie trimisă alerta prin email
        """
        # Trimitem mereu alertele critice și de urgență
        if alert["level"] in ["CRITICAL", "EMERGENCY"]:
            return True
        
        # În funcție de frecvența configurată
        if self.email_settings["email_frequency"] == "REAL-TIME":
            return True
        
        # Pentru celelalte frecvențe, alertele sunt colectate și trimise periodic
        # Acest comportament ar fi implementat printr-un sistem de programare a alertelor
        
        return False
    
    def _send_email_alert(self, alert):
        """
        Trimite o alertă prin email
        
        Args:
            alert (dict): Alerta de trimis
            
        Returns:
            bool: True dacă emailul a fost trimis cu succes
        """
        # Această funcție ar implementa trimiterea efectivă a email-ului
        # Simulăm doar procesul pentru acest exemplu
        
        recipient = self.email_settings["notification_email"]
        subject = f"[{alert['level']}] Alertă de Securitate: {alert['type']}"
        
        # Construim conținutul email-ului
        body = f"""
        ALERTĂ DE SECURITATE
        
        ID: {alert['alert_id']}
        Data și ora: {alert['timestamp']}
        Nivel: {alert['level']}
        Tip: {alert['type']}
        
        Mesaj: {alert['message']}
        
        """
        
        # Adăugăm detalii dacă sunt configurate
        if self.email_settings["include_details"] and alert.get("details"):
            body += "\nDETALII:\n"
            for key, value in alert["details"].items():
                body += f"{key}: {value}\n"
        
        # Adăugăm evidențe dacă sunt configurate
        if self.email_settings["include_evidence"] and alert.get("evidence"):
            body += "\nDOVEZI:\n"
            body += str(alert["evidence"])
        
        # Adăugăm semnătura
        body += f"\n\nGenerat de: Sistem de Alertă Anti-Scammer\nSemnătură: {alert['signature']}\n"
        body += f"© {datetime.datetime.now().year}-2033 Ervin Remus Radosavlevici. Toate drepturile rezervate."
        
        # În implementarea reală, aici ar fi codul pentru trimiterea efectivă prin SMTP
        # msg = MIMEMultipart()
        # msg["From"] = "alert-system@example.com"
        # msg["To"] = recipient
        # msg["Subject"] = subject
        # msg.attach(MIMEText(body, "plain"))
        # ...
        
        return True
    
    def _send_sms_alert(self, alert):
        """
        Trimite o alertă prin SMS
        
        Args:
            alert (dict): Alerta de trimis
            
        Returns:
            bool: True dacă SMS-ul a fost trimis cu succes
        """
        # Această funcție ar implementa trimiterea efectivă a SMS-ului
        # Ar fi necesară integrarea cu un serviciu de SMS precum Twilio
        # Simulăm doar procesul pentru acest exemplu
        
        # Construim un mesaj SMS concis
        sms_message = f"[{alert['level']}] {alert['type']}: {alert['message']}"
        
        # În implementarea reală, aici ar fi codul pentru trimiterea efectivă a SMS-ului
        
        return True
    
    def get_recent_alerts(self, count=10, level=None, alert_type=None):
        """
        Obține cele mai recente alerte
        
        Args:
            count (int): Numărul de alerte de returnat
            level (str, optional): Filtrează după nivelul alertei
            alert_type (str, optional): Filtrează după tipul alertei
            
        Returns:
            list: Lista alertelor recente
        """
        filtered_alerts = self.recent_alerts
        
        # Aplicăm filtrele
        if level:
            filtered_alerts = [a for a in filtered_alerts if a.get("level") == level]
        
        if alert_type:
            filtered_alerts = [a for a in filtered_alerts if a.get("type") == alert_type]
        
        # Sortăm după timestamp în ordine descrescătoare
        sorted_alerts = sorted(filtered_alerts, 
                              key=lambda a: datetime.datetime.strptime(a["timestamp"], "%d.%m.%Y %H:%M:%S"),
                              reverse=True)
        
        return sorted_alerts[:count]
    
    def get_critical_alerts(self, count=10):
        """
        Obține alertele critice și de urgență recente
        
        Args:
            count (int): Numărul de alerte de returnat
            
        Returns:
            list: Lista alertelor critice
        """
        return self.get_recent_alerts(count=count, level="CRITICAL") + self.get_recent_alerts(count=count, level="EMERGENCY")
    
    def get_alert_summary(self):
        """
        Generează un rezumat al alertelor recente
        
        Returns:
            dict: Rezumatul alertelor
        """
        current_time = datetime.datetime.now()
        
        # Calculăm statistici pentru ultimele 24 de ore
        last_24h = [a for a in self.recent_alerts 
                   if datetime.datetime.strptime(a["timestamp"], "%d.%m.%Y %H:%M:%S") > 
                   (current_time - datetime.timedelta(hours=24))]
        
        last_24h_levels = {
            "INFO": sum(1 for a in last_24h if a.get("level") == "INFO"),
            "WARNING": sum(1 for a in last_24h if a.get("level") == "WARNING"),
            "ALERT": sum(1 for a in last_24h if a.get("level") == "ALERT"),
            "CRITICAL": sum(1 for a in last_24h if a.get("level") == "CRITICAL"),
            "EMERGENCY": sum(1 for a in last_24h if a.get("level") == "EMERGENCY")
        }
        
        # Generăm rezumatul
        summary = {
            "timestamp": current_time.strftime("%d.%m.%Y %H:%M:%S"),
            "summary_id": hashlib.sha256(f"SUMMARY-{datetime.datetime.now()}".encode()).hexdigest()[:16],
            "total_alerts": len(self.recent_alerts),
            "total_last_24h": len(last_24h),
            "by_level_total": self.alert_statistics["by_level"],
            "by_level_last_24h": last_24h_levels,
            "by_type": self.alert_statistics["by_type"],
            "most_common_type": max(self.alert_statistics["by_type"].items(), key=lambda x: x[1])[0] if self.alert_statistics["by_type"] else None,
            "critical_count": self.alert_statistics["by_level"].get("CRITICAL", 0) + self.alert_statistics["by_level"].get("EMERGENCY", 0),
            "alert_system_signature": self.alert_system_signature
        }
        
        return summary
    
    def get_alert_system_status(self):
        """
        Returnează statusul complet al sistemului de alerte
        
        Returns:
            dict: Statusul sistemului
        """
        return {
            "alert_system_active": self.alert_system_active,
            "protection_level": self.protection_level,
            "email_alerts": self.email_alerts,
            "sms_alerts": self.sms_alerts,
            "dashboard_alerts": self.dashboard_alerts,
            "critical_alerts": self.critical_alerts,
            "email_settings": self.email_settings,
            "dashboard_settings": self.dashboard_settings,
            "alert_history_size": len(self.recent_alerts),
            "alert_statistics": self.alert_statistics,
            "alert_system_signature": self.alert_system_signature,
            "last_update": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "owner": "Ervin Remus Radosavlevici",
            "system_integrity": "100%"
        }
    
    def export_alerts(self, format="json", filter_level=None):
        """
        Exportă alertele pentru analiză
        
        Args:
            format (str): Formatul de export (json, csv, etc.)
            filter_level (str, optional): Filtrează după nivelul alertei
            
        Returns:
            str: Datele exportate în formatul specificat
        """
        if filter_level:
            filtered_alerts = [a for a in self.recent_alerts if a.get("level") == filter_level]
        else:
            filtered_alerts = self.recent_alerts
            
        if format == "json":
            export_data = {
                "export_id": hashlib.sha256(f"EXPORT-{datetime.datetime.now()}".encode()).hexdigest()[:16],
                "timestamp": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "exported_by": "ALERT_SYSTEM",
                "alert_count": len(filtered_alerts),
                "filter_level": filter_level,
                "owner": "Ervin Remus Radosavlevici",
                "alerts": filtered_alerts
            }
            
            return json.dumps(export_data, indent=2)
        
        # Implementarea pentru alte formate ar veni aici
        return "Format nesuportat"