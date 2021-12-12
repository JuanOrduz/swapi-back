from itertools import groupby
from typing import List

pokemons_base = """
audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig
gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune
landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz
registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon
simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix
wailord wartortle whismur wingull yamask
"""
pokemon_sequence = []


def pokemon_sequencer(pokemons: List[str]) -> List[str]:
    first_char_pokemons = {
        letter: list(group_pokemons)
        for letter, group_pokemons in groupby(pokemons, key=lambda pokemon: pokemon[0])
    }

    def generate_sequence(item, current_sequence):
        if item[-1] in first_char_pokemons:
            for first_char_pokemon in first_char_pokemons.get(item[-1]):
                if first_char_pokemon not in current_sequence:
                    generate_sequence(
                        first_char_pokemon,
                        current_sequence + [first_char_pokemon],
                    )
        global pokemon_sequence
        if len(current_sequence) > len(pokemon_sequence):
            pokemon_sequence = current_sequence
        return current_sequence

    for pokemon in pokemons:
        generate_sequence(pokemon, [pokemon])


if __name__ == "__main__":
    pokemons = pokemons_base.split()
    pokemon_sequencer(pokemons=pokemons)
    print(pokemon_sequence)
