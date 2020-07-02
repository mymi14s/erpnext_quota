import frappe
import json
import os, datetime
import subprocess
from frappe.utils import cint
from frappe import _

# mydate = datetime.datetime.now()
# mydate.strftime("%B")


def subscription_task():
	cur_date = datetime.datetime.today().date()
	pm = frappe.get_doc('Payment Manager')
	cur_month = datetime.datetime.now().strftime("%B")
	cur_year = str(datetime.date.today()).split("-")[0]
	if((pm.subscription_type=="Monthly") and (str(pm.expire)==str(cur_date))):
		if (cur_month == pm.month) and (pm.paid=='Paid'):
			pass
		else:
			pm.paid = 'Not Paid'
			pm.switch = 'Freeze'
			pm.month = cur_month
			pm.year = cur_year

			pm.save()
	elif((pm.subscription_type=="Yearly") and (str(pm.expire)==str(cur_date))):
		if (cur_year == pm.year) and (pm.paid=='Paid'):
			pass
		else:
			pm.paid = 'Not Paid'
			pm.switch = 'Freeze'
			pm.month = cur_month
			pm.year = cur_year

			pm.save()
		