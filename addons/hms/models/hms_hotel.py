from odoo import fields, models, api


class HMSHotel(models.Model):
    _name = 'hms.hotels'
    _description = 'Hotel'

    name = fields.Char(required=True)
    room_ids = fields.One2many(
        comodel_name='hms.rooms',
        inverse_name='hotel_id')