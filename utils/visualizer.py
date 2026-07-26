# ============================================================
# utils/visualizer.py
# 로또 번호 분포를 시각화하는 모듈 (2번 기능)
# 可视化彩票号码分布的模块 (2号功能)
# ============================================================

# ============================================================
# 1. 필요한 라이브러리 임포트 (导入所需库)
# ============================================================
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from collections import Counter
import os
import warnings

# ============================================================
# 2. 경고 메시지 숨기기 (隐藏警告消息) - 선택 사항
# ============================================================
warnings.filterwarnings('ignore', category=UserWarning, module='matplotlib')

# ============================================================
# 3. Windows 한글 폰트 설정 (Windows韩文字体设置)
# ============================================================
KOREAN_FONTS = [
    'NanumGothic',        # 나눔 고딕 (推荐 - 最推荐)
    'Malgun Gothic',      # 맑은 고딕
    'Gulim',              # 굴림
    'Batang',             # 바탕
    'Gungsuh',            # 궁서
    'NanumBarunGothic',   # 나눔바른고딕
    'NanumGothicCoding',  # 나눔고딕코딩
]

def get_available_korean_font():
    """시스템에 설치된 한글 폰트 중 사용 가능한 첫 번째 폰트를 반환합니다."""
    system_fonts = [f.name for f in fm.fontManager.ttflist]
    for font in KOREAN_FONTS:
        if font in system_fonts:
            return font
    # 없으면 기본값 (如果没有就返回默认)
    return 'DejaVu Sans'

# 폰트 설정 (字体设置)
KOREAN_FONT = get_available_korean_font()
plt.rcParams['font.family'] = KOREAN_FONT
plt.rcParams['axes.unicode_minus'] = False

print(f"✅ 시각화 폰트 설정 완료: {KOREAN_FONT}")


# ============================================================
# 4. LottoVisualizer 클래스 (LottoVisualizer类)
# ============================================================
class LottoVisualizer:
    """로또 번호 시각화 클래스 (彩票号码可视化类)"""

    @staticmethod
    def plot_distribution(numbers, save_path="lotto_distribution.png"):
        """
        번호 분포를 막대 그래프로 출력합니다.
        将号码分布输出为柱状图。
        """
        # 리스트를 NumPy 배열로 변환 (将列表转换为NumPy数组)
        arr = np.array(numbers)
        flat = arr.flatten()
        counter = Counter(flat)

        # 1~45 모든 번호에 대해 빈도수 설정 (对1~45所有号码设置频率)
        x = np.arange(1, 46)
        y = [counter.get(i, 0) for i in x]

        # 그래프 그리기 (绘制图表)
        plt.figure(figsize=(12, 6))
        bars = plt.bar(x, y, color='skyblue', edgecolor='black', alpha=0.8)

        # 그래프 꾸미기 (装饰图表) - **영문으로 변경하여 깨짐 방지**
        plt.xlabel("Number", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.title("Lotto Number Distribution", fontsize=14, fontweight='bold')
        plt.xticks(x, rotation=90, fontsize=8)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # 가장 많이 나온 번호 강조 표시 (高亮显示出现最多的号码)
        if y:
            max_value = max(y)
            if max_value > 0:
                for bar, count in zip(bars, y):
                    if count == max_value:
                        bar.set_color('orange')
                        bar.set_edgecolor('red')
                        bar.set_linewidth(2)

        plt.tight_layout()

        # 그래프 저장 (保存图表)
        full_path = os.path.abspath(save_path)
        plt.savefig(full_path, dpi=150, bbox_inches='tight')
        print(f"✅ 그래프 저장 완료: {full_path}")

        # 그래프 화면에 출력 (在屏幕上显示图表)
        plt.show()
        plt.close()

        return full_path

    @staticmethod
    def plot_frequency_comparison(numbers1, numbers2, label1="Set A", label2="Set B",
                                   save_path="comparison.png"):
        """두 개의 번호 세트를 비교하여 막대 그래프로 출력합니다."""
        arr1 = np.array(numbers1).flatten()
        arr2 = np.array(numbers2).flatten()

        counter1 = Counter(arr1)
        counter2 = Counter(arr2)

        x = np.arange(1, 46)
        y1 = [counter1.get(i, 0) for i in x]
        y2 = [counter2.get(i, 0) for i in x]

        plt.figure(figsize=(14, 6))

        width = 0.35
        plt.bar(x - width/2, y1, width, label=label1, color='skyblue', edgecolor='black', alpha=0.8)
        plt.bar(x + width/2, y2, width, label=label2, color='lightcoral', edgecolor='black', alpha=0.8)

        plt.xlabel("Number", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.title("Lotto Number Frequency Comparison", fontsize=14, fontweight='bold')
        plt.xticks(x, rotation=90, fontsize=8)
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✅ 비교 그래프 저장 완료: {save_path}")
        plt.show()
        plt.close()


# ============================================================
# 5. 단독 테스트 실행 (独立测试运行)
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  🧪 LottoVisualizer 단독 테스트 (独立测试)")
    print("=" * 60)

    sample_numbers = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [1, 7, 13, 19, 25, 31],
        [2, 8, 14, 20, 26, 32],
        [3, 9, 15, 21, 27, 33],
        [4, 10, 16, 22, 28, 34],
        [5, 11, 17, 23, 29, 35],
    ]

    LottoVisualizer.plot_distribution(sample_numbers, "test_lotto_distribution.png")
    print("✅ 테스트 완료!")