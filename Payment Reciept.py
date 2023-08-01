#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install reportlab')

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_payment_receipt(name, amount_paid, payment_method, receipt_number):
    # Create a PDF canvas
    pdf_file = f"PaymentReceipt_{receipt_number}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Set font and font size
    c.setFont("Helvetica-Bold", 12)

    # Receipt title
    c.drawString(250, 750, "Payment Receipt")
    c.line(220, 745, 370, 745)

    # Display payment details
    c.setFont("Helvetica", 11)
    c.drawString(100, 700, "Customer Name:")
    c.drawString(250, 700, name)
    c.drawString(100, 675, "Amount Paid:")
    c.drawString(250, 675, f"${amount_paid:.2f}")
    c.drawString(100, 650, "Payment Method:")
    c.drawString(250, 650, payment_method)
    c.drawString(100, 625, "Receipt Number:")
    c.drawString(250, 625, str(receipt_number))

    # Add a line separator
    c.line(50, 600, 550, 600)

    # Thank you message
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 560, "Thank you for your payment!")

    # Save the PDF file
    c.save()
    print(f"Payment receipt created: {pdf_file}")

if __name__ == "__main__":
    # Example usage:
    customer_name = "John Doe"
    amount_paid = 100.50
    payment_method = "Credit Card"
    receipt_number = 12345

    create_payment_receipt(customer_name, amount_paid, payment_method, receipt_number)


# In[ ]:




