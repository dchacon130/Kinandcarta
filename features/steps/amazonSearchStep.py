from behave import *
from pages.amazonPage import *

use_step_matcher("parse")

@given(u'the user navigates to "www.Amazon.com"')
def step_impl(context):
    AmazonPage.insert_text_to_search_bar(context)
    raise NotImplementedError(u'STEP: Given the user navigates to "<WebSite>"')


@given(u'Searches for "{SearchBy}"')
def step_impl(context, SearchBy):
    AmazonPage.insert_text_to_search_bar(context, SearchBy)
    AmazonPage.click_button_search(context)
    raise NotImplementedError(u'STEP: Given Searches for "<SearchBy>"')


@given(u'navigates to the second page')
def step_impl(context):
    AmazonPage.click_on_the_page_number()
    raise NotImplementedError(u'STEP: Given navigates to the second page')


@given(u'selects the third "<3>" item')
def step_impl(context):    
    AmazonPage.select_the_product()
    raise NotImplementedError(u'STEP: Given selects the third "<3>" item')


@then(u'assert that the item would be available for purchase')
def step_impl(context):
    AmazonPage.add_cart_button_exist()
    raise NotImplementedError(u'STEP: Then assert that the item would be available for purchase')
