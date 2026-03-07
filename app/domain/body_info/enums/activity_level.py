from enum import Enum


class ActivityStatus(str, Enum):
    """
    MEMO: DB保存時の値
    orm.activity = status.value
    """
    OFFICE = "OFFICE"

    @property
    def label(self):
        return {
            """
            MEMO: 画面表示用
            status = ActivityLStatus.OFFICE
            responses = { "activity": status.label }
            """
            "OFFICE": "オフィスワーク",
        }[self.value]
