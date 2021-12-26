from config import db
from model.person import Person
from model.subject import Subject

# Estudante da disciplina
class Student(db.Model):
    __tablename__ = 'student'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Semestre
    semester = db.Column(db.Integer)
    # Média final
    final_score = db.Column(db.Float)
    # Frequência
    frequency = db.Column(db.Float)
    # Pessoa
    person_id = db.Column(db.Integer, db.ForeignKey(Person.id), nullable=False)
    # Disciplina
    subject_id = db.Column(db.Integer, db.ForeignKey(Subject.id), nullable=False)
    # Filho no relacionamento One-To-One com a classe Person
    # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-one
    person = db.relationship("Person", back_populates="student")
    # Filho no relacionamento One-To-One com a classe Subject
    subject = db.relationship("Subject", back_populates="student")

    def to_json(self):
        return {
            'id': self.id,
            'semester': self.semester,
            'final_score': self.final_score,
            'frequency': self.frequency,
            'person_id': self.person_id,
            'subject_id': self.subject_id
        }
