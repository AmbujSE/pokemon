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

You'll see a welcome screen with available commands.

### Available Commands

| Command | Example | Description |
|---------|---------|-------------|
| `search name <query>` | `search name pikachu` | Search Pokémon by name (partial match) |
| `search type <type>` | `search type fire` | Search by type (case-insensitive) |
| `search generation <number>` | `search generation 1` | Find all Pokémon from a generation |
| `search legendary` | `search legendary` | Show only legendary Pokémon |
| `search normal` | `search normal` | Show only non-legendary Pokémon |
| `list all` | `list all` | Display all Pokémon in database |
| `help` | `help` | Show command reference |
| `exit` | `exit` | Exit the application |

### Example Session

```
> search name chu
ID    Name                 Type 1       Type 2       Total  
────────────────────────────────────────────────────────────
25    Pikachu              Electric     —            435    
172   Pichu                Electric     —            205    
309   Raichu               Electric     —            485    

Total results: 3

> search type water
[Displays all Water-type Pokémon]

> search generation 1
[Displays all 151 Pokémon from Generation 1]

> search legendary
[Displays all legendary Pokémon]
```

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
- User input parsing and validation
- Result formatting and display
- Interactive command loop

## 🔍 How It Works

1. **Data Loading**: Application reads `pokemon.csv` and converts it to a list of dictionaries
2. **User Input**: CLI prompts user for search commands
3. **Search & Filter**: Query is passed to `search_engine.py` functions
4. **Display Results**: Formatted table shows matching Pokémon
5. **Loop**: Process repeats until user exits

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
