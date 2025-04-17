# 🧠🚁 AeroNavis

کنترل کوادکوپتر با استفاده از هوش مصنوعی (TensorFlow) در یک محیط شبیه‌سازی شده و سبک، بدون نیاز به سنسور فیزیکی!  
این پروژه از شبیه‌ساز مجازی برای تولید داده و آموزش مدل شبکه عصبی استفاده می‌کند تا به صورت خودکار پرواز کوادکوپتر را یاد بگیرد.

---

## 📌 ویژگی‌ها

- ✨ بدون نیاز به سنسور فیزیکی (تماماً مجازی)
- 🧠 مدل سبک و سریع با TensorFlow (مناسب برای سیستم‌های ضعیف)
- 🔁 آموزش و ارزیابی مدل در حلقه‌ی شبیه‌سازی
- 📊 مستندسازی کامل با Jupyter Notebook
- 🧩 ساختار ماژولار و قابل توسعه

---

## 📁 ساختار پروژه
```
AeroNavis/ 
├── ai/  
|   └── model.py
├── simulator/
├── utils/
|   └── generate_data.py
├── data/
├── models/
├── configs/
├── notebooks/
├── main.py
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```
---

## ⚙️ نصب پیش‌نیازها

### نیازمند پایتون 3.10

```bash
git clone https://github.com/RaitonRed/AeroNavis.git
cd AeroNavis
py -3.10 -m venv .env
.env\Scripts\activate
pip install -r requirements.txt
```
---

## 🚀 اجرای پروژه

برای آموزش مدل:
```bash
python ai/train.py
```

برای اجرای مدل روی شبیه‌ساز:
```bash
python main.py
```
 برای باز کردن مستندات:
```bash
jupyter notebook notebooks/
```
---

## 📓 مستندات Jupyter
### هنوز کامل نشدن
- 01_Model_Design.ipynb: طراحی مدل و دلایل معماری

- 02_Simulator_Test.ipynb: تست حرکت شبیه‌ساز

- 03_Training_Results.ipynb: بررسی Loss و نمودارها

- 04_Evaluation_Examples.ipynb: عملکرد مدل روی ورودی جدید
---

## 📦 تکنولوژی‌های استفاده شده

- Python 3.x

- TensorFlow

- NumPy

- Matplotlib

- Jupyter Notebook
---
## 💡 ایده‌های آینده

- 🎮 کنترل با دسته یا کیبورد

- 🤖 ترکیب با بینایی ماشین (تصاویر دوربین مجازی)

- 🌐 گسترش پروژه به دنیای واقعی با سنسورهای فیزیکی
---
## 🤝 توسعه‌دهنده

پروژه توسط RaitonRed ساخته شده.
اگه علاقه‌مند به پروژه هستی، حتماً استار بده ⭐ و کامنت بذار!
