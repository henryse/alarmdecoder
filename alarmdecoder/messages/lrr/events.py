"""
Constants and utility functions used for LRR event handling.

.. moduleauthor:: Scott Petersen <scott@nutech.com>
"""


def get_event_description(event_type, event_code):
    """
    Retrieves the human-readable description of an LRR event.

    :param event_type: Base LRR event type.  Use LRR_EVENT_TYPE.*
    :type event_type: int
    :param event_code: LRR event code
    :type event_code: int

    :returns: string
    """
    description = 'Unknown'
    lookup_map = LRR_TYPE_MAP.get(event_type, None)

    if lookup_map is not None:
        description = lookup_map.get(event_code, description)

    return description


def get_event_source(prefix):
    """
    Retrieves the LRR_EVENT_TYPE corresponding to the prefix provided.abs

    :param prefix: Prefix to convert to event type
    :type prefix: string

    :returns: int
    """
    source = LRR_EVENT_TYPE.UNKNOWN

    if prefix == 'CID':
        source = LRR_EVENT_TYPE.CID
    elif prefix == 'DSC':
        source = LRR_EVENT_TYPE.DSC
    elif prefix == 'AD2':
        source = LRR_EVENT_TYPE.ALARMDECODER
    elif prefix == 'ADEMCO':
        source = LRR_EVENT_TYPE.ADEMCO

    return source


# noinspection PyPep8Naming
class LRR_EVENT_TYPE:
    """
    Base LRR event types
    """
    CID = 1
    DSC = 2
    ADEMCO = 3
    ALARMDECODER = 4
    UNKNOWN = 5


# noinspection PyPep8Naming
class LRR_EVENT_STATUS:
    """
    LRR event status codes
    """
    TRIGGER = 1
    RESTORE = 3


