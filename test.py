import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testFactorial(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_positive_title_name(self):
		driver = self.driver
		driver.get("localhost:6464")
		self.assertIn("Factorial", driver.title)

	def test_negative_title_name(self):
		driver = self.driver
		driver.get("localhost:6464")
		self.assertIn("Factoriall", driver.title)

	def test_positive_input_100(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("100")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_1000(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("1000")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_negative_number(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("-11")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_number_and_char(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("11a")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_char(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("aa")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_symbol(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("!@#$%^&")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_number_and_symbol(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("11!@")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_negative_input_char_and_symbol(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		# find the form element
		field = driver.find_element_by_id("number")
		submit = driver.find_element_by_id("getFactorial")
		
		# Fill the form with data
		field.send_keys("aa!@")
		# submitting the form
		submit.send_keys(Keys.RETURN)

	def test_positive_clicking_terms_and_conditions(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		driver.find_element_by_link_text("Terms and Conditions").click()
		assert "This is the terms and conditions document. We are not yet ready with it. Stay tuned!"

	def test_negative_clicking_terms_and_conditions(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		driver.find_element_by_link_text("Terms and Conditions").click()
		assert "This is the privacy document. We are not yet ready with it. Stay tuned!"

	def test_positive_clicking_privacy(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		driver.find_element_by_link_text("Privacy").click()
		assert "This is the privacy document. We are not yet ready with it. Stay tuned!"

	def test_negative_clicking_privacy(self):
		driver = self.driver
		# Opening the link we want to test
		driver.get("localhost:6464")

		driver.find_element_by_link_text("Privacy").click()
		assert "This is the terms and conditions document. We are not yet ready with it. Stay tuned!"

	def tearDown(self):		 
		self.driver.close()

if __name__ == "__main__": 
	unittest.main()