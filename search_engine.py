from typing import List, Dict, Any

def search_by_name(pokemon_list: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """
    Filter Pokémon by name (case-insensitive, partial match).
    
    Args:
        pokemon_list: List of Pokémon dictionaries
        query: Name query string
        
    Returns:
        Filtered list of Pokémon
    """
    query = query.lower()
    return [p for p in pokemon_list if query in p['name'].lower()]


def search_by_type(pokemon_list: List[Dict[str, Any]], type_name: str) -> List[Dict[str, Any]]:
    """
    Filter Pokémon by type (primary or secondary).
    
    Args:
        pokemon_list: List of Pokémon dictionaries
        type_name: Type to filter by
        
    Returns:
        Filtered list of Pokémon
    """
    type_name = type_name.strip().lower()
    return [p for p in pokemon_list 
            if p['type1'].lower() == type_name or (p['type2'] and p['type2'].lower() == type_name)]


def search_by_generation(pokemon_list: List[Dict[str, Any]], generation: int) -> List[Dict[str, Any]]:
    """
    Filter Pokémon by generation.
    
    Args:
        pokemon_list: List of Pokémon dictionaries
        generation: Generation number
        
    Returns:
        Filtered list of Pokémon
    """
    return [p for p in pokemon_list if p['generation'] == generation]


def search_legendary(pokemon_list: List[Dict[str, Any]], legendary_only: bool = True) -> List[Dict[str, Any]]:
    """
    Filter Pokémon by legendary status.
    
    Args:
        pokemon_list: List of Pokémon dictionaries
        legendary_only: If True, return only legendaries; if False, return non-legendaries
        
    Returns:
        Filtered list of Pokémon
    """
    return [p for p in pokemon_list if p['legendary'] == legendary_only]


def apply_filters(pokemon_list: List[Dict[str, Any]], **filters) -> List[Dict[str, Any]]:
    """
    Apply multiple filters at once.
    
    Args:
        pokemon_list: List of Pokémon dictionaries
        **filters: Keyword arguments like name="pikachu", type="electric", generation=1, legendary=True
        
    Returns:
        Filtered list of Pokémon
    """
    results = pokemon_list
    
    if 'name' in filters:
        results = search_by_name(results, filters['name'])
    
    if 'type' in filters:
        results = search_by_type(results, filters['type'])
    
    if 'generation' in filters:
        results = search_by_generation(results, filters['generation'])
    
    if 'legendary' in filters:
        results = search_legendary(results, filters['legendary'])
    
    return results
