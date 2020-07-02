# -*- coding: utf-8 -*-
# Copyright (c) 2020, Havenir Solutions Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import datetime
from dateutil import relativedelta
from frappe.model.document import Document

class PaymentManager(Document):
	
	def before_save(self):
		if self.paid == 'Paid':
			self.switch = 'Unfreeze'

			# if((self.subscription_type=="Monthly") and (self.month!=datetime.datetime.now().strftime("%B"))):
			# 	# format date from data
			# 	format_str = '%Y-%m-%d' # The format
			# 	datetime_obj = datetime.datetime.strptime(self.expire, format_str)
			# 	self.expire = datetime_obj + relativedelta.relativedelta(months=1)

			# print('Unfreeze')
		else:
			self.switch = 'Freeze'
			# print('Freeze')

# import datetime
# from dateutil import relativedelta
# nextmonth = datetime.date.today() + relativedelta.relativedelta(months=1)