#Damak 05642e58555628a672241f003963cd00
import requests,json,sys,pprint,pyinputplus;
sys_argument=sys.argv;
try:
    if(len(sys.argv)<2):
        print("Usage:cityname apiid");

    sys_argument=sys_argument[1:];
    city_name=sys_argument[0];
    app_id=sys_argument[1];
    url="http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s"%(city_name,app_id)
    response=requests.get(url);
    response.raise_for_status();
    
    json_data=response.json();
    user_input=pyinputplus.inputYesNo("Would u like verbose information[Y/n]:").lower();
    if(user_input=="yes" or user_input=="y"):
        pprint.pprint(json_data);
    else:
        weather=json_data["weather"][0]["main"];
        weather_description=json_data["weather"][0]["description"];
        city=json_data["name"];
        country=json_data["sys"]["country"]
        temperature=json_data["main"]["temp"]-273.15;
        humidity=json_data["main"]["humidity"]
        print(f"""
            country:{country}
            city:{city}
            temperature={temperature.__round__(2)}
            humidity={humidity}
            weather:{weather}
            Weather_description:{weather_description}
        """)
        
except:
    print("please provide the proper argument.");
