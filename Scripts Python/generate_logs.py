#!/usr/bin/python
#
# Generate log files                                                                                                                  
# Log will be of the format :                                                                                                         
# date : (SUCCESS|ERROR) : COUNTRY : IP                                                                                               
#                                                                                                                                     
                                                                                                                                      
from random import randrange                                                                                                          
import random                                                                                                                         
import logging                                                                                                                        
from optparse import OptionParser                                                                                                     
from time import strftime                                                                                                             
from datetime import timedelta, date, time, datetime                                                                                  
                                                                                                                                      
def read_options():                                                                                                                   
    parser = OptionParser()                                                                                                           
    parser.add_option("-t", "--time", dest="duration", help="Generate logs for X Hours. Default=48H ( 2 days)", default="48", type="in
t")                                                                                                                                   
    parser.add_option("-l", "--legit-connection", dest="legal", help="How many legal users are connecting. Default=1000", default="100
0", type="int")                                                                                                                       
    parser.add_option("-s", "--start-ddos", dest="start", help="Start DDoS after X hours. Default=24H", default="24", type="int")     
    parser.add_option("-d", "--ddos-connection", dest="ddos", help="How many DDoS connection. Default=10000", default="10000", type="i
nt")                                                                                                                                  
    parser.add_option("-i", "--increment", dest="increment", help="Generate logs every X minutes. Default=60min", default="60", type="
int")                                                                                                                                 
    parser.add_option("-f", "--logfile", dest="logfile", help="Specify a log file. Default=C:\Utilisateurs\Arnaud\Favoris\Bureau\eventlog-demo.log", default="C:\Utilisateurs\Arnaud\Favoris\Bureau\eventlog-demo.log", type="string")                                                                                                
    (options, args) = parser.parse_args()                                                                                             
    return options                                                                                                                    
                                                                                                                                      
def timestamp():                                                                                                                      
    timestamp = strftime("%Y-%m-%dT%H:%M:%S")                                                                                         
    print timestamp                                                                                                                   
    return timestamp                                                                                                                  
                                                                                                                                      
                                                                                                                                      
def generate_log(timestamp,users,status,logfile):                                                                                     
    logging.basicConfig(filename=logfile,                                                                                             
                        format='%(message)s',                                                                                         
                        level=logging.DEBUG)                                                                                          
    if status == 'SUCCESS':                                                                                                           
        countries = weight_good_country(users)                                                                                        
    else :                                                                                                                            
        countries = weight_bad_country(users)                                                                                         
    for country, concurrent_user in countries.iteritems():                                                                            
        i = 0                                                                                                                         
        while i < concurrent_user :                                                                                                   
            logging.info('%s|%s|%s|%s'%(timestamp, random_ip(), country, status))                                                     
            i += 1                                                                                                                    
                                                                                                                                      
def WeightedPick(d):                                                                                                                  
    r = random.uniform(0, sum(d.itervalues()))                                                                                        
    s = 0.0                                                                                                                           
    for k, w in d.iteritems():                                                                                                        
        s += w                                                                                                                        
        if r < s: return k                                                                                                            
    return k                                                                                                                          
                                                                                                                                      
def weight_good_country(user):                                                                                                        
    countries = {'US':60,'GB':20,'DE':15,'FR':5}                                                                                      
    results = {}                                                                                                                      
    for x in xrange(user):                                                                                                            
        p = WeightedPick(countries)                                                                                                   
        results[p] = results.get(p, 0) + 1                                                                                            
    return results                                                                                                                    
                                                                                                                                      
def weight_bad_country(user):                                                                                                         
    countries = {'CN':1330044000,'IN':1173108018, 'US':610232863,'ID':242968342, 'BR':201103330,'PK':184404791, 'BD':156118464,'NG':15
4000000, 'RU':140702000,'JP':127288000, 'MX':112468855,'PH':99900177, 'VN':89571130,'ET':88013491, 'DE':81802257,'EG':80471869, 'TR':7
7804122,'IR':76923300, 'CD':70916439,'TH':67089500, 'FR':64768389,'GB':62348447, 'IT':60340328,'MM':53414374, 'ZA':49000000,'KR':48422
644, 'ES':46505963,'UA':45415596, 'CO':44205293,'TZ':41892895, 'AR':41343201,'KE':40046566, 'PL':38500000,'SD':35000000, 'DZ':34586184
,'CA':33679000, 'UG':33398682,'MA':31627428, 'PE':29907003,'IQ':29671605, 'AF':29121286,'NP':28951852, 'MY':28274729,'UZ':27865738, 'V
E':27223228,'SA':25731776, 'GH':24339838,'YE':23495361, 'KP':22912177,'TW':22894384, 'SY':22198110,'MZ':22061451, 'RO':21959278,'AU':2
1515754, 'LK':21513990,'MG':21281844, 'CI':21058798,'CM':19294149, 'CL':16746491,'NL':16645000, 'BF':16241811,'NE':15878271, 'MW':1544
7500,'KZ':15340000, 'EC':14790608,'KH':14453680, 'ML':13796354,'GT':13550440, 'ZM':13460305,'AO':13068161, 'SN':12323252,'ZW':11651858
, 'CU':11423000,'RW':11055976, 'GR':11000000,'CS':10829175, 'PT':10676000,'TN':10589025, 'TD':10543464,'CZ':10476000, 'BE':10403000,'G
N':10324025, 'SO':10112453,'BO':9947418, 'HU':9930000,'BI':9863117, 'DO':9823821,'BY':9685000, 'HT':9648924,'BJ':9056010, 'SE':9045000
,'AZ':8303512, 'SS':8260490,'AT':8205000, 'HN':7989415,'CH':7581000, 'TJ':7487489,'IL':7353985, 'RS':7344847,'BG':7148785, 'RS':734484
7,'BG':7148785, 'HK':6898686,'TG':6587239, 'LY':6461454,'JO':6407085, 'PY':6375830,'LA':6368162, 'PG':6064515,'SV':6052064, 'NI':59959
28,'ER':5792984, 'KG':5508626,'DK':5484000, 'SK':5455000,'SL':5245695, 'FI':5244000,'NO':5009150, 'AE':4975593,'TM':4940916, 'CF':4844
927,'SG':4701069, 'GE':4630000,'IE':4622917, 'BA':4590000,'CR':4516220, 'HR':4491000,'MD':4324000, 'NZ':4252277,'LB':4125247, 'PR':391
6632,'PS':3800000, 'LR':3685076,'LT':3565000, 'UY':3477000,'PA':3410676, 'MR':3205060,'MN':3086918, 'CG':3039126,'AL':2986952, 'AM':29
68000,'OM':2967717, 'JM':2847232,'KW':2789132, 'LV':2217969,'NA':2128471, 'MK':2061000,'BW':2029307, 'SI':2007000,'LS':1919552, 'XK':1
800000,'GM':1593256, 'GW':1565126,'GA':1545255, 'SZ':1354051,'MU':1294104, 'EE':1291170,'TT':1228691, 'TL':1154625,'CY':1102677, 'GQ':
1014999,'FJ':875983, 'QA':840926,'RE':776948, 'KM':773407,'GY':748486, 'DJ':740528,'BH':738004, 'BT':699847,'ME':666730, 'SB':559198,'
CV':508659, 'LU':497538,'SR':492829, 'MO':449198,'GP':443000, 'MQ':432900,'MT':403000, 'MV':395650,'BN':395027, 'BZ':314522,'IS':30891
0, 'BS':301790,'BB':285653, 'EH':273008,'PF':270485, 'VU':221552,'NC':216494, 'GF':195506,'WS':192001, 'ST':175808,'LC':160922, 'GU':1
59358,'YT':159042, 'CW':141766,'AN':136197, 'TO':122580,'VI':108708, 'GD':107818,'FM':107708, 'VC':104217,'KI':92533, 'JE':90812,'SC':
88340, 'AG':86754,'AD':84000, 'IM':75049,'DM':72813, 'AW':71566,'MH':65859, 'BM':65365,'GG':65228, 'AS':57881,'GL':56375, 'MP':53883,'
KN':49898, 'FO':48228,'KY':44270, 'SX':37429,'MF':35925, 'LI':35000,'MC':32965, 'SM':31477,'GI':27884, 'AX':26711,'VG':21730, 'CK':213
88,'TC':20556, 'PW':19907,'BQ':18012, 'WF':16025,'AI':13254, 'TV':10472,'NR':10065, 'MS':9341,'BL':8450, 'SH':7460,'PM':7012, 'IO':400
0,'FK':2638, 'SJ':2550,'NU':2166, 'NF':1828,'CX':1500, 'TK':1466,'VA':921, 'CC':628,'TF':140, 'PN':46,'GS':30 }                       
    results = {}                                                                                                                      
    for x in xrange(user):                                                                                                            
        p = WeightedPick(countries)                                                                                                   
        results[p] = results.get(p, 0) + 1                                                                                            
    return results                                                                                                                    
                                                                                                                                      
def random_ip():                                                                                                                      
    not_valid = [10,127,169,172,192]                                                                                                  
                                                                                                                                      
    first = randrange(1,256)                                                                                                          
    while first in not_valid:                                                                                                         
        first = randrange(1,256)                                                                                                      
                                                                                                                                      
    ip = ".".join([str(first),str(randrange(1,256)),                                                                                  
    str(randrange(1,256)),str(randrange(1,256))])                                                                                     
    return ip                                                                                                                         
                                                                                                                                      
def concurrent_connection(users):                                                                                                     
    return randrange(1,users)                                                                                                         
                                                                                                                                      
def main():                                                                                                                           
    options = read_options()                                                                                                          
    current_time = datetime.now()-timedelta(hours=options.duration)                                                                   
    attack_time = current_time + timedelta(hours=options.start)                                                                       
    print current_time.strftime("%Y-%m-%dT%H:%M:%S")                                                                                  
    while  datetime.now() > current_time:                                                                                             
        generate_log(current_time.strftime("%Y-%m-%dT%H:%M:%S"),concurrent_connection(options.legal),"SUCCESS",options.logfile)       
        if attack_time < current_time:                                                                                                
            generate_log(current_time.strftime("%Y-%m-%dT%H:%M:%S"),concurrent_connection(options.ddos),"ERROR",options.logfile)      
        current_time = current_time+timedelta(minutes=(options.increment))                                                            
                                                                                                                                      
if __name__ == "__main__":                                                                                                            
    main()                                                                                                                              
                                                             
                                                                                                      
