import requests

API_TOKEN = "SEU_API_TOKEN_AQUI"
API_URL = "https://pay.crypt.bot/api/"
HEADERS = {
    "Crypto-Pay-API-Token": API_TOKEN,
    "Content-Type": "application/json"
}

def create_invoice(amount, currency="TON", description="Pagamento FlowPay"):
    """Cria uma nova invoice na Crypto Pay API"""
    payload = {
        "asset": currency,
        "amount": str(amount),
        "description": description
    }
    
    response = requests.post(f"{API_URL}createInvoice", json=payload, headers=HEADERS)
    data = response.json()
    
    if data.get("ok"):
        invoice = data["result"]
        print(f"✅ Invoice Criada!\nID: {invoice['invoice_id']}\nLink de Pagamento: {invoice['pay_url']}")
        return invoice["pay_url"]  # Retorna o link da invoice
    
    print(f"❌ Erro ao criar invoice: {data}")
    return None
