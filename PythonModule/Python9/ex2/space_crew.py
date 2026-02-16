from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    cadet = "Cadet"
    officer = "Officer"
    lieutenant = "Lieutenant"
    captain = "Captain"
    commander = "Commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        # Regle 1: L'ID doit commencer par "M"
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Regle 2: Il doit y avoir au moins un capitaine ou commandant
        has_leader = any(
            member.rank in [Rank.captain, Rank.commander]
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Regle 3: Tout les membres de l'equipage doivent être actifs
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        # Regle 4 : Les missions longues (> 365 jours) doivent avoir
        # au moins 50% de membres expérimentés (>= 5 ans d'expérience)
        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need at least 50% experienced crew"
                )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        sarah = CrewMember(
            member_id="SC001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=45,
            specialization="Mission Command",
            years_experience=15
        )

        john = CrewMember(
            member_id="JS002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=8
        )

        alice = CrewMember(
            member_id="AJ003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=28,
            specialization="Engineering",
            years_experience=4
        )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 5, 15),
            duration_days=900,
            crew=[sarah, john, alice],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value.lower()}) - "
                f"{member.specialization}"
            )

    except Exception as e:
        print(f"Unexpected error: {e}")

    print("\n=========================================")
    print("Expected validation error:")

    try:
        # Mission sans capitaine ou commandant (invalide)
        john_local = CrewMember(
            member_id="JS002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=8
        )
        alice_local = CrewMember(
            member_id="AJ003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=28,
            specialization="Engineering",
            years_experience=4
        )

        SpaceMission(
            mission_id="M2025_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime(2024, 12, 1),
            duration_days=30,
            crew=[john_local, alice_local],
            budget_millions=500.0
        )
    except ValueError as e:
        activate = False
        error_text = str(e)
        for line in error_text.split('\n'):
            if "Mission must have at least one Commander or Captain" in line:
                activate = True
        if activate:
            print("Mission must have at least one Commander or Captain")
        else:
            print(e)


if __name__ == "__main__":
    main()
