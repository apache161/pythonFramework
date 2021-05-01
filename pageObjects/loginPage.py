class loginPage:
    textbox_usrname_id = "Email"
    textbox_passwd_id = "Password"
    button_login_xpath ="//button[@type='submit']"
    button_logout_linktext = "Logout"


    def __init__(self, driver):
        self.driver = driver

    def Usrname(self,usrname):
        self.driver.find_element_by_id(self.textbox_usrname_id).clear()
        self.driver.find_element_by_id(self.textbox_usrname_id).send_keys(usrname)

    def Password(self, passwd):
        self.driver.find_element_by_id(self.textbox_passwd_id).clear()
        self.driver.find_element_by_id(self.textbox_passwd_id).send_keys(passwd)

    def Login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def Logout(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()


