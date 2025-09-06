from fpdf import FPDF
from fpdf.enums import XPos, YPos


class InvoicePDF(FPDF):
    def header(self):
        # Header with Company Name and Details
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 51, 102)  # Dark blue text
        self.cell(0, 8, "Sahir Electricals Enterprise", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", size=10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 5, "Baghat Barzulla | Phone: +91 9797123473", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 5, "PAN: ARTPB2973K", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

        # Additional Business Info
        self.set_font("Helvetica", size=9)
        self.cell(0, 6, "Deals with: Electrical Goods and Appliances", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 6, "Specializing in: LED Bulbs, Ceiling Fans, Switch Boards, Decorative Lights, Wires", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 6, "Address: Baghat Barzulla | Account Number: 0392040100002629", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

        # Invoice Header
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, " INVOICE", border=0, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

        self.set_font("Helvetica", size=10)
        self.cell(95, 6, "Invoice No: S01", align="L")
        self.cell(95, 6, "Invoice Date: 05 december 2024", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

    def add_customer_details(self):
        # Customer Details
        self.set_font("Helvetica", "B", 10)
        self.set_fill_color(0, 51, 102)
        self.set_text_color(255, 255, 255)
        self.cell(95, 8, "BILL TO", fill=True)
        self.cell(95, 8, "SHIP TO", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("Helvetica", size=10)
        self.set_text_color(0, 0, 0)
        #self.cell(95, 8, "Rayees Hassan\nBaghat Barzulla, Srinagar\nPhone: +91 9797123473", border=1)
        self.cell(95, 8, "Rayees Hassan\ ARI BAGH KANIPORA, Phone: +91 7006265140", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

    def add_items_table(self, items):
        # Items Table Header
        self.set_font("Helvetica", "B", 10)
        self.set_fill_color(200, 200, 200)
        self.cell(70, 10, "Item Description", border=1, fill=True)
        self.cell(30, 10, "Quantity", border=1, fill=True, align="C")
        self.cell(40, 10, "Price per Unit", border=1, fill=True, align="C")
        self.cell(40, 10, "Total", border=1, fill=True, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Items Table Content
        self.set_font("Helvetica", size=10)
        total_amount = 0
        for item, quantity, price in items:
            total = quantity * price
            total_amount += total
            self.cell(70, 10, item, border=1)
            self.cell(30, 10, str(quantity), border=1, align="C")
            self.cell(40, 10, f"Rs. {price}", border=1, align="C")
            self.cell(40, 10, f"Rs. {total}", border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Total Amount Row
        self.set_font("Helvetica", "B", 10)
        self.cell(140, 10, "Total Amount", border=1, align="R", fill=True)
        self.cell(40, 10, f"Rs. {total_amount}", border=1, align="C", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

        # Add total in words
        self.cell(0, 8, f"Total in Words: Two Lakh Twenty-Four Thousand Five Hundred Only", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def add_terms_and_conditions(self):
        self.set_font("Helvetica", size=9)
        self.ln(6)
        self.multi_cell(0, 6, 
            "Terms and Conditions:\n"
            "1. No return policy.\n"
            "2. Payment due within 15 days.\n"
            "3. Electrical goods must be installed by certified electricians to claim warranty.\n")


# Items list adjusted to total Rs. 224,500 (Inverter and Battery Removed)
items = [
    ("Switch Boards", 10, 3500),
    ("Ceiling Fans", 5, 3500),
    ("LED Bulbs", 100, 200),
    ("Circuit Breakers (MCBs)", 10, 250),
    ("Electrical Wires (1mm)", 120, 100),
    ("Electrical Wires (2mm)", 60, 150),
    ("Electrical Wires (7mm)", 50, 800),
    ("Socket Outlets", 50, 250),
    ("Electrical Tape", 40, 50),
    ("Fan Regulators", 20, 300),
    ("Chandeliers", 2, 15000),
    ("LED Panels", 4, 3500),
    ("Decorative Lights", 12, 2000),
]

# Generate the invoice
pdf = InvoicePDF()
pdf.add_page()
pdf.add_customer_details()
pdf.add_items_table(items)
pdf.add_terms_and_conditions()
pdf.output("Bill_rayess_original_1.pdf")
