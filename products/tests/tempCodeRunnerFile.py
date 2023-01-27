def test_search_bar(self):
        store = self.live_server_url + "/en/store"
        
        self.browser.get(store)
        
       
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_box"]')))
        print(self.browser)
        search_bar = self.browser.find_element(By.XPATH, '//*[@id="search_box"]')
        search_bar.send_keys(self.product_name)
        # time.sleep(500)
        self.assertEquals(search_bar.get_attribute("value"), self.product_name)