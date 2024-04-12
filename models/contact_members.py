from odoo import fields, models


class ContactMember(models.Model):
    _name = "contact.member"
    _description = "Contact Member"

    first_name = fields.Char("First name", required=True, size=225)
    last_name = fields.Char("Last name", required=True, size=225)
    job_title = fields.Char("Job title", size=225)
    company_name = fields.Char("Company name", size=225)
    email = fields.Char("Email", required=True, size=225)
    phone_number = fields.Char("Phone number", required=True, size=225)
    address = fields.Char("Address", size=225)
    city = fields.Char("City", size=225)
    state = fields.Char("State", size=225)
    postal_code = fields.Char("Postal code", size=225)
    country = fields.Char("Country", size=225)
    interest = fields.Char("Interest", size=225)
    membership_category = fields.Char("Membership category", size=225)
    stamp_date = fields.Date("Stamp date")
    transaction_id = fields.Char("Transaction ID", size=225)
    amount = fields.Float("Amount")
    code = fields.Char("Code", size=225)
