from fpdf import FPDF

class LandRecordForm(FPDF):
    def header(self):
        # Title Header
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Office of the Tehsil Srinagar', align='C', ln=True)
        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Land Record Form (Kaash Kari Form)', align='C', ln=True)
        self.ln(10)
        
    def footer(self):
        # Footer with page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_section(self, title, fields):
        # Add a section to the form
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font('Arial', '', 12)
        for field in fields:
            self.cell(0, 10, f"{field}: __________________________", ln=True)
        self.ln(10)

# Create the PDF
pdf = LandRecordForm()
pdf.add_page()

# Adding sections to the form
pdf.add_section("Personal Details", [
    "Full Name", 
    "Parentage", 
    "Address", 
    "Contact Number"
])

pdf.add_section("Land Details", [
    "Mouza (Village/Area Name)", 
    "Khasra Number", 
    "Type of Land (Agricultural/Residential/Commercial)", 
    "Total Land Area (in Kanals, Marlas, or Acres)", 
    "Ownership Share", 
    "Boundary Details (North, South, East, West)"
])

pdf.add_section("Revenue Information", [
    "Annual Tax", 
    "Payment Status (Paid/Unpaid)", 
    "Date of Last Revenue Update"
])

pdf.add_section("Signatures and Verification", [
    "Signature of Applicant", 
    "Date", 
    "Signature of Tehsildar/Official", 
    "Official Stamp"
])

# Save the PDF
output_file = "Land_Record_Form.pdf"
pdf.output(output_file)
print(f"Form created successfully! Check the file: {output_file}")
