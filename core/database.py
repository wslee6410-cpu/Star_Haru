# ============================================================
# core/database.py
# SQLite 데이터베이스 저장 및 조회 모듈 (3번 기능)
# SQLite数据库存储和查询模块 (3号功能)
# ============================================================

import sqlite3
from datetime import datetime


class LottoDB:
    """로또 번호 DB 관리 클래스 (彩票号码数据库管理类)"""

    def __init__(self, db_path="lotto_history.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """DB 테이블 생성 (创建数据库表)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lotto_sets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                set_number INTEGER,
                num1 INTEGER, num2 INTEGER, num3 INTEGER,
                num4 INTEGER, num5 INTEGER, num6 INTEGER,
                created_at TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save_set(self, set_number, numbers):
        """한 세트를 DB에 저장합니다. (将一组号码保存到数据库)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO lotto_sets (set_number, num1, num2, num3, num4, num5, num6, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (set_number, *numbers, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    def save_multiple_sets(self, all_sets):
        """여러 세트를 DB에 저장합니다. (将多组号码保存到数据库)"""
        for idx, one_set in enumerate(all_sets, start=1):
            self.save_set(idx, one_set)
        print(f"✅ DB 저장 완료: {len(all_sets)}개 세트")

    def get_all_sets(self):
        """모든 세트를 조회합니다. (查询所有组)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lotto_sets")
        rows = cursor.fetchall()
        conn.close()
        return rows