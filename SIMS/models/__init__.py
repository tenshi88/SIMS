import re
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
from flask_login import UserMixin
from SIMS import db

# 生徒テーブル
class Student(db.Model):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    school = Column(String(64))
    class_name = Column(String(64))
    gender = Column(Integer)
    birthday = Column(DateTime)
    address = Column(String(64))
    phone = Column(String(13))
    email = Column(String(64))
    gmail = Column(String(64))
    note = Column(String(400))

    # データを辞書型で取得する
    def getData(self):
        birthday = self.birthday.strftime('%Y-%m-%d')
        # 1:男、2:女、3:その他
        int(self.gender)
        return {
            'id': int(self.id),
            'name': str(self.name),
            'school': str(self.school),
            'class_name': str(self.class_name),
            'gender': int(self.gender),
            'birthday': str(birthday),
            'address': str(self.address),
            'phone': str(self.phone),
            'email': str(self.email),
            'email_school': str(self.gmail),
            'note': str(self.note)
        }

    # nullは許可しない
    @validates('name', 'school', 'class_name', 'gender', 'birthday', 'address', 'phone')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

    # emailのバリデーション
    @validates('email', 'gmail')
    def validate_email(self, key, value):
        is_valid_email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value)
        if not is_valid_email:
            raise ValueError(f'errors.invalid_{key} メールアドレスが不正です。')
        return value

# 学校一覧のテーブル
class School(db.Model):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))

    # データを辞書型で取得する
    def getData(self):
        return {
            'id': int(self.id),
            'name': str(self.name)
        }

    # nullは許可しない
    @validates('name')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

# クラス一覧のテーブル
class Class(db.Model):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))

    # データを辞書型で取得する
    def getData(self):
        return {
            'id': int(self.id),
            'name': str(self.name)
        }

    # nullは許可しない
    @validates('name')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

# ユーザーのテーブル
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64))
    password = Column(String(64))

    # データを辞書型で取得する
    def getData(self):
        return {
            'id': int(self.id),
            'user_id': str(self.user_id),
            'password': str(self.password)
        }

    # nullは許可しない
    @validates('user_id', 'password')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

# 生徒一覧をクラスごとに分けたリストを取得する
def get_divide_students_by_class(school):
    if school is None:
        students = Student.query.all()
    else:
        students = Student.query.filter_by(school=school).all()
    students = [student.getData() for student in students]
    classes = Class.query.all()
    classes = [cls.getData() for cls in classes]
    students_by_class = []
    for cls in classes:
        students_by_class.append({
            'class_name': cls['name'],
            'students': [student for student in students if student['class_name'] == cls['name']]
        })
    return students_by_class