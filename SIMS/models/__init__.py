import datetime
import re
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
from flask_login import UserMixin
from SIMS import db, app

# テーブルの基底クラス
class BaseMixin(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    # データを追加する
    @classmethod
    def add(cls, **kwargs):
        data = cls(**kwargs)
        db.session.add(data)
        db.session.commit()

    # データを更新する
    @classmethod
    def update(cls, id, **kwargs):
        data = cls.query.filter_by(id=id).first()
        for key, value in kwargs.items():
            setattr(data, key, value)
        db.session.commit()

    # データを削除する
    @classmethod
    def delete(cls, id):
        data = cls.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()

    # 全データを取得する
    @classmethod
    def get_all(cls, **kwargs):
        if not kwargs:
            all_data = cls.query.all()
        else:
            all_data = cls.query.filter_by(**kwargs).all()
        if all_data is None:
            return None
        return [data.to_dict() for data in all_data]

    # 一つのデータを取得する
    @classmethod
    def get_one(cls, **kwargs):
        data = cls.query.filter_by(**kwargs).first()
        if data is None:
            return None
        return data.to_dict()

    # データを辞書型に変換する
    def to_dict(self):
        dic = self.__dict__.copy()
        if '_sa_instance_state' in dic:
            del dic['_sa_instance_state']
        return dic

# 生徒テーブル
class Student(BaseMixin):
    __tablename__ = 'student'
    name = Column(String(64))
    name_kana = Column(String(64))
    school = Column(String(64))
    class_name = Column(String(64))
    gender = Column(Integer)
    birthday = Column(DateTime)
    address = Column(String(64))
    phone = Column(String(13))
    email = Column(String(64))
    gmail = Column(String(64))
    note = Column(String(400))

    # nullは許可しない
    @validates('name', 'school', 'class_name', 'birthday', 'address', 'phone')
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

    # genderのバリデーション
    @validates('gender')
    def validate_gender(self, key, value):
        if value not in [1, 2, 3]:
            raise ValueError(f'errors.invalid_{key} 性別が不正です。')
        return value

    # 生徒一覧をクラスごとに分けたリストを取得する
    def get_divide_by_class(school):
        if school is None:
            students = Student.get_all()
        else:
            students = Student.get_all(school=school)
        classes = Class.get_all()
        students_by_class = []
        for cls in classes:
            students_by_class.append({
                'class_name': cls['name'],
                'students': [student for student in students if student['class_name'] == cls['name']]
            })
        return students_by_class

    # 生年月日から年齢を取得する
    def get_age(self, birthday):
        today = datetime.date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    # データを辞書型に変換する
    def to_dict(self):
        dic = super().to_dict()
        #dic['birthday'] = dic['birthday'].strftime('%Y-%m-%d')
        dic['age'] = self.get_age(dic['birthday'])
        # 1:男、2:女、3:その他 に変換
        match (dic['gender']):
            case 1:
                dic['gender'] = '男'
            case 2:
                dic['gender'] = '女'
            case 3:
                dic['gender'] = 'その他'
        return dic

# 学校一覧のテーブル
class School(BaseMixin):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))

    # nullは許可しない
    @validates('name')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

# クラス一覧のテーブル
class Class(BaseMixin):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))

    # nullは許可しない
    @validates('name')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

# ユーザーのテーブル
class User(BaseMixin, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64))
    password = Column(String(64))

    # nullは許可しない
    @validates('user_id', 'password')
    def validate_not_null(self, key, value):
        if value is None:
            raise ValueError(f'errors.required {key}は必須です。')
        return value

# データベースのテーブルを作成
with app.app_context():
    db.create_all()
