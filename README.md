# El-Menus technical task
Automate E2E scenario on elmenus.com 

### Description
Applying POM design pattern for making an order from MacDonald's restaurant while creating new account and setting up user location and address to complete the order.
### Note:
This project implemented and tested on the following specs

1- Ubuntu 20.4

2- python3 

3- behave framework

4- selenium webdriver

5- allure report

6- Chrome webdriver

7- Firefox geckodriver

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages in the requirements.txt.
```bash
pip3 install -r requirements.txt
```

### Usage
Clone the repo or download as zip. This project can be run on Chrome, Firefox, Safari, Internet Explorer, Opera, and PhantomJs. It tested using Chrome and Firefox browsers, However to run the suite on different browsers you need to install their drivers frist.

```shell
# CHANGE YOUR DIRECTORY TO REPOSITORY PARENT DIRECTORY
cd elmenus

# RUN WITH DEFAULT WEB BROWSER (Chrome)
behave

# USING DIFFERENT WEB BROWSER
behave -D BROWSER=firefox

# TO RUN ALL FEATURES USING ALLURE REPORTS
behave -f allure_behave.formatter:AllureFormatter -o reports/

# TO RUN A SINGLE FEATURE FILE
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/test_scenarios/sign_up.feature

# VIEW TEST REPORTS
allure serve reports/
```

