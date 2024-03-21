from reportlab.lib.pagesizes import letter      # provides predefined page sizes.
from reportlab.pdfgen import canvas     #provides functionality for drawing shapes, text, and images onto a PDF document
import random
def generate_receipt(name, amount, paymentMethod):    
    r = str(random.random())
    pdfName = "receipt_" + r + ".pdf"
    canvasObj = canvas.Canvas(pdfName, pagesize = letter)     # canvas is set to generate a PDF file  
                                               
    canvasObj.drawString(100, 650, "Receipt")   # drawString is used to draw text elements on the canvas
    canvasObj.drawString(100, 640, "-" * 25)    # draws a line of 50 dashes at coordinates(x,y)
    canvasObj.drawString(100, 620, "Name: " + name)   # draws the name of the customer on the receipt
    canvasObj.drawString(100, 610, "Amount: ₹" + str(amount))   # draws the name of the customer on the receipt. 
    canvasObj.drawString(100, 600, "Payment Method: " + paymentMethod)  # draws the payment method used for the transaction on the receipt.
    
    canvasObj.save() # save the canvas to a PDF file named "receipt.pdf"

generate_receipt("Ravi ", 50.00, "Credit Card")     # 
