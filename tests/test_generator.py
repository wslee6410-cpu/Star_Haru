# ============================================================
# tests/test_generator.py
# LottoGenerator 클래스의 단위 테스트
# LottoGenerator 类的单元测试
# ============================================================

import unittest
from core.generator import LottoGenerator


class TestLottoGenerator(unittest.TestCase):
    """LottoGenerator 테스트 클래스 (测试类)"""

    def setUp(self):
        """각 테스트 전에 실행되는 준비 메서드 (每个测试前执行的准备方法)"""
        self.generator = LottoGenerator(seed=42)  # 고정된 시드로 재현 가능 (固定种子可重现)

    def test_generate_one_set_length(self):
        """생성된 세트의 길이가 6인지 테스트 (测试生成的组长度是否为6)"""
        numbers = self.generator.generate_one_set()
        self.assertEqual(len(numbers), 6)

    def test_generate_one_set_unique(self):
        """중복이 없는지 테스트 (测试是否有重复)"""
        numbers = self.generator.generate_one_set()
        self.assertEqual(len(set(numbers)), len(numbers))

    def test_generate_one_set_sorted(self):
        """오름차순 정렬되어 있는지 테스트 (测试是否升序排列)"""
        numbers = self.generator.generate_one_set()
        self.assertEqual(numbers, sorted(numbers))

    def test_generate_one_set_range(self):
        """모든 번호가 1~45 범위 내인지 테스트 (测试所有号码是否在1~45范围内)"""
        numbers = self.generator.generate_one_set()
        for num in numbers:
            self.assertTrue(1 <= num <= 45)

    def test_generate_multiple_sets_count(self):
        """여러 세트 생성 시 개수가 맞는지 테스트 (测试生成多组时数量是否正确)"""
        count = 10
        result = self.generator.generate_multiple_sets(count)
        self.assertEqual(len(result), count)


if __name__ == "__main__":
    # 테스트 실행 (运行测试)
    unittest.main()