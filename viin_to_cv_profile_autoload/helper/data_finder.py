from datetime import date


class DataFinder():

    def __init__(self, string_text):
        self.data = str(string_text).lower()
        self.data_dictionary = {}
        self.keyls_profile = ['name', 'address', 'education', 'gender', 'experience',
                      'place_of_birth', 'id_card_number' , 'id_card_provided_place' ,
                      'young_union_admissin_place' , 'communist_union_admissin_place']
        
        self.keyls_cv = ['name', 'address', 'education', 'gender', 'experience',
                         'certificate', 'phone_number' , 'work_phone_number', 'work_email', 'skills']
        
        self.keytime = ['birthday', 'date_of_id_card', 'admission_date_of_young_union', 'admission_date_of_communist_union']

    def __searchkey(self, string):
        index = self.data.find(string)
        if index != -1:
            last_index = index + len(string)
            key = self.data[index:last_index]
            return index, key
        else:
            return index, None
    
    def __searchval(self, key):
        index, f_key = self.__searchkey(key)
        if f_key != None:
            index_val = self.data.find('\n', index)
            val = self.data[(index + len(key)):index_val]
            self.data = self.data.replace(f_key, '@', 1)
            return val
        else:
            return None

    def __searchingdatetime(self, key):
        date_day, date_month, date_year = 1, 1, 1970
        index, f_key = self.__searchkey(key)
        if f_key != None:
            index_val = self.data.find('\n', index)
            val = self.data[index:index_val]
            iday = val.rfind('tháng')
            if iday != -1:
                try:
                    date_day = int(val[0:iday]) 
                    val.replace(date_day, '', 1)
                    val.replace('tháng', '*')
                except ValueError:
                    pass
            imonth = val.rfind('năm')
            if imonth != -1:
                try:
                    date_month = int(val[0:imonth])
                    date_year = int(val[imonth:len(val)]) 
                    val.replace(date_month, '', 1)
                    val.replace('năm', '*')
                    val.replace(date_year, '', 1)
                except ValueError:
                    pass
        try:
            fdate = date.fromisoformat("%s-%s-%s" % (str(date_year), str(date_month), str(date_day)))
        except (TypeError, ValueError):
            if date_day < 10:
                date_day = '0%s' % (str(date_day))
            if date_month < 10:
                date_month = '0%s' % (str(date_month))

            fdate = date.fromisoformat("%s-%s-%s" % (str(date_year), date_month, date_day))
        else:
            fdate = date.fromisoformat("1970-01-01")
        return fdate
        
    def write_data_dictionary(self, is_profile):
        searching_key = {'name': ('họ và tên',),
                        'address': ('nơi đăng ký hộ khẩu thường trú hiện nay', 'chỗ ở hiện nay', 'địa chỉ thường trú', 'thường trú', 'địa chỉ'),
                        'education': ('trình độ văn hóa', 'học vấn'),
                        'gender': ('nam, nữ', 'giới tính'),
                        'experience':('nghề nghiệp hoặc trình độ chuyên môn', 'kinh nghiệm làm việc'),
                        'certificate': ('chứng chỉ',),
                        'phone_number': ('điện thoại liên hệ', 'điện thoại'),
                        'work_phone_number': ('điện thoại',),
                        'work_email': ('email',),
                        'skills': ('kỹ năng',),
                        'place_of_birth': ('nguyên quán', 'nơi sinh'),
                        'id_card_number': ('chứng minh thư nhân dân số', 'căn cước công dân số'),
                        'id_card_provided_place':('nới cấp',),
                        'young_union_admissin_place': ('nơi kết nạp', 'tại'),
                        'communist_union_admissin_place':('nơi kết nạp', 'tại')
                        }

        searching_datetime_key = {'birthday': ('sinh ngày', 'ngày sinh', 'năm sinh', 'ngày', 'tháng', 'năm'),
                                  'date_of_id_card':('ngày cấp', 'cấp ngày'),
                                  'admission_date_of_young_union': ('kết nạp đoàn thanh niên cộng sản hồ chí minh ngày',
                                                                     'ngày vào đoàn thanh niên'),
                                  'admission_date_of_communist_union': ('kết nạp đảng cộng sản việt nam ngày',
                                                                         'ngày vào đảng cộng sản'), }
        
        if is_profile:
            for i in self.keyls_profile:
                for key in searching_key[i]:
                    value = self.__searchval(key)
                    if value != None:
                        self.data_dictionary.update({'%s' % (i):'%s' % (value)})
            for i in self.keytime:
                for key in searching_datetime_key[i]:
                    fdate = self.__searchingdatetime(key)
                    self.data_dictionary.update({'%s' % (i):fdate})
                
            if len(self.data_dictionary) <= len(self.keyls_profile):
                return False
            else:
                return True
        else:
            for i in self.keyls_cv:
                for key in searching_key[i]:
                    value = self.__searchval(key)
                    if value != None:
                        self.data_dictionary.update({'%s' % (i):'%s' % (value)})
            for key in searching_datetime_key['birthday']:
                fdate = self.__searchingdatetime(key)
                self.data_dictionary.update({'birthday':fdate})
            if len(self.data_dictionary) <= len(self.keyls_cv):
                return False
            else:
                return True
