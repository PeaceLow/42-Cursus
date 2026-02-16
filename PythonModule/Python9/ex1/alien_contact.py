from enum import Enum
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(description="Datetime of contact")
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if (self.contact_type == ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=========================================")
    print("Valid contact report:")
    contact_alpha = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 5, 10, 14, 30),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    if contact_alpha.is_verified:
        print("ID:", contact_alpha.contact_id)
        print("Type:", contact_alpha.contact_type.value)
        print("Location:", contact_alpha.location)
        print(f"Signal: {contact_alpha.signal_strength:.1f}/10")
        print(f"Duration: {contact_alpha.duration_minutes} minutes")
        print(f"Witnesses: {contact_alpha.witness_count}")
        if contact_alpha.message_received:
            print("Message:", contact_alpha.message_received)
    print("\n=========================================")
    print("Expected validation error:")
    try:
        contact_beta = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2026, 5, 11, 9, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=9.0,
            duration_minutes=30,
            witness_count=2,
            message_received=None,
            is_verified=False
        )
        if contact_beta.is_verified:
            print("ID:", contact_beta.contact_id)
            print("Type:", contact_beta.contact_type.value)
            print("Location:", contact_beta.location)
            print(f"Signal: {contact_beta.signal_strength:.1f}/10")
            print(f"Duration: {contact_beta.duration_minutes} minutes")
            print(f"Witnesses: {contact_beta.witness_count}")
            if contact_beta.message_received:
                print("Message:", contact_beta.message_received)
    except Exception as e:
        activate = False
        error_text = str(e)
        for line in error_text.split('\n'):
            if "Telepathic contact requires at least 3 witnesses" in line:
                activate = True
        if activate:
            print("Telepathic contact requires at least 3 witnesses")
        else:
            print(e)


if __name__ == "__main__":
    main()
