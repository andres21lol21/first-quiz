import pets_db
import sqlite3

conn = sqlite3.connect(pets_db.DB_NAME)


################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
SELECT name, species, age
FROM animals
WHERE animal_id NOT IN (SELECT pet_id FROM people_animals);
"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
SELECT COUNT(*) 
FROM animals AS a
INNER JOIN people_animals AS pa ON a.animal_id = pa.pet_id
INNER JOIN people AS p ON pa.owner_id = p.person_id
WHERE a.age > p.age;
"""


# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """
SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM people AS p
JOIN people_animals AS pa ON p.person_id = pa.owner_id
JOIN animals AS a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie'
AND pa.pet_id NOT IN (
    SELECT pet_id
    FROM people_animals
    WHERE owner_id != pa.owner_id
);


"""


conn = pets_db.get_connection() 
cursor = conn.cursor()


cursor.execute(sql_pets_owned_by_nobody)
results_4A = cursor.fetchall()


cursor.execute(sql_pets_older_than_owner)
results_4B = cursor.fetchone()[0]


cursor.execute(sql_only_owned_by_bessie)
results_4C = cursor.fetchall()


conn.close()


results_4A_formatted = [(name, species, age) for name, species, age in results_4A]

print("Parte 4.A: Mascotas sin propietario")
for result in results_4A_formatted:
    print(result)

print("Parte 4.B: Cantidad de mascotas más viejas que sus propietarios:", results_4B)

print("Parte 4.C: Mascotas propiedad de Bessie y nadie más")
for result in results_4C:
    print(result)
