# ============================================================
# utils/kakao_sender.py
# 카카오톡 메시지 전송 모듈 (5번 기능)
# KakaoTalk消息发送模块 (5号功能)
# ============================================================

import requests
import json
from config.settings import KAKAO_ACCESS_TOKEN


class KakaoSender:
    """카카오톡 메시지 전송 클래스 (KakaoTalk消息发送类)"""

    @staticmethod
    def send_message(numbers, receiver="별아"):
        """생성된 번호를 카카오톡으로 전송합니다. (把生成的号码通过KakaoTalk发送)"""
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

        headers = {
            "Authorization": f"Bearer {KAKAO_ACCESS_TOKEN}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        msg = {
            "object_type": "text",
            "text": f"🍀 행복로또번호 🍀\n{numbers}",
            "link": {"web_url": "http://localhost:5000", "mobile_web_url": "http://localhost:5000"}
        }

        data = {"template_object": json.dumps(msg)}
        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            print("📱 카카오톡 전송 완료!")
        else:
            print(f"❌ 전송 실패: {response.text}")