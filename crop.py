class Crop:
    def __init__(self,first_crop,second_crop):
        self.first_crop = first_crop
        self.second_crop = second_crop
        if second_crop == '':
            self.type = 'Simple'
        else:
            self.type = 'Double'

    def get_type(self):
        return self.type

    def get_crop_end(self):
        if self.type == 'Simple':
            return self.first_crop
        else:
            return self.second_crop

    def get_string(self):
        crop_name = self.first_crop
        if self.type == 'Double':
            crop_name = crop_name + ' ' + self.second_crop
        return crop_name

    def get_crop_list(self):
        crop_list = []
        crop_list.append(self.first_crop) 
        if self.type == 'Double':
            crop_list.append(self.second_crop) 
        return crop_list

    def __eq__(self, other):
        if isinstance(other, Crop):
            if self.first_crop == other.first_crop and self.type == other.type:
                if self.type == 'Simple':
                    return True
                if self.type == 'Double' and self.second_crop == other.second_crop:
                    return True
        return False


    def __ne__(self, other):
        return not self.__eq__(other)   



    #def get_first_crop(self):
    #    return self.first_crop

    #def get_second_crop(self):
    #    return self.second_crop