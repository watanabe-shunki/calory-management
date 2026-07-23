from typing_extensions import Annotated

from sqlalchemy import BigInteger, MetaData, String

# TODO: Annotatedについて調査
str1 = Annotated[str, 1]
str2 = Annotated[str, 2]
str3 = Annotated[str, 3]
str4 = Annotated[str, 4]
str10 = Annotated[str, 10]
str20 = Annotated[str, 20]

bigint = Annotated[int, "bigint"]
metadata = MetaData()

# TODO: String()について調査
TYPE_ANNOTATION_MAP = {
    str1: String(1),
    str2: String(2),
    str20: String(20),
    str: String().with_variant(String(255), "sqlite"),
    bigint: BigInteger(),
}