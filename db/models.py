from .database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ ="user"
    id=Column(Integer, 
                primary_key=True)
    nombre=Column(String(30))
    apellido=Column(String(20))
    correo=Column(String(30))
    celular=Column(Integer)

class Planes(Base):
    __tablename__="planes"
    id=Column(Integer, primary_key=True)
    nombre=Column(String(30))
    ubicacion=Column(String(30))
    descripcion=Column(String(30))
    numero_dias=Column(Integer)
    numero_noches=Column(Integer)

class Reservas(Base):
    __tablename__="reservas"
    id=Column(Integer, primary_key=True)
    nombre=Column(String(30))
    descripcion=Column(String(30))
    fecha_inicio=Column(Integer)
    fecha_fin=Column(Integer)
    precio=Column(Integer)  
    user_id=Column(Integer, ForeignKey("user.id"))

#jsagdfhsagdfhg