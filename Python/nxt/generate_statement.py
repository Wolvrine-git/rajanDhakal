from datetime import datetime
def Statement(ID, start_date, end_date):
    try:
        with open(f"Customers/{ID}/trans.txt", 'r') as f:
            print(f"Transaction statements between {start_date} and {end_date}:")
            for line in f:
                transaction_date = datetime.strptime(line.split()[0],"%Y-%m-%d").date()
                if start_date <= transaction_date <= end_date:
                    print(line.strip())
    
    except FileNotFoundError:
        print("Transaction log not found.")


