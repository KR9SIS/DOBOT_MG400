alarm_controller_list = [
    {
        "id": 0,
        "level": 0,
        "en": {"description": "No error", "cause": "", "solution": ""},
        "zh_CN": {"description": "无错误", "cause": "", "solution": ""},
    },
    {
        "id": 1,
        "level": 0,
        "en": {"description": "UniIO Borad dropped", "cause": "", "solution": ""},
        "zh_CN": {"description": "通用IO板掉线", "cause": "", "solution": ""},
    },
    {
        "id": 2,
        "level": 0,
        "en": {"description": "Axis 1 dropped", "cause": "", "solution": ""},
        "zh_CN": {"description": "关节1掉线", "cause": "", "solution": ""},
    },
    {
        "id": 3,
        "level": 0,
        "en": {"description": "Axis 2 dropped", "cause": "", "solution": ""},
        "zh_CN": {"description": "关节2掉线", "cause": "", "solution": ""},
    },
    {
        "id": 4,
        "level": 0,
        "en": {"description": "Axis 3 dropped", "cause": "", "solution": ""},
        "zh_CN": {"description": "关节3掉线", "cause": "", "solution": ""},
    },
    {
        "id": 5,
        "level": 0,
        "en": {"description": "Axis 4 dropped", "cause": "", "solution": ""},
        "zh_CN": {"description": "关节4掉线", "cause": "", "solution": ""},
    },
    {
        "id": 16,
        "level": 5,
        "en": {
            "description": "Inverse kinematics error with singularity",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "规划位置接近臂奇异点",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 17,
        "level": 5,
        "en": {
            "description": "Inverse kinematics error with no solution",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "逆解算无解",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 18,
        "level": 5,
        "en": {
            "description": "Target position triggers joint limit",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "目标位置触发关节限位",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 19,
        "level": 5,
        "en": {
            "description": "Duplicated data in JUMP or ARC or Circles instruction",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "JUMP或ARC或Circles指令点位重复",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 20,
        "level": 5,
        "en": {
            "description": "Wrong input parameters for arc",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "圆弧输入参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 21,
        "level": 5,
        "en": {
            "description": "The Start and the End is negative or the zLimit is below the start and end points",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "抬升高度、下降高度为负或者zLimit低于起始点和结束点的高度",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 22,
        "level": 5,
        "en": {
            "description": "Wrong arm orientation switch",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "手势切换错误",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 23,
        "level": 5,
        "en": {
            "description": "Plan point during linear motion out of working area",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "直线运动过程中规划点超出工作空间",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 24,
        "level": 5,
        "en": {
            "description": "Plan point during circular arc motion out of working area",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "圆弧运动过程中规划点超出工作空间",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 25,
        "level": 5,
        "en": {
            "description": "Wrong mode for motion instruction",
            "cause": "",
            "solution": "Internal software error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "运动指令模式错误",
            "cause": "",
            "solution": "内部软件错误，重启或联系厂商",
        },
    },
    {
        "id": 26,
        "level": 5,
        "en": {
            "description": "Wrong input parameters for speed",
            "cause": "",
            "solution": "input correct parameter",
        },
        "zh_CN": {
            "description": "速度输入参数错误",
            "cause": "",
            "solution": "输入正确的参数",
        },
    },
    {
        "id": 27,
        "level": 5,
        "en": {
            "description": "Wrong trajectory motion plan of continuous path",
            "cause": "",
            "solution": "input correct parameter",
        },
        "zh_CN": {
            "description": "CP轨迹运动规划错误",
            "cause": "",
            "solution": "输入正确的参数",
        },
    },
    {
        "id": 28,
        "level": 5,
        "en": {
            "description": "Wrong input parameters for circle",
            "cause": "",
            "solution": "input correct parameter",
        },
        "zh_CN": {
            "description": "整圆输入参数错误",
            "cause": "",
            "solution": "输入正确的参数",
        },
    },
    {
        "id": 29,
        "level": 5,
        "en": {
            "description": "Plan point during circular circle motion out of working circle",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "整圆运动过程中规划点超出工作空间",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 30,
        "level": 5,
        "en": {
            "description": "Inching target position inaccessible",
            "cause": "",
            "solution": "Reverse inch out of limit",
        },
        "zh_CN": {
            "description": "寸动目标位置不可达",
            "cause": "",
            "solution": "反向寸动离开限位",
        },
    },
    {
        "id": 32,
        "level": 5,
        "en": {
            "description": "Inverse kinematics singularity during moving",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "运动过程逆解算奇异",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 33,
        "level": 5,
        "en": {
            "description": "Inverse kinematics with no solution during moving",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "运动过程逆解算无解",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 34,
        "level": 5,
        "en": {
            "description": "Inverse kinematcis with result out of working area",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "运动过程逆解算限位",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 48,
        "level": 5,
        "en": {
            "description": "Joint1 overspeed",
            "cause": "",
            "solution": "Reset the speed or re-select the movement point away from the singularity",
        },
        "zh_CN": {
            "description": "关节1超速",
            "cause": "",
            "solution": "重新设置速度或重新选取运动点位远离奇异点",
        },
    },
    {
        "id": 49,
        "level": 5,
        "en": {
            "description": "Joint2 overspeed",
            "cause": "",
            "solution": "Reset the speed or re-select the movement point away from the singularity",
        },
        "zh_CN": {
            "description": "关节2超速",
            "cause": "",
            "solution": "重新设置速度或重新选取运动点位远离奇异点",
        },
    },
    {
        "id": 50,
        "level": 5,
        "en": {
            "description": "Joint3 overspeed",
            "cause": "",
            "solution": "Reset the speed or re-select the movement point away from the singularity",
        },
        "zh_CN": {
            "description": "关节3超速",
            "cause": "",
            "solution": "重新设置速度或重新选取运动点位远离奇异点",
        },
    },
    {
        "id": 51,
        "level": 5,
        "en": {
            "description": "Joint4 overspeed",
            "cause": "",
            "solution": "Reset the speed or re-select the movement point away from the singularity",
        },
        "zh_CN": {
            "description": "关节4超速",
            "cause": "",
            "solution": "重新设置速度或重新选取运动点位远离奇异点",
        },
    },
    {
        "id": 52,
        "level": 5,
        "en": {
            "description": "Joint1 position out of range",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节1位置超差",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 53,
        "level": 5,
        "en": {
            "description": "Joint2 position lag error",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节2位置超差",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 54,
        "level": 5,
        "en": {
            "description": "Joint3 position lag error",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节3位置超差",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 55,
        "level": 5,
        "en": {
            "description": "Joint4 position lag error",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节4位置超差",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 64,
        "level": 5,
        "en": {
            "description": "Joint1 exceeds positive limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节1正向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 65,
        "level": 5,
        "en": {
            "description": "Joint1 exceeds negative limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节1负向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 66,
        "level": 5,
        "en": {
            "description": "Joint2 exceeds positive limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节2正向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 67,
        "level": 5,
        "en": {
            "description": "Joint2 exceeds negative limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节2负向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 68,
        "level": 5,
        "en": {
            "description": "Joint3 exceeds positive limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节3正向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 69,
        "level": 5,
        "en": {
            "description": "Joint3 exceeds negative limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节3负向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 70,
        "level": 5,
        "en": {
            "description": "Joint4 exceeds positive limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节4正向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 71,
        "level": 5,
        "en": {
            "description": "Joint4 exceeds negative limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "关节4负向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 72,
        "level": 5,
        "en": {
            "description": "Parallelogram positive limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "平行四边形正向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 73,
        "level": 5,
        "en": {
            "description": "Parallelogram negative limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "平行四边形负向限位",
            "cause": "",
            "solution": "反向点动脱离限位",
        },
    },
    {
        "id": 74,
        "level": 5,
        "en": {
            "description": "Joint6 exceeds positive limit",
            "cause": "",
            "solution": "",
        },
        "zh_CN": {"description": "关节6正向限位", "cause": "", "solution": ""},
    },
    {
        "id": 75,
        "level": 5,
        "en": {
            "description": "Joint6 exceeds negative limit",
            "cause": "",
            "solution": "",
        },
        "zh_CN": {"description": "关节6负向限位", "cause": "", "solution": ""},
    },
    {
        "id": 80,
        "level": 0,
        "en": {
            "description": "Joint1 lose step",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节1位置丢失",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 81,
        "level": 0,
        "en": {
            "description": "Joint2 lose step",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节2位置丢失",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 82,
        "level": 0,
        "en": {
            "description": "Joint3 lose step",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节3位置丢失",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 83,
        "level": 0,
        "en": {
            "description": "Joint4 lose step",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "关节4位置丢失",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 84,
        "level": 5,
        "en": {
            "description": "Algorithm timeout",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "算法超时",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 85,
        "level": 0,
        "en": {
            "description": "Hardware emergency stop button press or software emergency stop trigger",
            "cause": "",
            "solution": "If the hardware emergency stop button is pressed, release the hardware emergency stop button; if the software emergency stop triggers, click the software emergency stop button again",
        },
        "zh_CN": {
            "description": "硬件急停按钮按下或软件急停触发",
            "cause": "",
            "solution": "如果硬件急停按钮按下则松开硬件急停按钮，如果软件急停触发则再次点击软件急停按钮",
        },
    },
    {
        "id": 86,
        "level": 0,
        "en": {
            "description": "User emergency button pressed",
            "cause": "",
            "solution": "Release the user emergency stop button",
        },
        "zh_CN": {
            "description": "用户急停被按下",
            "cause": "",
            "solution": "松开用户急停按钮",
        },
    },
    {
        "id": 96,
        "level": 0,
        "en": {
            "description": "Joint1 drive alarm",
            "cause": "",
            "solution": "Check if the communication of joint 1 is normal and then clear the error",
        },
        "zh_CN": {
            "description": "关节一伺服报警",
            "cause": "",
            "solution": "检查关节1通信是否正常再清除错误",
        },
    },
    {
        "id": 97,
        "level": 0,
        "en": {
            "description": "Joint1 Servo power off",
            "cause": "",
            "solution": "Re-enable joint 1",
        },
        "zh_CN": {
            "description": "关节一伺服掉电",
            "cause": "",
            "solution": "重新使能关节1",
        },
    },
    {
        "id": 98,
        "level": 0,
        "en": {
            "description": "Joint2 drive alarm",
            "cause": "",
            "solution": "Check if the communication of joint 2 is normal and then clear the error",
        },
        "zh_CN": {
            "description": "关节二伺服报警",
            "cause": "",
            "solution": "检查关节2通信是否正常再清除错误",
        },
    },
    {
        "id": 99,
        "level": 0,
        "en": {
            "description": "Joint2 Servo power off",
            "cause": "",
            "solution": "Re-enable joint 2",
        },
        "zh_CN": {
            "description": "关节二伺服掉电",
            "cause": "",
            "solution": "重新使能关节2",
        },
    },
    {
        "id": 100,
        "level": 0,
        "en": {
            "description": "Joint3 drive alarm",
            "cause": "",
            "solution": "Re-enable joint 3",
        },
        "zh_CN": {
            "description": "关节三伺服报警",
            "cause": "",
            "solution": "重新使能关节3",
        },
    },
    {
        "id": 101,
        "level": 0,
        "en": {
            "description": "Joint3 Servo power off",
            "cause": "",
            "solution": "Re-enable joint 3",
        },
        "zh_CN": {
            "description": "关节三伺服掉电",
            "cause": "",
            "solution": "重新使能关节3",
        },
    },
    {
        "id": 102,
        "level": 0,
        "en": {
            "description": "Joint4 drive alarm",
            "cause": "",
            "solution": "Re-enable joint 4",
        },
        "zh_CN": {
            "description": "关节四伺服报警",
            "cause": "",
            "solution": "重新使能关节4",
        },
    },
    {
        "id": 103,
        "level": 0,
        "en": {
            "description": "Joint4 drive power off",
            "cause": "",
            "solution": "Re-enable joint 4",
        },
        "zh_CN": {
            "description": "关节四伺服掉电",
            "cause": "",
            "solution": "重新使能关节4",
        },
    },
    {
        "id": 104,
        "level": 5,
        "en": {
            "description": "Robot homing failed",
            "cause": "",
            "solution": "Home again",
        },
        "zh_CN": {"description": "机器人回零失败", "cause": "", "solution": "重新回零"},
    },
    {
        "id": 105,
        "level": 5,
        "en": {
            "description": "Robot Servo on failed",
            "cause": "",
            "solution": "Check whether the hardware is normal and re-enable",
        },
        "zh_CN": {
            "description": "机器人使能失败",
            "cause": "",
            "solution": "检查硬件是否正常，重新使能",
        },
    },
    {
        "id": 106,
        "level": 5,
        "en": {"description": "Abnormal conveyor data", "cause": "", "solution": ""},
        "zh_CN": {"description": "传送带数据异常", "cause": "", "solution": ""},
    },
    {
        "id": 107,
        "level": 5,
        "en": {
            "description": "Abnormal conveyor synchronization",
            "cause": "",
            "solution": "",
        },
        "zh_CN": {"description": "传送带同步异常", "cause": "", "solution": ""},
    },
    {
        "id": 108,
        "level": 5,
        "en": {
            "description": "Conveyor conveyor encoder 1 is disconnected",
            "cause": "",
            "solution": "",
        },
        "zh_CN": {"description": "传送带编码器1断开连接", "cause": "", "solution": ""},
    },
    {
        "id": 109,
        "level": 5,
        "en": {
            "description": "Conveyor conveyor encoder 2 is disconnected",
            "cause": "",
            "solution": "",
        },
        "zh_CN": {"description": "传送带编码器2断开连接", "cause": "", "solution": ""},
    },
    {
        "id": 110,
        "level": 5,
        "en": {
            "description": "Encoder position error",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "伺服编码器数据超差",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 112,
        "level": 5,
        "en": {
            "description": "Collision Detection",
            "cause": "",
            "solution": "Keep away from the work area and continue to run",
        },
        "zh_CN": {
            "description": "碰撞检测停机",
            "cause": "",
            "solution": "离开工作区域，继续运行",
        },
    },
    {
        "id": 161,
        "level": 5,
        "en": {
            "description": "Error switching drag and drop mode",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "切换拖拽模式错误",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 4096,
        "level": 5,
        "en": {
            "description": "Faield to open mechanical file",
            "cause": "",
            "solution": "Check if the file location is correct and restart",
        },
        "zh_CN": {
            "description": "打开机械参数文件失败",
            "cause": "",
            "solution": "检查文件位置是否正确并重启",
        },
    },
    {
        "id": 8192,
        "level": 5,
        "en": {
            "description": "Faield to open project file",
            "cause": "",
            "solution": "Check if the file location is correct and restart",
        },
        "zh_CN": {
            "description": "打开工程文件失败",
            "cause": "",
            "solution": "检查文件位置是否正确并重启",
        },
    },
    {
        "id": 8193,
        "level": 5,
        "en": {
            "description": "Faield to open program file",
            "cause": "",
            "solution": "Check if the file location is correct and restart",
        },
        "zh_CN": {
            "description": "打开程序文件失败",
            "cause": "",
            "solution": "检查文件位置是否正确并重启",
        },
    },
    {
        "id": 8194,
        "level": 5,
        "en": {
            "description": "Faield to open global variable file",
            "cause": "",
            "solution": "Check if the file location is correct and restart",
        },
        "zh_CN": {
            "description": "打开全局参数文件失败",
            "cause": "",
            "solution": "检查文件位置是否正确并重启",
        },
    },
    {
        "id": 8195,
        "level": 5,
        "en": {
            "description": "Failed to open teaching point file",
            "cause": "",
            "solution": "Check if the file location is correct and restart",
        },
        "zh_CN": {
            "description": "打开示教点文件失败",
            "cause": "",
            "solution": "检查文件位置是否正确并重启",
        },
    },
    {
        "id": 8196,
        "level": 0,
        "en": {
            "description": "Failed to start debugger process",
            "cause": "",
            "solution": "Rerun",
        },
        "zh_CN": {
            "description": "启动调试进程失败",
            "cause": "",
            "solution": "重新运行",
        },
    },
    {
        "id": 12288,
        "level": 0,
        "en": {
            "description": "Emergency stop detected",
            "cause": "",
            "solution": "Power on again",
        },
        "zh_CN": {
            "description": "紧急停止按键按下",
            "cause": "",
            "solution": "重新上电",
        },
    },
    {
        "id": 12289,
        "level": 0,
        "en": {
            "description": "External emergency stop detected",
            "cause": "",
            "solution": "Power on again",
        },
        "zh_CN": {"description": "检测到外部急停", "cause": "", "solution": "重新上电"},
    },
    {
        "id": 12290,
        "level": 0,
        "en": {
            "description": "The servo power board temperature is too high",
            "cause": "",
            "solution": "Turn off the machine and let it cool for a period of time",
        },
        "zh_CN": {
            "description": "伺服功率板温度过高",
            "cause": "",
            "solution": "关闭机器后冷却一段时间",
        },
    },
    {
        "id": 12292,
        "level": 0,
        "en": {
            "description": "Safeguard stop detected",
            "cause": "",
            "solution": "After ensuring safety, restore the safeguard device",
        },
        "zh_CN": {
            "description": "检测到安全防护停止",
            "cause": "",
            "solution": "确保安全后，恢复安全防护装置",
        },
    },
    {
        "id": 12293,
        "level": 0,
        "en": {
            "description": "servor offline detected",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "检测到伺服通讯断开",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 12294,
        "level": 5,
        "en": {
            "description": "Collision Detection",
            "cause": "",
            "solution": "Keep away from the work area and continue to run",
        },
        "zh_CN": {
            "description": "碰撞检测停机",
            "cause": "",
            "solution": "离开工作区域，继续运行",
        },
    },
    {
        "id": 20480,
        "level": 5,
        "en": {
            "description": "AUX Joint1 exceeds positive limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "扩展轴1正向限位",
            "cause": "",
            "solution": "反向点动离开限位",
        },
    },
    {
        "id": 20481,
        "level": 5,
        "en": {
            "description": "AUX Joint1 exceeds negative limit",
            "cause": "",
            "solution": "Reverse jog out of limit",
        },
        "zh_CN": {
            "description": "扩展轴1负向限位",
            "cause": "",
            "solution": "反向点动离开限位",
        },
    },
    {
        "id": 20482,
        "level": 5,
        "en": {
            "description": "AUX Joint1 communication failed",
            "cause": "",
            "solution": "Check if the communication of AUX joint 1 is normal and then clear the error",
        },
        "zh_CN": {
            "description": "扩展轴1通讯中断",
            "cause": "",
            "solution": "检查扩展轴1线路连接是否异常",
        },
    },
    {
        "id": 20483,
        "level": 5,
        "en": {
            "description": "AUX Joint1 position out of working area",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "扩展轴1指令位置限位",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 20484,
        "level": 0,
        "en": {
            "description": "AUX Joint1 emergency stop button press",
            "cause": "",
            "solution": "release the hardware emergency stop button",
        },
        "zh_CN": {
            "description": "扩展轴急停按钮按下",
            "cause": "",
            "solution": "松开硬件急停按钮",
        },
    },
    {
        "id": 33024,
        "level": 5,
        "en": {
            "description": "No input parameters for CP instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "CP指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 33025,
        "level": 5,
        "en": {
            "description": "Input parameters of CP instruction out of range",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "CP指令参数超出范围",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 33280,
        "level": 5,
        "en": {
            "description": "No input parameters for Arch instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Arch指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 33281,
        "level": 5,
        "en": {
            "description": "Index parameter of Arch instruction out of range",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Arch指令索引超出范围",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 33282,
        "level": 5,
        "en": {
            "description": "Index parameter of Arch instruction not configured yet",
            "cause": "",
            "solution": "Please set index parameters",
        },
        "zh_CN": {
            "description": "Arch指令索引对应参数尚未设置",
            "cause": "",
            "solution": "请设置索引参数",
        },
    },
    {
        "id": 33536,
        "level": 5,
        "en": {
            "description": "No input parameters for LimZ instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "LimZ指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 33537,
        "level": 5,
        "en": {
            "description": "Input parameters of LimZ instruction out of range",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "LimZ指令参数超出范围",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 33792,
        "level": 5,
        "en": {
            "description": "No input parameters for Speed instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Speed指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 33793,
        "level": 5,
        "en": {
            "description": "Ratio parameter of Speed instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Speed指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 34048,
        "level": 5,
        "en": {
            "description": "No input parameters for Accel instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Accel指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 34049,
        "level": 5,
        "en": {
            "description": "Ratio parameter of Accel instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Accel指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 34304,
        "level": 5,
        "en": {
            "description": "No input parameters for Jerk instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Jerk指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 34305,
        "level": 5,
        "en": {
            "description": "Ratio parameter of Jerk instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Jerk指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 34560,
        "level": 5,
        "en": {
            "description": "No input parameters for SpeedS instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "SpeedS指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 34561,
        "level": 5,
        "en": {
            "description": "Ratio parameter of SpeedS instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SpeedS指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 34816,
        "level": 5,
        "en": {
            "description": "No input parameters for SpeedR instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "SpeedR指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 34817,
        "level": 5,
        "en": {
            "description": "Ratio parameter of SpeedR instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SpeedR指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 35072,
        "level": 5,
        "en": {
            "description": "No input parameters for AccelS instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "AccelS指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 35073,
        "level": 5,
        "en": {
            "description": "Ratio parameter of AccelS instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "AccelS指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 35328,
        "level": 5,
        "en": {
            "description": "No input parameters for AccelR instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "AccelR指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 35329,
        "level": 5,
        "en": {
            "description": "Ratio parameter of AccelR instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "AccelR指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 35584,
        "level": 5,
        "en": {
            "description": "No input parameters for JerkS instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "JerkS指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 35585,
        "level": 5,
        "en": {
            "description": "Ratio parameter of JerkS instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "JerkS指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 35840,
        "level": 5,
        "en": {
            "description": "No input parameters for JerkR instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "JerkR指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 35841,
        "level": 5,
        "en": {
            "description": "Ratio parameter of JerkR instruction out of range [1, 100]",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "JerkR指令比例参数超出范围[1, 100]",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36096,
        "level": 5,
        "en": {
            "description": "No input parameters for Go instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Go指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36097,
        "level": 5,
        "en": {
            "description": "No motion point parameter for Go instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Go指令缺少坐标点参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36098,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for Go instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Go指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36099,
        "level": 5,
        "en": {
            "description": "Incorrect control parameter for Go instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Go指令控制参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36352,
        "level": 5,
        "en": {
            "description": "No input parameters for Move instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Move指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36353,
        "level": 5,
        "en": {
            "description": "No motion point parameter for Move instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Move指令缺少坐标点参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36354,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for Move instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Move指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36355,
        "level": 5,
        "en": {
            "description": "Incorrect control parameter for Move instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Move指令控制参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36608,
        "level": 5,
        "en": {
            "description": "No input parameters for Arch3 instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Arch3指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36609,
        "level": 5,
        "en": {
            "description": "No motion point parameter for Arch3 instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Arch3指令缺少坐标点参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36610,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for Arch3 instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Arch3指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36611,
        "level": 5,
        "en": {
            "description": "Incorrect control parameter for Arch3 instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Arch3指令控制参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36864,
        "level": 5,
        "en": {
            "description": "No input parameters for Jump instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Jump指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36865,
        "level": 5,
        "en": {
            "description": "No motion point parameter for Jump instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Jump指令缺少坐标点参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 36866,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for Jump instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Jump指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36867,
        "level": 5,
        "en": {
            "description": "Incorrect control parameter for Jump instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Jump指令控制参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 40960,
        "level": 5,
        "en": {
            "description": "No input parameters for Circle3 instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Circle3指令无输入参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 40961,
        "level": 5,
        "en": {
            "description": "No motion point parameter for Circle3 instruction",
            "cause": "",
            "solution": "Please enter parameters",
        },
        "zh_CN": {
            "description": "Circle3指令缺少坐标点参数",
            "cause": "",
            "solution": "请输入参数",
        },
    },
    {
        "id": 40962,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for Circle3 instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Circle3指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 40963,
        "level": 5,
        "en": {
            "description": "Incorrect control parameter for Circle3 instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Circle3指令控制参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45056,
        "level": 5,
        "en": {
            "description": "Circle3 Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Circle3 Option 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45057,
        "level": 5,
        "en": {
            "description": "Jump  Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Jump  Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45058,
        "level": 5,
        "en": {
            "description": "Arch Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Arch Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45059,
        "level": 5,
        "en": {
            "description": "Arch3 Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Arch3 Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45060,
        "level": 5,
        "en": {
            "description": "Jerk Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Jerk Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45061,
        "level": 5,
        "en": {
            "description": "JerkR Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "JerkR Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45062,
        "level": 5,
        "en": {
            "description": "JerkS Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "JerkS Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45063,
        "level": 5,
        "en": {
            "description": "Accel Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Accel Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45064,
        "level": 5,
        "en": {
            "description": "AccelR Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "AccelR Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45065,
        "level": 5,
        "en": {
            "description": "AccelS Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "AccelS Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45066,
        "level": 5,
        "en": {
            "description": "SpeedFactor Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SpeedFactor Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45067,
        "level": 5,
        "en": {
            "description": "Speed Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Speed Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45068,
        "level": 5,
        "en": {
            "description": "SpeedR Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SpeedR Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45069,
        "level": 5,
        "en": {
            "description": "Limz Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Limz Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45070,
        "level": 5,
        "en": {
            "description": "CP Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "CP Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45071,
        "level": 5,
        "en": {
            "description": "DO Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "DO Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45072,
        "level": 5,
        "en": {
            "description": "Go Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Go Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45073,
        "level": 5,
        "en": {
            "description": "Move Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Move Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45074,
        "level": 5,
        "en": {
            "description": "MoveJ Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJ Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45075,
        "level": 5,
        "en": {
            "description": "Ecp Option  Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Ecp Option   参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45076,
        "level": 5,
        "en": {
            "description": "EcpSet Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "EcpSet Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45077,
        "level": 5,
        "en": {
            "description": "SetExicitMode Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SetExicitMode Option  参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 106,
        "level": 5,
        "en": {
            "description": "Conveyor tracking stop failed Error",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "传送带跟踪停止失败",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 107,
        "level": 5,
        "en": {
            "description": "Conveyor tracking synchronization failed Error",
            "cause": "",
            "solution": "Internal error, restart or contact manufacturer",
        },
        "zh_CN": {
            "description": "传送带跟踪同步失败",
            "cause": "",
            "solution": "内部错误，重启或联系厂商",
        },
    },
    {
        "id": 32768,
        "level": 5,
        "en": {
            "description": "No input parameters for speedFactor instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SpeedFactor指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 32769,
        "level": 5,
        "en": {
            "description": "Input parameters of speedFactor instruction out of range",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "SpeedFactor指令参数超出范围",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 32770,
        "level": 5,
        "en": {
            "description": "DO input parameters Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "DO 输入参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 32771,
        "level": 5,
        "en": {
            "description": "DI input parameters Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "DI 输入参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 32776,
        "level": 5,
        "en": {
            "description": "DOGroup params number err",
            "cause": "",
            "solution": "params is too much",
        },
        "zh_CN": {
            "description": "DOGroup 参数数量错误",
            "cause": "",
            "solution": "点位过多，最好不要一次输入超过100个点",
        },
    },
    {
        "id": 32777,
        "level": 5,
        "en": {
            "description": "DOGroup have some params's index out of range",
            "cause": "",
            "solution": "input correct params",
        },
        "zh_CN": {
            "description": "DOGroup 参数中存在的点位索引 超出边界",
            "cause": "",
            "solution": "请核对点位范围",
        },
    },
    {
        "id": 32778,
        "level": 5,
        "en": {
            "description": "DOGroup have some params's index type error",
            "cause": "",
            "solution": "input correct params",
        },
        "zh_CN": {
            "description": "DOGroup 参数中存在的点位索引的类型错误",
            "cause": "",
            "solution": "只能输入数字",
        },
    },
    {
        "id": 32779,
        "level": 5,
        "en": {
            "description": "DOGroup have some params's value type error",
            "cause": "",
            "solution": "input correct params,number type and boolean is needed eg.(0/1) || (true/false) || (ON/OFF)",
        },
        "zh_CN": {
            "description": "DOGroup 参数中存在的点位输出值的类型错误",
            "cause": "",
            "solution": "请输入数字(0/1)或bool(true/false)或内置的 ON/OFF",
        },
    },
    {
        "id": 32780,
        "level": 5,
        "en": {
            "description": "DOGroup have some params's isqueue type error",
            "cause": "",
            "solution": "eg.(0/1) || (true/false) || (ON/OFF) . true means queue command(default),false:Immediate command",
        },
        "zh_CN": {
            "description": "DOGroup 参数中存在的可选参数 指令类型的类型错误",
            "cause": "",
            "solution": "请输入数字(0/1)或bool(true/false)或内置的 ON/OFF 真 : 队列指令(默认) 假: 立即指令",
        },
    },
    {
        "id": 32781,
        "level": 5,
        "en": {
            "description": "DOGroup err internal ",
            "cause": "",
            "solution": "internal error has happend,try again.",
        },
        "zh_CN": {
            "description": "DOGroup 发生内部错误",
            "cause": "",
            "solution": "再次尝试，如果一直存在错误，请联系技术支持",
        },
    },
    {
        "id": 36100,
        "level": 5,
        "en": {
            "description": "No input parameters for movej instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJ指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36101,
        "level": 5,
        "en": {
            "description": "No motion point parameter for  movej instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJ指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36102,
        "level": 5,
        "en": {
            "description": "No motion point parameter for  movej instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJ指令缺少坐标点参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36103,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for  RP instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "RP 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36104,
        "level": 5,
        "en": {
            "description": "Incorrect offset for  RP instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "RP 偏移值参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36105,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for  RJ instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "RJ 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36106,
        "level": 5,
        "en": {
            "description": "Incorrect offset for  RJ instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "RJ 偏移值参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36107,
        "level": 5,
        "en": {
            "description": "No input parameters for GoR instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "GoR 指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36108,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for  GoR instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "GoR 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36109,
        "level": 5,
        "en": {
            "description": "No input parameters for MoveJR instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJR 指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36110,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for  MoveJR instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJR 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36121,
        "level": 5,
        "en": {
            "description": "RP Inverse kinematics error with no solution",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "RP指令给定点位逆解算无解",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 36122,
        "level": 5,
        "en": {
            "description": "RP Inverse kinematics error with result out of working area",
            "cause": "",
            "solution": "Reselect movement points",
        },
        "zh_CN": {
            "description": "RP指令给定点位逆解算超限位",
            "cause": "",
            "solution": "重新选取运动点位",
        },
    },
    {
        "id": 45079,
        "level": 5,
        "en": {
            "description": "loadSwitch Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "loadSwitch Option参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45080,
        "level": 5,
        "en": {
            "description": "loadSet Options Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "loadSet Options参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45081,
        "level": 5,
        "en": {
            "description": "CPParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option CP 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45082,
        "level": 5,
        "en": {
            "description": "TOOLParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option TOOL 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45083,
        "level": 5,
        "en": {
            "description": "USERParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option USERParam 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45084,
        "level": 5,
        "en": {
            "description": "SPEEDParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option SPEED 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45085,
        "level": 5,
        "en": {
            "description": "SPEEDSParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option SPEEDS 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45086,
        "level": 5,
        "en": {
            "description": "ACCELParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option ACCEL 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45087,
        "level": 5,
        "en": {
            "description": "ACCELSParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option ACCELS 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45088,
        "level": 5,
        "en": {
            "description": "ARCHParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option ARCH 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45089,
        "level": 5,
        "en": {
            "description": "STARTParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option START 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45090,
        "level": 5,
        "en": {
            "description": "ZLIMITParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option ZLIMIT 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45091,
        "level": 5,
        "en": {
            "description": "ENDParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option END 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45092,
        "level": 5,
        "en": {
            "description": "SYNCaramErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option SYNC 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45093,
        "level": 5,
        "en": {
            "description": "ARMParamErrorOption",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "Option ARM 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45312,
        "level": 5,
        "en": {
            "description": "loadSwitch Option Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "loadSwitch Option参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 45313,
        "level": 5,
        "en": {
            "description": "loadSet Options Error",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "loadSet Options参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 49152,
        "level": 5,
        "en": {
            "description": "Enable remote control when enabled",
            "cause": "",
            "solution": "Next enable and then switch",
        },
        "zh_CN": {
            "description": "使能状态下，启动远程控制",
            "cause": "",
            "solution": "下使能后再切换",
        },
    },
    {
        "id": 36111,
        "level": 5,
        "en": {
            "description": "No input parameters for GoIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "GoIO 指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36112,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for GoIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "GoIO 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36113,
        "level": 5,
        "en": {
            "description": "Incorrect parameters for GoIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "GoIO IO 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36114,
        "level": 5,
        "en": {
            "description": "No input parameters for MoveIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveIO 指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36115,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for MoveIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveIO 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36116,
        "level": 5,
        "en": {
            "description": "Incorrect parameters for MoveIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveIO IO 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36117,
        "level": 5,
        "en": {
            "description": "No input parameters for MoveJIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJIO 指令无输入参数",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36118,
        "level": 5,
        "en": {
            "description": "Incorrect motion point for MoveJIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJIO 指令坐标点参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
    {
        "id": 36119,
        "level": 5,
        "en": {
            "description": "No input parameters for MoveJIO instruction",
            "cause": "",
            "solution": "Enter the correct parameters",
        },
        "zh_CN": {
            "description": "MoveJIO IO 参数错误",
            "cause": "",
            "solution": "输入正确参数",
        },
    },
]
