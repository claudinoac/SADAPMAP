EESchema Schematic File Version 2
LIBS:74xgxx
LIBS:74xx
LIBS:ac-dc
LIBS:actel
LIBS:adc-dac
LIBS:Altera
LIBS:analog_devices
LIBS:analog_switches
LIBS:atmel
LIBS:audio
LIBS:brooktre
LIBS:cmos4000
LIBS:cmos_ieee
LIBS:conn
LIBS:contrib
LIBS:cypress
LIBS:dc-dc
LIBS:device
LIBS:digital-audio
LIBS:diode
LIBS:display
LIBS:dsp
LIBS:elec-unifil
LIBS:ESD_Protection
LIBS:ftdi
LIBS:gennum
LIBS:graphic
LIBS:hc11
LIBS:intel
LIBS:interface
LIBS:ir
LIBS:Lattice
LIBS:linear
LIBS:logo
LIBS:maxim
LIBS:memory
LIBS:microchip
LIBS:microchip_dspic33dsc
LIBS:microchip_pic10mcu
LIBS:microchip_pic12mcu
LIBS:microchip_pic16mcu
LIBS:microchip_pic18mcu
LIBS:microchip_pic32mcu
LIBS:microcontrollers
LIBS:motor_drivers
LIBS:motorola
LIBS:msp430
LIBS:nordicsemi
LIBS:nxp_armmcu
LIBS:onsemi
LIBS:opto
LIBS:Oscillators
LIBS:philips
LIBS:power
LIBS:powerint
LIBS:Power_Management
LIBS:references
LIBS:regul
LIBS:relays
LIBS:rfcom
LIBS:sensors
LIBS:silabs
LIBS:siliconi
LIBS:stm8
LIBS:stm32
LIBS:supertex
LIBS:switches
LIBS:texas
LIBS:transf
LIBS:transistors
LIBS:ttl_ieee
LIBS:valves
LIBS:video
LIBS:w_analog
LIBS:w_connectors
LIBS:w_device
LIBS:w_logic
LIBS:w_memory
LIBS:w_microcontrollers
LIBS:w_opto
LIBS:Worldsemi
LIBS:w_relay
LIBS:w_rtx
LIBS:w_transistor
LIBS:w_vacuum
LIBS:Xicor
LIBS:xilinx
LIBS:Zilog
LIBS:TEMP_MODULE-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "SADAMAP Temperature Sensor Module"
Date "2018-03-07"
Rev "1"
Comp "LAPMA/CTA - IF/UFRGS"
Comment1 "Projected and Designed by Alisson Claudino"
Comment2 ""
Comment3 "This shield has connections for the SADAMAP ADC/MCU Module"
Comment4 "This is a shield for the MAX31856 ThermoCoupler Reader Module."
$EndDescr
$Comp
L MAX31856_ThermoCouple_Module J1
U 1 1 5A9D6132
P 6350 4125
F 0 "J1" H 6350 4925 60  0000 C CNN
F 1 "MAX31856_ThermoCouple_Module" H 6350 3325 60  0000 C CNN
F 2 "w_conn_misc:arduino_nano_header" H 6350 4125 60  0001 C CNN
F 3 "" H 6350 4125 60  0000 C CNN
	1    6350 4125
	1    0    0    -1  
$EndComp
Text GLabel 6000 4725 0    47   Input ~ 0
MOSI
Text GLabel 6000 4825 0    47   Output ~ 0
MISO
Text GLabel 6000 4425 0    47   Input ~ 0
~CS
$Comp
L +5V #PWR01
U 1 1 5A9EE8DA
P 6700 3725
F 0 "#PWR01" H 6700 3575 50  0001 C CNN
F 1 "+5V" V 6700 3900 50  0000 C CNN
F 2 "" H 6700 3725 50  0000 C CNN
F 3 "" H 6700 3725 50  0000 C CNN
	1    6700 3725
	0    1    1    0   
$EndComp
$Comp
L GND #PWR02
U 1 1 5A9EE90A
P 6700 3525
F 0 "#PWR02" H 6700 3275 50  0001 C CNN
F 1 "GND" V 6700 3350 50  0000 C CNN
F 2 "" H 6700 3525 50  0000 C CNN
F 3 "" H 6700 3525 50  0000 C CNN
	1    6700 3525
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR03
U 1 1 5A9EE97C
P 6000 3725
F 0 "#PWR03" H 6000 3475 50  0001 C CNN
F 1 "GND" V 6000 3550 50  0000 C CNN
F 2 "" H 6000 3725 50  0000 C CNN
F 3 "" H 6000 3725 50  0000 C CNN
	1    6000 3725
	0    1    1    0   
