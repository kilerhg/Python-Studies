def convert_float_from_str(value):
    value = str(value).strip() #.replace('-','0')
    if value == '-':
        value = str(value).replace('-','0')
    elif value != '' and value != 'nan' and value != None:
        
        if not ',' in value:
            return float(value)
        else:
            return float(value.replace('.','').replace(',','.'))
    else:
        return float(0)


def convert_int_from_str(value):
    value = str(value).strip() # .replace(',','.')
    if value == '-':
        value = int(str(value).replace('-','0'))
    elif value != '' and value != 'nan' and not None:
        if not ',' in value:
            if '.' in value:
                value = int(value[:value.find('.')])
            else:
                value = int(value)
        else:
            value = int(value[:value.replace(',', '.').find('.')])
    else:
        value = int(0)
    return value


if __name__ == '__main__':
    print(convert_int_from_str(''))