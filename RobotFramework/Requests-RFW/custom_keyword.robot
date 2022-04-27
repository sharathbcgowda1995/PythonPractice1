*** Settings ***
Library     RequestsLibrary
Library     Collections
Library     ../Requests-RFW/CustomLibraries/customKeywords.py

*** Variables ***

${base_url} =   https://api.numbers.plivodev.com/v1/Account/MAYJLIZGQ5MWVKZWM4NZ/Number/
${endpoint} =   /Number/
${username} =   MAYJLIZGQ5MWVKZWM4NZ
${password} =   MjFkZjQ3MzhiODFlZmY4MjIyODk2NTgxOGVmMDdm
${status_code} =    200

*** Test Cases ***
Retrieving all the user rented numbers.
    ${response}     Create session with the basic authentication        ${base_url}     ${username}     ${password}
    Set Global Variable    ${response}
    log to console      ${response.status_code}
    Call the get API to fetch all the rented numbers
    validate the response with the expected status code         ${status_code}
    #Log the response of the GET api

#Get the specific number details.
    #Create session with the basic authentication        ${base_url}     ${username}     ${password}
    #Call the get API with with specific number


#*** Keywords ***
#Log the response of the GET api
    #log to console      ${response.status_code}