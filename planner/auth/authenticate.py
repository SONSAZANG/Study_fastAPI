from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_access_token

# Depends: oauth2_scheme을 의존 라이브러리 함수에 주입
# OAuth2PasswordBearer: 보안 로직이 존재한다는 것을 애플리케이션에 알려준다
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access"
        )

    # verify_access_token: 앞서 정의한 토큰 생성 및 검증 함수, 토큰의 유효성을 확인
    decoded_token = verify_access_token(token)
    return decoded_token["user"]
