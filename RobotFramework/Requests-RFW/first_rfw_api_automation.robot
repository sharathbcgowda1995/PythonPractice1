*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
#we should not keep the variables value in a " " double quotes
${base_url} =   https://api.numbers.plivodev.com/v1/Account/MAYJLIZGQ5MWVKZWM4NZ
${endpoint} =   /Number/
${user_name} =  MAYJLIZGQ5MWVKZWM4NZ
${password}  =  MjFkZjQ3MzhiODFlZmY4MjIyODk2NTgxOGVmMDdm

*** Test Cases ***
Retrieving all the user rented numbers.
    ${auth} =   create list  ${user_name}    ${password}
    create session   mysession  ${base_url}    auth=${auth}
    ${response} =    get request    mysession  ${endpoint}
    log to console   ${response.status_code}
    log to console   ${response.content}
    #log to console   ${response.header}