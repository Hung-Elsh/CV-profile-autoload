from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProfileAbstractModel(models.AbstractModel):
    _name = 'profile.abstract.model'
    _description = 'Profile Abstract Model'
    
    name = fields.Char(string='Employee Name')
    birthday = fields.Date(string='Date of birth')
    address = fields.Char(string='Address')
    education = fields.Char(string='Education')
    gender = fields.Char(string='Gender')
    experience = fields.Char(string='Experience')
    
    # @api.constrains('birthday')
    # def check_birthday(self):
    #     for record in self:
    #         if record.birthday == False:
    #             record.birthday = fields.Date.today()
    #         elif record.birthday >= fields.Date.today():
    #             raise ValidationError('Invalid date of birth')
            
class CvAutoloadModel(models.Model):
    _name = 'cv.autoload.model'
    _description = 'CV Autoload Model'
    _inherit = 'profile.abstract.model'
    
    certificate = fields.Text(string='Certificate')
    phone_number = fields.Char(string='Phone number')
    work_phone_number = fields.Char(string='Work Phone Number')
    work_email = fields.Char(string='Email')
    skills = fields.Text(string="Skills")


class ProfileAutoloadModel(models.Model):
    _name = 'profile.autoload.model'
    _description = 'Profile Autoload Model'
    _inherit = 'profile.abstract.model'
    
    place_of_birth = fields.Char(string='Place of birth')
    id_card_number = fields.Char(string='ID card number')
    
    id_card_provided_place = fields.Char(string='provided by')
    date_of_id_card = fields.Date(string='ID card Date')
    
    admission_date_of_young_union = fields.Date(string='Date')
    young_union_admissin_place = fields.Char(string='Place')
    admission_date_of_communist_union = fields.Date(string='Date')
    communist_union_admissin_place = fields.Char(string='Place')
    
    # @api.constrains('date_of_id_card')
    # def check_id_card_date(self):
    #     for record in self:
    #         if record.date_of_id_card.year - record.date_of_birth.year < 15:
    #             raise ValidationError('Invalid date of ID card')
            