# noinspection PyPep8Naming
class LRR_CID_EVENT:
    """
    ContactID event codes
    """
    MEDICAL = 0x100
    MEDICAL_PENDANT = 0x101
    MEDICAL_FAIL_TO_REPORT = 0x102
    # 103-108: ?
    TAMPER_ZONE = 0x109  # NOTE: Where did we find this?
    FIRE = 0x110
    FIRE_SMOKE = 0x111
    FIRE_COMBUSTION = 0x112
    FIRE_WATER_FLOW = 0x113
    FIRE_HEAT = 0x114
    FIRE_PULL_STATION = 0x115
    FIRE_DUCT = 0x116
    FIRE_FLAME = 0x117
    FIRE_NEAR_ALARM = 0x118
    PANIC = 0x120
    PANIC_DURESS = 0x121
    PANIC_SILENT = 0x122
    PANIC_AUDIBLE = 0x123
    PANIC_DURESS_ACCESS_GRANTED = 0x124
    PANIC_DURESS_EGRESS_GRANTED = 0x125
    PANIC_HOLDUP_SUSPICION = 0x126
    # 127-128: ?
    PANIC_HOLDUP_VERIFIER = 0x129
    BURGLARY = 0x130
    BURGLARY_PERIMETER = 0x131
    BURGLARY_INTERIOR = 0x132
    BURGLARY_AUX = 0x133
    BURGLARY_ENTRYEXIT = 0x134
    BURGLARY_DAYNIGHT = 0x135
    BURGLARY_OUTDOOR = 0x136
    BURGLARY_TAMPER = 0x137
    BURGLARY_NEAR_ALARM = 0x138
    BURGLARY_INTRUSION_VERIFIER = 0x139
    ALARM_GENERAL = 0x140
    ALARM_POLLING_LOOP_OPEN = 0x141
    ALARM_POLLING_LOOP_SHORT = 0x142
    ALARM_EXPANSION_MOD_FAILURE = 0x143
    ALARM_SENSOR_TAMPER = 0x144
    ALARM_EXPANSION_MOD_TAMPER = 0x145
    BURGLARY_SILENT = 0x146
    TROUBLE_SENSOR_SUPERVISION = 0x147
    # 148-149: ?
    ALARM_AUX = 0x150
    ALARM_GAS_DETECTED = 0x151
    ALARM_REFRIDGERATION = 0x152
    ALARM_LOSS_OF_HEAT = 0x153
    ALARM_WATER_LEAKAGE = 0x154
    TROUBLE_FOIL_BREAK = 0x155
    TROUBLE_DAY_TROUBLE = 0x156
    ALARM_LOW_BOTTLED_GAS_LEVEL = 0x157
    ALARM_HIGH_TEMP = 0x158
    ALARM_LOW_TEMP = 0x159
    # 160: ?
    ALARM_LOSS_OF_AIR_FLOW = 0x161
    ALARM_CARBON_MONOXIDE = 0x162
    TROUBLE_TANK_LEVEL = 0x163
    # 164-167: ?
    TROUBLE_HIGH_HUMIDITY = 0x168
    TROUBLE_LOW_HUMIDITY = 0x169
    # 170-199: ?
    SUPERVISORY_FIRE = 0x200
    SUPERVISORY_LOW_PRESSURE = 0x201
    SUPERVISORY_LOW_CO2 = 0x202
    SUPERVISORY_GATE_VALVE_SENSOR = 0x203
    SUPERVISORY_LOW_WATER_LEVEL = 0x204
    SUPERVISORY_PUMP_ACTIVATED = 0x205
    SUPERVISORY_PUMP_FAILURE = 0x206
    # 207-299: ?
    TROUBLE_SYSTEM_TROUBLE = 0x300
    TROUBLE_AC_LOSS = 0x301
    TROUBLE_LOW_BATTERY = 0x302
    TROUBLE_RAM_CHECKSUM_BAD = 0x303
    TROUBLE_ROM_CHECKSUM_BAD = 0x304
    TROUBLE_RESET = 0x305
    TROUBLE_PANEL_PROGRAMMING_CHANGED = 0x306
    TROUBLE_SELF_TEST_FAILURE = 0x307
    TROUBLE_SHUTDOWN = 0x308
    TROUBLE_BATTERY_TEST_FAIL = 0x309
    TROUBLE_GROUND_FAULT = 0x310
    TROUBLE_BATTERY_MISSING = 0x311
    TROUBLE_POWER_SUPPLY_OVERCURRENT = 0x312
    STATUS_ENGINEER_RESET = 0x313
    TROUBLE_PRIMARY_POWER_SUPPLY_FAILURE = 0x314
    # 315: ?
    TROUBLE_TAMPER = 0x316
    # 317-319: ?
    TROUBLE_SOUNDER = 0x320
    TROUBLE_BELL_1 = 0x321
    TROUBLE_BELL_2 = 0x322
    TROUBLE_ALARM_RELAY = 0x323
    TROUBLE_TROUBLE_RELAY = 0x324
    TROUBLE_REVERSING_RELAY = 0x325
    TROUBLE_NOTIFICATION_APPLIANCE_CIRCUIT_3 = 0x326
    TROUBLE_NOTIFICATION_APPLIANCE_CIRCUIT_4 = 0x327
    # 328-329: ?
    TROUBLE_SYSTEM_PERIPHERAL = 0x330
    TROUBLE_POLLING_LOOP_OPEN = 0x331
    TROUBLE_POLLING_LOOP_SHORT = 0x332
    TROUBLE_EXPANSION_MODULE_FAILURE = 0x333
    TROUBLE_REPEATER_FAILURE = 0x334
    TROUBLE_LOCAL_PRINTER_PAPER_OUT = 0x335
    TROUBLE_LOCAL_PRINTER_FAILURE = 0x336
    TROUBLE_EXPANDER_MODULE_DC_LOSS = 0x337
    TROUBLE_EXPANDER_MODULE_LOW_BATTERY = 0x338
    TROUBLE_EXPANDER_MODULE_RESET = 0x339
    # 340: ?
    TROUBLE_EXPANDER_MODULE_TAMPER = 0x341
    TROUBLE_EXPANDER_MODULE_AC_LOSS = 0x342
    TROUBLE_EXPANDER_MODULE_SELF_TEST_FAIL = 0x343
    TROUBLE_RF_RECEIVER_JAM_DETECTED = 0x344
    TROUBLE_AES_ENCRYPTION = 0x345
    # 346-349: ?
    TROUBLE_COMMUNICATION = 0x350
    TROUBLE_TELCO_1_FAULT = 0x351
    TROUBLE_TELCO_2_FAULT = 0x352
    TROUBLE_LRR_TRANSMITTER_FAULT = 0x353
    TROUBLE_FAILURE_TO_COMMUNICATE = 0x354
    TROUBLE_LOSS_OF_RADIO_SUPERVISION = 0x355
    TROUBLE_LOSS_OF_CENTRAL_POLLING = 0x356
    TROUBLE_LRR_TRANSMITTER_VSWR = 0x357
    TROUBLE_PERIODIC_COMM_TEST = 0x358
    # 359-369: ?
    TROUBLE_PROTECTION_LOOP = 0x370
    TROUBLE_PROTECTION_LOOP_OPEN = 0x371
    TROUBLE_PROTECTION_LOOP_SHORT = 0x372
    TROUBLE_FIRE = 0x373
    TROUBLE_EXIT_ERROR = 0x374
    TROUBLE_PANIC_ZONE_TROUBLE = 0x375
    TROUBLE_HOLDUP_ZONE_TROUBLE = 0x376
    TROUBLE_SWINGER_TROUBLE = 0x377
    TROUBLE_CROSS_ZONE_TROUBLE = 0x378
    # 379: ?
    TROUBLE_SENSOR_TROUBLE = 0x380
    TROUBLE_RF_LOSS_OF_SUPERVISION = 0x381
    TROUBLE_RPM_LOSS_OF_SUPERVISION = 0x382
    TROUBLE_SENSOR_TAMPER = 0x383
    TROUBLE_RF_LOW_BATTERY = 0x384
    TROUBLE_SMOKE_HI_SENS = 0x385
    TROUBLE_SMOKE_LO_SENS = 0x386
    TROUBLE_INTRUSION_HI_SENS = 0x387
    TROUBLE_INTRUSION_LO_SENS = 0x388
    TROUBLE_SELF_TEST_FAIL = 0x389
    # 390: ?
    TROUBLE_SENSOR_WATCH_FAIL = 0x391
    TROUBLE_DRIFT_COMP_ERROR = 0x392
    TROUBLE_MAINTENANCE_ALERT = 0x393
    # 394-399: ?
    OPENCLOSE = 0x400
    OPENCLOSE_BY_USER = 0x401
    OPENCLOSE_GROUP = 0x402
    OPENCLOSE_AUTOMATIC = 0x403
    OPENCLOSE_LATE = 0x404
    OPENCLOSE_DEFERRED = 0x405
    OPENCLOSE_CANCEL_BY_USER = 0x406
    OPENCLOSE_REMOTE_ARMDISARM = 0x407
    OPENCLOSE_QUICK_ARM = 0x408
    OPENCLOSE_KEYSWITCH = 0x409
    # 410: ?
    REMOTE_CALLBACK_REQUESTED = 0x411
    REMOTE_SUCCESS = 0x412
    REMOTE_UNSUCCESSFUL = 0x413
    REMOTE_SYSTEM_SHUTDOWN = 0x414
    REMOTE_DIALER_SHUTDOWN = 0x415
    REMOTE_SUCCESSFUL_UPLOAD = 0x416
    # 417-420: ?
    ACCESS_DENIED = 0x421
    ACCESS_REPORT_BY_USER = 0x422
    ACCESS_FORCED_ACCESS = 0x423
    ACCESS_EGRESS_DENIED = 0x424
    ACCESS_EGRESS_GRANTED = 0x425
    ACCESS_DOOR_PROPPED_OPEN = 0x426
    ACCESS_POINT_DSM_TROUBLE = 0x427
    ACCESS_POINT_RTE_TROUBLE = 0x428
    ACCESS_PROGRAM_MODE_ENTRY = 0x429
    ACCESS_PROGRAM_MODE_EXIT = 0x430
    ACCESS_THREAT_LEVEL_CHANGE = 0x431
    ACCESS_RELAY_FAIL = 0x432
    ACCESS_RTE_SHUNT = 0x433
    ACCESS_DSM_SHUNT = 0x434
    ACCESS_SECOND_PERSON = 0x435
    ACCESS_IRREGULAR_ACCESS = 0x436
    # 437-440: ?
    OPENCLOSE_ARMED_STAY = 0x441
    OPENCLOSE_KEYSWITCH_ARMED_STAY = 0x442
    # 443-449: ?
    OPENCLOSE_EXCEPTION = 0x450
    OPENCLOSE_EARLY = 0x451
    OPENCLOSE_LATE = 0x452
    TROUBLE_FAILED_TO_OPEN = 0x453
    TROUBLE_FAILED_TO_CLOSE = 0x454
    TROUBLE_AUTO_ARM_FAILED = 0x455
    OPENCLOSE_PARTIAL_ARM = 0x456
    OPENCLOSE_EXIT_ERROR = 0x457
    OPENCLOSE_USER_ON_PREMISES = 0x458
    TROUBLE_RECENT_CLOSE = 0x459
    # 460: ?
    ACCESS_WRONG_CODE_ENTRY = 0x461
    ACCESS_LEGAL_CODE_ENTRY = 0x462
    STATUS_REARM_AFTER_ALARM = 0x463
    STATUS_AUTO_ARM_TIME_EXTENDED = 0x464
    STATUS_PANIC_ALARM_RESET = 0x465
    ACCESS_SERVICE_ONOFF_PREMISES = 0x466
    # 467-469: ?
    OPENCLOSE_PARTIAL_CLOSING = 0x470
    # HACK: This is from our DSC firmware implementation,
    #       and is named far too closely to 0x480.
    # 471-479: ?
    OPENCLOSE_PARTIAL_CLOSE = 0x480
    # 481-500: ?
    DISABLE_ACCESS_READER = 0x501
    # 502-519: ?
    DISABLE_SOUNDER = 0x520
    DISABLE_BELL_1 = 0x521
    DISABLE_BELL_2 = 0x522
    DISABLE_ALARM_RELAY = 0x523
    DISABLE_TROUBLE_RELAY = 0x524
    DISABLE_REVERSING_RELAY = 0x525
    DISABLE_NOTIFICATION_APPLIANCE_CIRCUIT_3 = 0x526
    DISABLE_NOTIFICATION_APPLIANCE_CIRCUIT_4 = 0x527
    # 528-530: ?
    SUPERVISORY_MODULE_ADDED = 0x531
    SUPERVISORY_MODULE_REMOVED = 0x532
    # 533-550: ?
    DISABLE_DIALER = 0x551
    DISABLE_RADIO_TRANSMITTER = 0x552
    DISABLE_REMOTE_UPLOADDOWNLOAD = 0x553
    # 554-569: ?
    BYPASS_ZONE = 0x570
    BYPASS_FIRE = 0x571
    BYPASS_24HOUR_ZONE = 0x572
    BYPASS_BURGLARY = 0x573
    BYPASS_GROUP = 0x574
    BYPASS_SWINGER = 0x575
    BYPASS_ACCESS_ZONE_SHUNT = 0x576
    BYPASS_ACCESS_POINT_BYPASS = 0x577
    BYPASS_ZONE_VAULT = 0x578
    BYPASS_ZONE_VENT = 0x579
    # 580-600: ?
    TEST_MANUAL = 0x601
    TEST_PERIODIC = 0x602
    TEST_PERIODIC_RF_TRANSMISSION = 0x603
    TEST_FIRE = 0x604
    TEST_FIRE_STATUS = 0x605
    TEST_LISTENIN_TO_FOLLOW = 0x606
    TEST_WALK = 0x607
    TEST_SYSTEM_TROUBLE_PRESENT = 0x608
    TEST_VIDEO_TRANSMITTER_ACTIVE = 0x609
    # 610: ?
    TEST_POINT_TESTED_OK = 0x611
    TEST_POINT_NOT_TESTED = 0x612
    TEST_INTRUSION_ZONE_WALK_TESTED = 0x613
    TEST_FIRE_ZONE_WALK_TESTED = 0x614
    TEST_PANIC_ZONE_WALK_TESTED = 0x615
    TROUBLE_SERVICE_REQUEST = 0x616
    # 617-620: ?
    TROUBLE_EVENT_LOG_RESET = 0x621
    TROUBLE_EVENT_LOG_50PERCENT_FULL = 0x622
    TROUBLE_EVENT_LOG_90PERCENT_FULL = 0x623
    TROUBLE_EVENT_LOG_OVERFLOW = 0x624
    TROUBLE_TIMEDATE_RESET = 0x625
    TROUBLE_TIMEDATE_INACCURATE = 0x626
    TROUBLE_PROGRAM_MODE_ENTRY = 0x627
    TROUBLE_PROGRAM_MODE_EXIT = 0x628
    TROUBLE_32HOUR_EVENT_LOG_MARKER = 0x629
    SCHEDULE_CHANGE = 0x630
    SCHEDULE_EXCEPTION_SCHEDULE_CHANGE = 0x631
    SCHEDULE_ACCESS_SCHEDULE_CHANGE = 0x632
    # 633-640: ?
    TROUBLE_SENIOR_WATCH_TROUBLE = 0x641
    STATUS_LATCHKEY_SUPERVISION = 0x642
    # 643-650: ?
    SPECIAL_ADT_AUTHORIZATION = 0x651
    RESERVED_652 = 0x652
    RESERVED_653 = 0x653
    TROUBLE_SYSTEM_INACTIVITY = 0x654
    # 750-789: User Assigned
    # 790-795: ?
    TROUBLE_UNABLE_TO_OUTPUT_SIGNAL = 0x796
    # 797: ?
    TROUBLE_STU_CONTROLLER_DOWN = 0x798
    # 799-899: ?
    REMOTE_DOWNLOAD_ABORT = 0x900
    REMOTE_DOWNLOAD_STARTEND = 0x901
    REMOTE_DOWNLOAD_INTERRUPTED = 0x902
    REMOTE_CODE_DOWNLOAD_STARTEND = 0x903
    REMOTE_CODE_DOWNLOAD_FAILED = 0x904
    # 905-909: ?
    OPENCLOSE_AUTOCLOSE_WITH_BYPASS = 0x910
    OPENCLOSE_BYPASS_CLOSING = 0x911
    EVENT_FIRE_ALARM_SILENCED = 0x912
    EVENT_SUPERVISOR_POINT_STARTEND = 0x913
    EVENT_HOLDUP_TEST_STARTEND = 0x914
    EVENT_BURGLARY_TEST_PRINT_STARTEND = 0x915
    EVENT_SUPERVISORY_TEST_PRINT_STARTEND = 0x916
    EVENT_BURGLARY_DIAGNOSTICS_STARTEND = 0x917
    EVENT_FIRE_DIAGNOSTICS_STARTEND = 0x918
    EVENT_UNTYPED_DIAGNOSTICS = 0x919
    EVENT_TROUBLE_CLOSING = 0x920
    EVENT_ACCESS_DENIED_CODE_UNKNOWN = 0x921
    ALARM_SUPERVISORY_POINT = 0x922
    EVENT_SUPERVISORY_POINT_BYPASS = 0x923
    TROUBLE_SUPERVISORY_POINT = 0x924
    EVENT_HOLDUP_POINT_BYPASS = 0x925
    EVENT_AC_FAILURE_FOR_4HOURS = 0x926
    TROUBLE_OUTPUT = 0x927
    EVENT_USER_CODE_FOR_EVENT = 0x928
    EVENT_LOG_OFF = 0x929
    # 930-953: ?
    EVENT_CS_CONNECTION_FAILURE = 0x954
    # 955-960: ?
    EVENT_RECEIVER_DATABASE_CONNECTION = 0x961
    EVENT_LICENSE_EXPIRATION = 0x962
    # 963-998: ?
    OTHER_NO_READ_LOG = 0x999


