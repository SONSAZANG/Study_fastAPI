# bcrypt를 사용해 문자열을 해싱할 수 있도록 CryptContext 임포트
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    # 문자열을 해싱한 값을 반환
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    # 일반 패스워드와 해싱한 패스워드를 인수로 받고 두 값이 일차하는지를 비교한 return을 bool형으로 반환
    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)
