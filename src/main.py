from currency_api import CurrencyApi

obj_current_api = CurrencyApi('dea67470959faa0bad84') #criação do objeto

response_all_currencies = obj_current_api.get_all_currencies()

converted_dict = {'BRL': 1}
count = 0
for i in response_all_currencies['results']:

    current_coin = response_all_currencies['results'][i]
    if 'id' in current_coin:
        currency_coin = current_coin['id']
    
        response_convert_real = obj_current_api.convert_real(currency_coin)

        key = list(response_convert_real.keys())[0]
        currency_converted = key.split('_')[1]

        converted_dict[currency_converted] = response_convert_real[key]

    count+=1
    if count == 2:
        break

print(converted_dict)