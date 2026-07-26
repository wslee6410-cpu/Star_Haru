# ============================================================
# web/app.py
# Flask 웹 서버 실행 파일 (4번 기능)
# Flask Web服务器执行文件 (4号功能)
# ============================================================

from flask import Flask, render_template, request
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.generator import LottoGenerator
from core.analyzer import LottoAnalyzer
from core.database import LottoDB

app = Flask(__name__)
generator = LottoGenerator()
db = LottoDB()


@app.route('/')
def index():
    """메인 페이지 (主页)"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """번호 생성 요청 처리 (处理号码生成请求)"""
    count = int(request.form.get('count', 5))
    numbers = generator.generate_multiple_sets(count)
    db.save_multiple_sets(numbers)
    return render_template('index.html', numbers=numbers, count=count)


@app.route('/analyze')
def analyze():
    """분석 결과 페이지 (分析结果页面)"""
    analyzer = LottoAnalyzer()
    past = analyzer.load_past_wins()
    freq = analyzer.get_frequent_numbers(past)
    cold = analyzer.get_cold_numbers(past)
    return render_template('index.html', frequent=freq, cold=cold)


if __name__ == '__main__':
    app.run(debug=True, port=5000)