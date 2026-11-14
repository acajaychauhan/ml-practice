output = [950, 1020, 880, 1100, 990]
print(output[0])
print(output[-1])
print(len(output))
output.append(1050)
print(f"Total: {sum(output)}")
print(f"Average: {sum(output)/len(output):.2f}")
print(f"Best day: {max(output)}, worst day: {min(output)}")
worker = {"name": "Ramesh", "shift": "A", "pieces": 945, "rate": 4.5}
print(worker["name"])
worker["pieces"] = 960
wage = worker["pieces"] * worker["rate"]
print(f"{worker['name']} earned Rs {wage:,.2f}")