# noinspection PyPep8Naming
class LRR_DSC_EVENT:
    """
    DSC event codes
    """
    ZONE_EXPANDER_SUPERVISORY_ALARM = 0x04c
    ZONE_EXPANDER_SUPERVISORY_RESTORE = 0x04d
    AUX_INPUT_ALARM = 0x051
    SPECIAL_CLOSING = 0x0bf
    CROSS_ZONE_POLICE_CODE_ALARM = 0x103
    AUTOMATIC_CLOSING = 0x12b
    ZONE_BYPASS = 0x570
    REPORT_DSC_USER_LOG_EVENT = 0x800


# noinspection PyPep8Naming
class LRR_ADEMCO_EVENT:
    """
    ADEMCO event codes
    """
    pass


# noinspection PyPep8Naming
class LRR_ALARMDECODER_EVENT:
    """
    AlarmDecoder event codes
    """
    CUSTOM_PROG_MSG = 0x0
    CUSTOM_PROG_KEY = 0x1


# noinspection PyPep8Naming
class LRR_UNKNOWN_EVENT:
    """
    Unknown event codes.  Realistically there shouldn't ever be anything here.
    """
    pass


# Map of ContactID event codes to human-readable text.
LRR_CID_MAP = {
    LRR_CID_EVENT.MEDICAL: 'Medical Emergency: Non-specific',
    LRR_CID_EVENT.MEDICAL_PENDANT: 'Emergency Assistance Request',
    LRR_CID_EVENT.MEDICAL_FAIL_TO_REPORT: 'Medical: Failed to activate monitoring device',
    LRR_CID_EVENT.TAMPER_ZONE: 'Zone Tamper',
    LRR_CID_EVENT.FIRE: 'Fire: Non-specific',
    LRR_CID_EVENT.FIRE_SMOKE: 'Fire: Smoke Alarm',
    LRR_CID_EVENT.FIRE_COMBUSTION: 'Fire: Combustion',
    LRR_CID_EVENT.FIRE_WATER_FLOW: 'Fire: Water Flow',
    LRR_CID_EVENT.FIRE_HEAT: 'Fire: Heat',
    LRR_CID_EVENT.FIRE_PULL_STATION: 'Fire: Pull Station',
    LRR_CID_EVENT.FIRE_DUCT: 'Fire: Duct',
    LRR_CID_EVENT.FIRE_FLAME: 'Fire: Flame',
    LRR_CID_EVENT.FIRE_NEAR_ALARM: 'Fire: Near Alarm',
    LRR_CID_EVENT.PANIC: 'Panic',
    LRR_CID_EVENT.PANIC_DURESS: 'Panic: Duress',
    LRR_CID_EVENT.PANIC_SILENT: 'Panic: Silent',
    LRR_CID_EVENT.PANIC_AUDIBLE: 'Panic: Audible',
    LRR_CID_EVENT.PANIC_DURESS_ACCESS_GRANTED: 'Fire: Duress',
    LRR_CID_EVENT.PANIC_DURESS_EGRESS_GRANTED: 'Fire: Egress',
    LRR_CID_EVENT.PANIC_HOLDUP_SUSPICION: 'Panic: Hold-up, Suspicious Condition',
    LRR_CID_EVENT.PANIC_HOLDUP_VERIFIER: 'Panic: Hold-up Verified',
    LRR_CID_EVENT.BURGLARY: 'Burglary',
    LRR_CID_EVENT.BURGLARY_PERIMETER: 'Burglary: Perimeter',
    LRR_CID_EVENT.BURGLARY_INTERIOR: 'Burglary: Interior',
    LRR_CID_EVENT.BURGLARY_AUX: 'Burglary: 24 Hour',
    LRR_CID_EVENT.BURGLARY_ENTRYEXIT: 'Burglary: Entry/Exit',
    LRR_CID_EVENT.BURGLARY_DAYNIGHT: 'Burglary: Day/Night',
    LRR_CID_EVENT.BURGLARY_OUTDOOR: 'Burglary: Outdoor',
    LRR_CID_EVENT.BURGLARY_TAMPER: 'Burglary: Tamper',
    LRR_CID_EVENT.BURGLARY_NEAR_ALARM: 'Burglary: Near Alarm',
    LRR_CID_EVENT.BURGLARY_INTRUSION_VERIFIER: 'Burglary: Intrusion Verifier',
    LRR_CID_EVENT.ALARM_GENERAL: 'Alarm: General',
    LRR_CID_EVENT.ALARM_POLLING_LOOP_OPEN: 'Alarm: Polling Loop Open',
    LRR_CID_EVENT.ALARM_POLLING_LOOP_SHORT: 'Alarm: Polling Loop Closed',
    LRR_CID_EVENT.ALARM_EXPANSION_MOD_FAILURE: 'Alarm: Expansion Module Failure',
    LRR_CID_EVENT.ALARM_SENSOR_TAMPER: 'Alarm: Sensor Tamper',
    LRR_CID_EVENT.ALARM_EXPANSION_MOD_TAMPER: 'Alarm: Expansion Module Tamper',
    LRR_CID_EVENT.BURGLARY_SILENT: 'Burglary: Silent',
    LRR_CID_EVENT.TROUBLE_SENSOR_SUPERVISION: 'Trouble: Sensor Supervision Failure',
    LRR_CID_EVENT.ALARM_AUX: 'Alarm: 24 Hour Non-Burglary',
    LRR_CID_EVENT.ALARM_GAS_DETECTED: 'Alarm: Gas Detected',
    LRR_CID_EVENT.ALARM_REFRIDGERATION: 'Alarm: Refridgeration',
    LRR_CID_EVENT.ALARM_LOSS_OF_HEAT: 'Alarm: Loss of Heat',
    LRR_CID_EVENT.ALARM_WATER_LEAKAGE: 'Alarm: Water Leakage',
    LRR_CID_EVENT.TROUBLE_FOIL_BREAK: 'Trouble: Foil Break',
    LRR_CID_EVENT.TROUBLE_DAY_TROUBLE: 'Trouble: Day Trouble',
    LRR_CID_EVENT.ALARM_LOW_BOTTLED_GAS_LEVEL: 'Alarm: Low Bottled Gas Level',
    LRR_CID_EVENT.ALARM_HIGH_TEMP: 'Alarm: High Temperature',
    LRR_CID_EVENT.ALARM_LOW_TEMP: 'Alarm: Low Temperature',
    LRR_CID_EVENT.ALARM_LOSS_OF_AIR_FLOW: 'Alarm: Loss of Air Flow',
    LRR_CID_EVENT.ALARM_CARBON_MONOXIDE: 'Alarm: Carbon Monoxide',
    LRR_CID_EVENT.TROUBLE_TANK_LEVEL: 'Trouble: Tank Level',
    LRR_CID_EVENT.TROUBLE_HIGH_HUMIDITY: 'Trouble: High Humidity',
    LRR_CID_EVENT.TROUBLE_LOW_HUMIDITY: 'Trouble: Low Humidity',
    LRR_CID_EVENT.SUPERVISORY_FIRE: 'Supervisory: Fire',
    LRR_CID_EVENT.SUPERVISORY_LOW_PRESSURE: 'Supervisory: Low Water Pressure',
    LRR_CID_EVENT.SUPERVISORY_LOW_CO2: 'Supervisory: Low CO2',
    LRR_CID_EVENT.SUPERVISORY_GATE_VALVE_SENSOR: 'Supervisory: Gate Valve Sensor',
    LRR_CID_EVENT.SUPERVISORY_LOW_WATER_LEVEL: 'Supervisory: Low Water Level',
    LRR_CID_EVENT.SUPERVISORY_PUMP_ACTIVATED: 'Supervisory: Pump Activated',
    LRR_CID_EVENT.SUPERVISORY_PUMP_FAILURE: 'Supervisory: Pump Failure',
    LRR_CID_EVENT.TROUBLE_SYSTEM_TROUBLE: 'Trouble: System Trouble',
    LRR_CID_EVENT.TROUBLE_AC_LOSS: 'Trouble: AC Loss',
    LRR_CID_EVENT.TROUBLE_LOW_BATTERY: 'Trouble: Low Battery',
    LRR_CID_EVENT.TROUBLE_RAM_CHECKSUM_BAD: 'Trouble: RAM Checksum Bad',
    LRR_CID_EVENT.TROUBLE_ROM_CHECKSUM_BAD: 'Trouble: ROM Checksum Bad',
    LRR_CID_EVENT.TROUBLE_RESET: 'Trouble: System Reset',
    LRR_CID_EVENT.TROUBLE_PANEL_PROGRAMMING_CHANGED: 'Trouble: Panel Programming Changed',
    LRR_CID_EVENT.TROUBLE_SELF_TEST_FAILURE: 'Trouble: Self-Test Failure',
    LRR_CID_EVENT.TROUBLE_SHUTDOWN: 'Trouble: System Shutdown',
    LRR_CID_EVENT.TROUBLE_BATTERY_TEST_FAIL: 'Trouble: Battery Test Failure',
    LRR_CID_EVENT.TROUBLE_GROUND_FAULT: 'Trouble: Ground Fault',
    LRR_CID_EVENT.TROUBLE_BATTERY_MISSING: 'Trouble: Battery Missing',
    LRR_CID_EVENT.TROUBLE_POWER_SUPPLY_OVERCURRENT: 'Trouble: Power Supply Overcurrent',
    LRR_CID_EVENT.STATUS_ENGINEER_RESET: 'Status: Engineer Reset',
    LRR_CID_EVENT.TROUBLE_PRIMARY_POWER_SUPPLY_FAILURE: 'Trouble: Primary Power Supply Failure',
    LRR_CID_EVENT.TROUBLE_TAMPER: 'Trouble: System Tamper',
    LRR_CID_EVENT.TROUBLE_SOUNDER: 'Trouble: Sounder',
    LRR_CID_EVENT.TROUBLE_BELL_1: 'Trouble: Bell 1',
    LRR_CID_EVENT.TROUBLE_BELL_2: 'Trouble: Bell 2',
    LRR_CID_EVENT.TROUBLE_ALARM_RELAY: 'Trouble: Alarm Relay',
    LRR_CID_EVENT.TROUBLE_TROUBLE_RELAY: 'Trouble: Trouble Relay',
    LRR_CID_EVENT.TROUBLE_REVERSING_RELAY: 'Trouble: Reversing Relay',
    LRR_CID_EVENT.TROUBLE_NOTIFICATION_APPLIANCE_CIRCUIT_3: 'Trouble: Notification Appliance Circuit #3',
    LRR_CID_EVENT.TROUBLE_NOTIFICATION_APPLIANCE_CIRCUIT_4: 'Trouble: Notification Appliance Circuit #3',
    LRR_CID_EVENT.TROUBLE_SYSTEM_PERIPHERAL: 'Trouble: System Peripheral',
    LRR_CID_EVENT.TROUBLE_POLLING_LOOP_OPEN: 'Trouble: Pooling Loop Open',
    LRR_CID_EVENT.TROUBLE_POLLING_LOOP_SHORT: 'Trouble: Polling Loop Short',
    LRR_CID_EVENT.TROUBLE_EXPANSION_MODULE_FAILURE: 'Trouble: Expansion Module Failure',
    LRR_CID_EVENT.TROUBLE_REPEATER_FAILURE: 'Trouble: Repeater Failure',
    LRR_CID_EVENT.TROUBLE_LOCAL_PRINTER_PAPER_OUT: 'Trouble: Local Printer Out Of Paper',
    LRR_CID_EVENT.TROUBLE_LOCAL_PRINTER_FAILURE: 'Trouble: Local Printer Failure',
    LRR_CID_EVENT.TROUBLE_EXPANDER_MODULE_DC_LOSS: 'Trouble: Expander Module, DC Power Loss',
    LRR_CID_EVENT.TROUBLE_EXPANDER_MODULE_LOW_BATTERY: 'Trouble: Expander Module, Low Battery',
    LRR_CID_EVENT.TROUBLE_EXPANDER_MODULE_RESET: 'Trouble: Expander Module, Reset',
    LRR_CID_EVENT.TROUBLE_EXPANDER_MODULE_TAMPER: 'Trouble: Expander Module, Tamper',
    LRR_CID_EVENT.TROUBLE_EXPANDER_MODULE_AC_LOSS: 'Trouble: Expander Module, AC Power Loss',
    LRR_CID_EVENT.TROUBLE_EXPANDER_MODULE_SELF_TEST_FAIL: 'Trouble: Expander Module, Self-test Failure',
    LRR_CID_EVENT.TROUBLE_RF_RECEIVER_JAM_DETECTED: 'Trouble: RF Receiver Jam Detected',
    LRR_CID_EVENT.TROUBLE_AES_ENCRYPTION: 'Trouble: AES Encryption',
    LRR_CID_EVENT.TROUBLE_COMMUNICATION: 'Trouble: Communication',
    LRR_CID_EVENT.TROUBLE_TELCO_1_FAULT: 'Trouble: Telco 1',
    LRR_CID_EVENT.TROUBLE_TELCO_2_FAULT: 'Trouble: Telco 2',
    LRR_CID_EVENT.TROUBLE_LRR_TRANSMITTER_FAULT: 'Trouble: Long Range Radio Transmitter Fault',
    LRR_CID_EVENT.TROUBLE_FAILURE_TO_COMMUNICATE: 'Trouble: Failure To Communicate',
    LRR_CID_EVENT.TROUBLE_LOSS_OF_RADIO_SUPERVISION: 'Trouble: Loss of Radio Supervision',
    LRR_CID_EVENT.TROUBLE_LOSS_OF_CENTRAL_POLLING: 'Trouble: Loss of Central Polling',
    LRR_CID_EVENT.TROUBLE_LRR_TRANSMITTER_VSWR: 'Trouble: Long Range Radio Transmitter/Antenna',
    LRR_CID_EVENT.TROUBLE_PERIODIC_COMM_TEST: 'Trouble: Periodic Communication Test',
    LRR_CID_EVENT.TROUBLE_PROTECTION_LOOP: 'Trouble: Protection Loop',
    LRR_CID_EVENT.TROUBLE_PROTECTION_LOOP_OPEN: 'Trouble: Protection Loop Open',
    LRR_CID_EVENT.TROUBLE_PROTECTION_LOOP_SHORT: 'Trouble: Protection Loop Short',
    LRR_CID_EVENT.TROUBLE_FIRE: 'Trouble: Fire',
    LRR_CID_EVENT.TROUBLE_EXIT_ERROR: 'Trouble: Exit Error',
    LRR_CID_EVENT.TROUBLE_PANIC_ZONE_TROUBLE: 'Trouble: Panic',
    LRR_CID_EVENT.TROUBLE_HOLDUP_ZONE_TROUBLE: 'Trouble: Hold-up',
    LRR_CID_EVENT.TROUBLE_SWINGER_TROUBLE: 'Trouble: Swinger',
    LRR_CID_EVENT.TROUBLE_CROSS_ZONE_TROUBLE: 'Trouble: Cross-zone',
    LRR_CID_EVENT.TROUBLE_SENSOR_TROUBLE: 'Trouble: Sensor',
    LRR_CID_EVENT.TROUBLE_RF_LOSS_OF_SUPERVISION: 'Trouble: RF Loss of Supervision',
    LRR_CID_EVENT.TROUBLE_RPM_LOSS_OF_SUPERVISION: 'Trouble: RPM Loss of Supervision',
    LRR_CID_EVENT.TROUBLE_SENSOR_TAMPER: 'Trouble: Sensor Tamper',
    LRR_CID_EVENT.TROUBLE_RF_LOW_BATTERY: 'Trouble: RF Low Battery',
    LRR_CID_EVENT.TROUBLE_SMOKE_HI_SENS: 'Trouble: Smoke Detector, High Sensitivity',
    LRR_CID_EVENT.TROUBLE_SMOKE_LO_SENS: 'Trouble: Smoke Detector, Low Sensitivity',
    LRR_CID_EVENT.TROUBLE_INTRUSION_HI_SENS: 'Trouble: Intrusion Detector, High Sensitivity',
    LRR_CID_EVENT.TROUBLE_INTRUSION_LO_SENS: 'Trouble: Intrusion Detector, Low Sensitivity',
    LRR_CID_EVENT.TROUBLE_SELF_TEST_FAIL: 'Trouble: Self-test Failure',
    LRR_CID_EVENT.TROUBLE_SENSOR_WATCH_FAIL: 'Trouble: Sensor Watch',
    LRR_CID_EVENT.TROUBLE_DRIFT_COMP_ERROR: 'Trouble: Drift Compensation Error',
    LRR_CID_EVENT.TROUBLE_MAINTENANCE_ALERT: 'Trouble: Maintenance Alert',
    LRR_CID_EVENT.OPENCLOSE: 'Open/Close',
    LRR_CID_EVENT.OPENCLOSE_BY_USER: 'Open/Close: By User',
    LRR_CID_EVENT.OPENCLOSE_GROUP: 'Open/Close: Group',
    LRR_CID_EVENT.OPENCLOSE_AUTOMATIC: 'Open/Close: Automatic',
    LRR_CID_EVENT.OPENCLOSE_LATE: 'Open/Close: Late',
    LRR_CID_EVENT.OPENCLOSE_DEFERRED: 'Open/Close: Deferred',
    LRR_CID_EVENT.OPENCLOSE_CANCEL_BY_USER: 'Open/Close: Cancel',
    LRR_CID_EVENT.OPENCLOSE_REMOTE_ARMDISARM: 'Open/Close: Remote',
    LRR_CID_EVENT.OPENCLOSE_QUICK_ARM: 'Open/Close: Quick Arm',
    LRR_CID_EVENT.OPENCLOSE_KEYSWITCH: 'Open/Close: Keyswitch',
    LRR_CID_EVENT.REMOTE_CALLBACK_REQUESTED: 'Remote: Callback Requested',
    LRR_CID_EVENT.REMOTE_SUCCESS: 'Remote: Successful Access',
    LRR_CID_EVENT.REMOTE_UNSUCCESSFUL: 'Remote: Unsuccessful Access',
    LRR_CID_EVENT.REMOTE_SYSTEM_SHUTDOWN: 'Remote: System Shutdown',
    LRR_CID_EVENT.REMOTE_DIALER_SHUTDOWN: 'Remote: Dialer Shutdown',
    LRR_CID_EVENT.REMOTE_SUCCESSFUL_UPLOAD: 'Remote: Successful Upload',
    LRR_CID_EVENT.ACCESS_DENIED: 'Access: Denied',
    LRR_CID_EVENT.ACCESS_REPORT_BY_USER: 'Access: Report By User',
    LRR_CID_EVENT.ACCESS_FORCED_ACCESS: 'Access: Forced Access',
    LRR_CID_EVENT.ACCESS_EGRESS_DENIED: 'Access: Egress Denied',
    LRR_CID_EVENT.ACCESS_EGRESS_GRANTED: 'Access: Egress Granted',
    LRR_CID_EVENT.ACCESS_DOOR_PROPPED_OPEN: 'Access: Door Propped Open',
    LRR_CID_EVENT.ACCESS_POINT_DSM_TROUBLE: 'Access: Door Status Monitor Trouble',
    LRR_CID_EVENT.ACCESS_POINT_RTE_TROUBLE: 'Access: Request To Exit Trouble',
    LRR_CID_EVENT.ACCESS_PROGRAM_MODE_ENTRY: 'Access: Program Mode Entry',
    LRR_CID_EVENT.ACCESS_PROGRAM_MODE_EXIT: 'Access: Program Mode Exit',
    LRR_CID_EVENT.ACCESS_THREAT_LEVEL_CHANGE: 'Access: Threat Level Change',
    LRR_CID_EVENT.ACCESS_RELAY_FAIL: 'Access: Relay Fail',
    LRR_CID_EVENT.ACCESS_RTE_SHUNT: 'Access: Request to Exit Shunt',
    LRR_CID_EVENT.ACCESS_DSM_SHUNT: 'Access: Door Status Monitor Shunt',
    LRR_CID_EVENT.ACCESS_SECOND_PERSON: 'Access: Second Person Access',
    LRR_CID_EVENT.ACCESS_IRREGULAR_ACCESS: 'Access: Irregular Access',
    LRR_CID_EVENT.OPENCLOSE_ARMED_STAY: 'Open/Close: Armed Stay',
    LRR_CID_EVENT.OPENCLOSE_KEYSWITCH_ARMED_STAY: 'Open/Close: Keyswitch, Armed Stay',
    LRR_CID_EVENT.OPENCLOSE_EXCEPTION: 'Open/Close: Armed with Trouble Override',
    LRR_CID_EVENT.OPENCLOSE_EARLY: 'Open/Close: Early',
    LRR_CID_EVENT.TROUBLE_FAILED_TO_OPEN: 'Trouble: Failed To Open',
    LRR_CID_EVENT.TROUBLE_FAILED_TO_CLOSE: 'Trouble: Failed To Close',
    LRR_CID_EVENT.TROUBLE_AUTO_ARM_FAILED: 'Trouble: Auto Arm Failed',
    LRR_CID_EVENT.OPENCLOSE_PARTIAL_ARM: 'Open/Close: Partial Arm',
    LRR_CID_EVENT.OPENCLOSE_EXIT_ERROR: 'Open/Close: Exit Error',
    LRR_CID_EVENT.OPENCLOSE_USER_ON_PREMISES: 'Open/Close: User On Premises',
    LRR_CID_EVENT.TROUBLE_RECENT_CLOSE: 'Trouble: Recent Close',
    LRR_CID_EVENT.ACCESS_WRONG_CODE_ENTRY: 'Access: Wrong Code',
    LRR_CID_EVENT.ACCESS_LEGAL_CODE_ENTRY: 'Access: Legal Code',
    LRR_CID_EVENT.STATUS_REARM_AFTER_ALARM: 'Status: Re-arm After Alarm',
    LRR_CID_EVENT.STATUS_AUTO_ARM_TIME_EXTENDED: 'Status: Auto-arm Time Extended',
    LRR_CID_EVENT.STATUS_PANIC_ALARM_RESET: 'Status: Panic Alarm Reset',
    LRR_CID_EVENT.ACCESS_SERVICE_ONOFF_PREMISES: 'Status: Service On/Off Premises',
    LRR_CID_EVENT.OPENCLOSE_PARTIAL_CLOSING: 'Open/Close: Partial Closing',
    LRR_CID_EVENT.OPENCLOSE_PARTIAL_CLOSE: 'Open/Close: Partial Close',
    LRR_CID_EVENT.DISABLE_ACCESS_READER: 'Disable: Access Reader',
    LRR_CID_EVENT.DISABLE_SOUNDER: 'Disable: Sounder',
    LRR_CID_EVENT.DISABLE_BELL_1: 'Disable: Bell 1',
    LRR_CID_EVENT.DISABLE_BELL_2: 'Disable: Bell 2',
    LRR_CID_EVENT.DISABLE_ALARM_RELAY: 'Disable: Alarm Relay',
    LRR_CID_EVENT.DISABLE_TROUBLE_RELAY: 'Disable: Trouble Relay',
    LRR_CID_EVENT.DISABLE_REVERSING_RELAY: 'Disable: Reversing Relay',
    LRR_CID_EVENT.DISABLE_NOTIFICATION_APPLIANCE_CIRCUIT_3: 'Disable: Notification Appliance Circuit #3',
    LRR_CID_EVENT.DISABLE_NOTIFICATION_APPLIANCE_CIRCUIT_4: 'Disable: Notification Appliance Circuit #4',
    LRR_CID_EVENT.SUPERVISORY_MODULE_ADDED: 'Supervisory: Module Added',
    LRR_CID_EVENT.SUPERVISORY_MODULE_REMOVED: 'Supervisory: Module Removed',
    LRR_CID_EVENT.DISABLE_DIALER: 'Disable: Dialer',
    LRR_CID_EVENT.DISABLE_RADIO_TRANSMITTER: 'Disable: Radio Transmitter',
    LRR_CID_EVENT.DISABLE_REMOTE_UPLOADDOWNLOAD: 'Disable: Remote Upload/Download',
    LRR_CID_EVENT.BYPASS_ZONE: 'Bypass: Zone',
    LRR_CID_EVENT.BYPASS_FIRE: 'Bypass: Fire',
    LRR_CID_EVENT.BYPASS_24HOUR_ZONE: 'Bypass: 24 Hour Zone',
    LRR_CID_EVENT.BYPASS_BURGLARY: 'Bypass: Burglary',
    LRR_CID_EVENT.BYPASS_GROUP: 'Bypass: Group',
    LRR_CID_EVENT.BYPASS_SWINGER: 'Bypass: Swinger',
    LRR_CID_EVENT.BYPASS_ACCESS_ZONE_SHUNT: 'Bypass: Access Zone Shunt',
    LRR_CID_EVENT.BYPASS_ACCESS_POINT_BYPASS: 'Bypass: Access Point',
    LRR_CID_EVENT.BYPASS_ZONE_VAULT: 'Bypass: Vault',
    LRR_CID_EVENT.BYPASS_ZONE_VENT: 'Bypass: Vent',
    LRR_CID_EVENT.TEST_MANUAL: 'Test: Manual Trigger',
    LRR_CID_EVENT.TEST_PERIODIC: 'Test: Periodic',
    LRR_CID_EVENT.TEST_PERIODIC_RF_TRANSMISSION: 'Test: Periodic RF Transmission',
    LRR_CID_EVENT.TEST_FIRE: 'Test: Fire',
    LRR_CID_EVENT.TEST_FIRE_STATUS: 'Test: Fire, Status Report To Follow',
    LRR_CID_EVENT.TEST_LISTENIN_TO_FOLLOW: 'Test: Listen-in To Follow',
    LRR_CID_EVENT.TEST_WALK: 'Test: Walk',
    LRR_CID_EVENT.TEST_SYSTEM_TROUBLE_PRESENT: 'Test: Periodic Test, System Trouble Present',
    LRR_CID_EVENT.TEST_VIDEO_TRANSMITTER_ACTIVE: 'Test: Video Transmitter Active',
    LRR_CID_EVENT.TEST_POINT_TESTED_OK: 'Test: Point Tested OK',
    LRR_CID_EVENT.TEST_POINT_NOT_TESTED: 'Test: Point Not Tested',
    LRR_CID_EVENT.TEST_INTRUSION_ZONE_WALK_TESTED: 'Test: Intrusion Zone Walk Tested',
    LRR_CID_EVENT.TEST_FIRE_ZONE_WALK_TESTED: 'Test: Fire Zone Walk Tested',
    LRR_CID_EVENT.TEST_PANIC_ZONE_WALK_TESTED: 'Test: Panic Zone Walk Tested',
    LRR_CID_EVENT.TROUBLE_SERVICE_REQUEST: 'Trouble: Service Request',
    LRR_CID_EVENT.TROUBLE_EVENT_LOG_RESET: 'Trouble: Event Log Reset',
    LRR_CID_EVENT.TROUBLE_EVENT_LOG_50PERCENT_FULL: 'Trouble: Event Log 50% Full',
    LRR_CID_EVENT.TROUBLE_EVENT_LOG_90PERCENT_FULL: 'Trouble: Event Log 90% Full',
    LRR_CID_EVENT.TROUBLE_EVENT_LOG_OVERFLOW: 'Trouble: Event Log Overflow',
    LRR_CID_EVENT.TROUBLE_TIMEDATE_RESET: 'Trouble: Time/Date Reset',
    LRR_CID_EVENT.TROUBLE_TIMEDATE_INACCURATE: 'Trouble: Time/Date Inaccurate',
    LRR_CID_EVENT.TROUBLE_PROGRAM_MODE_ENTRY: 'Trouble: Program Mode Entry',
    LRR_CID_EVENT.TROUBLE_PROGRAM_MODE_EXIT: 'Trouble: Program Mode Exit',
    LRR_CID_EVENT.TROUBLE_32HOUR_EVENT_LOG_MARKER: 'Trouble: 32 Hour Event Log Marker',
    LRR_CID_EVENT.SCHEDULE_CHANGE: 'Schedule: Change',
    LRR_CID_EVENT.SCHEDULE_EXCEPTION_SCHEDULE_CHANGE: 'Schedule: Exception Schedule Change',
    LRR_CID_EVENT.SCHEDULE_ACCESS_SCHEDULE_CHANGE: 'Schedule: Access Schedule Change',
    LRR_CID_EVENT.TROUBLE_SENIOR_WATCH_TROUBLE: 'Schedule: Senior Watch Trouble',
    LRR_CID_EVENT.STATUS_LATCHKEY_SUPERVISION: 'Status: Latch-key Supervision',
    LRR_CID_EVENT.SPECIAL_ADT_AUTHORIZATION: 'Special: ADT Authorization',
    LRR_CID_EVENT.RESERVED_652: 'Reserved: For Ademco Use',
    LRR_CID_EVENT.RESERVED_653: 'Reserved: For Ademco Use',
    LRR_CID_EVENT.TROUBLE_SYSTEM_INACTIVITY: 'Trouble: System Inactivity',
    LRR_CID_EVENT.TROUBLE_UNABLE_TO_OUTPUT_SIGNAL: 'Trouble: Unable To Output Signal (Derived Channel)',
    LRR_CID_EVENT.TROUBLE_STU_CONTROLLER_DOWN: 'Trouble: STU Controller Down (Derived Channel)',
    LRR_CID_EVENT.REMOTE_DOWNLOAD_ABORT: 'Remote: Download Aborted',
    LRR_CID_EVENT.REMOTE_DOWNLOAD_STARTEND: 'Remote: Download Start/End',
    LRR_CID_EVENT.REMOTE_DOWNLOAD_INTERRUPTED: 'Remote: Download Interrupted',
    LRR_CID_EVENT.REMOTE_CODE_DOWNLOAD_STARTEND: 'Remote: Device Flash Start/End',
    LRR_CID_EVENT.REMOTE_CODE_DOWNLOAD_FAILED: 'Remote: Device Flash Failed',
    LRR_CID_EVENT.OPENCLOSE_AUTOCLOSE_WITH_BYPASS: 'Open/Close: Auto-Close With Bypass',
    LRR_CID_EVENT.OPENCLOSE_BYPASS_CLOSING: 'Open/Close: Bypass Closing',
    LRR_CID_EVENT.EVENT_FIRE_ALARM_SILENCED: 'Event: Fire Alarm Silenced',
    LRR_CID_EVENT.EVENT_SUPERVISOR_POINT_STARTEND: 'Event: Supervisory Point Test Start/End',
    LRR_CID_EVENT.EVENT_HOLDUP_TEST_STARTEND: 'Event: Hold-up Test Start/End',
    LRR_CID_EVENT.EVENT_BURGLARY_TEST_PRINT_STARTEND: 'Event: Burglary Test Print Start/End',
    LRR_CID_EVENT.EVENT_SUPERVISORY_TEST_PRINT_STARTEND: 'Event: Supervisory Test Print Start/End',
    LRR_CID_EVENT.EVENT_BURGLARY_DIAGNOSTICS_STARTEND: 'Event: Burglary Diagnostics Start/End',
    LRR_CID_EVENT.EVENT_FIRE_DIAGNOSTICS_STARTEND: 'Event: Fire Diagnostics Start/End',
    LRR_CID_EVENT.EVENT_UNTYPED_DIAGNOSTICS: 'Event: Untyped Diagnostics',
    LRR_CID_EVENT.EVENT_TROUBLE_CLOSING: 'Event: Trouble Closing',
    LRR_CID_EVENT.EVENT_ACCESS_DENIED_CODE_UNKNOWN: 'Event: Access Denied, Code Unknown',
    LRR_CID_EVENT.ALARM_SUPERVISORY_POINT: 'Alarm: Supervisory Point',
    LRR_CID_EVENT.EVENT_SUPERVISORY_POINT_BYPASS: 'Event: Supervisory Point Bypass',
    LRR_CID_EVENT.TROUBLE_SUPERVISORY_POINT: 'Trouble: Supervisory Point',
    LRR_CID_EVENT.EVENT_HOLDUP_POINT_BYPASS: 'Event: Hold-up Point Bypass',
    LRR_CID_EVENT.EVENT_AC_FAILURE_FOR_4HOURS: 'Event: AC Failure For 4 Hours',
    LRR_CID_EVENT.TROUBLE_OUTPUT: 'Trouble: Output Trouble',
    LRR_CID_EVENT.EVENT_USER_CODE_FOR_EVENT: 'Event: User Code For Event',
    LRR_CID_EVENT.EVENT_LOG_OFF: 'Event: Log-off',
    LRR_CID_EVENT.EVENT_CS_CONNECTION_FAILURE: 'Event: Central Station Connection Failure',
    LRR_CID_EVENT.EVENT_RECEIVER_DATABASE_CONNECTION: 'Event: Receiver Database Connection',
    LRR_CID_EVENT.EVENT_LICENSE_EXPIRATION: 'Event: License Expiration',
    LRR_CID_EVENT.OTHER_NO_READ_LOG: 'Other: No Read Log',
}

