/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : prosystem

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 18/11/2022 20:27:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `field_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of classes
-- ----------------------------
BEGIN;
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (1, '哺乳类', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (2, '鸟类', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (3, '食肉类', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (4, '蹄类', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (5, '节肢动物', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (6, '水生动物', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (7, '两栖动物', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (8, '陆生动物', 1);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (9, '12代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (10, '13代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (11, '1代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (12, '2代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (14, '孢子植物', 2);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (15, '蕨类植物', 2);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (16, '苔藓植物', 2);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (17, '被子植物', 2);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (18, '裸子植物', 2);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (19, '种子植物', 2);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (20, '3代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (21, '4代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (22, '5代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (23, '6代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (24, '7代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (25, '8代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (26, '9代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (27, '10代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (28, '11代', 3);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (29, '川菜', 4);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (30, '湘菜', 4);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (31, '粤菜', 4);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (32, '苏菜', 4);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (33, '浙菜', 4);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (34, '徽菜', 4);
INSERT INTO `classes` (`id`, `class`, `field_id`) VALUES (35, '鲁菜', 4);
COMMIT;

-- ----------------------------
-- Table structure for classes_query
-- ----------------------------
DROP TABLE IF EXISTS `classes_query`;
CREATE TABLE `classes_query` (
  `class_id` int NOT NULL,
  `property_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of classes_query
-- ----------------------------
BEGIN;
INSERT INTO `classes_query` (`class_id`, `property_id`) VALUES (1, 2);
INSERT INTO `classes_query` (`class_id`, `property_id`) VALUES (3, 6);
INSERT INTO `classes_query` (`class_id`, `property_id`) VALUES (3, 7);
INSERT INTO `classes_query` (`class_id`, `property_id`) VALUES (4, 16);
INSERT INTO `classes_query` (`class_id`, `property_id`) VALUES (2, 3);
INSERT INTO `classes_query` (`class_id`, `property_id`) VALUES (2, 8);
COMMIT;

