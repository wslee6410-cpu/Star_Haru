# ============================================================
# utils/file_io.py
# 파일 저장 및 불러오기 유틸리티 모듈
# 文件保存和加载工具模块
# ============================================================

import os
from datetime import datetime
from config.settings import DATA_OUTPUT_DIR, OUTPUT_FILE_PREFIX, OUTPUT_FILE_EXTENSION


class FileIO:
    """파일 입출력 관련 기능 제공 클래스 (文件输入输出功能类)"""

    @staticmethod
    def save_to_txt(numbers_list, filename=None):
        """생성된 번호를 텍스트 파일로 저장합니다. (将生成的号码保存为文本文件)"""
        os.makedirs(DATA_OUTPUT_DIR, exist_ok=True)

        if filename is None:
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{OUTPUT_FILE_PREFIX}_{now}{OUTPUT_FILE_EXTENSION}"

        filepath = os.path.join(DATA_OUTPUT_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write("  🍀 행복로또번호 자동 생성기 🍀\n")
            f.write("=" * 50 + "\n")
            f.write(f"생성 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"생성 세트 수: {len(numbers_list)}\n")
            f.write("-" * 50 + "\n\n")

            for idx, one_set in enumerate(numbers_list, start=1):
                nums = "  ".join(f"{n:2d}" for n in one_set)
                f.write(f"세트 {idx:2d} : {nums}\n")

            f.write("\n" + "=" * 50 + "\n")
            f.write("  💖 행복한 하루 되세요! 💖\n")
            f.write("=" * 50 + "\n")

        print(f"✅ 파일 저장 완료: {filepath}")
        return filepath

    @staticmethod
    def load_from_txt(filepath):
        """텍스트 파일에서 로또 번호를 불러옵니다. (从文本文件加载彩票号码)"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filepath}")

        result = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("세트") and ":" in line:
                    parts = line.split(":")
                    if len(parts) >= 2:
                        nums = [int(x) for x in parts[1].split() if x.isdigit()]
                        if len(nums) == 6:
                            result.append(nums)
        print(f"✅ 파일 로드 완료: {filepath} ({len(result)}개 세트)")
        return result