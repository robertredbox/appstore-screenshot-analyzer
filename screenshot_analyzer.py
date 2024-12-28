from PIL import Image
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import io
import imagehash
import numpy as np

def analyze_app_screenshots(app_store_url):
    # Scrape screenshots
    response = requests.get(app_store_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    screenshot_urls = [img['src'] for img in soup.find_all('img') if 'screenshot' in img.get('class', [])]
    
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    for url in screenshot_urls:
        # Download and analyze image
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        
        # Basic image analysis
        width, height = img.size
        aspect_ratio = width / height
        colors = len(img.getcolors(maxcolors=10000)) if img.getcolors(maxcolors=10000) else "More than 10000"
        brightness = np.mean(img)
        
        # Generate feedback based on measurements
        feedback = [
            f"Resolution: {width}x{height}",
            f"Aspect Ratio: {aspect_ratio:.2f}",
            f"Color Variety: {colors} distinct colors",
            f"Average Brightness: {brightness:.2f}/255",
            "Suggestions:",
            "- Consider image compression if file size is large",
            f"- {'Good' if 1.5 < aspect_ratio < 2 else 'Review'} aspect ratio for mobile display",
            f"- {'Good' if 30 < brightness < 225 else 'Review'} brightness levels"
        ]
        
        # Add to PDF
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Screenshot Analysis', ln=True)
        pdf.set_font('Arial', '', 12)
        
        for line in feedback:
            pdf.cell(0, 10, line, ln=True)
    
    # Save PDF
    pdf.output("screenshot_analysis.pdf")
    return "screenshot_analysis.pdf"

if __name__ == "__main__":
    # Example usage
    app_url = input("Enter App Store URL: ")
    analyze_app_screenshots(app_url)