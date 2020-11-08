import json
import requests  # package used for API intractions
from behave import *  # package for behave test framework
from selenium import webdriver
import logging as logger
from selenium.webdriver.support.select import Select  # select class to handle elements with "select" tag


# Web UI testing
@given(u'I launch the browser: {browser_name}')
def launch_browser(context, browser_name):
    context.browser = browser_name
    if context.browser is not None:
        try:
            if context.browser == 'Google':
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-certificate-errors')
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                context.browser_access = webdriver.Chrome(
                    executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                    chrome_options=options)
                context.browser_access.implicitly_wait(5)
            elif context.browser == 'Firefox':
                context.browser_access = webdriver.Firefox(
                    executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe")
                context.browser_acess.implicitly_wait(5)
        except:
            print("Check the browser name {} or the webdriver exe is not in the valid path ".format(context.browser))


@when(u'The webpage: {} is reachable')
def webpage_reachability(context, webpage):
    webpage = webpage
    context.browser_access.get(webpage)
    page_check = context.browser_access.current_url
    assert webpage in page_check, (" the webpage : {} is not rechable".format(webpage))


@then(u'I query for used cars listing and its details')
def car_details_list(context):
    context.cars_query = Select(context.browser_access.find_element_by_xpath("//select[@id='SearchType']"))
    context.cars_query.select_by_visible_text("Cars, bikes & boats")
    context.browser_access.find_element_by_xpath('//*[@id="generalSearch"]/div[2]/button').click()
    context.browser_access.find_element_by_xpath(
        "//table[@id='Control_Table']/tbody/tr/td/ul/li/ul/li/a[@href='/motors/used-cars']").click()
    available_cars_list = context.browser_access.find_elements_by_xpath("//div[@id='motors']/ul/li/div/a")
    if len(available_cars_list) > 0:
        available_cars_list[0].click()  # The first entry from the listed car list is selected
        selected_car_details_keys = context.browser_access.find_elements_by_xpath('//div[@class="attributes-box '
                                                                                  'key-details-box"]/ul/li/div/label['
                                                                                  '@class="motors-attribute-label"]')
        selected_car_details_values = context.browser_access.find_elements_by_xpath('//div[@class="attributes-box '
                                                                                    'key-details-box"]/ul/li/div/span['
                                                                                    '@class="motors-attribute-value"]')
        context.car_details = {}
        for i in range(0, len(selected_car_details_keys)):
            key = selected_car_details_keys[i].text
            value = selected_car_details_values[i].text
            context.car_details[key] = value # stores the car details as key value pair
        logger.info("car details{}".format(context.car_details))
    # Checks if there is at least one used car listed
    assert (len(context.car_details)) > 0, "Sorry, there are currently no listings in this category"
    context.browser_access.quit()


@then(u'I check for: {information} information')
def kilometres_details(context, information):
    queried_information = information
    assert queried_information in context.car_details, (
        "Sorry, the {0} information is not available".format(queried_information))
    if queried_information in context.car_details:  # stores the value for queried car's detail
        context.car_details.get(queried_information)

# API Testing

@given(u'I send get request to TradeME for Charity list')
def validate_request(context):
    api_locator = 'https://api.trademe.co.nz/v1/Charities.json'
    context.retvals = requests.get(api_locator)  # quering api end point
    context.return_status_code = context.retvals.status_code  # retrive status code form respose


@when(u'The response is: {status_code}')  #
def validate_status_code(context, status_code):
    status_code = int(status_code)
    # validating the expected and retrived status code
    assert status_code == context.return_status_code, (
        "The status code from webisite is {}".format(context.return_status_code))


@then(u'I check for: {charity_name} charity in the charity list')
def check_charity_entry(context, charity_name):
    charity_name = charity_name
    charity_list = json.loads(context.retvals.text)  # converting the response content into Unicode
    charities = []
    for i in range(0, len(charity_list)):
        context.retval = charity_list[i]
        charities.append(
            context.retval.get("Description"))  # parsing response to retrive charity names and appending it to list
    # check if the given charity name is in the created charity list
    assert charity_name in charities, ("{} is not in the charity list {}".format(charity_name, charities))