# Map of DSC event codes to human-readable text.
LRR_DSC_MAP = {
    LRR_DSC_EVENT.ZONE_EXPANDER_SUPERVISORY_ALARM: 'Zone Expander Supervisory Alarm',
    LRR_DSC_EVENT.ZONE_EXPANDER_SUPERVISORY_RESTORE: 'Zone Expander Supervisory Restore',
    LRR_DSC_EVENT.AUX_INPUT_ALARM: 'Auxillary Input Alarm',
    LRR_DSC_EVENT.SPECIAL_CLOSING: 'Special Closing',
    LRR_DSC_EVENT.CROSS_ZONE_POLICE_CODE_ALARM: 'Cross-zone Police Code Alarm',
    LRR_DSC_EVENT.AUTOMATIC_CLOSING: 'Automatic Closing',
    LRR_DSC_EVENT.ZONE_BYPASS: 'Zone Bypass',
    LRR_DSC_EVENT.REPORT_DSC_USER_LOG_EVENT: 'Report DSC User Log Event',
}

# Map of ADEMCO event codes to human-readable text.
LRR_ADEMCO_MAP = {

}

LRR_ALARMDECODER_MAP = {
    LRR_ALARMDECODER_EVENT.CUSTOM_PROG_MSG: 'Custom Programming Message',
    LRR_ALARMDECODER_EVENT.CUSTOM_PROG_KEY: 'Custom Programming Key'
}

