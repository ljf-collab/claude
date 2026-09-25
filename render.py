# Renders book.html -> book.pdf. Requires: pip install playwright && playwright install chromium
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
subprocess.run([sys.executable, "build.py"], check=True)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto("file://" + os.path.join(here, "book.html")); pg.wait_for_timeout(600)
    pg.pdf(path="Sarah in New York - Part Seven.pdf", prefer_css_page_size=True, print_background=True)
    b.close()
print("wrote Sarah in New York - Part Seven.pdf")
