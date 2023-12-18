from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"

    name = fields.Char(string="Name", required=True)
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tags")
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availabitity = fields.Date(string="Date")
    expected_price = fields.Float(string="Expected_price")
    selling_price = fields.Float(string="Selling Price")
    best_price = fields.Float(string="Best Price")
    badrooms = fields.Integer(string="Badrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garden = fields.Boolean(string="Garden", default=False)
    garage = fields.Boolean(string="Garage", default=False)
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')], string="Garden Orientation", default='north')

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    name = fields.Char(string="name", required=True)

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"

    name = fields.Char(string="name", required=True)