# Map of UNKNOWN event codes to human-readable text.
LRR_UNKNOWN_MAP = {

}

# Map of event type codes to text maps.
LRR_TYPE_MAP = {
    LRR_EVENT_TYPE.CID: LRR_CID_MAP,
    LRR_EVENT_TYPE.DSC: LRR_DSC_MAP,
    LRR_EVENT_TYPE.ADEMCO: LRR_ADEMCO_MAP,
    LRR_EVENT_TYPE.ALARMDECODER: LRR_ALARMDECODER_MAP,
    LRR_EVENT_TYPE.UNKNOWN: LRR_UNKNOWN_MAP,
}

# LRR events that should be considered Fire events.
LRR_FIRE_EVENTS = [
    LRR_CID_EVENT.FIRE,
    LRR_CID_EVENT.FIRE_SMOKE,
    LRR_CID_EVENT.FIRE_COMBUSTION,
    LRR_CID_EVENT.FIRE_WATER_FLOW,
    LRR_CID_EVENT.FIRE_HEAT,
    LRR_CID_EVENT.FIRE_PULL_STATION,
    LRR_CID_EVENT.FIRE_DUCT,
    LRR_CID_EVENT.FIRE_FLAME,
    LRR_CID_EVENT.OPENCLOSE_CANCEL_BY_USER  # HACK: Don't really like having this here
]

