# 游戏在此开始。
label start:

    call init_script_variables

    scene black

    call part01_main

    return

# 此处初始化游戏中使用的各种变量
label init_script_variables:

    # 见 definitions.rpy 中的解释

    $ _dismiss_pause = config.developer

    # 达成【此生难忘】的共识！
    # 一个存档一种【体验】！
    # $ tantan_commentary_mode = persistent.tantan_commentary_mode

    return