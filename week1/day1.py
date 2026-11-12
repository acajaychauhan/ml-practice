product = "Gear Housing"
produced = 1200
rejected = 36
rate_per_piece = 4.5
good_pieces = produced - rejected
rejection_percent = rejected/produced * 100
wage = good_pieces * rate_per_piece
print(f"{product}: {good_pieces} good pieces out of {produced}")
print(f"Rejection rate: {rejection_percent:.2f}%")
print(f"Wage earned: Rs {wage:,.2f}")
shift ="A"
planned = 1000
actual = 945
rejected_qty = 20
achievement = actual/planned * 100
rejection = rejected_qty/actual * 100
print(f"Shift {shift}: achieved {achievement:.2f}%, rejection {rejection:.2f}%")