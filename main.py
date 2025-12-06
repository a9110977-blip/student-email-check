import re

def check_email(email):
    # 驗證規則：以 .edu 結尾 (例如 .edu 或 .edu.tw)
    rule = r'\.edu(\.[a-z]{2})?$'
    
    if re.search(rule, email):
        return "✅ 驗證通過：是學生！"
    else:
        return "❌ 驗證失敗：這不是學生信箱。"

# --- 測試區 ---
print(check_email("albert@school.edu"))
print(check_email("user@gmail.com"))
