mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

missionTotal = 0 
for number in mission_names:
    missionTotal = missionTotal + 1
print("Total number of missions:" ,missionTotal)

successMissions = 0
for number in mission_success:
    if number == True:
        successMissions = successMissions + 1
print("Number of successful missions",successMissions)  

numberSuccess = successMissions/missionTotal * 100
print(f"Success rate: {numberSuccess:.2f}%")

for number in mission_years:
    if number < 2012:
        print("Missions launched before the year 2000:")
        print(mission_names[mission_years.index(number)])