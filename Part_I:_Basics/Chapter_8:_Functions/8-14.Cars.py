def cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_information = cars('subaru', 'outback', color='blue', tow_packae=True)
print(car_information)

