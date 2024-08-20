from Credentials.credentials import credentials_array
from Browser.browser import browser_class

PAGE_LINK = "http://sipare.imss.gob.mx/sipare_webapp/index.jsp"
WAIT_TIME = 3

def main():

    browser = browser_class()
    browser.start_web_browser(PAGE_LINK)

    for credential in credentials_array:

        # L O G I N  P A R T

        element = browser.wait_for_id("login", WAIT_TIME)
        if element == -1:
            raise Exception("Login element not found")  # Or handle the error gracefully

        browser.copy_paste(credential['user'])  # Now that we know it is selected, write credential

        element = browser.wait_for_id("password", WAIT_TIME - 1)
        if element == -1:
            raise Exception("Password element not found")  # Or handle the error gracefully

        browser.copy_paste(credential['password'])  # Now that we know it is selected, write credential

        browser.keyboard("Tab Enter", WAIT_TIME - 2)


        # L A N D  O F  L I N E A  D E  C A P T U R A

        element = browser.wait_for_id("menu", WAIT_TIME)
        if element == -1:
            raise Exception("Menu element not found")  # Or handle the error gracefully
        
        browser.keyboard("Tab Tab Tab Tab Tab Tab Enter", WAIT_TIME - 2)



    x = input("Press enter to terminate")


main()