## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`
num_rows = len(moma)

## 2. Reading our MoMA Dataset ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
moma = list(read_file)

# remove the first row of the data, which
# contains the column names
moma = moma[1:]

# Write your code here

## 3. Replacing Substrings with the Replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace("one","two")

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
def CleanParanthesis(index):
    for row in moma:
        nat = row[index]
        nat = nat.replace("(", "")
        nat = nat.replace(")", "")
        row[index] = nat
            
CleanParanthesis(2)
CleanParanthesis(5)
print(moma[:5])

## 5. String Capitalization ##

def CleanUnknown(index, defaultString):
    for row in moma:
        Gender = row[5]
        Gender = Gender.title()
        if not Gender:
            Gender = defaultString
        row[5] = Gender
    
CleanUnknown(5, "Gender Unknown/Other")
CleanUnknown(2, "Nationality Unknown")

print(moma[:5])

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    bDate = row[3]
    eDate = row[4]
    bDate = clean_and_convert(bDate)
    eDate = clean_and_convert(eDate)
    row[3] = bDate
    row[4] = eDate

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(data):
    for ch in bad_chars:
        data = data.replace(ch, "")
    return data

stripped_test_data = []
for data in test_data:
    cleaned = strip_characters(data)
    stripped_test_data.append(cleaned)

print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(dString):
    if "-" in dString:
        years = dString.split("-")
        return round((int(years[0])+int(years[1]))/2)
    else:
        return int(dString)
    
processed_test_data = []

for dString in stripped_test_data:
    year = process_date(dString)
    processed_test_data.append(year)

print(processed_test_data)
    
for row in moma:
    dString = row[6]
    dString = strip_characters(dString)
    date = process_date(dString)
    row[6] = date