from config import db


# Pessoa
class Person(db.Model):
    __tablename__ = 'person'
    # Identificador
    id = db.Column(db.Integer, primary_key=True)
    # Nome
    name = db.Column(db.String(255))
    # CPF
    cpf = db.Column(db.String(11))
    # Pai no relacionamento One-To-One com a classe Student
    student = db.relationship("Student", back_populates="person", uselist=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
        }

    def __str__(self):
        return f'Person:[ id: {self.id}, name: {self.name}, cpf: {self.cpf} ]'
