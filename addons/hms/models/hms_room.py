from email.policy import default

from odoo import fields, models, api

class Room(models.Model):
    _name = 'hms.rooms'           # Technical name of the model
    _description = 'Room'         # Description shown in the UI

    name = fields.Char(
        string="Room Number",     # Label shown in the form view
        required=True             # Field must be filled
    )
    hotel_id = fields.Many2one(comodel_name='hms.hotels', string="Hotel")
    type_id =  fields.Selection(
        [
            ('normal', 'Normal'),
            ('vip', 'VIP'),
            ('vvip', 'VVIP')
        ],default='normal'
    )