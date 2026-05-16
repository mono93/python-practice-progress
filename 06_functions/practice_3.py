def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
    # Write your code below this line
    total = 0.0
    invoice_lines = [f"Invoice for {customer_name}:"]
 
    if items:
        invoice_lines.append("Items:")
        for item in items:
            invoice_lines.append(f"- {item}")
 
    if charges:
        invoice_lines.append("Charges:")
        for label, amount in charges.items():
            invoice_lines.append(f"{label.capitalize()}: {amount}")
            total += amount
 
    invoice_lines.append(f"Total Amount Due: {total}")
    return "\\n".join(invoice_lines)
