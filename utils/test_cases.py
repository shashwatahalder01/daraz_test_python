# -*- coding: utf8 -*- we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently we can obtain test cases from test management
#  tools, I used this for my previous project:
# http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx We can also record the result of test
# cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array


def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['test-1', 'In Main page, when user click "Login" link, user should see Login Page'],
    ['test-2', 'In Login page, when user click "Login" button, user should see Home page'],
    ['test-3', 'In Home page, when user click "search" button, user should see searched result'],
    ['test-4', 'In Home page, when user click a "product" button, user should see clicked product ppopup page'],
    ['test-5', 'In product ppopup page, when user click "Add To Cart" button, user should see Cart product popup page'],
    ['test-6', 'In Cart product popup page, when user click "Go TO cart" button, user should see Cart page'],
    
    ['test-1', 'In Main page, when user click "Affiliate" link, user should see Affiliate Page'],
    ['test-2', 'In Affiliate page, user should get Home Page link'],
    ['test-3', 'In Affiliate page, when user click "Help Center" link, user should see Help Center Page'],
    ['test-4', 'In Affiliate page, when user click "How To Buy" link, user should see How To Buy Page'],
    ['test-5', 'In Affiliate page, when user click "Return & Refunds" link, user should see Return & Refunds Page'],
    ['test-6', 'In Affiliate page, when user click "Contact US, user should see Contact US Page'],
   


]
