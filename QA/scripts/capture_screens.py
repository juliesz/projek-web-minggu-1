import os
import sys
import time
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:8000"
OUTPUT_DIR = os.path.abspath(r"D:\laragon\www\projek-web-minggu-1-copy\QA\screenshots")

def capture():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 1. Public Pages
        print("--- Capturing Public Pages ---")
        context = browser.new_context(viewport={"width": 1366, "height": 768})
        page = context.new_page()

        public_pages = [
            ("/", "PAGE_PUB_01_HOME.png"),
            ("/login", "PAGE_PUB_02_LOGIN.png"),
            ("/register", "PAGE_PUB_03_REGISTER.png"),
            ("/forgot-password", "PAGE_PUB_04_FORGOT_PASSWORD.png"),
            ("/checkout", "PAGE_PUB_05_CHECKOUT.png"),
            ("/orders/payment", "PAGE_PUB_06_PAYMENT.png"),
            ("/pesanan-saya", "PAGE_PUB_07_MY_ORDERS.png"),
        ]

        for path, filename in public_pages:
            url = BASE_URL + path
            try:
                page.goto(url, wait_until="networkidle", timeout=15000)
                time.sleep(1)
                filepath = os.path.join(OUTPUT_DIR, filename)
                page.screenshot(path=filepath, full_page=True)
                print(f"[OK] {filename} saved")
            except Exception as e:
                print(f"[FAIL] {filename}: {e}")
        context.close()

        # 2. Kasir Section
        print("--- Capturing Kasir Pages ---")
        kasir_context = browser.new_context(viewport={"width": 1366, "height": 768})
        kasir_page = kasir_context.new_page()
        try:
            kasir_page.goto(f"{BASE_URL}/login", wait_until="networkidle", timeout=15000)
            kasir_page.fill('#username', 'kasir')
            kasir_page.fill('#password', 'kasir123')
            kasir_page.click('button[type="submit"]')
            kasir_page.wait_for_timeout(2000)
            print("Kasir logged in, landing URL:", kasir_page.url)

            kasir_pages = [
                ("/kasir/dashboard", "PAGE_KAS_01_DASHBOARD.png"),
                ("/kasir/pesanan", "PAGE_KAS_02_PESANAN.png"),
                ("/kasir/riwayat", "PAGE_KAS_03_RIWAYAT.png"),
            ]
            for path, filename in kasir_pages:
                kasir_page.goto(BASE_URL + path, wait_until="networkidle", timeout=15000)
                time.sleep(1)
                filepath = os.path.join(OUTPUT_DIR, filename)
                kasir_page.screenshot(path=filepath, full_page=True)
                print(f"[OK] {filename} saved (size: {os.path.getsize(filepath)})")
        except Exception as e:
            print(f"[FAIL] Kasir session: {e}")
        finally:
            kasir_context.close()

        # 3. Admin Section
        print("--- Capturing Admin Pages ---")
        admin_context = browser.new_context(viewport={"width": 1366, "height": 768})
        admin_page = admin_context.new_page()
        try:
            admin_page.goto(f"{BASE_URL}/login", wait_until="networkidle", timeout=15000)
            admin_page.fill('#username', 'admin')
            admin_page.fill('#password', 'admin123')
            admin_page.click('button[type="submit"]')
            admin_page.wait_for_timeout(2000)
            print("Admin logged in, landing URL:", admin_page.url)

            admin_pages = [
                ("/admin/dashboard", "PAGE_ADM_01_DASHBOARD.png"),
                ("/admin/produk", "PAGE_ADM_02_PRODUK.png"),
                ("/admin/supplier", "PAGE_ADM_03_SUPPLIER.png"),
                ("/admin/pembelian", "PAGE_ADM_04_PEMBELIAN.png"),
                ("/admin/pengguna", "PAGE_ADM_05_PENGGUNA.png"),
                ("/admin/transaksi", "PAGE_ADM_06_TRANSAKSI.png"),
                ("/admin/laporan", "PAGE_ADM_07_LAPORAN.png"),
                ("/admin/password-request", "PAGE_ADM_08_PASSWORD_REQUEST.png"),
            ]
            for path, filename in admin_pages:
                admin_page.goto(BASE_URL + path, wait_until="networkidle", timeout=15000)
                time.sleep(1)
                filepath = os.path.join(OUTPUT_DIR, filename)
                admin_page.screenshot(path=filepath, full_page=True)
                print(f"[OK] {filename} saved (size: {os.path.getsize(filepath)})")
        except Exception as e:
            print(f"[FAIL] Admin session: {e}")
        finally:
            admin_context.close()

        browser.close()
        print("--- All Screenshots Captured Successfully ---")

if __name__ == "__main__":
    capture()
