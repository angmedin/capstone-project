START TRANSACTION;

DROP DATABASE IF EXISTS `dry_bean`;

CREATE DATABASE `dry_bean`;

USE `dry_bean`;

CREATE TABLE `bean` (
    `id`                BIGINT auto_increment NOT NULL,
    `load_timestamp`    DATETIME NOT NULL,
    `area`              INT NOT NULL,
    `perimeter`         DECIMAL(7, 3) NOT NULL,
    `major_axis_length` DECIMAL(10, 7) NOT NULL,
    `minor_axis_length` DECIMAL(10, 7) NOT NULL,
    `aspect_ration`     DECIMAL(10, 9) NOT NULL,
    `eccentricity`      DECIMAL(10, 9) NOT NULL,
    `convex_area`       INT NOT NULL,
    `equiv_diameter`    DECIMAL(10, 7) NOT NULL,
    `extent`            DECIMAL(10, 9) NOT NULL,
    `solidity`          DECIMAL(10, 9) NOT NULL,
    `roundness`         DECIMAL(10, 9) NOT NULL,
    `compactness`       DECIMAL(10, 9) NOT NULL,
    `shape_factor_1`    DECIMAL(10, 9) NOT NULL,
    `shape_factor_2`    DECIMAL(10, 9) NOT NULL,
    `shape_factor_3`    DECIMAL(10, 9) NOT NULL,
    `shape_factor_4`    DECIMAL(10, 9) NOT NULL,
    `class`             VARCHAR(10),
    CONSTRAINT `pk_bean` PRIMARY KEY (`id`)
);

CREATE INDEX `bean_idx_load_timestamp` ON `bean`(`load_timestamp`);

COMMIT;