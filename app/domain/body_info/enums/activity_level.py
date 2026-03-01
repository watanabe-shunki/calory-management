from enum import Enum


class ActivityLStatus(str, Enum):
    OFFICE = "OFFICE"

    @property
    def label(self):
        return {
            "OFFICE": "オフィスワーク",
        }[self.value]
