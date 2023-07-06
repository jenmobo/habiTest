-- Tabla de Usuarios
CREATE TABLE Usuarios (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255) NOT NULL,
    Contraseña VARCHAR(255) NOT NULL,
    -- Otros campos
);

-- Tabla de MeGusta
CREATE TABLE MeGusta (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT NOT NULL,
    InmuebleID INT NOT NULL,
    Fecha DATETIME NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Usuarios(ID),
    FOREIGN KEY (InmuebleID) REFERENCES Inmuebles(ID)
);