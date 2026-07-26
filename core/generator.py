# ============================================================
# core/generator.py
# 로또 번호를 랜덤으로 생성하는 핵심 모듈
# 随机生成彩票号码的核心模块
# ============================================================

import numpy as np
from config.settings import LOTTO_MIN_NUMBER, LOTTO_MAX_NUMBER, LOTTO_PICK_COUNT


class LottoGenerator:
    """
    로또 번호를 생성하는 클래스
    生成彩票号码的类
    """

    def __init__(self, seed=None):
        """
        생성자: 난수 생성기를 초기화합니다.
        构造函数: 初始化随机数生成器。
        
        Parameters
        ----------
        seed : int, optional
            난수 시드값 (재현성 확보용)
            随机数种子 (用于确保可重现性)
        """
        self.rng = np.random.default_rng(seed)
        self.min_num = LOTTO_MIN_NUMBER
        self.max_num = LOTTO_MAX_NUMBER
        self.pick_count = LOTTO_PICK_COUNT

    def generate_one_set(self):
        """
        1세트(6개)의 로또 번호를 생성합니다. (중복 없음, 오름차순 정렬)
        生成1组(6个)彩票号码。(无重复，升序排列)
        
        Returns
        -------
        list
            오름차순 정렬된 6개 번호 리스트
            升序排列的6个号码列表
        """
        # 1~45에서 중복 없이 6개 선택 (从1~45中无放回选6个)
        numbers = self.rng.choice(
            a=self.max_num,
            size=self.pick_count,
            replace=False,
            shuffle=False
        ) + 1  # 0-based → 1-based 변환 (转换)

        return np.sort(numbers).tolist()

    def generate_multiple_sets(self, count):
        """
        여러 세트의 로또 번호를 생성합니다.
        生成多组彩票号码。
        
        Parameters
        ----------
        count : int
            생성할 세트 수 (要生成的组数)
        
        Returns
        -------
        list of list
            각 세트가 리스트로 담긴 2차원 리스트
            每组为一个列表的二维列表
        """
        return [self.generate_one_set() for _ in range(count)]

    def generate_with_bonus(self):
        """
        보너스 번호를 포함한 로또 번호를 생성합니다. (6개 + 보너스 1개)
        生成包含Bonus号码的彩票号码。(6个 + Bonus 1个)
        
        Returns
        -------
        tuple
            (main_numbers, bonus_number)
            (主号码6个, Bonus号码1个)
        """
        seven = self.rng.choice(self.max_num, size=7, replace=False, shuffle=False) + 1
        main = np.sort(seven[:6]).tolist()
        bonus = int(seven[6])
        return main, bonus