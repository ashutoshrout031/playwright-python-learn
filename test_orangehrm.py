from playwright.sync_api import Page, expect

# 1. Test Case: Validate URL is NOT the actual URL
def test_url_notreal(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    expect(page).not_to_have_url("https://opensource-demo.orangehrmlive.com/")
    print("TC1 Passed")

# 2. Test Case: Validate URL redirected to actual page
def test_url_is_real(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("TC2 Passed")

# 3. Test Case: Validate title IS OrangeHRM
def test_title_is_correct(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    expect(page).to_have_title("OrangeHRM")
    print("TC3 Passed")

# 4. Test Case: Validate title is NOT Orange HRM
def test_title_is_notcorrect(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    expect(page).not_to_have_title("Orange HRM")
    print("TC4 Passed")

