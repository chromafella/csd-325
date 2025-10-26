from typing import Optional, Union

def city_country(city: str, 
                country: str,
                language: Optional[str] = None, 
                population: Optional[Union[int, float, str]] = None
            ) -> str:

    #normalize input
    city_fmt = city.strip().title()
    country_fmt = country.strip().title()

    #base
    base = f"{city_fmt}, {country_fmt}"

    #normalize population if written
    pop_part = ""
    if population is not None:
        if isinstance(population, (int, float)):
            pop_str = str(int(population))
        else:
            pop_str = str(population).strip().replace(",", "")
        pop_part = f" - Population {pop_str}"

    #normalize langauge if written
    lang_part = ""
    if language is not None and language.strip():
        lang_part = f", {language.strip().title()}"

    return f"{base}{pop_part}{lang_part}"

#test calls
print(city_country("sanitago", "chile",))
print(city_country("sanitago", "chile", population=5000000))
print(city_country("santiago", "chile", "spanish", population=5000000))
#print(city_country("los angeles", "united states", "english", population=4000000))
#print(city_country("tokyo", "japan", "japanese", population=37000000))