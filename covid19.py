from covid import Covid
#import fcntl  #this module is not available for windows
covid = Covid()
cases = covid.get_status_by_country_name("us")
for x in cases:
    print(x,":",cases[x])