import time
from datetime import datetime


from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings

Settings = Settings()

# 토큰 생성 함수
# 문자열 하나를 받은 후 payload 딕셔너리에 전달
# payload 딕셔너리는 사용자명과 만료 시간을 포함하며 JWT가 디코딩될 때 반환
# expires값(만료 시간)은 생성 시점에서 한 시간 후(3600)로 설정 
def create_access_token(user: str):
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }

    # encode()
    # 페이로드: 값이 저장된 딕셔너리, 인코딩할 대상이다
    # 키: 페이로드를 사인하기 위한 키
    # 알고리즘: 페이로드를 사인 및 암호화하는 알고리즘, 기본값인 HS256 알고리즘이 가장 많이 사용된다.
    token = jwt.encode(payload, Settings.SECRET_KEY, algorithm="HS256")
    return token

# 애플리케이션에 전달된 토큰을 검증하는 함수
def verify_access_token(token: str):
    try:
        data = jwt.decode(token, Settings.SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")

        # 토큰의 만료 시간이 존재하는지 여부 확인
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        
        # 토큰이 유효한지 (만료 시간이 지나지 않았는지) 여부 확인
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )
        return data
    
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        )