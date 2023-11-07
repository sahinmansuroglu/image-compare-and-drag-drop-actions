*** Settings ***
Library           SeleniumLibrary
Library           Test1.py
*** Variables ***



*** Test Cases ***
Draw Sample
    Open Browser    https://www.autodraw.com/    chrome
    Click Element    //div[text()=' Start Drawing ']
    Sleep    3
    Sekil Ciz
    Sleep    3

*** Keywords ***
