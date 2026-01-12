#Script using REST API to retrieve personal account, tariff  and consumption detals on Octupus Energy Website
import requests
import pandas as pd
import json
import sys
######################### Function Definitions #######################################################
def energy_json(url,api):
        r = requests.get(url,auth=(api,''))
        output_dict = r.json()
        json_info = json.dumps(output_dict, indent=3)
        return json_info#returns in json format
def energy_dict(url,api):
        r = requests.get(url,auth=(api,''))
        output_dict = r.json()
        return output_dict#returns in a dictionary format
################################# Electric & Gas Credentials ############################################
mpan_electric = '<electric mpan id>'#Type in your mpan number as derived from 'acct_info option
mprn_gas ='<gas mprn id>'#Type in your mprn number as derived from 'acct_info option



serial_electric = '<electric serial id>'#Type in your electric serial number as derived from 'acct_info option
serial_gas ='<gas serial id>'#Type in your gas serial number as derived from 'acct_info option


period_from = 'period_from=2026-01-01T00:00Z'#Type in the 'from' period. Note put a date at least 2 days prior to the current date
period_to = 'period_to=2026-01-07T23:59Z'#Type in the 'to' period. Note put a date at least 2 days prior to the current date

############################# Meter & Serial lists  ###################################################
mpan = [mpan_electric,mprn_gas]
serial = [serial_electric,serial_gas]

meter_type = ['electricity-meter-points','gas-meter-points']


url1 = f"https://api.octopus.energy/v1/{meter_type[0]}/{mpan[0]}/meters/{serial[0]}/consumption/?{period_from}&{period_to}"
url2 = f"https://api.octopus.energy/v1/{meter_type[1]}/{mpan[1]}/meters/{serial[1]}/consumption/?{period_from}&{period_to}"
api_key = "sk_live_<24 characters>"#Go onto the Octupus website under ure account to obtain your API key. Note this is personal and must not be shared
acct_info = "https://api.octopus.energy/v1/accounts/<account_number>/"#Type in your account number as derived from 'acct_info option

url_input = [url1,url2,acct_info]# A list showing the different options

try:
    url_number = int(input('Enter \'0\' for electric: \nEnter \'1\' for gas: \nEnter \'2\' for account information: '))
    if url_number not in [0,1,2]:
         sys.exit('You have entered a number outside the permitted range. Please try again using either 0,1 or 2')

    file_output_json=energy_json(url_input[url_number],api_key)
except ValueError:
     sys.exit('You have entered a wrong character type. Please enter an integer 0,1 or 2')


print(file_output_json)# Out put of the json file
################################### This creates a DataFrame to hold the out put of the Json file ################################
if url_number in [0,1]:
    octupus_energy=energy_dict(url_input[url_number],api_key)
    length_list=len(octupus_energy['results'])
    
    df = pd.DataFrame(octupus_energy['results'],index=[x for x in range(1,length_list+1)])
    df['interval_start'] = df['interval_start'].str.replace('T','  ',regex=False)#In the interval_start column put a space between the date and time 
    df['interval_end'] = df['interval_end'].str.replace('T','  ',regex=False)#In the interval_end column put a space between the date and time 
    
    print(df)
    
    print('\n'+'*'*30+' The Output Format to Import into a CSV Format '+'*'*30) 
    #df.to_csv(f'<filename_{url_number}.txt',index=False)#Convert the DataFrame into a csv file

#with open('<filename>.txt','w') as  file:
   #file.write(str(file_output_json))