-- ----------------------------
-- Table structure for fields
-- ----------------------------
DROP TABLE IF EXISTS `fields`;
CREATE TABLE `fields` (
  `id` int NOT NULL AUTO_INCREMENT,
  `field` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of fields
-- ----------------------------
BEGIN;
INSERT INTO `fields` (`id`, `field`) VALUES (1, '动物');
INSERT INTO `fields` (`id`, `field`) VALUES (2, '植物');
INSERT INTO `fields` (`id`, `field`) VALUES (3, '中央处理器');
INSERT INTO `fields` (`id`, `field`) VALUES (4, '美食');
INSERT INTO `fields` (`id`, `field`) VALUES (6, '电影');
COMMIT;

-- ----------------------------
-- Table structure for objects
-- ----------------------------
DROP TABLE IF EXISTS `objects`;
CREATE TABLE `objects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `object` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `field_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of objects
-- ----------------------------
BEGIN;
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (1, '金钱豹', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (2, '小老虎', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (3, '长颈鹿', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (4, '斑马', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (5, '鸵鸟', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (6, '企鹅', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (7, '信天翁', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (9, '牛', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (10, '咩咩羊', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (12, '骆驼', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (13, '驴', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (14, '孔雀', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (15, '壁虎', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (16, '螃蟹', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (17, '老虎', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (18, '螃蟹', 1);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (23, 'test_obj', NULL);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (25, 'i7-7700K', 3);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (26, 'i3-12100', 3);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (27, 'i5-12600K', 3);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (28, 'i7-12700K', 3);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (29, '水仙花', 2);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (30, '鹿角蕨', 2);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (31, '海带', 2);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (32, '裙带菜', 2);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (33, '万年藓', 2);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (34, '糖醋里脊', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (35, '宫保鸡丁', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (36, '九转大肠', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (37, '汤爆双脆', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (38, '奶汤蒲菜', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (39, '南肠', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (40, '玉记扒鸡', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (42, '济南烤鸭', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (43, '肉末海参', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (44, '酸辣鱼丸', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (45, '夫妻肺片', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (46, '蚂蚁上树', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (47, '蒜蓉白肉', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (48, '盐煎肉', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (49, '鱼香肉丝', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (50, '锅巴肉片', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (51, '翘脚牛肉', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (52, '青椒鸡', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (53, '白切鸡', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (54, '烧鹅', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (55, '烤乳猪', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (56, '红烧乳鸽', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (57, '蜜汁叉烧', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (58, '脆皮烧肉', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (59, '干炒牛河', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (60, '上汤焗龙虾', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (61, '小笼包子', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (62, '葱油饼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (63, '大煮干丝', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (64, '扬州炒饭', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (65, '牛肉锅贴', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (66, '文楼汤包', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (67, '回卤干', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (68, '佛跳墙', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (69, '鸡汤汆海蚌', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (70, '淡糟香螺片', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (71, '荔枝肉', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (72, '醉糟鸡', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (73, '嘉兴肉粽', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (74, '宁波汤圆', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (75, '绍兴臭豆腐', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (76, '舟山虾爆鳝面', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (77, '湖州馄饨', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (78, '龙井虾仁', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (79, '西湖莼菜', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (80, '虾爆鳝背', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (81, '西湖醋鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (82, '冰糖甲鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (83, '剔骨锅烧河鳗', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (84, '苔菜小方烤', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (85, '雪菜大黄鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (86, '火腿炖甲鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (87, '腌鲜鳜鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (88, '毛峰熏鲥鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (89, '黄山炖鸽', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (90, '雪冬烧山鸡', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (91, '东安子鸡', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (92, '剁椒鱼头', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (93, '腊味合蒸', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (94, '组庵鱼翅', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (95, '冰糖湘莲', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (96, '红椒腊牛肉', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (97, '发丝牛百页', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (98, '浏阳蒸菜', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (99, '干锅牛肚', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (100, '平江火焙鱼', 4);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (101, '肖申克的救赎', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (102, '霸王别姬', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (103, '阿甘正传', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (104, '泰坦尼克号', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (105, '这个杀手不太冷', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (106, '美丽人生', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (107, '千与千寻', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (108, '辛德勒的名单', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (109, '盗梦空间', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (110, '星际穿越', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (111, '忠犬八公的故事', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (112, '楚门的世界', 6);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (113, 'R5-5600X', 3);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (114, 'R7-5800X', 3);
INSERT INTO `objects` (`id`, `object`, `field_id`) VALUES (115, 'R5-5600G', 3);
COMMIT;

-- ----------------------------
-- Table structure for objects_query
-- ----------------------------
DROP TABLE IF EXISTS `objects_query`;
CREATE TABLE `objects_query` (
  `object_id` int NOT NULL,
  `property_id` int NOT NULL,
  `field_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of objects_query
-- ----------------------------
BEGIN;
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (6, 1, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (6, 5, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (1, 12, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (1, 21, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (1, 23, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (1, 29, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (2, 12, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (2, 14, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (2, 21, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (2, 23, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (4, 14, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (4, 24, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (3, 29, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (3, 14, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (3, 15, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (3, 24, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (7, 20, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (7, 22, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (5, 4, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (5, 15, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (5, 16, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (5, 22, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (6, 17, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (6, 18, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (6, 19, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (6, 22, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (9, 1, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (9, 2, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (9, 21, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (9, 1, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (9, 2, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (9, 17, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (15, 31, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (34, 33, 4);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (34, 34, 4);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (34, 35, 4);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (34, 36, 4);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (10, 1, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (10, 2, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (10, 4, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (10, 17, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (12, 1, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (12, 4, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (12, 2, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (13, 4, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (13, 17, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (13, 12, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (14, 3, 1);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (113, 38, 3);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (113, 43, 3);
INSERT INTO `objects_query` (`object_id`, `property_id`, `field_id`) VALUES (113, 48, 3);
COMMIT;

-- ----------------------------
-- Table structure for properties
-- ----------------------------
DROP TABLE IF EXISTS `properties`;
CREATE TABLE `properties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `info` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `field_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of properties
-- ----------------------------
BEGIN;
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (1, ' 有毛发 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (2, ' 产奶 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (3, ' 有羽毛 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (4, '不会飞捏', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (5, ' 会下蛋 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (6, ' 吃肉 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (7, ' 有犬齿 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (8, ' 有爪 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (9, ' 眼盯前方 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (10, ' 有蹄 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (11, ' 反刍 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (12, ' 黄褐色 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (14, ' 有黑色条纹 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (15, ' 长脖 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (16, ' 长腿 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (17, ' 不会飞 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (18, ' 会游泳 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (19, ' 黑白二色 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (20, ' 善飞 ', 1);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (33, '清香', 4);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (34, '鲜嫩', 4);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (35, '味纯', 4);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (36, '海鲜', 4);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (37, '4核心', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (38, '6核心', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (39, '8核心', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (40, '4线程', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (41, '2线程', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (42, '8线程', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (43, '12线程', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (44, '16线程', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (45, '20线程', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (46, '2核心', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (47, 'Intel', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (48, 'AMD', 3);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (49, '外观呈扁平带状', 2);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (50, '外观像裙带', 2);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (51, '粗大呈树形', 2);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (52, '形似鹿角', 2);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (53, '动画片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (54, '幻想电影', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (55, '黑帮片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (56, '科幻片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (57, '西部片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (58, '体育电影', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (59, '悬念片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (60, '浪漫喜剧', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (61, '史诗片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (62, '战争片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (63, '恐怖片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (64, '剧情片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (65, '纪录片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (66, '动作片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (67, '喜剧片', 6);
INSERT INTO `properties` (`id`, `info`, `field_id`) VALUES (68, '冒险片', 6);
COMMIT;

-- ----------------------------
-- Table structure for query_table
-- ----------------------------
DROP TABLE IF EXISTS `query_table`;
CREATE TABLE `query_table` (
  `object_id` int DEFAULT NULL,
  `relation_id` int NOT NULL AUTO_INCREMENT,
  `class_id` int DEFAULT NULL,
  `property_id` int DEFAULT NULL,
  PRIMARY KEY (`relation_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of query_table
-- ----------------------------
BEGIN;
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (9, 1, 1, 17);
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (9, 2, 1, 2);
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (7, 3, 2, 20);
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (7, 4, 2, 3);
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (7, 5, 2, 8);
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (3, 6, 1, 2);
INSERT INTO `query_table` (`object_id`, `relation_id`, `class_id`, `property_id`) VALUES (3, 7, 1, 15);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
