# ===========================================================
# 12. Virtual Environments and Packages
#
# ===========================================================


# ===========================================================
# 12.1 Introduction
# 
# ปัญหา แอปพลิเคชัน A ต้องการไลบรารี X เวอร์ชัน 1.0 ในขณะที่แอปพลิเคชัน B ต้องการไลบรารี X เวอร์ชัน 2.0 ทำไง ??
# Virtual Environment คือทางแก้ปัญหานี้ มันคือ ไดเรกทอรีต้นไม้ที่แยกออกมาและทำงานด้วยตัวเอง ประกอบด้วย:
#   - Python installation สำหรับ Python เวอร์ชันใดเวอร์ชันหนึ่งโดยเฉพาะ
#   - ชุดของแพ็กเกจเพิ่มเติม (ไลบรารี) ที่ติดตั้งอยู่ภายใน
# ===========================================================


# ===========================================================
# 12.2 Creating Virtual Environments
# 
# >> python -m venv tutorial-env
# create the tutorial-env directory if it doesn’t exist, 
#   and also create directories inside it containing a copy of the Python interpreter and various supporting files.
# 
# Once you’ve created a virtual environment, you may activate it.
# >> tutorial-env\Scripts\activate
# 
# your shell’s prompt to show what virtual environment you’re using
# >> $source ~/envs/tutorial-env/bin/activate
#    (tutorial-env)$ 
# 
# To deactivate a virtual environment
# >> deactivate
# ===========================================================


# ===========================================================
# 12.3 Managing Packages with pip
# 
# pip เป็นโปรแกรมที่ใช้ในการติดตั้ง อัปเกรด และลบแพ็กเกจ
# 
# install the latest version
#   >> pip install novas 
# install a specific version
#   >> pip install requests==2.6.0
# upgrade the package to the latest version
#   >> pip install --upgrade requests
# remove the packages
#   >> pip uninstall requests
# display information about a particular package
#   >> pip show requests
# display all of the packages installed
#   >> pip list
# create install requirement
#   >> pip freeze > requirements.txt
# install from requirement
#   >> pip install -r requirements.txt
# ===========================================================