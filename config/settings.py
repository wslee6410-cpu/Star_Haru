# ============================================================
# config/settings.py
# 프로젝트 전역 설정을 정의하는 모듈
# 定义项目全局设置的模块
# ============================================================

import os

# -------- 로또 기본 규칙 (彩票基本规则) --------
LOTTO_MIN_NUMBER = 1          # 최소 번호 (最小号码)
LOTTO_MAX_NUMBER = 45         # 최대 번호 (最大号码)
LOTTO_PICK_COUNT = 6          # 선택할 번호 개수 (选号个数)

# -------- 생성 기본값 (生成默认值) --------
DEFAULT_SET_COUNT = 5

# -------- 디렉토리 경로 (目录路径) --------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw") + os.sep
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed") + os.sep
DATA_OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output") + os.sep

LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "app.log")

# -------- 출력 파일 설정 (输出文件设置) --------
OUTPUT_FILE_PREFIX = "lotto_numbers"
OUTPUT_FILE_EXTENSION = ".txt"

# -------- 카카오톡 설정 (KakaoTalk设置) --------
# ❗ 실제 사용 시에는 본인의 Access Token으로 교체하세요.
# ❗ 实际使用时请替换为自己的Access Token。
KAKAO_ACCESS_TOKEN = "YOUR_KAKAO_ACCESS_TOKEN_HERE"