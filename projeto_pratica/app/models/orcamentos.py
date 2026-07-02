from app import db
from datetime import datetime, UTC

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)

    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    valor_total = db.Column(db.Float, nullable=False)
    desconto = db.Column(db.Float, nullable=False)
    valor_final = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(50), nullable=False)

    data_criacao = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC)
    )
    data_validade = db.Column(db.DateTime(timezone=True), nullable=False)
    data_envio = db.Column(db.DateTime(timezone=True), nullable=True)