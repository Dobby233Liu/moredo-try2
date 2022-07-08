## 各种变量 #######################################################################

## 引擎行为级别

# 使玩家无法跳过暂停与过场
define _dismiss_pause = config.developer

## 游戏设置级别

# 尽量在游戏中体现原视频中碳碳对游戏内容的评论/反应
# 未实现
# （https://www.bilibili.com/video/BV16Y411E72C）
# default persistent.tantan_commentary_mode = False

## 图像效果 #######################################################################

## 过场

# 淡出并淡入场景的过场（较慢的变种，用于 part01 开始）
# 用法：
#   scene [...]
#   with dissolve_scene_outin_start
define dissolve_scene_outin_start = MultipleTransition([
    False, Dissolve(0.5), # 从过渡图像淡出到黑色
    "#000", Pause(0.25), # 保持黑色1/4秒钟
    "#000", Dissolve(0.5), # 从黑色淡入到目前图像
    True # 显示目前图像
])

# 淡出并淡入场景的过场
# 用法：
#   scene [...]
#   with dissolve_scene_outin
define dissolve_scene_outin = MultipleTransition([
    False, Dissolve(0.5), # 从过渡图像淡出到黑色
    "#000", Dissolve(0.5), # 从黑色淡入到目前图像
    True # 显示目前图像
])

## 背景图像 #######################################################################

# 游戏第一幕的学校门前背景
# 来源：https://gakaisozai.seesaa.net/article/200806article_16.html
image bg school_front = "images/bg/school_front_day.jpg"