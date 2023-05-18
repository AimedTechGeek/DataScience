## 1. Reading the MoMA Dataset ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##

ages = []
for row in moma:
    artYear = row[6]
    bYear = row[3]
    age = 0
    if bYear!= "":
        age = artYear - bYear
    ages.append(age)
    
final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)    
      

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen
decades = []
for age in final_ages:
    if age=="Unknown":
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]+"0s"
    decades.append(decade)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for decade in decades:
    if decade in decade_frequency:
        decade_frequency[decade]+=1
    else:
        decade_frequency[decade] = 1

## 5. Inserting Variables into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{}'s birth year is {}".format(artist, birth_year)
print(template)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist in artist_freq:
        artist_freq[artist] += 1
    else:
        artist_freq[artist] = 1
        

## 7. Creating an Artist Summary Function ##

def artist_summary(name):
    artsNum = artist_freq[name]
    template = "There are {} artworks by {} in the dataset".format(artsNum, name)
    print(template)
artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {} is {:,.2f} million"

for item in pop_millions:
    print(template.format(item[0], item[1]))

## 9. Challenge: Summarizing Artwork Gender Data ##

freq_gender = {}

for row in moma:
    gender = row[5]
    if gender in freq_gender:
        freq_gender[gender] += 1
    else:
        freq_gender[gender] = 1

for name, artsNum in freq_gender.items():
    template = "There are {:,} artworks by {} artists"
    print(template.format(artsNum, name)) 
    