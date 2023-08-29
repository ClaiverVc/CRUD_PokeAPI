-- Active: 1651785329905@@127.0.0.1@3306@entrenadores_pokemon
--Scritps para la creacion de la tablas
CREATE DATABASE entrenadores_pokemon
    DEFAULT CHARACTER SET = 'utf8mb4';

-- Tabla de entrenadores
CREATE TABLE Entrenadores (
  Pokemon VARCHAR(50) NOT NULL PRIMARY KEY,
  Entrenador VARCHAR(50) NOT NULL
);

 -- Tabla de pokemones
CREATE TABLE Pokemones (
  Pokemon VARCHAR(50) NOT NULL,
  Tipo VARCHAR(50) NOT NULL,
  ImagenURL VARCHAR(1000),
  FOREIGN KEY (Pokemon) REFERENCES Entrenadores(Pokemon)
);

--DROP TABLE entrenadores