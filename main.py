import os
from data_loader import load_pokemon_data
from search_engine import *


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


def select_from_results(pokemon_list):
    """Allow user to select a specific Pokémon from search results."""
    if not pokemon_list or len(pokemon_list) <= 1:
        return pokemon_list
    
    print("\nWould you like to select a specific Pokémon from the results? (y/n): ", end="")
    if input().strip().lower() == "y":
        print("\nEnter the exact name of the Pokémon you want:")
        for i, p in enumerate(pokemon_list, 1):
            print(f"  {i}. {p['name']}")
        
        try:
            choice = input("\nEnter name or number: ").strip()
            
            # Try as number first
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(pokemon_list):
                    return [pokemon_list[idx]]
            except ValueError:
                pass
            
            # Try as name
            for p in pokemon_list:
                if p['name'].lower() == choice.lower():
                    return [p]
            
            print("Pokémon not found in results.")
            return pokemon_list
        except Exception as e:
            print(f"Error: {e}")
            return pokemon_list
    
    return pokemon_list



def show_menu():
    """Display the main menu with search options."""
    print("""
╔══════════════════════════════════════════════════════════╗
║             🔍 POKÉMON SEARCH ENGINE 🔍                  ║
╚══════════════════════════════════════════════════════════╝

What would you like to do?

  1. Search by Name
  2. Search by Type
  3. Search by Generation
  4. Show Legendary Pokémon
  5. Show Non-Legendary Pokémon
  6. List All Pokémon
  7. Exit

Please enter the number (1-7):""")


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
    while True:
        try:
            # Display menu
            show_menu()
            
            # Get user input
            choice = input("\n> ").strip()
            
            if choice == "1":
                query = input("Enter Pokémon name to search: ").strip()
                if query:
                    results = search_by_name(pokemon_list, query)
                    display_pokemon(results)
                    results = select_from_results(results)
                    if results:
                        display_pokemon(results)
                else:
                    print("Please enter a valid name.")
            
            elif choice == "2":
                type_query = input("Enter Pokémon type to search: ").strip()
                if type_query:
                    results = search_by_type(pokemon_list, type_query)
                    display_pokemon(results)
                else:
                    print("Please enter a valid type.")
            
            elif choice == "3":
                try:
                    gen = int(input("Enter generation number (1-9): ").strip())
                    results = search_by_generation(pokemon_list, gen)
                    display_pokemon(results)
                except ValueError:
                    print("Error: Generation must be a number.")
            
            elif choice == "4":
                results = search_legendary(pokemon_list, legendary_only=True)
                display_pokemon(results)
            
            elif choice == "5":
                results = search_legendary(pokemon_list, legendary_only=False)
                display_pokemon(results)
            
            elif choice == "6":
                display_pokemon(pokemon_list)
            
            elif choice == "7":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main()
