import datetime, re
import itertools
from sqlalchemy import Column, Integer, String, DateTime, func
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

    # データを複数追加する
    @classmethod
    def add_many(cls, data_list):
        db.session.bulk_insert_mappings(cls, data_list)
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

    # データをすべて削除する
    @classmethod
    def delete_all(cls):
        cls.query.delete()
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
    name = Column(String(64), nullable=False)
    name_kana = Column(String(64), nullable=False)
    school = Column(String(64), nullable=False)
    class_name = Column(String(64), nullable=False)
    gender = Column(Integer, nullable=False)
    birthday = Column(DateTime, nullable=False)
    address = Column(String(64), nullable=False)
    phone = Column(String(13), nullable=False)
    email = Column(String(64), nullable=False)
    gmail = Column(String(64), nullable=False)
    note = Column(String(400), nullable=False)

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

    # 生徒一覧を学校、クラスごとに分けたリストを取得する
    def get_categorized_list(school):
        if school is None:
            students = Student.get_all()
            schools = list(set([dic['school'] for dic in students]))
        else:
            students = Student.get_all(school=school)
            schools = [school]
        # 名前順にソート
        students = sorted(students, key=lambda x: x['name_kana'])
        classes = Class.get_all()
        categorized_list = []
        for scl in schools:
            for cls in classes:
                categorized_list.append({
                    'school': scl,
                    'class_name': cls['name'],
                    'class_number': cls['class_number'],
                    'open_date': cls['open_date'].strftime('%Y-%m-%d'), # 日付を文字列に変換
                    'close_date': cls['close_date'].strftime('%Y-%m-%d'), # 日付を文字列に変換
                    'is_open': cls['open_date'] <= datetime.datetime.now() <= cls['close_date'],
                    'students': [student for student in students if student['class_name'] == cls['name'] and student['school'] == scl]
                })
        return categorized_list

    # 一つのデータを取得する場合、一つ前と一つ後のIDを取得して追加
    @classmethod
    def get_one(cls, **kwargs):
        dic = super().get_one(**kwargs)
        students = [listByClass['students'] for listByClass in cls.get_categorized_list(dic['school'])]
        categorized_id_list = [student['id'] for student in itertools.chain.from_iterable(students)]
        index = categorized_id_list.index(dic['id'])
        dic['prev_id'] = categorized_id_list[index-1] if index != 0 else None
        dic['next_id'] = categorized_id_list[index+1] if index != len(categorized_id_list)-1 else None
        return dic

    # 生年月日から年齢を取得する
    def get_age(self, birthday):
        today = datetime.date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    # データを辞書型に変換する
    def to_dict(self):
        dic = super().to_dict()
        dic['age'] = self.get_age(dic['birthday']) # 年齢を追加
        dic['birthday'] = dic['birthday'].strftime('%Y-%m-%d') # 日付を文字列に変換
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
    name = Column(String(64), unique=True, nullable=False)

# クラス一覧のテーブル
class Class(BaseMixin):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
    class_number = Column(Integer, unique=True, nullable=False)
    open_date = Column(DateTime, nullable=False)
    close_date = Column(DateTime, nullable=False)

# ユーザーのテーブル
class User(BaseMixin, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)

# データベースのテーブルを作成
with app.app_context():
    #Student.__table__.drop(bind=db.engine)
    #School.__table__.drop(bind=db.engine)
    #Class.__table__.drop(bind=db.engine)
    #User.__table__.drop(bind=db.engine)
    db.create_all()
