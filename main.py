# ============================================================
# main.py
# 행복로또번호 자동 생성기 - 통합 실행 파일
# 幸福彩票号码自动生成器 - 集成执行文件
# ============================================================

import argparse
from core.generator import LottoGenerator
from core.analyzer import LottoAnalyzer
from core.database import LottoDB
from core.validator import LottoValidator
from utils.file_io import FileIO
from utils.formatter import Formatter
from utils.visualizer import LottoVisualizer
from utils.kakao_sender import KakaoSender


def main():
    parser = argparse.ArgumentParser(description="행복로또번호 자동 생성기")
    parser.add_argument('--analyze', action='store_true', help='당첨 번호 분석 (1번)')
    parser.add_argument('--visualize', action='store_true', help='시각화 출력 (2번)')
    parser.add_argument('--save-db', action='store_true', help='DB 저장 (3번)')
    parser.add_argument('--send-kakao', action='store_true', help='카카오톡 전송 (5번)')
    parser.add_argument('--count', type=int, default=5, help='생성할 세트 수')
    args = parser.parse_args()

    generator = LottoGenerator()
    db = LottoDB()
    analyzer = LottoAnalyzer()
    validator = LottoValidator()

    numbers = generator.generate_multiple_sets(args.count)
    validator.validate_multiple_sets(numbers)

    Formatter.print_sets(numbers)
    FileIO.save_to_txt(numbers)

    if args.save_db:
        db.save_multiple_sets(numbers)

    if args.analyze:
        past = analyzer.load_past_wins()
        print("📊 자주 나온 번호:", analyzer.get_frequent_numbers(past))
        print("📊 잘 안 나온 번호:", analyzer.get_cold_numbers(past))

    if args.visualize:
        LottoVisualizer.plot_distribution(numbers)

    if args.send_kakao:
        KakaoSender.send_message(numbers)


if __name__ == "__main__":
    main()