import csv

def compare_pops(pops, age_sex_year1, age_sex_year2):
    '''Finds the populations (pop1 and pop2) for the two 
    passed-in age, sex, and year tuples.
    
    Returns a two-item tuple containing:
     - the numeric difference in population (pop2 - pop1)
     - the ratio (pop2 / pop1)

    Keyword arguments:
    pops -- a sequence holding dictionaries
    age_sex_year1 -- a tuple holding age, sex, and year values
    age_sex_year2 -- a tuple holding age, sex, and year values'''
    pop1, pop2 = -1, -1
    for row in pops:
        if (row['AGE'] == str(age_sex_year1[0]) 
				and row['SEX'] == age_sex_year1[1]):
            pop1 = row['POPESTIMATE' + str(age_sex_year1[2])]
            pop1 = int(pop1.replace(',',''))
        if (row['AGE'] == str(age_sex_year2[0]) 
				and row['SEX'] == age_sex_year2[1]):
            pop2 = row['POPESTIMATE' + str(age_sex_year2[2])]
            pop2 = int(pop2.replace(',',''))
        if pop1 > 0 and pop2 > 0:
            return (pop2 - pop1, pop2/pop1)

with open('../csvs/us-population-2010-2014.csv', newline='') as csvfile:
    pops = list(csv.DictReader(csvfile))
    
pop1 = (30, 'F', 2011)
pop2 = (30, 'M', 2011)

diff = compare_pops(pops, pop1, pop2)
print(diff)