from playwright.sync_api import sync_playwright
import os
import glob

def run_cuj(page):
    page.goto("http://localhost:8000")
    page.wait_for_timeout(1500)

    # Check the dashboard/map
    print("Navigating map filters...")
    page.locator("select").nth(0).select_option("13101")
    page.wait_for_timeout(500)

    page.locator("select").nth(0).select_option("")
    page.wait_for_timeout(500)

    # Click one of the map markers to open sidebar
    print("Clicking marker on map...")
    # This just clicks the middle of the map where points generally are.
    page.mouse.click(500, 400)
    page.wait_for_timeout(1000)

    # Move to Campaigns Viewer
    print("Navigating to Campaigns Viewer...")
    page.get_by_text("Simulador").click()
    page.wait_for_timeout(1000)

    # Try selecting a campaign face
    page.locator('input[type="checkbox"]').nth(1).check()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Simular Campaña").click()
    page.wait_for_timeout(1500)

    # Take screenshot at the key moment (Campaign results)
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()

    print("Video file:", glob.glob("/home/jules/verification/videos/*.webm"))
