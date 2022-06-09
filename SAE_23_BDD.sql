-- MySQL Script generated by MySQL Workbench
-- Thu Jun  9 11:47:19 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema sae_23
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sae_23
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sae_23` DEFAULT CHARACTER SET utf8mb3 ;
USE `sae_23` ;

-- -----------------------------------------------------
-- Table `sae_23`.`aeroport`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae_23`.`aeroport` (
  `IdAeroport` INT NOT NULL AUTO_INCREMENT,
  `NomAeroport` VARCHAR(45) CHARACTER SET 'utf8mb3' NOT NULL,
  `PaysAeroport` VARCHAR(45) CHARACTER SET 'utf8mb3' NOT NULL,
  PRIMARY KEY (`IdAeroport`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sae_23`.`compagnie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae_23`.`compagnie` (
  `IdCompagnie` INT NOT NULL,
  `NomCompagnie` VARCHAR(45) NOT NULL,
  `DescriCompagnie` TEXT NOT NULL,
  `PaysCompagnie` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`IdCompagnie`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sae_23`.`modele`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae_23`.`modele` (
  `IdModele` INT NOT NULL AUTO_INCREMENT,
  `NomModele` VARCHAR(45) NOT NULL,
  `MarqueModele` VARCHAR(45) NOT NULL,
  `TypeModele` VARCHAR(45) NOT NULL,
  `DescriModele` TEXT NOT NULL,
  `ImageModele` TEXT NOT NULL,
  `LongPisteModele` INT NOT NULL,
  PRIMARY KEY (`IdModele`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sae_23`.`avion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae_23`.`avion` (
  `IdAvion` INT NOT NULL,
  `IdCompagnie` INT NOT NULL,
  `IdModele` INT NOT NULL,
  PRIMARY KEY (`IdAvion`),
  INDEX `IdCompagnie_idx` (`IdCompagnie` ASC) VISIBLE,
  INDEX `IdType_idx` (`IdModele` ASC) VISIBLE,
  CONSTRAINT `IdCompagnie`
    FOREIGN KEY (`IdCompagnie`)
    REFERENCES `sae_23`.`compagnie` (`IdCompagnie`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `IdModele`
    FOREIGN KEY (`IdModele`)
    REFERENCES `sae_23`.`modele` (`IdModele`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sae_23`.`piste`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae_23`.`piste` (
  `IdPiste` INT NOT NULL,
  `LongueurPiste` INT NOT NULL,
  `IdAeroport` INT NOT NULL,
  PRIMARY KEY (`IdPiste`),
  INDEX `IdAeroport_idx` (`IdAeroport` ASC) VISIBLE,
  CONSTRAINT `IdAeroport`
    FOREIGN KEY (`IdAeroport`)
    REFERENCES `sae_23`.`aeroport` (`IdAeroport`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sae_23`.`vol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sae_23`.`vol` (
  `IdVol` INT NOT NULL,
  `IdAvion` INT NOT NULL,
  `PiloteVol` VARCHAR(45) NOT NULL,
  `IdAeroportDepart` INT NOT NULL,
  `IdAeroportArrivee` INT NOT NULL,
  `DateDepartVol` DATE NOT NULL,
  `DateArriveeVol` DATE NOT NULL,
  PRIMARY KEY (`IdVol`),
  INDEX `IdAvion_idx` (`IdAvion` ASC) VISIBLE,
  INDEX `IdAeroportDepart_idx` (`IdAeroportDepart` ASC) VISIBLE,
  INDEX `IdAeroportArrivee_idx` (`IdAeroportArrivee` ASC) VISIBLE,
  CONSTRAINT `IdAeroportArrivee`
    FOREIGN KEY (`IdAeroportArrivee`)
    REFERENCES `sae_23`.`aeroport` (`IdAeroport`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `IdAeroportDepart`
    FOREIGN KEY (`IdAeroportDepart`)
    REFERENCES `sae_23`.`aeroport` (`IdAeroport`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `IdAvion`
    FOREIGN KEY (`IdAvion`)
    REFERENCES `sae_23`.`avion` (`IdAvion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
