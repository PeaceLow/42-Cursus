

def artifact_sorter(
    artifacts: list[dict]
) -> list[dict]:
    if not artifacts:
        return []
    try:
        return sorted(artifacts, key=lambda x: x['power'], reverse=True)
    except KeyError:
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(filter(lambda x: x['power'] >= min_power, mages))
    except (KeyError, TypeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    if not spells:
        return []
    try:
        return list(map(lambda x: f"* {x} *", spells))
    except (TypeError, AttributeError):
        return []


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {}

    try:
        max_mage = max(mages, key=lambda x: x['power'])
        min_mage = min(mages, key=lambda x: x['power'])
        total_power = sum(map(lambda x: x['power'], mages))
        count = len(mages)

        return {
            'max_power': max_mage['power'],
            'min_power': min_mage['power'],
            'avg_power': round(total_power / count, 2)
        }
    except (KeyError, TypeError):
        return {}


def main() -> None:
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Scrying'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'Combat'},
        {'name': 'Invisibility Cloak', 'power': 70, 'type': 'Stealth'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        print(
            f"{sorted_artifacts[0]['name']} "
            f"({sorted_artifacts[0]['power']} power) comes before "
            f"{sorted_artifacts[1]['name']} "
            f"({sorted_artifacts[1]['power']} power)"
        )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))


if __name__ == "__main__":
    main()
