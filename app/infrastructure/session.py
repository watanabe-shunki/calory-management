from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from typing import AsyncGenerator, Generator

"""DBの接続については実行時に調査が必要かも。後、何のDBに接続するかにもよる。
Base.metadata.create_all(engine) に関してはtests/conftest.pyなどで、test_db関数とかで定義しておいて、機能ごとのテストファイルで参照する形を想定
ひとまず最小構成でuserのDB操作をテストでＣＲＵＤ層さできるところまで行う。
画面なしでPyTestで動作確認予定
"""
engine = create_engine("mysql+pymysql://mysqluser:Shunki970521@mysql_db:3306/mydb")

"""MEMO: 以下の関数をエンドポイントの引数で
async def get_user(
    request: RequestBaseModel
    db_session: Session = Depends(get_db_session)
)
    # infrastructureのクラスの引数に設定
    # 補足：UseCase層はDBのsessionの存在を知らない
    user_repository = UserRepository(db_session)
    use_case = GetUserUseCase(user_repository)
"""

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
"""
ここら辺のDBの接続方法は、
APIの実装とは別なので調査/理解は後回し
"""
# TODO: AsyncGenerator調査
# async def get_db_session() -> AsyncGenerator:
#     with Session(bind=engine) as db_session:
#         try:
#             yield db_session
#             db_session.commit()
#         except Exception as e:
#             db_session.rollback()
#             raise e

def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()