import random
import time
from instagrapi import Client

# -- بياناتك —
USER = "sans_7_4"
PASS = "ksmk123456"
THREAD_ID = "4446457532343921"

NAMES = ["ركلم ابناء الدياثه هههههههههه","كسختم اولاد زبي","استحقار اولاد البارشميلو"]
MSGS = ["نـ,ـبـ,ـكـ,ـمـ,ـ آۅلـ,ـآډ ڒٍبـ,ـيـ,ـ آلـ,ـمـ,ـډيـ,ـثـ,ـهـ,ـ آلـ,ـحـ,ـيـ,ـۅآنـ,ـهـ,ـ هـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـ اعدائي","كـ,ـسـ,ـخـ,ـۅآتـ,ـمـ,ـكـ,ـ آلـ,ـمـ,ـډيـ,ـثـ,ـهـ,ـ هـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـهـ,ـ","تـ,ـډمـ,ـيـ,ـر آمـ,ـ عـ,ـمـ,ـر","ڒٍبـ,ـيـ,ـ بـ,ـكـ,ـسـ,ـمـ,ـكـ,ـ"]

cl = Client()

def run_bot():
    try:
        print("🚀 [1] جاري الدخول...")
        cl.login(USER, PASS)
        print("✅ [2] دخلنا الحساب!")
        
        while True:
            n = random.choice(NAMES)
            m = random.choice(MSGS)
              # -- تغيير الاسم (الرابط المصلح) —
            # -- تغيير الاسم (هذا هو الجزء المطلوب) —
            try:
                # سطر الرابط (تأكد إنه يبدأ بـ https وينتهي بـ /set_title/)
                url = f"https://i.instagram.com/api/v1/direct_v2/threads/{THREAD_ID}/set_title/"
                
                # إرسال الطلب
                response = cl.private.post(url, data={"title": n})
                print(f"🔄 رد السيرفر: {response.get('status')}")
            except Exception as e:
                print(f"⚠️ مشكلة: {e}")

            try:
                cl.direct_send(m, thread_ids=[THREAD_ID])
                print(f"✉️ أرسلت: {m}")
            except Exception as e:
                print(f"⚠️ مشكلة في الإرسال: {e}")
            
            time.sleep(32)
            
    except Exception as e:
        print(f"❌ خطأ تسجيل دخول: {e}")

if __name__ == "__main__":
    run_bot()
