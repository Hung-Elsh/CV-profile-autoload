from odoo import models, fields, api
from ..helper import tesseract_helper, data_finder
from odoo.exceptions import ValidationError
import base64


class CVProfileAutoloadWizardModel(models.TransientModel):
    _name = 'cv.profile.autoload.wizard.model'
    _description = 'CV-Profile Autoload Wizard Model'
    
    profile_capture = fields.Image(string='Profile', attachment=False)
    cv_pdf = fields.Binary(string='CV pdf file', attachment=False)
    read_data = fields.Text(string='Read Data', readonly=True , compute='_read_picture_data' , store=True)
    model_type = fields.Selection(string='Dạng văn bản', selection=[('sơ yếu lý lịch', 'Sơ Yếu Lý Lịch'),
                                            ('cv cá nhân', 'CV Cá Nhân'), ],
                                      default='sơ yếu lý lịch')
    
    @api.constrains('profile_capture', 'cv_pdf')
    def _check_data_in(self):
        for record in self:
            if record.profile_capture and record.cv_pdf:
                raise ValidationError('Chỉ nhập 1 dạng file đầu vào')

    @api.depends('profile_capture', 'cv_pdf')
    def _read_picture_data(self):
        for record in self:
            if record.profile_capture:
                record.read_data = record.read_b64data(record.profile_capture, False)
                finder = data_finder.DataFinder(record.read_data)
                finder.write_data_dictionary(True)
                record.model_type = 'sơ yếu lý lịch'
            if record.cv_pdf:
                record.read_data = record.read_b64data(record.cv_pdf, True)
                finder = data_finder.DataFinder(record.read_data)
                finder.write_data_dictionary(False)
                record.model_type = 'cv cá nhân'
                
    @api.model
    def create(self, vals):
        result = super(CVProfileAutoloadWizardModel, self).create(vals)
        if result.profile_capture:
            result.read_data = result.read_b64data(result.profile_capture, False)
            finder = data_finder.DataFinder(result.read_data)
            finder.write_data_dictionary(True)
            val = finder.data_dictionary 
            self.env['profile.autoload.model'].create(val)
            return result
        if result.cv_pdf:
            result.read_data = result.read_b64data(result.cv_pdf, True)
            finder = data_finder.DataFinder(result.read_data)
            finder.write_data_dictionary(False)
            val = finder.data_dictionary 
            self.env['cv.autoload.model'].create(val)
            return result
            
    def read_b64data(self, b64data, is_pdf):
        b64string_data = base64.decodebytes(b64data)
        tesseract_reader = tesseract_helper.TesseractHeplperPDFScan(b64string_data)
        if is_pdf:
            tesseract_reader.Scann_pdf()
            return tesseract_reader.extracted_information
        else:
            tesseract_reader.Scann_image()
            return tesseract_reader.extracted_information
