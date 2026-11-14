product = "Shaft"
produced = 500
rejected = 15
rate = 3.5
good_pieces = produced-rejected
rejection_percent = rejected/produced*100
wage = good_pieces*rate
print(f"{product}: {good_pieces} good pieces out of {produced}")
print(f"Rejection rate: {rejection_percent:,.2f}%")
print(f"Wage: Rs {wage:,.2f}")