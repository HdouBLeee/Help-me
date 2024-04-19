# noinspection PyUnresolvedReferences
from odoo import api, fields, models

class PlayerInformation(models.Model):
    _name = 'player.information'
    _description = 'Player Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Datetime(string='Day_of_birth', required=True)
    gender = fields.Selection([('male', 'Male'), ('female','Female')], default='male', string='Gender')
    club = fields.Char(string='Basketball Team')
    country = fields.Char(string='Nationality', required=True)
    image = fields.Binary(string='Image', attachment=True)
    position = fields.Char(string='Position')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')



