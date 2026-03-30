from enum import Enum


class ActivityStatus(str, Enum):
    """
    MEMO: DB保存時の値
    orm.activity = status.value
    """
    OFFICE = "OFFICE"

    @property
    def label(self):
        mapping = {
            ActivityStatus.OFFICE: "オフィスワーク",
        }
        return  mapping.get(self, "不明")
