import frappe
import json
import os
import subprocess
from frappe.utils import cint
from frappe import _


def on_session_creation(login_manager):
    """make feed"""
    if frappe.session['user'] != 'Guest':
        # log to timesheet
        pass


def boot_session(bootinfo):
    """make feed"""
    status = make_redirect()
    if status:
        frappe.local.flags.redirect_location = "subscription-expired"
        raise frappe.Redirect
    

def update_website_context(dictionary):
    # print('CONTEXT ACCESSED')
    status = make_redirect()
    if status:
        frappe.local.flags.redirect_location = "subscription-expired"
        raise frappe.Redirect
    



def check_payment(self, cdt):
    # print('PAYMENT CHECKED')
    status = make_redirect()
    if status:
        frappe.local.flags.redirect_location = "subscription-expired"
        raise frappe.Redirect




def make_redirect():
    # frappe.flags.redirect_location = "https://google.com"
    # raise frappe.Redirect
    try:
        if "subscription-expired" in str(frappe.local.request):
            return False
        if (frappe.session['user'] != 'Administrator' and frappe.session['user'] != 'Guest'):
            # print('WORKING FINE')
            # print(frappe.session)
            doc = frappe.get_doc('Payment Manager')
            # print(doc.switch, doc.paid, doc.month)
            if (doc.switch == "Freeze" and doc.paid == "Not Paid"):
                return True
            # frappe.local.flags.redirect_location = "https://google.com"
            # raise frappe.Redirect
        else:
            # print('doc not valid')
            return False
    except:
        return False

    # pass