# LRR events that should be considered Alarm events.
LRR_ALARM_EVENTS = [
    LRR_CID_EVENT.BURGLARY,
    LRR_CID_EVENT.BURGLARY_PERIMETER,
    LRR_CID_EVENT.BURGLARY_INTERIOR,
    LRR_CID_EVENT.BURGLARY_AUX,
    LRR_CID_EVENT.BURGLARY_ENTRYEXIT,
    LRR_CID_EVENT.BURGLARY_DAYNIGHT,
    LRR_CID_EVENT.BURGLARY_OUTDOOR,
    LRR_CID_EVENT.ALARM_GENERAL,
    LRR_CID_EVENT.BURGLARY_SILENT,
    LRR_CID_EVENT.ALARM_AUX,
    LRR_CID_EVENT.ALARM_GAS_DETECTED,
    LRR_CID_EVENT.ALARM_REFRIDGERATION,
    LRR_CID_EVENT.ALARM_LOSS_OF_HEAT,
    LRR_CID_EVENT.ALARM_WATER_LEAKAGE,
    LRR_CID_EVENT.ALARM_LOW_BOTTLED_GAS_LEVEL,
    LRR_CID_EVENT.ALARM_HIGH_TEMP,
    LRR_CID_EVENT.ALARM_LOW_TEMP,
    LRR_CID_EVENT.ALARM_LOSS_OF_AIR_FLOW,
    LRR_CID_EVENT.ALARM_CARBON_MONOXIDE,
    LRR_CID_EVENT.OPENCLOSE_CANCEL_BY_USER  # HACK: Don't really like having this here
]

