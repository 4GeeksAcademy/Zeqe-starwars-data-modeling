from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'USUARIO'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)  
    direccion = Column(String(50), nullable=False) 
    telefono = Column(String(50), nullable=False) 
    fecha_subscripcion = Column(Date(), nullable=False)

    favoritos = relationship("Favorito", back_populates="usuario")


class Planeta(Base):
    __tablename__ = 'PLANETA'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)  
    descripcion = Column(String(200), nullable=True)

    favoritos = relationship("Favorito", back_populates="planeta")
     

class Personaje(Base):
    __tablename__ = 'PERSONAJE'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)  
    descripcion = Column(String(200), nullable=True) 

    favoritos = relationship("Favorito", back_populates="personaje")


class Favorito(Base):
    __tablename__ = 'FAVORITO'
    
    usuario_id = Column(Integer, ForeignKey('USUARIO.id'), primary_key=True)
    personaje_id = Column(Integer, ForeignKey('PERSONAJE.id'), primary_key=True, nullable=True)
    planeta_id = Column(Integer, ForeignKey('PLANETA.id'), primary_key=True, nullable=True)

    usuario = relationship("Usuario", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")

render_er(Base, 'diagrama.png')
