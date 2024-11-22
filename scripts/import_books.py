
import os
import sys
import django
import pandas as pd
from django.db import IntegrityError

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将项目根目录添加到模块搜索路径中
sys.path.append(project_root)

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')  # 将your_project_name替换为实际的项目名称
django.setup()
from book_management.models import Book  # 将your_app_name替换为实际的应用名称

def import_books_from_excel(file_path):
    try:
        # 使用pandas读取Excel文件
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            try:
                # book = Book(
                #     title=row['title'],
                #     author=row['author'],
                #     isbn=row['isbn'],
                #     volume=row['volume'],
                #     publication_date=row['publication_date'],
                #     publisher=row['publisher'],
                #     quantity=row['quantity'],
                #     # 如果Excel中有对应status字段，可以类似下面这样处理，这里先注释掉原有的choices示例
                #     # status=row['status']
                # )
                # book.save()
                print(row)
            except IntegrityError as e:
                print(f"插入数据时出现完整性错误，可能是重复数据等原因，错误信息：{e}")
                continue
            except KeyError as e:
                print(f"Excel文件中缺少列 {e}，请检查列名是否匹配。")
                continue
            break
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查文件路径是否正确。")


if __name__ == "__main__":
    # 替换为实际的Excel文件路径，这里假设文件在项目根目录下名为books.xlsx
    file_path = r"C:\Users\ljw\Documents\办公\运城博物馆\信息中心\博物馆图书采购\图书清单单表.xlsx"
    import_books_from_excel(file_path)