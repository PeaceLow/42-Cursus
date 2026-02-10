def record_spell(spell_name: str, ingredients: str) -> str:
    import alchemy.grimoire.validator as validator
    validation_result = validator.validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} {validation_result}"
    elif "VALID" in validation_result:
        return f"Spell recorded: {spell_name} {validation_result}"
    else:
        return f"Spell recording error: {spell_name} {validation_result}"
