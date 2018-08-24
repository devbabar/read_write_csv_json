import csv
import time
import json
import string
from prettytable import PrettyTable
start_time = time.time()


def check_location(file_name, city_name):
    with open(file_name) as f:
        csv_data = csv.reader(f)

        all_locations = []
        sorted_loc = []

        ''' map(string.strip, i) to remove any whitespaces from location'''
        for i in csv_data:
            all_locations.append(i)
            i = map(string.strip, i)
            sorted_loc.append(i[1])

        sorted_loc = set(sorted_loc)

        if city_name in sorted_loc:
            return all_locations


def read_and_write(result):
    count = 0
    price_per_sqft = []
    row_counter = 0
    my_list = []
    price = []

    ''' map(string.strip, i) to remove any whitespaces from location'''
    for i in result:
        i = map(string.strip, i)
        row_counter += 1

        if i[1] == city_name:
            price.append(float(i[2]))
            price_per_sqft.append(float(i[6]))
            count += 1
            my_list.append(i)

    max_price = max(price)
    min_price = min(price)
    avg_price = sum(price)/count
    avg_price_per_sqft = sum(price_per_sqft)/count

    header = ["MLS",
              "Location",
              "Price",
              "Bedrooms",
              "Bathrooms",
              "Size",
              "Price/SQ.Ft",
              "Status"]

    # Get output as csv file
    with open(city_name + '.csv', 'w') as file_out:
        wrt = csv.writer(file_out)
        wrt.writerow(header)
        wrt.writerows(my_list)

    # Get output as json file, user mls# as object id and label each field.
    res = {}
    for MLS, Location, Price, Bedrooms, Bathrooms, Size, price_sqft, Status in my_list:
        res[MLS] = dict(mls=MLS, label={
            "location": Location,
            "price": Price,
            "bedrooms": Bedrooms,
            "bathrooms": Bathrooms,
            "size": Size,
            "price/sqft": price_sqft,
            "status": Status})

    with open(city_name + '.json', 'w') as json_out:
        json.dump(res, json_out)

    table = PrettyTable([
        "MLS",
        "Location",
        "Price",
        "Bedrooms",
        "Bathrooms",
        "Size",
        "Price/SQ.Ft",
        "Status"])

    for l in my_list:
        table.add_row([l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]])
    print table

    print "--------------------------------------------------------"
    print "Total number of properties are : {}".format(count)
    print "Most expensive property $ {}".format(max_price)
    print "Least expensive property $ {}".format(min_price)
    print "Average property price $ {}".format(avg_price)
    print "Average property price per sq/ft $ {}".format(avg_price_per_sqft)
    print "--------------------------------------------------------"

    end_time = time.time()
    print ("Total time to execute {} rows was : {} seconds ".format(row_counter, (end_time - start_time)))
    return {
        "max_price": max_price,
        "min_price": min_price,
        "avg_price": avg_price,
        "avg_price_per_sqft": avg_price_per_sqft}

''' This will keep asking for location till matching location is being found '''
while True:
    city_name = raw_input("\nEnter Location: ").title()
    result = check_location(file_name='RealEstate.csv', city_name=city_name)
    if result is not None:
        read_and_write(result)
        break
    else:
        print "Sorry, No location found, Try again.\n"
