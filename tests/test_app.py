from app.main import app


def test_home():
    """Test the home endpoint."""
    # Flask 테스트 클라이언트 생성
    client = app.test_client()

    # GET 요청 테스트
    response = client.get("/")

    # HTTP 상태 코드 검증
    assert response.status_code == 200

    # 동적 부분 제외하고 정적 메시지만 검증
    assert b"Hello, Flask CI/CD on MS Azure" in response.data
    