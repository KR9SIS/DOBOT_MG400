alarm_servo_list = [
    {
        "id": 0,
        "level": 0,
        "en": {"description": "No error", "cause": "", "solution": ""},
        "zh_CN": {"description": "无错误", "cause": "", "solution": ""},
    },
    {
        "id": 25376,
        "level": 0,
        "en": {
            "description": "Abnormalities in internal servo parameters",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "伺服内部参数出现异常",
            "cause": "1.控制电源电压瞬时下降 2.参数存储过程中瞬时掉电 3.一定时间内参数的写入次数超过了最大值 4.更新了软件 5.伺服驱动器故障",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description": "Programmable logic configuration faults",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "可编程逻辑配置故障",
            "cause": "1.FPGA和MCU软件版本不匹配 2.FPGA故障",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29953,
        "level": 0,
        "en": {
            "description": "FPGA software version too low",
            "cause": "",
            "solution": "Please contact technical support engineer",
        },
        "zh_CN": {
            "description": "FPGA软件版本过低",
            "cause": "",
            "solution": "请联系技术支持工程师",
        },
    },
    {
        "id": 29954,
        "level": 0,
        "en": {
            "description": "Programmable logic interrupt fault",
            "cause": "",
            "solution": "If connecting the power for many times, the alarm is still reported, please replace the drive",
        },
        "zh_CN": {
            "description": "可编程逻辑中断故障",
            "cause": "1.FPGA故障 2.FPGA与MCU通信握手异常 3.驱动器内部运算超时",
            "solution": "多次接通电源后仍报故障，更换驱动器",
        },
    },
    {
        "id": 25377,
        "level": 0,
        "en": {
            "description": "Internal program exceptions",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "内部程序异常",
            "cause": "1.EEPROM故障 2.伺服驱动器故障",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21808,
        "level": 0,
        "en": {
            "description": "Parameter storage failure",
            "cause": "",
            "solution": "Reset the parameter and power on again, or please contact technical support engineer",
        },
        "zh_CN": {
            "description": "参数存储故障",
            "cause": "1.参数写入出现异常 2.参数读取出现异常",
            "solution": "更改参数后，重新上电，或联系技术支持工程师",
        },
    },
    {
        "id": 28962,
        "level": 0,
        "en": {
            "description": "Product matching faults",
            "cause": "",
            "solution": "1. Check whether the motor parameter matches the motor model in nameplate; 2.Check whether the motor and driver match, otherwise, select the right motor and driver",
        },
        "zh_CN": {
            "description": "产品匹配故障",
            "cause": "1.产品编号（电机或者驱动器）不存在 2.电机与驱动器功率等级不匹配",
            "solution": "1.查看电机铭牌与电机品牌参数设置是否匹配 2.确认选择的电机与驱动器是否配套，否则调配匹配的电机与驱动器",
        },
    },
    {
        "id": 21574,
        "level": 0,
        "en": {
            "description": "Invalid servo ON command fault",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "伺服ON指令无效故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 28964,
        "level": 0,
        "en": {
            "description": "Absolute position mode product matching fault",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "绝对位置模式产品匹配故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25378,
        "level": 0,
        "en": {
            "description": "Repeated assignment of DI functions",
            "cause": "",
            "solution": "1. Check whether  the same function is assigned to different DI's; 2. Confirm whether the corresponding MCU supports the assigned functionality",
        },
        "zh_CN": {
            "description": "DI功能重复分配",
            "cause": "1.DI功能分配时，同一功能重复分配多个DI端子 2.DI功能编号超出DI功能个数 3.DI功能不支持",
            "solution": "1.检查DI组参数，是否有同一个功能分配在不同的DI上 2.确认对应MCU版本是否支持这些分配的功能",
        },
    },
    {
        "id": 25379,
        "level": 0,
        "en": {
            "description": "DO function allocation overrun",
            "cause": "",
            "solution": "Check whether the motor and circuit are working properly, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "DO功能分配超限",
            "cause": "1.控制器异常 2.通讯线缆接触不良或者断开 3.通讯线缆未接地或者接地不良",
            "solution": "检测电机和线路是否正常，或联系技术支持工程师",
        },
    },
    {
        "id": 29488,
        "level": 0,
        "en": {
            "description": "Data in the motor encoder ROM is incorrectly checked or parameters are not stored",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
        "zh_CN": {
            "description": "电机编码器ROM中数据校验错误或未存入参数",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
    },
    {
        "id": 8752,
        "level": 0,
        "en": {
            "description": "Hardware overcurrent",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "硬件过流",
            "cause": "1.输入指令与接通伺服同步或输入指令过快 2.制动电阻过小或短路 3.电机线缆接触不良4.电机线缆接地 5.电机UVW线缆短路 6.电机烧坏 7.增益设置不合理，电机振荡 8.编码器接线错误、老化腐蚀，编码器插头松动 9.驱动器故障",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 8977,
        "level": 0,
        "en": {
            "description": "DQ axis current overflow fault",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "DQ轴电流溢出故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 65288,
        "level": 0,
        "en": {
            "description": "FPGA system sampling operation timeout",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "FPGA系统采样运算超时",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 9024,
        "level": 0,
        "en": {
            "description": "Output shorted to ground",
            "cause": "",
            "solution": "Please contact technical support engineer",
        },
        "zh_CN": {
            "description": "输出对地短路",
            "cause": "1.驱动器动力线缆（U V W）对地发生短路 2.电机对地短路 3.驱动器故障",
            "solution": "请联系技术支持工程师",
        },
    },
    {
        "id": 13184,
        "level": 0,
        "en": {
            "description": "UVW phase sequence error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "UVW相序错误",
            "cause": "电机U V W与驱动器的U V W相序不对应",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 33922,
        "level": 0,
        "en": {
            "description": "Flying Cars",
            "cause": "",
            "solution": "Please contact technical support engineer",
        },
        "zh_CN": {
            "description": "飞车",
            "cause": "1.U V W相序接线错误 2.上电时，干扰信号导致电机转子初始相位检测错误 3.编码器型号错误或接线错误 4.编码器接线松动 5.负载过大",
            "solution": "请联系技术支持工程师",
        },
    },
    {
        "id": 12816,
        "level": 0,
        "en": {
            "description": "Electrical over-voltage in the main circuit",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "主回路电过压",
            "cause": "1.输入电压等级错误 2.制动电阻失效 3.制动电阻过大，吸收能量速度过慢",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 12832,
        "level": 0,
        "en": {
            "description": "Main circuit voltage undervoltage",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "主回路电压欠压",
            "cause": "1.输入电源电压不稳或者掉电 2.急加速过程中电压下降明显 3.伺服驱动器故障",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 12592,
        "level": 0,
        "en": {
            "description": "Main circuit electrical shortage",
            "cause": "",
            "solution": "Check the cable connection of power, otherwise, replace the driver",
        },
        "zh_CN": {
            "description": "主回路电缺相",
            "cause": "1.输入电源 R S T缺失2相 2.驱动器损坏",
            "solution": "1.确认输入电源接线是否正常 2.更换驱动器",
        },
    },
    {
        "id": 12576,
        "level": 0,
        "en": {
            "description": "Control of electrical undervoltage",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "控制电欠压",
            "cause": "1.控制电电源不稳定或者掉电 2.控制电线缆接触不良",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 33920,
        "level": 0,
        "en": {
            "description": "Overspeed",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "电机超速",
            "cause": "1.U V W相序接线错误 2.过速度故障判定阈值设置过小 3.电机速度超调 4.驱动器损坏",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 65296,
        "level": 0,
        "en": {
            "description": "Pulse output overspeed",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "脉冲输出过速",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 65282,
        "level": 0,
        "en": {
            "description": "Failure to identify angles",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "角度辨识失败",
            "cause": "电机编码器校零失败",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 9040,
        "level": 0,
        "en": {
            "description": "Drive overload",
            "cause": "",
            "solution": "Replace the driver",
        },
        "zh_CN": {
            "description": "驱动器过载",
            "cause": "电机与驱动器功率不匹配",
            "solution": "更换功率匹配的驱动器",
        },
    },
    {
        "id": 29056,
        "level": 0,
        "en": {
            "description": "Motor overload",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "电机过载",
            "cause": "1.负载过重，实效转矩超过额定转矩，长时间持续运转。2.增益调整不良导致发振、摆动动作。电机出现振动、异音。3.电机配线错误、断线。4.机械受到碰撞、机械突然变重，机械扭曲。5.制动器未打开时，电机动作。6.在多台机械配线中，误将电机线连接到其它轴，错误配线。",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 28961,
        "level": 0,
        "en": {
            "description": "Overheating protection for blocked motors",
            "cause": "",
            "solution": "Check whether the hardware is working properly, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "电机堵转过热保护",
            "cause": "1.电机被机械卡主 2.驱动器U V W输出缺相或者相序错误",
            "solution": "检查硬件是否正常，或联系技术支持工程师",
        },
    },
    {
        "id": 17168,
        "level": 0,
        "en": {
            "description": "Radiator overheating",
            "cause": "",
            "solution": "Drop the environment temperature, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "散热器过热",
            "cause": "1.环境温度过高2.驱动器风扇损坏 3.伺服驱动器内部故障",
            "solution": "降低环境温度，或联系技术支持工程师",
        },
    },
    {
        "id": 29571,
        "level": 0,
        "en": {
            "description": "Encoder battery failure",
            "cause": "",
            "solution": "Connect battery, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器电池失效",
            "cause": "1.断电期间，编码器未接电池 2.编码器电池电压过低",
            "solution": "接上电池, 或联系技术支持工程",
        },
    },
    {
        "id": 29490,
        "level": 0,
        "en": {
            "description": "Encoder multi-turn count error",
            "cause": "",
            "solution": "Replace the motor",
        },
        "zh_CN": {
            "description": "编码器多圈计数错误",
            "cause": "编码器故障",
            "solution": "更换电机",
        },
    },
    {
        "id": 29491,
        "level": 0,
        "en": {
            "description": "Encoder multi-turn count overflow",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器多圈计数溢出",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29492,
        "level": 0,
        "en": {
            "description": "Encoder interference",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器干扰",
            "cause": "编码器Z信号倍干扰，导致Z信号对应角度变化过大",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29493,
        "level": 0,
        "en": {
            "description": "External encoder scale failure",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "外部编码器标尺故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29494,
        "level": 0,
        "en": {
            "description": "Encoder data abnormalities",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器数据异常",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29495,
        "level": 0,
        "en": {
            "description": "Encoder return checksum exception",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器回送校验异常",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29496,
        "level": 0,
        "en": {
            "description": "Loss of encoder Z signal",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器Z信号丢失",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 34321,
        "level": 0,
        "en": {
            "description": "Excessive position deviation",
            "cause": "",
            "solution": "Check whether the motor is working properly, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "位置偏差过大",
            "cause": "1.电机未旋转 2.驱动器增益偏小 3.相对于运行条件，H0A.08设置过小",
            "solution": "1.确定电机是否被卡住 2.正确设置增益系数 3.设置合理的H0A.08的值",
        },
    },
    {
        "id": 34322,
        "level": 0,
        "en": {
            "description": "Position command too large",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "位置指令过大",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 34323,
        "level": 0,
        "en": {
            "description": "Excessive deviation from fully closed-loop position",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "全闭环位置偏差过大",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25380,
        "level": 0,
        "en": {
            "description": "Electronic gear setting overrun",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "电子齿轮设定超限",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25381,
        "level": 0,
        "en": {
            "description": "Wrong parameter setting for fully closed loop function",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "全闭环功能参数设置错误",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25382,
        "level": 0,
        "en": {
            "description": "Software position upper and lower limits set incorrectly",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "软件位置上下限设置错误",
            "cause": "对象字典0x607D-01h设置的数值小于0x607D-02h的值",
            "solution": "正确的设置0x607D-01h，0x607D-02h的值",
        },
    },
    {
        "id": 25383,
        "level": 0,
        "en": {
            "description": "Wrong home position offset setting",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "原点偏置设置错误",
            "cause": "原点偏置值在软件位置上下限之外",
            "solution": "正确的设置0x607D-01h，0x607D-02h的值，保证原点偏置值0x607C介于二者之间",
        },
    },
    {
        "id": 30083,
        "level": 0,
        "en": {"description": "Loss of synchronisation", "cause": "", "solution": ""},
        "zh_CN": {
            "description": "同步丢失",
            "cause": "同步通信时，主站同步信号丢失",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 30081,
        "level": 0,
        "en": {
            "description": "Unburned XML configuration file",
            "cause": "",
            "solution": "Burn the XML configuration file",
        },
        "zh_CN": {
            "description": "未烧录XML配置文件",
            "cause": "未烧录设备配置文件",
            "solution": "烧录设备配置文件",
        },
    },
    {
        "id": 65298,
        "level": 0,
        "en": {
            "description": "Network initialization failure",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "网络初始化失败",
            "cause": "1.未烧录FPGA固件 2.未烧录设备配置文件 3.驱动器故障",
            "solution": "1.烧录FPGA故障 2.烧录设备配置文件 3.更换伺服驱动器",
        },
    },
    {
        "id": 30082,
        "level": 0,
        "en": {
            "description": "Sync cycle configuration error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "同步周期配置错误",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 30084,
        "level": 0,
        "en": {
            "description": "Excessive synchronisation period error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "同步周期误差过大",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25384,
        "level": 0,
        "en": {
            "description": "Fault in crossover pulse output setting",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "分频脉冲输出设定故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 65521,
        "level": 0,
        "en": {
            "description": "Zero return timeout fault",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "回零点超时故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29570,
        "level": 0,
        "en": {
            "description": "Encoder battery warning",
            "cause": "",
            "solution": "Replace battery",
        },
        "zh_CN": {
            "description": "编码器电池警告",
            "cause": "电池电压低于3.0V",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21570,
        "level": 0,
        "en": {
            "description": "DI emergency brake",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "DI紧急刹车",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 12851,
        "level": 0,
        "en": {
            "description": "Motor overload warning",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "电机过载警告",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 12817,
        "level": 0,
        "en": {
            "description": "Brake resistor overload alarm",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "制动电阻过载报警",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25385,
        "level": 0,
        "en": {
            "description": "External braking resistor too small",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "外接制动电阻过小",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 13105,
        "level": 0,
        "en": {
            "description": "Motor power cable disconnection",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "电机动力线断线",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 25386,
        "level": 0,
        "en": {
            "description": "Change of parameters requires re-powering to take effect",
            "cause": "",
            "solution": "Clear the alarm and power on again",
        },
        "zh_CN": {
            "description": "变更参数需要重新上电生效",
            "cause": "修改的参数属于断电生效参数",
            "solution": "清除告警，并重新上电",
        },
    },
    {
        "id": 30208,
        "level": 0,
        "en": {
            "description": "Frequent parameter storage",
            "cause": "",
            "solution": "Check whether the upper computer is working normal, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "参数存储频繁",
            "cause": "上位机系统反复重新更改参数",
            "solution": "检查上位机是否工作异常，或联系技术支持工程师",
        },
    },
    {
        "id": 21571,
        "level": 0,
        "en": {
            "description": "Forward overtravel warning",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "正向超程警告",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21572,
        "level": 0,
        "en": {
            "description": "Reverse overtravel warning",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "反向超程警告",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29569,
        "level": 0,
        "en": {
            "description": "Internal failure of the encoder",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器内部故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 12597,
        "level": 0,
        "en": {
            "description": "Input phase failure warning",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "输入缺相警告",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 65432,
        "level": 0,
        "en": {
            "description": "Zero return mode setting error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "回零模式设置错误",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 65344,
        "level": 0,
        "en": {
            "description": "Parameter recognition failure",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "参数辨识失败",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21121,
        "level": 0,
        "en": {
            "description": "internal error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "内部错误",
            "cause": "看门狗复位",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29956,
        "level": 0,
        "en": {
            "description": "FPGA configuration error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "FPGA配置错误",
            "cause": "FPGA初始化失败",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 51020,
        "level": 0,
        "en": {
            "description": "Driver board identification error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "驱动板辨识错误",
            "cause": "PowerID错误",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29568,
        "level": 0,
        "en": {
            "description": "Encoder connection error",
            "cause": "",
            "solution": "Check the cable connection of encoder, or contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器连接错误",
            "cause": "1.编码器插头松动 2.编码器类型设置错误 3.电机编码器损坏 4.驱动器故障",
            "solution": "请检查编码器接线是否正常，或联系技术支持工程师",
        },
    },
    {
        "id": 8992,
        "level": 0,
        "en": {
            "description": "Software overcurrent",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "软件过流",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 9088,
        "level": 0,
        "en": {
            "description": "Current zero point too large",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "电流零点过大",
            "cause": "电流采样模块自举失败",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 30080,
        "level": 0,
        "en": {
            "description": "EtherCAT communication failure",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "EtherCAT通讯故障",
            "cause": "EtherCAT通讯断开",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 33921,
        "level": 0,
        "en": {
            "description": "Excessive speed tracking error",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "速度跟踪误差过大",
            "cause": "1.电机堵转 2.UVW输出断开 3.转矩输出限制 4.驱动器增益设置过小 5.驱动器或者电机损坏",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description": "STO Warning",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "STO警告",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 21569,
        "level": 0,
        "en": {
            "description": "Upper and lower board connection failure",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "上下板连接故障",
            "cause": "伺服控制板与驱动板连接异常",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 8980,
        "level": 0,
        "en": {
            "description": "Busbar overcurrent",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "母线过流",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 17169,
        "level": 0,
        "en": {
            "description": "Damaged or uninstalled temperature measuring resistors",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "测温电阻损坏或者未安装",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 29572,
        "level": 0,
        "en": {
            "description": "Encoder Eeprom reading CRC fault",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "编码器Eeprom读取CRC故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
    {
        "id": 12928,
        "level": 0,
        "en": {
            "description": "Servo and motor power matching faults",
            "cause": "",
            "solution": "System error, please contact technical support engineer",
        },
        "zh_CN": {
            "description": "伺服和电机功率匹配故障",
            "cause": "",
            "solution": "系统错误，请联系技术支持工程师",
        },
    },
]