# LRR events that should be considered Power events.
LRR_POWER_EVENTS = [
    LRR_CID_EVENT.TROUBLE_AC_LOSS
]

# LRR events that should be considered Bypass events.
LRR_BYPASS_EVENTS = [
    LRR_CID_EVENT.BYPASS_ZONE,
    LRR_CID_EVENT.BYPASS_24HOUR_ZONE,
    LRR_CID_EVENT.BYPASS_BURGLARY
]

# LRR events that should be considered Battery events.
LRR_BATTERY_EVENTS = [
    LRR_CID_EVENT.TROUBLE_LOW_BATTERY
]

# LRR events that should be considered Panic events.
LRR_PANIC_EVENTS = [
    LRR_CID_EVENT.MEDICAL,
    LRR_CID_EVENT.MEDICAL_PENDANT,
    LRR_CID_EVENT.MEDICAL_FAIL_TO_REPORT,
    LRR_CID_EVENT.PANIC,
    LRR_CID_EVENT.PANIC_DURESS,
    LRR_CID_EVENT.PANIC_SILENT,
    LRR_CID_EVENT.PANIC_AUDIBLE,
    LRR_CID_EVENT.PANIC_DURESS_ACCESS_GRANTED,
    LRR_CID_EVENT.PANIC_DURESS_EGRESS_GRANTED,
    LRR_CID_EVENT.OPENCLOSE_CANCEL_BY_USER  # HACK: Don't really like having this here
]

# LRR events that should be considered Arm events.
LRR_ARM_EVENTS = [
    LRR_CID_EVENT.OPENCLOSE,
    LRR_CID_EVENT.OPENCLOSE_BY_USER,
    LRR_CID_EVENT.OPENCLOSE_GROUP,
    LRR_CID_EVENT.OPENCLOSE_AUTOMATIC,
    LRR_CID_EVENT.OPENCLOSE_REMOTE_ARMDISARM,
    LRR_CID_EVENT.OPENCLOSE_QUICK_ARM,
    LRR_CID_EVENT.OPENCLOSE_KEYSWITCH,
    LRR_CID_EVENT.OPENCLOSE_ARMED_STAY,  # HACK: Not sure if I like having these in here.
    LRR_CID_EVENT.OPENCLOSE_KEYSWITCH_ARMED_STAY
]

# LRR events that should be considered Arm Stay events.
LRR_STAY_EVENTS = [
    LRR_CID_EVENT.OPENCLOSE_ARMED_STAY,
    LRR_CID_EVENT.OPENCLOSE_KEYSWITCH_ARMED_STAY
]
