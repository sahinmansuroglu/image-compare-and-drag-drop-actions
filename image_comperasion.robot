*** Settings ***
Library           SeleniumLibrary
Library           Test1.py
*** Variables ***

${SELECT_BUTTON}        xpath=//a[@title='Add more images']
${TRANSFORM_BUTTON}     xpath=(//button)[4]
${ROTATE_BUTTON}        xpath=(//button[@class='rotate-button button-with-image small'])[1]
${CLOSE_BUTTON}         xpath=//span[text()='Close']
${CANSEL_BUTTON}         xpath=//span[text()='Cancel']
${APPLY_BUTTON}         xpath=//span[text()='Apply']
${IMG}                  xpath=//canvas[@class='upper-canvas ']

*** Test Cases ***

Aç Web Sitesi-2
    Delete Image Files in directory    ${OUTPUTDIR}/images/
    Select File
    Sleep    10
    Save Img To File    filebefore.png
    Rotate
    Sleep    10
    Save Img To File    fileafter.png
    Log To Console    Ali
    Log To Console    ${CURDIR}
   ${deger1}=     Compare Images By finding Edge    ${OUTPUTDIR}\\images\\filebefore.png    ${OUTPUTDIR}\\images\\fileafter.png
#   ${deger2}=     Compare Images By Rotateting First Image    ${OUTPUTDIR}\\images\\fileafter.png    ${OUTPUTDIR}\\images\\fileafter.png
    Log To Console    ${deger1}
#    Log To Console    ${deger2}
    Close Browser


*** Keywords ***
Select File
     Open Browser    https://www.iloveimg.com/photo-editor    chrome
     Maximize Browser Window

     Choose File    //input[@id='fileUpload']       E:/KODLAMA_ILE_ILGILI/Python/RobotFrameWork/robot framework image comperasion/proj1/img/img.png
     Sleep    2
Rotate
    Click Element    ${TRANSFORM_BUTTON}
     Sleep    1
    Click Element    ${ROTATE_BUTTON}
     Sleep    1
    Click Element   ${APPLY_BUTTON}
     Sleep    1

Save Img To File
    [Arguments]     ${filename}
    Log To Console    ${OUTPUTDIR}\\images\\${filename}
    Capture Element Screenshot  ${IMG}        ${OUTPUTDIR}\\images\\${filename}