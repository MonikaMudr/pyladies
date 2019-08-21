# Složitejší příklad, který pracuje s primárními a cizími klíči
# a se spojováním tabulek

import sqlite3

# Připojíme se k databázi (v souboru)
connection = sqlite3.connect('pyladies_example_2.db')

# Získáme instanci třídy `Cursor`, pomocí které bude do databáze posílat příkazy
cursor = connection.cursor()

# Pokud tabulky už existují, tak ji odstraníme,
# abychom mohli skript spouštět opakovaně
cursor.execute("""DROP TABLE IF EXISTS ROBOT""")
cursor.execute("""DROP TABLE IF EXISTS BATTLE""")

# Vytvoříme tabulku s roboty a tabulky s výsledky bitev
cursor.execute("""
-- u jednotlivých roborů si ukládáme ID, jméno a typ
CREATE TABLE ROBOT (
    ROBOT_ID INT PRIMARY KEY,
    NAME TEXT,
    TYPE TEXT)
""")

cursor.execute("""
-- bitva se skládá z ID bitvy, ID vítěze a poraženého (odpovídají ID v tabulce ROBOT)
-- a z bodů pro vítěze a poraženého
CREATE TABLE BATTLE (
    BATTLE_ID INT PRIMARY KEY,
    WINNER_ID INT,
    LOSER_ID INT,
    WINNER_POINTS INT,
    LOSER_POINTS INT,
    FOREIGN KEY(WINNER_ID) REFERENCES ROBOT(ROBOT_ID),
    FOREIGN KEY(LOSER_ID) REFERENCES ROBOT(ROBOT_ID)
    )
""")

# Vložíme do tabulkek data
cursor.execute("""
    INSERT INTO ROBOT (ROBOT_ID, NAME, TYPE) VALUES
    (1, "JIM", "DEFENSIVE"), (2, "JACK", "OFFENSIVE"), (3, "JIMMY", "OFFESIVE")
""")

cursor.execute("""
    INSERT INTO BATTLE (BATTLE_ID, WINNER_ID, LOSER_ID, WINNER_POINTS, LOSER_POINTS) VALUES
    (1, 1, 2, 10, 8), -- robot 1 porazil robota 2 se skóre 10:8 (v bitvě 1)
    (2, 2, 1, 6, 9),
    (3, 2, 3, 10, 9),
    (4, 1, 3, 5, 4),
    (5, 3, 2, 2, 0),
    (6, 1, 2, 9, 6)
""")

# Dotážeme se na výsledky bitev, které vyhrál robot se jménem "JIM"
scores = cursor.execute("""
    SELECT BATTLE.WINNER_POINTS, BATTLE.LOSER_POINTS
    FROM BATTLE
    JOIN ROBOT ON ROBOT.ROBOT_ID = BATTLE.WINNER_ID
    WHERE ROBOT.NAME = "JIM"
""")

for score in scores:
    print(score)

# Uložíme změny a uzavřeme spojení
connection.commit()
connection.close()