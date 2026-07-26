# ============================================================
# core/validator.py
# 생성된 로또 번호의 유효성을 검증하는 모듈
# 验证生成的彩票号码是否有效的模块
# ============================================================

from config.settings import LOTTO_MIN_NUMBER, LOTTO_MAX_NUMBER, LOTTO_PICK_COUNT


class LottoValidator:
    """로또 번호 유효성 검사 클래스 (彩票号码有效性检查类)"""

    @staticmethod
    def validate_one_set(numbers):
        """하나의 로또 세트가 유효한지 검사합니다. (检查一组彩票号码是否有效)"""
        # 리스트 여부 (是否为列表)
        if not isinstance(numbers, list):
            return False
        # 길이 6 확인 (检查长度是否为6)
        if len(numbers) != LOTTO_PICK_COUNT:
            return False
        # 정수 확인 (检查是否为整数)
        if not all(isinstance(n, int) for n in numbers):
            return False
        # 범위 확인 (检查是否在1~45范围内)
        if not all(LOTTO_MIN_NUMBER <= n <= LOTTO_MAX_NUMBER for n in numbers):
            return False
        # 중복 확인 (检查是否有重复)
        if len(set(numbers)) != len(numbers):
            return False
        # 오름차순 확인 (检查是否升序排列)
        if numbers != sorted(numbers):
            return False
        return True

    @staticmethod
    def validate_multiple_sets(all_sets):
        """여러 세트를 한 번에 검사합니다. (一次检查多组号码)"""
        for idx, one_set in enumerate(all_sets):
            if not LottoValidator.validate_one_set(one_set):
                print(f"❌ {idx+1}번째 세트에서 오류 발견")
                return False
        print("✅ 모든 세트가 유효합니다.")
        return True