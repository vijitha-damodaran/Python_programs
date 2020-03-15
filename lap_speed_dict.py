"""
The lap speeds recorded for 
     Michael Schumacher,  
     Montoya Juan-Pablo and 
     Barrichello Rubens in a F1 race are

( 258.626, 255.931, 258.998, 255.195 ), 
(258.680, 257.925, 259.828, 257.422) and 
(258.405, 256.700, 260.395) respectively

- Find the fastest lap for each driver
- Find the average speed for each driver
- Which driver has recorded the fastest lap ?
- Which driver has the fastest lap average ?
"""

def save_in_dict():
    lap_speed=dict()
    lap_speed['Michael']=[258.626, 255.931, 258.998, 255.195]
    lap_speed['Rubens']=[258.405, 256.700, 260.395,0]
    lap_speed['Montoya']=[258.680, 257.925, 259.828, 257.422]
    return lap_speed

def fastest_lap(lap_speed):
    fast_lap=dict()
    for key in lap_speed.keys():
        fast_lap[key]=max(lap_speed[key])
    return fast_lap

def avg_speed(lap_speed):
    speed_avg=dict()
    for key in lap_speed.keys():
        speed_avg[key]=sum(lap_speed[key])/len(lap_speed[key])
    return speed_avg
    
#main pgm starts from here
if __name__=="__main__":
    sort_list=dict()
    new_dict=dict()
    lap_speed=save_in_dict()
    fastest=fastest_lap(lap_speed)
    speed_average=avg_speed(lap_speed)
    print('Maximum speed of each is',fastest.items(),end='\n\n')
    print('Average speed of each is',speed_average.items(),end='\n\n')
    print('The fastest record is for',[key  for (key, value) in fastest.items() if value == max(fastest.values())],end='\n\n')
    print('The fastest lap avg is for',[key  for (key, value) in speed_average.items() if value == max(speed_average.values())],end='\n\n')
    print('Values in given table format:')
    print('{0} {1:<8} {2:<8} {3}'.format('Race',*lap_speed.keys()))
    for i , value in zip(range(4),zip(*lap_speed.values())):
        print('{0:<4} {1:<8} {2:<8} {3}'.format(i+1,value[0],value[1],value[2]))
    print('\n')
    print('{0:<8} {1:<8} {2:<8}'.format('Rank','Driver','Speed'))
    for item in lap_speed.values():
        for val in item:
            new_dict[val]=[key for key, value in lap_speed.items() if value==item]
    for i,x in zip(range(11),sorted(new_dict,reverse=True)):
        print('{0:<8} {2:<8} {1:<8}'.format(i+1,x,*new_dict[x]))    
