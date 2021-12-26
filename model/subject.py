from config import db


# Disciplina
class Subject(db.Model):
    __tablename__ = 'subject'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Nome
    name = db.Column(db.String(255))
    # Carga horária
    workload = db.Column(db.Integer)
    # Ementa
    syllabus = db.Column(db.String(3200))
    # Pai no relacionamento One-To-One com a classe Student
    student = db.relationship("Student", back_populates="subject", uselist=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'workload': self.workload,
            'syllabus': self.syllabus,
        }
