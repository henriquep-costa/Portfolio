import sqlite3

# Conectar ao banco SQLite (ou criar se não existir)
conn = sqlite3.connect('jiujitsu.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS techniques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    level TEXT,
    position TEXT
)
''')
conn.commit()
# Função pra adicionar tecnica

def add_technique():
    name = input('Technique name:').strip()
    category = input('Category(sweep or pass):').strip()
    position = input('Position:').strip()
    level = input('Level:').strip()

    if not name or not category or not position:
        print("Missing required fields.")
        return
    
    cursor.execute('''
                   INSERT INTO techniques (name, category, position, level) VALUES (?,?,?,?)
                   ''', (name, category, position, level))

    conn.commit()
    print('Technique added.')    

def list_by_category():
    category = input('Which category: sweep or pass?').strip()
    cursor.execute('''
                   SELECT name, position, level 
                   FROM techniques where category = ?''',(category,))
    results = cursor.fetchall()
    if results:#true
        print(f"\nTechniques in category '{category}':")
        for i, (name, position, level) in enumerate(results, 1):
            print(f"{i}. {name} | Position: {position} | Level: {level}")
    else:#false
        print(f"No techniques found for category '{category}'.")

def list_by_position():
    position = input('Which position: open guard, closed guard...?').strip()  
    cursor.execute('''
                   SELECT name, category, level 
                   FROM techniques where position = ?''',(position,))
    results = cursor.fetchall()
    if results: 
        print(f"\nTechniques in position '{position}':")
        for i, (name, category, level) in enumerate(results, 1):
            print(f"{i}. {name} | Category: {category} | Level: {level}")
    else:
        print(f"No techniques found for position '{position}'.")      

def search_by_name():
    name = input('Whats the technique name you want to search?').strip()
    cursor.execute('''
                    SELECT name, category, level, position FROM techniques where name = ?''',(name,))
    results = cursor.fetchall()
    if results:
        print(f"\nTechniques with name '{name}':")
        for i, (name, category, level, position) in enumerate(results, 1):
            print(f"{i}. {name} | Category: {category} | Level: {level} | Position: {position}")
    else:
        print(f"No techniques found with this name '{name}'.")

def filter_by_level():
    level = input('Whats level you want to filter? Beginner, intermediate or advanced?').strip()
    cursor.execute('''
                    SELECT name, category, position FROM techniques where level = ?''',(level,))
    results = cursor.fetchall()
    if results:
        print(f"\nTechniques for level '{level}':")
        for i, (name, category, position) in enumerate(results, 1):
            print(f"{i}. {name} | Category: {category} | Position: {position}")
    else:
        print(f"No techniques found for the level '{level}'.")

# Cria o menu de acesso
def menu():
    while True:
        print("\n=== JIU-JITSU TECHNIQUES ===")
        print("1 - Add technique")
        print("2 - List by category")
        print("3 - List by position")
        print("4 - Search by name")
        print("5 - Filter by level")
        print("0 - Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            add_technique()
        elif choice == "2":
            list_by_category()
        elif choice == "3":
            list_by_position()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            filter_by_level()
        else:
            print("Invalid option")

# Run program
menu()

# Close database
conn.close()