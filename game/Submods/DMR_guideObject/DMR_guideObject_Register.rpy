init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="DMR_guideObject",
        description="DMR 示例约会",
        version='0.0.2',
        dependencies={'DokiMonikaReworkCore':('0.0.1','2.0.0')}
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
        'EndLabel':'dmr_g_EndLabel'
    }

    # 添加到可用的约会列表
    dmr_DateList.append(DMR_Test)

##################################################