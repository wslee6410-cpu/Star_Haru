# ============================================================
# core/analyzer.py
# 과거 당첨 번호를 분석하는 모듈 (1번 기능)
# 分析历史中奖号码的模块 (1号功能)
# ============================================================

import numpy as np
import pandas as pd
from collections import Counter
from config.settings import DATA_RAW_DIR


class LottoAnalyzer:
    """
    로또 당첨 번호 분석 클래스
    彩票中奖号码分析类
    """

    @staticmethod
    def load_past_wins(filepath=None):
        """
        CSV 파일에서 과거 당첨 번호를 불러옵니다.
        从CSV文件加载历史中奖号码。
        """
        if filepath is None:
            filepath = f"{DATA_RAW_DIR}past_wins.csv"

        try:
            df = pd.read_csv(filepath)
            # 컬럼명: num1~num6 (列名: num1~num6)
            numbers = df[['num1', 'num2', 'num3', 'num4', 'num5', 'num6']].values
            return numbers
        except FileNotFoundError:
            print("⚠️ 과거 당첨 데이터 파일이 없습니다. 샘플 데이터를 생성합니다.")
            # 샘플 데이터 20세트 생성 (生成20组示例数据)
            sample = np.random.randint(1, 46, size=(20, 6))
            return sample

    @staticmethod
    def get_frequent_numbers(numbers, top_n=5):
        """자주 나온 번호 top_n을 반환합니다. (返回出现频率最高的 top_n 个号码)"""
        counter = Counter(numbers.flatten())
        return counter.most_common(top_n)

    @staticmethod
    def get_cold_numbers(numbers, top_n=5):
        """잘 안 나온 번호 top_n을 반환합니다. (返回出现频率最低的 top_n 个号码)"""
        counter = Counter(numbers.flatten())
        return counter.most_common()[:-top_n-1:-1]