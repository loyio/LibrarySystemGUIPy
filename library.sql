/*
 Navicat Premium Data Transfer

 Source Server         : mysqlLoyio
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : library

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 27/06/2021 21:31:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `book_author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `book_press` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `book_quantity` int DEFAULT NULL,
  PRIMARY KEY (`book_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of book
-- ----------------------------
BEGIN;
INSERT INTO `book` VALUES (1, 'Python程序设计', '董付国', '清华大学出版社', 6);
INSERT INTO `book` VALUES (3, '操作系统原理', '庞丽萍', '华中科技大学出版社', 10);
INSERT INTO `book` VALUES (4, '机器学习', '周志华', '清华大学出版社', 12);
INSERT INTO `book` VALUES (8, '计算机网络', '谢希仁', '电子工业出版社', 8);
INSERT INTO `book` VALUES (9, '计算机组成原理', '唐朔飞', '高等教育出版社', 5);
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `u_id` int NOT NULL AUTO_INCREMENT,
  `u_name` varchar(20) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `u_passwd` varchar(20) CHARACTER SET gbk COLLATE gbk_chinese_ci DEFAULT '123456',
  `u_role` varchar(20) DEFAULT 'student',
  PRIMARY KEY (`u_id`) USING BTREE,
  UNIQUE KEY `u_name` (`u_name`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` VALUES (1, 'Loyio', '123456', 'student');
INSERT INTO `users` VALUES (2, 'HexOne', '123456', 'manager');
INSERT INTO `users` VALUES (7, 'niuniu', '123456', 'manager');
INSERT INTO `users` VALUES (56, 'NewTon', '123456', 'student');
INSERT INTO `users` VALUES (57, 'Newer', '123456', 'student');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
