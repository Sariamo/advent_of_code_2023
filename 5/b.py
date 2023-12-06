import time
import utils

inp = utils.get_input()
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
lowest_location = None

start = time.time()
ctr = 0
i = 0
while "seed-to-soil" not in inp[i]:
    i += 1
i += 1
while "soil-to-fertilizer" not in inp[i]:
    if inp[i] != "":
        seed_to_soil.append(inp[i].split(" "))
    i += 1
i += 1
while "fertilizer-to-water" not in inp[i]:
    if inp[i] != "":
        soil_to_fertilizer.append(inp[i].split(" "))
    i += 1
i += 1
while "water-to-light" not in inp[i]:
    if inp[i] != "":
        fertilizer_to_water.append(inp[i].split(" "))
    i += 1
i += 1
while "light-to-temperature" not in inp[i]:
    if inp[i] != "":
        water_to_light.append(inp[i].split(" "))
    i += 1
i += 1
while "temperature-to-humidity" not in inp[i]:
    if inp[i] != "":
        light_to_temperature.append(inp[i].split(" "))
    i += 1
i += 1
while "humidity-to-location" not in inp[i]:
    if inp[i] != "":
        temperature_to_humidity.append(inp[i].split(" "))
    i += 1
i += 1
while i < len(inp):
    if inp[i] != "":
        humidity_to_location.append(inp[i].split(" "))
    i += 1

seeds_raw = inp[0].replace("seeds: ", "").split(" ")
seeds = []
i = 0
while i < len(seeds_raw):
    raw_seed = seeds_raw[i]
    i += 1
    for j in range(int(seeds_raw[i])):
        seed = int(raw_seed) + j
        soil, fertilizer, water, light, temperature, humidity, location = "", "", "", "", "", "", ""

        for so, se, ra in seed_to_soil:
            if soil != "":
                break
            if int(se) <= int(seed) < int(se) + int(ra):
                soil = int(seed) + int(so) - int(se)
                break
        if soil == "":
            soil = seed

        for fer, so, ra in soil_to_fertilizer:
            if fertilizer != "":
                break
            if int(so) <= int(soil) < int(so) + int(ra):
                fertilizer = int(soil) + int(fer) - int(so)
                break
        if fertilizer == "":
            fertilizer = soil

        for wa, fe, ra in fertilizer_to_water:
            if water != "":
                break
            if int(fe) <= int(fertilizer) < int(fe) + int(ra):
                water = int(fertilizer) + int(wa) - int(fe)
                break
        if water == "":
            water = fertilizer

        for li, wa, ra in water_to_light:
            if light != "":
                break
            if int(wa) <= int(water) < int(wa) + int(ra):
                light = int(water) + int(li) - int(wa)
                break
        if light == "":
            light = water

        for te, li, ra in light_to_temperature:
            if temperature != "":
                break
            if int(li) <= int(light) < int(li) + int(ra):
                temperature = int(light) + int(te) - int(li)
                break
        if temperature == "":
            temperature = light

        for hu, te, ra in temperature_to_humidity:
            if humidity != "":
                break
            if int(te) <= int(temperature) < int(te) + int(ra):
                humidity = int(temperature) + int(hu) - int(te)
                break
        if humidity == "":
            humidity = temperature

        for lo, hu, ra in humidity_to_location:
            if location != "":
                break
            if int(hu) <= int(humidity) < int(hu) + int(ra):
                location = int(humidity) + int(lo) - int(hu)
                break
        if location == "":
            location = humidity

        ctr += 1
        print(str(ctr) + " (" + str(float((ctr/1600000000)*100)) + "%, " + str(time.time() - start) + ")")
        if lowest_location is None or lowest_location > location:
            lowest_location = location
    i += 1

print(lowest_location)
