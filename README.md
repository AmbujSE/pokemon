# Pokémon Search Engine

A command-line Pokémon search and filter application built with Python. Search and explore Pokémon data by name, type, generation, and legendary status.

## 📋 Features

- **Search by Name**: Find Pokémon using partial name matching (case-insensitive)
- **Search by Type**: Filter Pokémon by primary or secondary type (e.g., Fire, Water, Grass)
- **Search by Generation**: Find all Pokémon from a specific generation (1-8)
- **Legendary Filter**: Show only legendary or regular Pokémon
- **View All**: Display complete Pokémon database
- **Formatted Output**: Clean, readable table display

## 📁 Project Structure

```
pokemon/
├── data/
│   └── pokemon.csv          # Pokémon dataset with 1000+ entries
├── data_loader.py           # CSV reader & data converter
├── search_engine.py         # Search and filter logic
├── main.py                  # CLI controller & user interface
└── README.md                # This file
```

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd pokemon
```

2. Verify the `data/pokemon.csv` file exists in the project directory

## 🚀 Usage

### Start the Application
```bash
python main.py
```

You'll see an interactive menu with numbered options.

### Main Menu

Upon starting, you'll be presented with the following options:

```
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
```

Simply enter the number (1-7) to perform an action.

### Features

| Option | Description |
|--------|-------------|
| **1. Search by Name** | Enter a partial or full name to find Pokémon. Results can be refined by selecting a specific Pokémon from the list. |
| **2. Search by Type** | Enter a type (e.g., Fire, Water, Electric) to find all Pokémon of that type. |
| **3. Search by Generation** | Enter a generation number (1-9) to see all Pokémon from that generation. |
| **4. Show Legendary Pokémon** | Display all legendary Pokémon in the database. |
| **5. Show Non-Legendary Pokémon** | Display all regular (non-legendary) Pokémon in the database. |
| **6. List All Pokémon** | Display the entire Pokémon database. |
| **7. Exit** | Quit the application. |

### Example Session

```
1. Search by Name
   > Enter Pokémon name to search: chu
   
   Results found:
   ID    Name                 Type 1       Type 2       Total  
   ────────────────────────────────────────────────────────────
   25    Pikachu              Electric     —            320    
   26    Raichu               Electric     —            485    
   172   Pichu                Electric     —            205    
   238   Smoochum             Ice          Psychic      305    
   
   Would you like to select a specific Pokémon from the results? (y/n): y
   
   1. Pikachu
   2. Raichu
   3. Pichu
   4. Smoochum
   
   Enter name or number: 2
   
   Final result:
   ID    Name                 Type 1       Type 2       Total  
   ────────────────────────────────────────────────────────────
   26    Raichu               Electric     —            485    
```

### Selection Feature

When searching by name, if multiple results are found, you have the option to refine your search:
- View all matching Pokémon in a numbered list
- Select by **number** (e.g., enter `2`)
- Select by **exact name** (e.g., enter `Raichu`)
- Or continue with all results by entering `n`

## 📊 Data Format

The `pokemon.csv` file contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `#` | Integer | Pokédex ID |
| `Name` | String | Pokémon name |
| `Type 1` | String | Primary type |
| `Type 2` | String | Secondary type (if any) |
| `Total` | Integer | Total stats sum |
| `HP` | Integer | Hit Points |
| `Attack` | Integer | Attack stat |
| `Defense` | Integer | Defense stat |
| `Sp. Atk` | Integer | Special Attack stat |
| `Sp. Def` | Integer | Special Defense stat |
| `Speed` | Integer | Speed stat |
| `Generation` | Integer | Generation (1-8) |
| `Legendary` | Boolean | Legendary status |

## 🏗️ Architecture

### Separation of Concerns

**data_loader.py**
- Handles CSV file I/O
- Converts raw CSV rows into clean dictionaries
- Type conversion (strings → integers for numeric fields)
- Error handling for missing or corrupt files

**search_engine.py**
- Pure search and filter functions
- No I/O operations
- Supports multiple filter types:
  - `search_by_name()`
  - `search_by_type()`
  - `search_by_generation()`
  - `search_legendary()`
  - `apply_filters()` for combined filtering

**main.py**
- CLI controller and entry point
- Interactive menu-based interface
- User input parsing and validation
- Result formatting and display
- Selection feature for refining search results
- Interactive command loop

## 🔍 How It Works

1. **Data Loading**: Application reads `pokemon.csv` and converts it to a list of dictionaries
2. **Menu Display**: CLI displays interactive numbered menu (1-7)
3. **User Selection**: User enters a number to choose an action
4. **Input Collection**: Application prompts for specific search parameters (name, type, generation)
5. **Search & Filter**: Query is passed to `search_engine.py` functions
6. **Result Display**: Formatted table shows matching Pokémon
7. **Optional Refinement**: For name searches, user can select a specific Pokémon from results
8. **Loop**: Process repeats until user selects exit (option 7)

## 💡 Example Use Cases

- Find all Pokémon of a specific type for team building
- Look up a Pokémon by partial name
- Explore Pokémon from favorite generation
- Find all legendary Pokémon
- Check stats and types of search results

## 🐛 Troubleshooting

**"File 'data/pokemon.csv' not found"**
- Ensure `pokemon.csv` is in the `data/` subdirectory
- Check file path is relative to where you run the script

**No results from search**
- Try searching without special characters
- Use lowercase for type searches (e.g., "fire" not "Fire")
- Partial name matching works (e.g., "chu" finds Pikachu, Pichu, Raichu)

**Program crashes**
- Ensure Python 3.7+ is installed: `python --version`
- Check CSV file is not corrupted
- Verify all three Python files are in the project directory

## 📝 License

This project uses the Pokémon dataset. Pokémon is © The Pokémon Company.

## 🤝 Contributing

Feel free to extend the search functionality with:
- Advanced filtering options
- GUI interface
- Export results to CSV/JSON
- Pokémon comparison tools
- Stats analysis features
