import random

from generator.generator import generated_person
from locators.webform_page_locators import WebFormPageLocators
from pages.base_page import BasePage


class WebFormPage(BasePage):
    locators = WebFormPageLocators()

    def fill_form(self):
        person_info = next(generated_person())
        # fill person info
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_info.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person_info.last_name)
        self.element_is_visible(self.locators.JOB_TITLE).send_keys(person_info.job_title)

        # select education
        education_list = self.elements_are_visible(self.locators.EDUCATION_LIST)
        education_list[random.randint(0, 2)].click()

        # select gender
        gender_list = self.elements_are_visible(self.locators.GENDER_LIST)
        gender_list[random.randint(0, 2)].click()

        # select experience
        self.element_is_visible(self.locators.EXPERIENCE_FIELD).click()
        experience_list = self.elements_are_visible(self.locators.EXPERIENCE_OPTION_LIST)
        experience_list[random.randint(1, 4)].click()

        # select date
        self.element_is_visible(self.locators.DATE).click()
        self.element_is_visible(self.locators.CURRENT_DATE).click()

        self.element_is_visible(self.locators.SUBMIT).click()

    def check_success_message(self):
        url = self.driver.current_url
        text_message = self.element_is_visible(self.locators.SUCCESS_MESSAGE).text
        assert url == 'https://formy-project.herokuapp.com/thanks', 'url is incorrect'
        assert text_message == 'The form was successfully submitted!', 'text message is incorrect'
