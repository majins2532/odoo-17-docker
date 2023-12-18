from odoo import fields, models

class SavingOrder(models.Model):
    _name = "saving.order"
    _inherit = ['mail.thread']
    _description = "Saving order recrod data Main for Gold"
    _order = "sequence"

    number = fields.Char('Number', required=True, translate=True)
    date = fields.Date("Date", required=True, states={'draft': [('readonly', False)]}, default=fields.Date.context_today)
    customer_id = fields.Many2one("res.panter", string="", required=True)
    #shop_id = fields.Many2One("pos.shop","Shop",required=True,readonly=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('opened','Opened'),
        ('waiting_close','Waiting Close'),
        ('closed','Closed'),
        ('void','void')], string="Status", required=True, copy=False, tracking=True, default="draft")
    date = fields.Date("Date", required=True, readonly=True)
    id_card_front = fields.Image(string="ID Card Front", attachment=True, copy=False, max_width=1024, max_heigth=1024)
    id_card_back = fields.Image(string="ID Card Back", attachment=True, copy=False, max_width=1024, max_heigth=1024)
    picture = fields.Image(string="Picture", attachment=True, copy=False, max_width=1024, max_heigth=1024)