# city, country: write a function that accepts 2 parameters: a city name and a country name. The function should
# return a single string of the form City, Country; store the function in a module called city_functions.
# Create a file test_cities that tests the function you just wrote. Write a method called test_city_country to verify
# that calling your function results in the correct string.

def city_country(city_name, country_name, population=''):
    if population:
        formatted_city_country = f'{city_name}, {country_name} - population: {population}'
    else:
        formatted_city_country = f'{city_name}, {country_name}'
    return formatted_city_country.title()


# population: modify your function so it requires a third parameter, population. It should now return a single string of
# the form City, Country - population. Run test_cities again and make sure it fails this time.
# modify the function so the population parameter is optional. run test_cities again and make sure it passes again.
# write a second test called test_city_country_population that verifies you can call your function with the values
# 'santiago', 'chile', 5000000. run test_cities again and make sure this new test passes.
