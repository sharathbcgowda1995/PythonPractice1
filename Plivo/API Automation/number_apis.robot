*** Settings ***
Documentation   Rent a number
Library         RequestLibrary

*** Variables ***
${base_url}     https://api.numbers.plivodev.com/v1/Account/MAYJLIZGQ5MWVKZWM4NZ/Number/

*** Test Cases ***
User will rent a number successfully from the inventory
    User will create the session    ${base_url}
    User will pass the



*** Keywords ***
open the web page for the validation
    create webdriver    Chrome
    Go To       ${base_url}
