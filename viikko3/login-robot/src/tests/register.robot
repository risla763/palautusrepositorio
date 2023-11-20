*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  omenaaa12
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exists


Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  öööö  kalle123
    Output Should Contain  Username is Invalid

Register With Valid Username And Too Short Password
    Input Credentials  koira  ooo
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  koira  oooooooo
    Output Should Contain  Password is cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123