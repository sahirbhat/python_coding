from fpdf import FPDF

# Create a PDF object
pdf = FPDF()

# Add a page to the PDF
pdf.add_page()

# Set font to Helvetica (default)
pdf.set_font("Helvetica", size=12)

# Company Name and Address
pdf.cell(200, 10, txt="Fesh Max Health Food", ln=True, align="C")
pdf.cell(200, 10, txt="Company Address: C-28, SECTOR-6, NOIDA-201301, UP", ln=True, align="C")

# Employee Details
pdf.ln(10)
pdf.cell(200, 10, txt="Salary Slip for the Month", ln=True, align="C")
pdf.ln(5)
pdf.cell(100, 10, txt="Employee Name: Shashank Sharma", ln=True)
pdf.cell(100, 10, txt="Designation: Sales Officer", ln=True)
pdf.cell(100, 10, txt="Department: Inventory", ln=True)
pdf.cell(100, 10, txt="Number of Working Days: 30", ln=True)
pdf.cell(100, 10, txt="Leave: 0", ln=True)

# Salary Details Table
pdf.ln(10)
pdf.cell(100, 10, txt="Basic Pay: INR 28,500", ln=True)  # Replaced ₹ with INR
pdf.cell(100, 10, txt="HRA: INR 14,250", ln=True)  # Replaced ₹ with INR

# Calculating total salary
basic_pay = 28500
hra = 14250
other_allowances = 0  # No other allowances specified

total_salary = basic_pay + hra + other_allowances

# Total Salary
pdf.cell(100, 10, txt="Total Salary: INR " + str(total_salary), ln=True)  # Replaced ₹ with INR

# Save the PDF to a file
pdf.output("salary_slip_shashank_sharma.pdf")

print("Salary slip generated successfully!")
