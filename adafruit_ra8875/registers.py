# The MIT License (MIT)
#
# Copyright (c) 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_ra8875.registers`
====================================================

A useful index of RA8875 Registers

* Author(s): Melissa LeBlanc-Williams
"""

# Command/Data for SPI
DATWR = b'\x00'    # Data Write
DATRD = b'\x40'    # Data Read
CMDWR = b'\x80'    # Command Write
CMDRD = b'\xC0'    # Status Read

# Registers and Bits
PWRR = 0x01
PWRR_DISPON = 0x80
PWRR_DISPOFF = 0x00
PWRR_SLEEP = 0x02
PWRR_NORMAL = 0x00
PWRR_SOFTRESET = 0x01
MRWC = 0x02
GPIOX = 0xC7

PLLC1 = 0x88
PLLC1_PLLDIV1 = 0x00

PLLC2 = 0x89
PLLC2_DIV4 = 0x02

SYSR = 0x10
SYSR_8BPP = 0x00
SYSR_16BPP = 0x0C
SYSR_MCU8 = 0x00
SYSR_MCU16 = 0x03

PCSR = 0x04
PCSR_PDATR = 0x00
PCSR_PDATL = 0x80
PCSR_CLK = 0x00
PCSR_2CLK = 0x01
PCSR_4CLK = 0x02
PCSR_8CLK = 0x03

HDWR = 0x14

HNDFTR = 0x15
HNDFTR_DE_HIGH = 0x00
HNDFTR_DE_LOW = 0x80

HNDR = 0x16
HSTR = 0x17
HPWR = 0x18
HPWR_LOW = 0x00
HPWR_HIGH = 0x80

VDHR0 = 0x19
VNDR0 = 0x1B
VSTR0 = 0x1D
VPWR = 0x1F
VPWR_LOW = 0x00
VPWR_HIGH = 0x80

FNCR0 = 0x21
FNCR1 = 0x22

HSAW0 = 0x30
VSAW0 = 0x32

HEAW0 = 0x34
VEAW0 = 0x36

MCLR = 0x8E
MCLR_START = 0x80
MCLR_STOP = 0x00
MCLR_READSTATUS = 0x80
MCLR_FULL = 0x00
MCLR_ACTIVE = 0x40

DCR = 0x90
DCR_LNSQTR_START = 0x80
DCR_LNSQTR_STOP = 0x00
DCR_LNSQTR_STATUS = 0x80
DCR_CIRC_START = 0x40
DCR_CIRC_STATUS = 0x40
DCR_CIRC_STOP = 0x00
DCR_FILL = 0x20
DCR_NOFILL = 0x00
DCR_DRAWLN = 0x00
DCR_DRAWTRI = 0x01
DCR_DRAWSQU = 0x10

ELLIPSE = 0xA0
ELLIPSE_STATUS = 0x80

MWCR0 = 0x40
MWCR0_GFXMODE = 0x00
MWCR0_TXTMODE = 0x80

CURH0 = 0x46
CURV0 = 0x48

P1CR = 0x8A
P1CR_ENABLE = 0x80
P1CR_DISABLE = 0x00
P1CR_CLKOUT = 0x10
P1CR_PWMOUT = 0x00

P1DCR = 0x8B

P2CR = 0x8C
P2CR_ENABLE = 0x80
P2CR_DISABLE = 0x00
P2CR_CLKOUT = 0x10
P2CR_PWMOUT = 0x00

P2DCR = 0x8D
PWM_CLK_DIV1024 = 0x0A

TPCR0 = 0x70
TPCR0_ENABLE = 0x80
TPCR0_DISABLE = 0x00
TPCR0_WAIT_4096CLK = 0x30
TPCR0_WAKEENABLE = 0x08
TPCR0_WAKEDISABLE = 0x00
TPCR0_ADCCLK_DIV4 = 0x02
TPCR0_ADCCLK_DIV16 = 0x04

TPCR1 = 0x71
TPCR1_AUTO = 0x00
TPCR1_MANUAL = 0x40
TPCR1_DEBOUNCE = 0x04
TPCR1_NODEBOUNCE = 0x00

TPXH = 0x72
TPYH = 0x73
TPXYL = 0x74

INTC1 = 0xF0
INTC1_KEY = 0x10
INTC1_DMA = 0x08
INTC1_TP = 0x04
INTC1_BTE = 0x02

INTC2 = 0xF1
INTC2_KEY = 0x10
INTC2_DMA = 0x08
INTC2_TP = 0x04
INTC2_BTE = 0x02
