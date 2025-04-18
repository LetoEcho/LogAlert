import subprocess
import requests

# --- CONFIGURACIÓN ---
REMOTE_USER = USUARIO_SSH  # ← usuario SSH
TELEGRAM_BOT_TOKEN = TOKEN_TELEGRAM_BOT
TELEGRAM_CHAT_ID = ID_CHAT_BOT

LOG_COMMAND = "tail -f RUTE | grep 'OutOfMemoryError'"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def monitor_log(ip_address):
    ssh_cmd = [
        "ssh",
        f"{REMOTE_USER}@{ip_address}",
        LOG_COMMAND
    ]

    print(f"🔗 Connecting to {REMOTE_USER}@{ip_address}...")
    process = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        print(f"[+] {line.strip()}")
        send_telegram(f"🚨 MESSAGE {ip_address}!\n{line.strip()}")

if __name__ == "__main__":
    ip = input("🖥️ Which IP do you want to connect to via SSH? ➤ ")
    monitor_log(ip)
