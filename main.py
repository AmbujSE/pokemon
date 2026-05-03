import os
from data_loader import load_pokemon_data
from search_engine import search_by_name, search_by_type, search_by_generation, search_legendary, apply_filters


def display_pokemon(pokemon_list):
    """Display a list of Pokémon in a formatted way."""
    if not pokemon_list:
        print("No Pokémon found.")
        return
    
    print(f"\n{'ID':<5} {'Name':<20} {'Type 1':<12} {'Type 2':<12} {'Total':<7}")
    print("-" * 60)
    
    for p in pokemon_list:
        type2 = p['type2'] if p['type2'] else "—"
        print(f"{p['id']:<5} {p['name']:<20} {p['type1']:<12} {type2:<12} {p['total']:<7}")
    
    print(f"\nTotal results: {len(pokemon_list)}")


def show_help():
    """Display available commands."""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                    POKÉMON SEARCH ENGINE                      ║
╚═══════════════════════════════════════════════════════════════╝

Available Commands:
  search name <query>          - Search by name (e.g., "search name pikachu")
  search type <type>           - Search by type (e.g., "search type fire")
  search generation <number>   - Search by generation (e.g., "search generation 1")
  search legendary             - Show only legendary Pokémon
  search normal                - Show only non-legendary Pokémon
  list all                     - Display all Pokémon
  help                         - Show this message
  exit                         - Exit the program

Examples:
  search name chu
  search type water
  search generation 2
  search legendary
""")


def main():
    """Main controller - handles user input and coordinates everything."""
    
    # Step 1: Load Data
    print("Loading Pokémon data...")
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'pokemon.csv')
    pokemon_list = load_pokemon_data(data_path)
    
    if not pokemon_list:
        print("Failed to load Pokémon data. Exiting.")
        return
    
    print(f"Successfully loaded {len(pokemon_list)} Pokémon!\n")
    
    # Step 2-4: Interactive loop
    show_help()
    
    while True:
        try:
            # Step 2: Get User Input
            user_input = input("\n> ").strip().lower()
            
            if not user_input:
                continue
            
            # Step 3: Parse and Call Search Function
            if user_input == "exit":
                print("Goodbye!")
                break
            
            elif user_input == "help":
                show_help()
            
            elif user_input == "list all":
                display_pokemon(pokemon_list)
            
            elif user_input.startswith("search name "):
                query = user_input.replace("search name ", "").strip()
                results = search_by_name(pokemon_list, query)
                # Step 4: Display Results
                display_pokemon(results)
            
            elif user_input.startswith("search type "):
                type_query = user_input.replace("search type ", "").strip()
                results = search_by_type(pokemon_list, type_query)
                display_pokemon(results)
            
            elif user_input.startswith("search generation "):
                try:
                    gen = int(user_input.replace("search generation ", "").strip())
                    results = search_by_generation(pokemon_list, gen)
                    display_pokemon(results)
                except ValueError:
                    print("Error: Generation must be a number.")
            
            elif user_input == "search legendary":
                results = search_legendary(pokemon_list, legendary_only=True)
                display_pokemon(results)
            
            elif user_input == "search normal":
                results = search_legendary(pokemon_list, legendary_only=False)
                display_pokemon(results)
            
            else:
                print("Unknown command. Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
