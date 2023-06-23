from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import Coord
import serial
import serial.tools.list_ports
import time

# Conection
port = "COM6"
baud = 115200
DEBUG = True
mycobot = MyCobot(port, baud, debug=DEBUG)

table = op('table_status')
setAngles = op('null_motor')
getAngles = mycobot.get_angles()
positions = mycobot.get_coords()
colorLED =  op('null_color')
motorSpeed = op('null_speed')
RecordAngle = op('constant_RecordAngle')
realTimeAngle = op('constant_realTimeAngle')
Log = op('table_log')
modeRecAngle = op('null_modeRecAngle')



# Error判定
Log[0,0] = "電源ステータス：" + str(mycobot.is_power_on())
Log[1,0] = "ロボットステータス：" + str(mycobot.read_next_error())
Log[2,0] = "サーボステータス：" + str(mycobot.is_all_servo_enable())
Log[3,0] = "Atomステータス：" + str(mycobot.is_controller_connected())

# 電源ON/OFF
# mycobot.power_on()
# mycobot.power_off()

if op('null_mode_manual')[0] == 1:
    # LED
    mycobot.set_color(int(colorLED[0]),int(colorLED[1]),int(colorLED[2]))
    # //Servo
    mycobot.send_angles([int(setAngles[0]),
                        int(setAngles[1]),
                        int(setAngles[2]),
                        int(setAngles[3]),
                        int(setAngles[4]),
                        int(setAngles[5])],
                        int(motorSpeed[0])
                        )

if op('null_mode_record')[0] == 1:
    # free mode
    if op('null_move')[0] == 1:
        mycobot.release_all_servos()
        getAngles = mycobot.get_angles()
        realTimeAngle.par.value0 = int(getAngles[0])
        realTimeAngle.par.value1 = int(getAngles[1])
        realTimeAngle.par.value2 = int(getAngles[2])
        realTimeAngle.par.value3 = int(getAngles[3])
        realTimeAngle.par.value4 = int(getAngles[4])
        realTimeAngle.par.value5 = int(getAngles[5])
    # record mode
    if op('null_record')[0] == 1:
        mycobot.release_all_servos()
        getAngles = mycobot.get_angles()
        realTimeAngle.par.value0 = int(getAngles[0])
        realTimeAngle.par.value1 = int(getAngles[1])
        realTimeAngle.par.value2 = int(getAngles[2])
        realTimeAngle.par.value3 = int(getAngles[3])
        realTimeAngle.par.value4 = int(getAngles[4])
        realTimeAngle.par.value5 = int(getAngles[5])
        # 角度取得
        getAngles = mycobot.get_angles()
        RecordAngle.par.value0 = int(getAngles[0])
        RecordAngle.par.value1 = int(getAngles[1])
        RecordAngle.par.value2 = int(getAngles[2])
        RecordAngle.par.value3 = int(getAngles[3])
        RecordAngle.par.value4 = int(getAngles[4])
        RecordAngle.par.value5 = int(getAngles[5])
    # play mode
    if op('null_play')[0] == 1:
        mycobot.send_angles([int(modeRecAngle[0]),
                            int(modeRecAngle[1]),
                            int(modeRecAngle[2]),
                            int(modeRecAngle[3]),
                            int(modeRecAngle[4]),
                            int(modeRecAngle[5])],
                            int(motorSpeed[0])
                            )
        # getAngles = mycobot.get_angles()
        # realTimeAngle.par.value0 = int(recordVal1[0])
        # realTimeAngle.par.value1 = int(recordVal1[1])
        # realTimeAngle.par.value2 = int(recordVal1[2])
        # realTimeAngle.par.value3 = int(recordVal1[3])
        # realTimeAngle.par.value4 = int(recordVal1[4])
        # realTimeAngle.par.value5 = int(recordVal1[5])
        # time.sleep(1)


Log[4,0] = "角度取得：" + str(getAngles)
Log[5,0] = "位置取得：" + str(positions)
sys.stdout = op('text_log')
