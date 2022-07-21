from behave import *
from pages.amazonPage import *

use_step_matcher("parse")

@given(u'the user navigates to "<WebSite>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user navigates to "<WebSite>"')


@given(u'Searches for "<SearchBy>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Searches for "<SearchBy>"')


@given(u'navigates to the second page')
    raise NotImplementedError(u'STEP: Given navigates to the second page')


@given(u'selects the third "<3>" item')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given selects the third "<3>" item')


@then(u'assert that the item would be available for purchase')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then assert that the item would be available for purchase')
