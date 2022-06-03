init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="DMR_guideObject",
        description="DMR 示例约会",
        version='0.0.2',
        dependencies={'DokiMonikaReworkCore':('0.0.1','2.0.0')},
        setting_pane="dmr_g_ruleinfo"
    )
    # dependencies 表示这个模组强制需要DMR作为前置模组

init -900 python:
##################################################

    # 声明本次约会的变量
    # 变量名字必须改变
    # 所有的Label内都不允许jump语句
    DMR_Test = {
        # 约会事件id 唯一
        'Id':'dmr_guideObject',
        # 名称
        'Name':'DMR 示例约会',
        # 推送条件 python表达式
        # 这决定了你的约会是否被解锁
        'Conditional':True,
        # 约会开始之前的label(从默认房间跳转到约会场景)
        'pre_StartLabel':'dmr_g_preStartLabel',
        # 约会开始label
        # 在这里随意跳转label
        'StartLabel':'dmr_g_StartLabel',
        # 约会结束之前label
        # 类似于pre_StartLabel
        'pre_EndLabel':'dmr_g_preEndLabel',
        # 约会结束label
        # 回到太空教室后的对话
        'EndLabel':'dmr_g_EndLabel',
        # 相册
        # 用于展示约会中出现的CG
        # 格式为'定义名称，展示名称'
        'CGs':[
            ["miyako_cg", "Cool喵都"]
        ]
            
    }

    # 添加到可用的约会列表
    dmr_DateList.append(DMR_Test)

##################################################

screen dmr_g_ruleinfo():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"

        textbutton ">版权声明":
            ypos 1
            selected False
            action Show(screen = "dialog", message = dmr_g_ruletext, ok_action = Hide("dialog"))

dmr_g_ruletext = "本作品内的素材来自于日本Palette品牌的Galgame作品‘9-nine’系列。\n本作品仅供学习用途，严禁以商业目的分发本子模组，请在下载后24小时内删除。\n本子模组内出现的所有非DDLC背景/立绘/音乐等素材均归Palette所有。"