$EndComp
Text GLabel 6700 4825 2    47   BiDi ~ 0
SCK
$Comp
L CONN_01X06 P1
U 1 1 5A9EE9E7
P 5175 4025
F 0 "P1" H 5175 4375 50  0000 C CNN
F 1 "MCU_IN" V 5275 4025 50  0000 C CNN
F 2 "w_conn_kk100:kk100_22-23-2061" H 5175 4025 50  0001 C CNN
F 3 "" H 5175 4025 50  0000 C CNN
	1    5175 4025
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR04
U 1 1 5A9EEA44
P 5375 4275
F 0 "#PWR04" H 5375 4025 50  0001 C CNN
F 1 "GND" V 5375 4100 50  0000 C CNN
F 2 "" H 5375 4275 50  0000 C CNN
F 3 "" H 5375 4275 50  0000 C CNN
	1    5375 4275
	0    -1   -1   0   
$EndComp
$Comp
L +5V #PWR05
U 1 1 5A9EEA6F
P 5375 4175
F 0 "#PWR05" H 5375 4025 50  0001 C CNN
F 1 "+5V" V 5375 4350 50  0000 C CNN
F 2 "" H 5375 4175 50  0000 C CNN
F 3 "" H 5375 4175 50  0000 C CNN
	1    5375 4175
	0    1    -1   0   
$EndComp
Text GLabel 5375 4075 2    47   Output ~ 0
~CS
Text GLabel 5375 3875 2    47   Input ~ 0
MOSI
Text GLabel 5375 3975 2    47   Output ~ 0
MISO
Text GLabel 5375 3775 2    47   BiDi ~ 0
SCK
Wire Notes Line
	7250 3275 7250 5050
Wire Notes Line
	7250 5050 4975 5050
Wire Notes Line
	4975 5050 4975 3275
Wire Notes Line
	4975 3275 7250 3275
NoConn ~ 6000 3425
NoConn ~ 6000 3525
NoConn ~ 6000 3625
NoConn ~ 6000 3825
NoConn ~ 6000 3925
NoConn ~ 6000 4025
NoConn ~ 6000 4125
NoConn ~ 6000 4225
NoConn ~ 6000 4325
NoConn ~ 6000 4525
NoConn ~ 6000 4625
NoConn ~ 6700 4725
NoConn ~ 6700 4625
NoConn ~ 6700 4525
NoConn ~ 6700 4425
NoConn ~ 6700 4325
NoConn ~ 6700 4225
NoConn ~ 6700 4125
NoConn ~ 6700 4025
NoConn ~ 6700 3925
NoConn ~ 6700 3825
NoConn ~ 6700 3625
NoConn ~ 6700 3425
$Comp
L GND #PWR06
U 1 1 5AA07283
P 5350 4750
F 0 "#PWR06" H 5350 4500 50  0001 C CNN
F 1 "GND" V 5350 4575 50  0000 C CNN
F 2 "" H 5350 4750 50  0000 C CNN
F 3 "" H 5350 4750 50  0000 C CNN
	1    5350 4750
	0    -1   -1   0   
$EndComp
$Comp
L +5V #PWR07
U 1 1 5AA07289
P 5350 4650
F 0 "#PWR07" H 5350 4500 50  0001 C CNN
F 1 "+5V" V 5350 4825 50  0000 C CNN
F 2 "" H 5350 4650 50  0000 C CNN
F 3 "" H 5350 4650 50  0000 C CNN
	1    5350 4650
	0    1    -1   0   
$EndComp
$Comp
L PWR_FLAG #FLG08
U 1 1 5AA0729B
P 5300 4625
F 0 "#FLG08" H 5300 4720 50  0001 C CNN
F 1 "PWR_FLAG" H 5300 4805 50  0000 C CNN
F 2 "" H 5300 4625 50  0000 C CNN
F 3 "" H 5300 4625 50  0000 C CNN
	1    5300 4625
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG09
U 1 1 5AA072B3
P 5300 4800
F 0 "#FLG09" H 5300 4895 50  0001 C CNN
F 1 "PWR_FLAG" H 5300 4980 50  0000 C CNN
F 2 "" H 5300 4800 50  0000 C CNN
F 3 "" H 5300 4800 50  0000 C CNN
	1    5300 4800
	-1   0    0    1   
$EndComp
Wire Wire Line
	5300 4800 5300 4750
Wire Wire Line
	5300 4750 5350 4750
Wire Wire Line
	5300 4625 5300 4650
Wire Wire Line
	5300 4650 5350 4650
$EndSCHEMATC
