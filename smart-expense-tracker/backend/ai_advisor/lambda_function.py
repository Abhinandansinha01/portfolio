import json

def lambda_handler(event, context):
    """
    Analyzes transaction history and provides 'Smart' financial advice.
    Unique Feature: Detected Recurring Patterns & 'Guilt' Trip
    """
    
    # Mock input data
    transactions = event.get('transactions', [])
    
    coffee_spend = 0
    total_spend = 0
    
    for t in transactions:
        amount = t.get('amount', 0)
        category = t.get('category', 'misc')
        total_spend += amount
        
        if category.lower() == 'coffee':
            coffee_spend += amount
            
    advice = []
    
    if coffee_spend > 50:
        advice.append(f"☕ You spent ${coffee_spend} on coffee this month. That's a whole gym membership!")
        
    if total_spend > 1000:
        advice.append("💸 High spending alert! Let's enable 'Monk Mode' for next week.")
        
    if not advice:
        advice.append("✅ innovative! You are saving like a pro.")
        
    return {
        'statusCode': 200,
        'body': json.dumps({
            "financial_health": "Critical" if total_spend > 2000 else "Good",
            "ai_advice": advice
        })
    }
