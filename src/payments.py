import requests
import time

import os

API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("No API token provided. Set the API_TOKEN environment variable.")
API_URL = "https://pay.crypt.bot/api/"
HEADERS = {
    "Crypto-Pay-API-Token": API_TOKEN,
    "Content-Type": "application/json"
}

def get_payments():
    """Busca invoices e verifica pagamentos recebidos."""
    response = requests.get(f"{API_URL}getInvoices", headers=HEADERS)
    data = response.json()
    
    if data.get("ok"):
        for invoice in data["result"]["items"]:
            status = invoice.get("status")
            if status == "paid":
                print(f"✅ Pagamento Recebido!\nID: {invoice['invoice_id']}\nValor: {invoice['amount']} {invoice['currency']}")
    
    return data

# Loop para buscar pagamentos a cada 30 segundos
if __name__ == "__main__":
    print("🔄 Iniciando monitoramento de pagamentos...")
    while True:
        get_payments()
        time.sleep(30)  # Aguarda 30 segundos antes de verificar novamente
