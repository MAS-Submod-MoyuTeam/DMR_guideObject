# 准备资源
define my_sayer = "九条都"
define my = DynamicCharacter('九条都', image='miyako', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
image miyako_cg = "Submods/DMR_guideObject/assets/ev103d.png"
image nine_ball_a = "Submods/DMR_guideObject/assets/bg012a.png"
image nine_ball_b = "Submods/DMR_guideObject/assets/bg012b.png"
image nine_ball_c = "Submods/DMR_guideObject/assets/bg012c.png"
image nine_ball_night = "Submods/DMR_guideObject/assets/bg011c.png"

# 建议使用这种方式定义音乐 不要忘了替换该死的反斜杠 -> .replace('\\','/')
init python:
    ReAlize_PianoVer_2 = (renpy.config.basedir).replace('\\','/') + '/game/Submods/DMR_guideObject/assets/ReAlize_PianoVer.mp3'
    Eutopia = (renpy.config.basedir).replace('\\','/')  + '/game/Submods/DMR_guideObject/assets/Eutopia.mp3'

# 定义角色表情
image miyako a1 = im.Composite((960, 960), (0, 0), "DMR_guideObject/my1.png")
image miyako a2 = im.Composite((960, 960), (0, 0), "DMR_guideObject/my2.png")

# 准备资源结束-----------

label dmr_g_preStartLabel:
    # play_song(persistent.current_track) 播放开始约会前的音乐
    # 顺便一提 如果想停止音乐 就是play_song(None)
    $ play_song(ReAlize_PianoVer_2, set_per = False)
    "总之, 欢迎你决定尝试一下DokiMonikaRework."
    "这个模组的目的就是为了与莫妮卡进行约会, 仅此而已"
    "这个指南的目的是教会你基础的约会编写方法, 其实也并不难, 类似于普通的对话, 但是文本比较多"
    "建议结合源代码观看..."
    # 隐藏按钮 别了
    #$ HKBHideButtons()
    "直到切换场景完成之前, 这里的对话都是属于pre_StartLabel"
    "接下来就是切换场景, 暂时想不出更好的方法, 先这样用吧"
    # 接下来 跳转到约会场景:)
    # fade为渐进/出 具体的可以看renpy文档
    # 隐藏莫妮卡 同样可以使用with语句
    
    # 切换至空房间
    $ bg_change_info_moi = mas_changeBackground(dmr_empty, by_user=None, set_persistent=False)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    hide monika 
    show nine_ball_night with Fade(0.5,2,0.5,color="#000000")
    
label dmr_g_StartLabel:
    "从这里开始, 就属于StartLabel了"
    "我会在这里讲解一些脚本方法:)"
    "首先要记住, 一个show语句, 用完以后一定要记住hide"
    "比如刚刚的背景 nine_ball_night 一会换场景时我们要去隐藏, 也就是hide"
    # 这样写也是可以的
    hide nine_ball_night 
    show nine_ball_a 
    with dissolve_scene
    "假如说你想记录下某个角色是否选过某一个选项"
    "你同样也可以直接用一条persistent.声明一个变量来记录"
    "不过DMR提供了一种方式可以让信息记录在其本身的约会数据之中, 这样更加优雅~"
    "dmr_setDateData(id, key, value)"
    "id即为约会的id, key可以想成变量的名字（字符串）,value就是值了"
    "比如说...添加一个名为monika的key, 值为'justmonika'"
    $ dmr_setDateData('dmr_guideObject','monika','justmonika')
    "接下来, 我们读取刚刚保存的key"
    $ getkey = dmr_getDateDataKey('dmr_guideObject', 'monika')
    "getkey = [getkey]"
    "dmr_getDateDataKey(id, key) 如果没有找到key, 返回None"
    "但是如果没有找到id的话, 那就会报错了"
    "DMR会为每个约会id数据额外创建3个key"
    "Id - 约会id"
    "Count - 记录进入本约会的次数"
    "FirstTime - 第一次进入约会的时间"
    $ play_song(Eutopia, set_per=False)
    "啊对了, 如果你想播放bgm的话, 就用play_song(song, set_per=False)"
    "我不建议set_per=True,出bug的话审核是会打回的"
    "你也可以添加fadein和fadeout让音乐切换更舒适, 比如..."
    $ play_song(ReAlize_PianoVer_2, set_per = False, fadein = 1, fadeout = 1)
    "关于monika的表情...如果你用1eua这种, 那么就会显示mas的风格"
    "而如果你用原版的表情...要像这样"
    show monika_vanlia 5a at t11
    pause 2
    show monika_vanlia 5b at t11
    hide monika_vanlia
    hide nine_ball_a
    show nine_ball_b
    with dissolve
    "也许你对dmr_setDateData()和smr_getDateDataKey()还不是很理解, 那我举个场景你看看"
    $ play_song(Eutopia, set_per=False)
    show miyako a1 at t21
    show monika_vanlia 1a at t22
    my_sayer "你好, 欢迎光临, 请问要点些什么呢~"
    m "啊~等我问一下[player]"
    # 记录吃过的东西
    # 这里不提前写下面两行大概也是没问题的
    # 我测试了下 None在if语句中是认为False:)
    $ dmr_setDateData('dmr_guideObject','eated_RTea', False)
    $ dmr_setDateData('dmr_guideObject','eated_Pafi', False)
    m "这次想吃什么?{nw}"
    menu:
        "这次想吃什么?{fast}"
        "只有红茶可以吗?":
            # 标记我们喝过红茶了
            $ dmr_setDateData('dmr_guideObject','eated_RTea', True)
            # 你吃过帕菲吗?
            if not dmr_getDateDataKey('dmr_guideObject', 'eated_Pafi'):   
                # 如果你吃过帕菲, 则为True
                m "九号球家的帕菲也是很好吃的哦, 下次点一下吧~"
            m "既然这样...{w=0.5}那我也要红茶~"
            show miyako a2 at t21
            my_sayer "两份红茶是吗, 好的."
        "帕菲!":
            $ dmr_setDateData('dmr_guideObject','eated_Pafi', True)
            m "[player], 我之前来到这个世界, 可是特意踩过点的~"
            m "九号球家的帕菲, 那可真的是真的是真的是很棒, 你也试一下."
            m "啊哈哈, 好像有点过于激动了."
    hide miyako
    hide monika_vanlia
    with dissolve
    "另外, 如果你想展示或者隐藏莫妮卡, 要记住展示时 需要加上at语句, 具体可以去找一下renpy教学, 不知道就写at t11即可."
    # 也可以看一下https://docs.dokimod.cn/pages/91995e/#添加角色立绘
    "修改好感不允许使用MAS原版的修改好感度, 而要用..."
    $ dmr_gainAff(10, dmr_global.Id)
    $ dmr_loseAff(1, dmr_global.Id)
    "dmr_global.Id是必填项, 填就完了"
    # 本来设计不用填也可以...但是有bug 寄

    
    hide nine_ball_b
    show miyako_cg
    with dissolve
    # cg也是这样的 隐藏掉monika之后, 展示cg即可
    my_sayer "我们下次见喽"
    hide miyako_cg

    # 如果你可以完成一个不错的约会话题编写, 那么你已经有一定的写DDLCmod的能力了

label dmr_g_preEndLabel:
    # 这里是pre_EndLabel, 通常用于回到原太空教室的转场
    # 目前会回到默认的房间 懒得研究回到之前的房间了 摸大鱼!
    $ bg_change_info_moi = mas_changeBackground(mas_background_def, set_persistent=False)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    show monika 1eua with dissolve_scene


label dmr_g_EndLabel:
    "你不需要手动切换回原音乐, 在EndLabel结束后会自动播放"
    # 别忘了显示按钮
    #$ HKBHideButtons()
