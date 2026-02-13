from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(description="Date et heure de l'event")
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, description="les notes")


def main() -> None:
    print("Space Station Validation")
    print("=========================================")
    station_alpha = SpaceStation(
        station_id="ALPHA",
        name="Axel",
        crew_size=18,
        power_level=85.5,
        oxygen_level=70,
        last_maintenance=datetime(2026, 5, 10),
        is_operational=True,
        notes=None
    )
    print("Valid station created:")
    print("ID:", station_alpha.station_id)
    print("Name:", station_alpha.name)
    print(f"Crew: {station_alpha.crew_size} people")
    print(f"Power: {station_alpha.power_level:.1f}%")
    print(f"Oxygen: {station_alpha.oxygen_level:.1f}%")
    if station_alpha.is_operational:
        print("Status: Operational\n")
    else:
        print("Status: Not Operational\n")

    print("=========================================")
    try:
        station_beta = SpaceStation(
            station_id="BETA",
            name="Elsahin",
            crew_size=21,
            power_level=85.5,
            oxygen_level=70,
            last_maintenance=datetime(2026, 5, 10),
            is_operational=True,
            notes=None
        )
        print("Valid station created:")
        print("ID:", station_beta.station_id)
        print("Name:", station_beta.name)
        print(f"Crew: {station_beta.crew_size} people")
        print(f"Power: {station_beta.power_level:.1f}%")
        print(f"Oxygen: {station_beta.oxygen_level:.1f}%")
        if station_beta.is_operational:
            print("Status: Operational\n")
        else:
            print("Status: Not Operational\n")
    except Exception as e:
        print("Expected validation error:")
        # On transforme l'erreur en texte
        error_text = str(e)
        # On cherche la ligne qui commence par "Input should be..."
        for line in error_text.split('\n'):
            if "Input should be" in line:
                print(line.strip())


if __name__ == "__main__":
    main()
