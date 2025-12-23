from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_pdf(summary, key_points, decisions, actions):
    os.makedirs("outputs", exist_ok=True)

    path = f"outputs/meeting_minutes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    y = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Meeting Minutes")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"Generated on: {datetime.now().strftime('%d %b %Y %H:%M')}")
    y -= 30

    def draw(title, items):
        nonlocal y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, title)
        y -= 20
        c.setFont("Helvetica", 10)

        if not items:
            c.drawString(50, y, "- None")
            y -= 15
        else:
            for i in items:
                c.drawString(50, y, f"- {i}")
                y -= 15
                if y < 50:
                    c.showPage()
                    y = height - 40

        y -= 10

    draw("Summary", [summary])
    draw("Key Points", key_points)
    draw("Decisions", decisions)
    draw("Action Items", actions)

    c.save()
    return path
