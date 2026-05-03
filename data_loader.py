import csv
from typing import List, Dict, Any

def load_pokemon_data(csv_path: str) -> List[Dict[str, Any]]:
    """
    Read CSV file and convert each row into a clean Pokémon structure.
    
    Args:
        csv_path: Path to the pokemon.csv file
        
    Returns:
        List of dictionaries containing Pokémon data
    """
    pokemon_list = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert numeric fields to appropriate types
                pokemon = {
                    'id': int(row['#']),
                    'name': row['Name'].strip(),
                    'type1': row['Type 1'].strip(),
                    'type2': row['Type 2'].strip() if row['Type 2'].strip() else None,
                    'total': int(row['Total']),
                    'hp': int(row['HP']),
                    'attack': int(row['Attack']),
                    'defense': int(row['Defense']),
                    'sp_atk': int(row['Sp. Atk']),
                    'sp_def': int(row['Sp. Def']),
                    'speed': int(row['Speed']),
                    'generation': int(row['Generation']),
                    'legendary': row['Legendary'].lower() == 'true'
                }
                pokemon_list.append(pokemon)
        
        return pokemon_list
    
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []
