# ============================================================
# utils/formatter.py
# 결과 출력을 예쁘게 포맷하는 모듈
# 美化输出结果的格式化模块
# ============================================================


class Formatter:
    """출력 결과를 보기 좋게 포맷하는 클래스 (输出结果美化类)"""

    @staticmethod
    def print_sets(numbers_list):
        """번호 리스트를 보기 좋게 출력합니다. (将号码列表美观地打印出来)"""
        print("\n" + "=" * 60)
        print("  🍀  생성된 로또 번호  🍀")
        print("=" * 60)

        for idx, one_set in enumerate(numbers_list, start=1):
            nums = "  ".join(f"{n:2d}" for n in one_set)
            print(f"  세트 {idx:2d} : {nums}")

        print("=" * 60 + "\n")