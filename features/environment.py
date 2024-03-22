from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from support.logger import logger

from app.application import Application


#  Run Behave tests with Allure results
#  behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/main_page_ui.feature


# def browser_init(context):
#     """
#     Initialize the web driver for the tests.
#     :param context: Behave context
#     """

### BROWSERSTACK ###
def browser_init(context, scenario_name):
    """
        Initialize the web driver for the tests.
        :param context: Behave context
        :param scenario_name: Name of the scenario
        """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ## BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/17-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = ''
    bs_key = ''
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Edge',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    ### HEADLESS MODE ####
    # context.driver.set_window_size(1024, 768)

    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name) # print or logger
    logger.info(f"Started scenario: {scenario.name}")
    browser_init(context)


### BROWSERSTACK ###
def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step) # print or logger
    logger.info(f"Started step: {step}")


def after_step(context, step):
    if step.status == 'failed':
        # Screenshot:
        # context.driver.save_screenshot(f'step_failed_{step}.png')
        # print('\nStep failed: ', step) # print or logger
        logger.error(f"Step failed: {step}")


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
